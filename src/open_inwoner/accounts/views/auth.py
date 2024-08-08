import logging

from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView,
)
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.urls import reverse
from django.utils.translation import gettext as _

from digid_eherkenning.mock import conf as digid_conf
from digid_eherkenning.mock.views.digid import DigiDAssertionConsumerServiceMockView
from digid_eherkenning.views.base import get_redirect_url
from digid_eherkenning.views.digid import DigiDAssertionConsumerServiceView
from digid_eherkenning.views.eherkenning import eHerkenningAssertionConsumerServiceView
from onelogin.saml2.utils import OneLogin_Saml2_ValidationError

from digid_eherkenning_oidc_generics.views import (
    eHerkenningOIDCAuthenticationCallbackView,
)
from eherkenning.mock import eherkenning_conf
from eherkenning.mock.views.eherkenning import (
    eHerkenningAssertionConsumerServiceMockView,
)
from open_inwoner.openklant.clients import build_klanten_client
from open_inwoner.openklant.models import OpenKlantConfig
from open_inwoner.openzaak.models import OpenZaakConfig
from open_inwoner.utils.views import LogMixin

from ..choices import LoginTypeChoices
from ..forms import CustomPasswordResetForm

logger = logging.getLogger(__name__)


class LogPasswordChangeView(UserPassesTestMixin, LogMixin, PasswordChangeView):
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.login_type == LoginTypeChoices.default
        return False

    def form_valid(self, form):
        response = super().form_valid(form)

        object = self.request.user
        self.log_user_action(object, _("password was changed"))
        return response


class LogPasswordResetView(LogMixin, PasswordResetView):
    form_class = CustomPasswordResetForm

    def form_valid(self, form):
        self.log_system_action(_("password reset was accessed"))
        return super().form_valid(form)


class LogPasswordResetConfirmView(LogMixin, PasswordResetConfirmView):
    def form_valid(self, form):
        response = super().form_valid(form)

        object = self.get_user(self.kwargs["uidb64"])
        self.log_system_action(_("password reset was completed"), object)
        return response


class CustomDigiDAssertionConsumerServiceMockView(
    DigiDAssertionConsumerServiceMockView
):
    def get_login_url(self):
        """
        where to go after unsuccessful login
        """
        invite_url = self.request.session.get("invite_url")
        next_url = self.request.GET.get("next")

        if invite_url and next_url:
            if reverse("profile:registration_necessary") in next_url:
                # If user logs in via the invitation flow redirect to the invitation
                # accept view if login fails
                absolute_invite_url = self.request.build_absolute_uri(invite_url)
                return absolute_invite_url
            else:
                del self.request.session["invite_url"]

        url = self.request.build_absolute_uri(digid_conf.get_cancel_url())
        url = get_redirect_url(
            self.request, url, require_https=self.request.is_secure()
        )

        if url:
            return url

        return resolve_url(settings.LOGIN_URL)

    def get_success_url(self):
        session = self.request.session

        # Remove invite url from user's session after successful digid login
        if "invite_url" in session.keys():
            del session["invite_url"]

        return super().get_success_url()


class CustomDigiDAssertionConsumerServiceView(DigiDAssertionConsumerServiceView):
    def get(self, request):
        errors = []
        user = auth.authenticate(
            request=request,
            digid=True,
            saml_art=request.GET.get("SAMLart"),
            errors=errors,
        )
        if user is None:
            error_code = getattr(errors[0], "code", "") if errors else ""
            error_type = (
                "cancelled"
                if error_code == OneLogin_Saml2_ValidationError.STATUS_CODE_AUTHNFAILED
                else "default"
            )
            messages.error(request, self.error_messages[error_type])
            login_url = self.get_login_url(error_type=error_type)
            return HttpResponseRedirect(login_url)

        if (client := build_klanten_client()) and (
            klant := client.create_klant(user_bsn=user.bsn)
        ):
            logger.info("Created klant %s for new user %s", klant, user)

        auth.login(request, user)

        return HttpResponseRedirect(self.get_success_url())

    def get_login_url(self, **kwargs):
        invite_url = self.request.session.get("invite_url")
        next_url = self.request.GET.get("RelayState")

        if invite_url and next_url:
            if reverse("profile:registration_necessary") in next_url:
                # If user logs in via the invitation flow redirect to the invitation
                # accept view if login fails
                absolute_invite_url = self.request.build_absolute_uri(invite_url)
                return absolute_invite_url
            else:
                del self.request.session["invite_url"]

        url = self.get_redirect_url()
        if url:
            return url

        return resolve_url(settings.LOGIN_URL)

    def get_success_url(self):
        session = self.request.session
        # Remove invite url from user's session after successful digid login
        if "invite_url" in session.keys():
            del session["invite_url"]

        return super().get_success_url()


class BlockEenmanszaakLoginMixin:
    def get(self, request):
        response = super().get(request)

        openzaak_config = OpenZaakConfig.get_solo()
        openklant_config = OpenKlantConfig.get_solo()
        if (
            hasattr(request.user, "rsin")
            and not request.user.rsin
            and (
                openzaak_config.fetch_eherkenning_zaken_with_rsin
                or openklant_config.use_rsin_for_innNnpId_query_parameter
            )
        ):
            auth.logout(request)
            message = _("Use DigiD to log in as a sole proprietor.")
            messages.error(request, message)
            failure_url = self.get_failure_url()
            return HttpResponseRedirect(failure_url)
        return response


class CustomeHerkenningAssertionConsumerServiceMockView(
    BlockEenmanszaakLoginMixin, eHerkenningAssertionConsumerServiceMockView
):
    def get_login_url(self):
        """
        where to go after unsuccessful login
        """
        invite_url = self.request.session.get("invite_url")
        next_url = self.request.GET.get("next")

        if invite_url and next_url:
            if reverse("profile:registration_necessary") in next_url:
                # If user logs in via the invitation flow redirect to the invitation
                # accept view if login fails
                absolute_invite_url = self.request.build_absolute_uri(invite_url)
                return absolute_invite_url
            else:
                del self.request.session["invite_url"]

        url = self.request.build_absolute_uri(eherkenning_conf.get_cancel_url())
        url = get_redirect_url(
            self.request, url, require_https=self.request.is_secure()
        )

        if url:
            return url

        return resolve_url(settings.LOGIN_URL)

    def get_success_url(self):
        session = self.request.session

        # Remove invite url from user's session after successful digid login
        if "invite_url" in session.keys():
            del session["invite_url"]

        return super().get_success_url()


class CustomeHerkenningAssertionConsumerServiceView(
    eHerkenningAssertionConsumerServiceView
):
    def get_login_url(self, **kwargs):
        invite_url = self.request.session.get("invite_url")
        next_url = self.request.GET.get("RelayState")

        if invite_url and next_url:
            if reverse("profile:registration_necessary") in next_url:
                # If user logs in via the invitation flow redirect to the invitation
                # accept view if login fails
                absolute_invite_url = self.request.build_absolute_uri(invite_url)
                return absolute_invite_url
            else:
                del self.request.session["invite_url"]

        url = self.get_redirect_url()
        if url:
            return url

        return resolve_url(settings.LOGIN_URL)

    def get_success_url(self):
        session = self.request.session
        # Remove invite url from user's session after successful digid login
        if "invite_url" in session.keys():
            del session["invite_url"]

        return super().get_success_url()


class CustomEHerkenningOIDCAuthenticationCallbackView(
    BlockEenmanszaakLoginMixin, eHerkenningOIDCAuthenticationCallbackView
):
    def get_failure_url(self):
        return settings.LOGIN_URL
