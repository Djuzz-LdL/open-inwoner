from django.utils.translation import gettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from open_inwoner.configurations.models import SiteConfiguration
from open_inwoner.openklant.models import KlantenSysteemConfig


@plugin_pool.register_plugin
class FooterPagesPlugin(CMSPluginBase):
    name = _("Pages List")
    render_template = "cms/footer/footer_pages_plugin.html"

    # cache = False

    def render(self, context, instance, placeholder):
        # TODO move options to plugin model
        config = SiteConfiguration.get_solo()
        klant_config = KlantenSysteemConfig.get_solo()
        context["flatpages"] = config.get_ordered_flatpages
        context["has_form_configuration"] = klant_config.has_contactform_configuration
        return context
