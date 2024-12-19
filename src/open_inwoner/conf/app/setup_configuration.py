from ..utils import config

SETUP_CONFIGURATION_STEPS = [
    "mozilla_django_oidc_db.setup_configuration.steps.AdminOIDCConfigurationStep",
    "zgw_consumers.contrib.setup_configuration.steps.ServiceConfigurationStep",
    "open_inwoner.configurations.bootstrap.zgw.OpenZaakConfigurationStep",
    "open_inwoner.configurations.bootstrap.openklant.OpenKlantConfigurationStep",
    "open_inwoner.configurations.bootstrap.openklant.OpenKlant2ConfigurationStep",
]
OIP_ORGANIZATION = config("OIP_ORGANIZATION", "")

# ZGW configuration variables
ZGW_CONFIG_ENABLE = config("ZGW_CONFIG_ENABLE", default=False)
ZGW_SERVER_CERTIFICATE_LABEL = config("ZGW_SERVER_CERTIFICATE_LABEL", "")
ZGW_SERVER_CERTIFICATE_TYPE = config("ZGW_SERVER_CERTIFICATE_TYPE", "")
ZGW_SERVER_CERTIFICATE_PUBLIC_CERTIFICATE = (
    "ZGW_SERVER_CERTIFICATE_PUBLIC_CERTIFICATE",
    None,
)
ZGW_ZAAK_SERVICE_API_ROOT = config("ZGW_ZAAK_SERVICE_API_ROOT", "")
if ZGW_ZAAK_SERVICE_API_ROOT and not ZGW_ZAAK_SERVICE_API_ROOT.endswith("/"):
    ZGW_ZAAK_SERVICE_API_ROOT = f"{ZGW_ZAAK_SERVICE_API_ROOT.strip()}/"
ZGW_ZAKEN_OAS_URL = ZGW_ZAAK_SERVICE_API_ROOT  # this is still required by the form, but not actually used
ZGW_ZAAK_SERVICE_API_CLIENT_ID = config("ZGW_ZAAK_SERVICE_API_CLIENT_ID", "")
ZGW_ZAAK_SERVICE_API_SECRET = config("ZGW_ZAAK_SERVICE_API_SECRET", "")
ZGW_CATALOGI_SERVICE_API_ROOT = config("ZGW_CATALOGI_SERVICE_API_ROOT", "")
if ZGW_CATALOGI_SERVICE_API_ROOT and not ZGW_CATALOGI_SERVICE_API_ROOT.endswith("/"):
    ZGW_CATALOGI_SERVICE_API_ROOT = f"{ZGW_CATALOGI_SERVICE_API_ROOT.strip()}/"
ZGW_CATALOGI_OAS_URL = ZGW_CATALOGI_SERVICE_API_ROOT  # this is still required by the form, but not actually used
ZGW_CATALOGI_SERVICE_API_CLIENT_ID = config("ZGW_CATALOGI_SERVICE_API_CLIENT_ID", "")
ZGW_CATALOGI_SERVICE_API_SECRET = config("ZGW_CATALOGI_SERVICE_API_SECRET", "")
ZGW_DOCUMENTEN_SERVICE_API_ROOT = config("ZGW_DOCUMENTEN_SERVICE_API_ROOT", "")
if ZGW_DOCUMENTEN_SERVICE_API_ROOT and not ZGW_DOCUMENTEN_SERVICE_API_ROOT.endswith(
    "/"
):
    ZGW_DOCUMENTEN_SERVICE_API_ROOT = f"{ZGW_DOCUMENTEN_SERVICE_API_ROOT.strip()}/"
ZGW_DOCUMENTEN_OAS_URL = ZGW_DOCUMENTEN_SERVICE_API_ROOT  # this is still required by the form, but not actually used
ZGW_DOCUMENTEN_SERVICE_API_CLIENT_ID = config(
    "ZGW_DOCUMENTEN_SERVICE_API_CLIENT_ID", ""
)
ZGW_DOCUMENTEN_SERVICE_API_SECRET = config("ZGW_DOCUMENTEN_SERVICE_API_SECRET", "")
ZGW_FORM_SERVICE_API_ROOT = config("ZGW_FORM_SERVICE_API_ROOT", "")
if ZGW_FORM_SERVICE_API_ROOT and not ZGW_FORM_SERVICE_API_ROOT.endswith("/"):
    ZGW_FORM_SERVICE_API_ROOT = f"{ZGW_FORM_SERVICE_API_ROOT.strip()}/"
ZGW_FORMULIEREN_OAS_URL = ZGW_FORM_SERVICE_API_ROOT  # this is still required by the form, but not actually used
ZGW_FORM_SERVICE_API_CLIENT_ID = config("ZGW_FORM_SERVICE_API_CLIENT_ID", "")
ZGW_FORM_SERVICE_API_SECRET = config("ZGW_FORM_SERVICE_API_SECRET", "")
# ZGW config options
ZGW_ZAAK_MAX_CONFIDENTIALITY = config("ZGW_ZAAK_MAX_CONFIDENTIALITY", None)
ZGW_DOCUMENT_MAX_CONFIDENTIALITY = config("ZGW_DOCUMENT_MAX_CONFIDENTIALITY", None)
ZGW_ACTION_REQUIRED_DEADLINE_DAYS = config("ACTION_REQUIRED_DEADLINE_DAYS", None)
ZGW_ALLOWED_FILE_EXTENSIONS = config("ZGW_ALLOWED_FILE_EXTENSIONS", None)
ZGW_MIJN_AANVRAGEN_TITLE_TEXT = config("ZGW_MIJN_AANVRAGEN_TITLE_TEXT", None)
ZGW_ENABLE_CATEGORIES_FILTERING_WITH_ZAKEN = config(
    "ZGW_ENABLE_CATEGORIES_FILTERING_WITH_ZAKEN", None
)
ZGW_SKIP_NOTIFICATION_STATUSTYPE_INFORMEREN = config(
    "ZGW_SKIP_NOTIFICATION_STATUSTYPE_INFORMEREN", None
)
ZGW_REFORMAT_ESUITE_ZAAK_IDENTIFICATIE = config(
    "ZGW_REFORMAT_ESUITE_ZAAK_IDENTIFICATIE", None
)
ZGW_FETCH_EHERKENNING_ZAKEN_WITH_RSIN = config(
    "ZGW_FETCH_EHERKENNING_ZAKEN_WITH_RSIN", None
)

# KIC configuration variables
KIC_CONFIG_ENABLE = config("KIC_CONFIG_ENABLE", default=False)
KIC_SERVER_CERTIFICATE_LABEL = config("KIC_SERVER_CERTIFICATE_LABEL", "")
KIC_SERVER_CERTIFICATE_TYPE = config("KIC_SERVER_CERTIFICATE_TYPE", "")
KIC_SERVER_CERTIFICATE_PUBLIC_CERTIFICATE = config(
    "KIC_SERVER_CERTIFICATE_PUBLIC_CERTIFICATE",
    None,
)
KIC_KLANTEN_SERVICE_API_ROOT = config("KIC_KLANTEN_SERVICE_API_ROOT", "")
if KIC_KLANTEN_SERVICE_API_ROOT and not KIC_KLANTEN_SERVICE_API_ROOT.endswith("/"):
    KIC_KLANTEN_SERVICE_API_ROOT = f"{KIC_KLANTEN_SERVICE_API_ROOT.strip()}/"
KIC_KLANTEN_OAS_URL = KIC_KLANTEN_SERVICE_API_ROOT  # this is still required by the form, but not actually used
KIC_KLANTEN_SERVICE_API_CLIENT_ID = config("KIC_KLANTEN_SERVICE_API_CLIENT_ID", "")
KIC_KLANTEN_SERVICE_API_SECRET = config("KIC_KLANTEN_SERVICE_API_SECRET", "")
KIC_CONTACTMOMENTEN_SERVICE_API_ROOT = config(
    "KIC_CONTACTMOMENTEN_SERVICE_API_ROOT", ""
)
if (
    KIC_CONTACTMOMENTEN_SERVICE_API_ROOT
    and not KIC_CONTACTMOMENTEN_SERVICE_API_ROOT.endswith("/")
):
    KIC_CONTACTMOMENTEN_SERVICE_API_ROOT = (
        f"{KIC_CONTACTMOMENTEN_SERVICE_API_ROOT.strip()}/"
    )
KIC_CONTACTMOMENTEN_OAS_URL = KIC_CONTACTMOMENTEN_SERVICE_API_ROOT  # this is still required by the form, but not actually used
KIC_CONTACTMOMENTEN_SERVICE_API_CLIENT_ID = config(
    "KIC_CONTACTMOMENTEN_SERVICE_API_CLIENT_ID", ""
)
KIC_CONTACTMOMENTEN_SERVICE_API_SECRET = config(
    "KIC_CONTACTMOMENTEN_SERVICE_API_SECRET", ""
)
KIC_REGISTER_EMAIL = config("KIC_REGISTER_EMAIL", None)
KIC_REGISTER_CONTACT_MOMENT = config("KIC_REGISTER_CONTACT_MOMENT", None)
KIC_REGISTER_BRONORGANISATIE_RSIN = config("KIC_REGISTER_BRONORGANISATIE_RSIN", None)
KIC_REGISTER_CHANNEL = config("KIC_REGISTER_CHANNEL", None)
KIC_REGISTER_TYPE = config("KIC_REGISTER_TYPE", None)
KIC_REGISTER_EMPLOYEE_ID = config("KIC_REGISTER_EMPLOYEE_ID", None)
KIC_USE_RSIN_FOR_INNNNPID_QUERY_PARAMETER = config(
    "KIC_USE_RSIN_FOR_INNNNPID_QUERY_PARAMETER", None
)


#
# SiteConfiguration variables
#
SITE_CONFIG_ENABLE = config("SITE_CONFIG_ENABLE", False)
SITE_NAME = config("SITE_NAME", None)
SITE_PRIMARY_COLOR = config("SITE_PRIMARY_COLOR", None)
SITE_SECONDARY_COLOR = config("SITE_SECONDARY_COLOR", None)
SITE_ACCENT_COLOR = config("SITE_ACCENT_COLOR", None)
SITE_PRIMARY_FONT_COLOR = config("SITE_PRIMARY_FONT_COLOR", None)
SITE_SECONDARY_FONT_COLOR = config("SITE_SECONDARY_FONT_COLOR", None)
SITE_ACCENT_FONT_COLOR = config("SITE_ACCENT_FONT_COLOR", None)
SITE_WARNING_BANNER_ENABLED = config("SITE_WARNING_BANNER_ENABLED", None)
SITE_WARNING_BANNER_TEXT = config("SITE_WARNING_BANNER_TEXT", None)
SITE_WARNING_BANNER_BACKGROUND_COLOR = config(
    "SITE_WARNING_BANNER_BACKGROUND_COLOR", None
)
SITE_CONTACTMOMENT_CONTACT_FORM_ENABLED = config(
    "SITE_CONTACTMOMENT_CONTACT_FORM_ENABLED", None
)
SITE_WARNING_BANNER_FONT_COLOR = config("SITE_WARNING_BANNER_FONT_COLOR", None)
SITE_HERO_IMAGE_LOGIN = config("SITE_HERO_IMAGE_LOGIN", None)
SITE_LOGIN_SHOW = config("SITE_LOGIN_SHOW", None)
SITE_LOGIN_ALLOW_REGISTRATION = config("SITE_LOGIN_ALLOW_REGISTRATION", None)
SITE_LOGIN_2FA_SMS = config("SITE_LOGIN_2FA_SMS", None)
SITE_LOGIN_TEXT = config("SITE_LOGIN_TEXT", None)
SITE_REGISTRATION_TEXT = config("SITE_REGISTRATION_TEXT", None)
SITE_HOME_WELCOME_TITLE = config("SITE_HOME_WELCOME_TITLE", None)
SITE_HOME_WELCOME_INTRO = config("SITE_HOME_WELCOME_INTRO", None)
SITE_HOME_THEME_TITLE = config("SITE_HOME_THEME_TITLE", None)
SITE_HOME_THEME_INTRO = config("SITE_HOME_THEME_INTRO", None)
SITE_THEME_TITLE = config("SITE_THEME_TITLE", None)
SITE_THEME_INTRO = config("SITE_THEME_INTRO", None)
SITE_HOME_MAP_TITLE = config("SITE_HOME_MAP_TITLE", None)
SITE_HOME_MAP_INTRO = config("SITE_HOME_MAP_INTRO", None)
SITE_HOME_QUESTIONNAIRE_TITLE = config("SITE_HOME_QUESTIONNAIRE_TITLE", None)
SITE_HOME_QUESTIONNAIRE_INTRO = config("SITE_HOME_QUESTIONNAIRE_INTRO", None)
SITE_HOME_PRODUCT_FINDER_TITLE = config("SITE_HOME_PRODUCT_FINDER_TITLE", None)
SITE_HOME_PRODUCT_FINDER_INTRO = config("SITE_HOME_PRODUCT_FINDER_INTRO", None)
SITE_SELECT_QUESTIONNAIRE_TITLE = config("SITE_SELECT_QUESTIONNAIRE_TITLE", None)
SITE_SELECT_QUESTIONNAIRE_INTRO = config("SITE_SELECT_QUESTIONNAIRE_INTRO", None)
SITE_PLANS_INTRO = config("SITE_PLANS_INTRO", None)
SITE_PLANS_NO_PLANS_MESSAGE = config("SITE_PLANS_NO_PLANS_MESSAGE", None)
SITE_PLANS_EDIT_MESSAGE = config("SITE_PLANS_EDIT_MESSAGE", None)
SITE_FOOTER_LOGO_TITLE = config("SITE_FOOTER_LOGO_TITLE", None)
SITE_FOOTER_LOGO_URL = config("SITE_FOOTER_LOGO_URL", None)
SITE_HOME_HELP_TEXT = config("SITE_HOME_HELP_TEXT", None)
SITE_THEME_HELP_TEXT = config("SITE_THEME_HELP_TEXT", None)
SITE_PRODUCT_HELP_TEXT = config("SITE_PRODUCT_HELP_TEXT", None)
SITE_SEARCH_HELP_TEXT = config("SITE_SEARCH_HELP_TEXT", None)
SITE_ACCOUNT_HELP_TEXT = config("SITE_ACCOUNT_HELP_TEXT", None)
SITE_QUESTIONNAIRE_HELP_TEXT = config("SITE_QUESTIONNAIRE_HELP_TEXT", None)
SITE_PLAN_HELP_TEXT = config("SITE_PLAN_HELP_TEXT", None)
SITE_SEARCH_FILTER_CATEGORIES = config("SITE_SEARCH_FILTER_CATEGORIES", None)
SITE_SEARCH_FILTER_TAGS = config("SITE_SEARCH_FILTER_TAGS", None)
SITE_SEARCH_FILTER_ORGANIZATIONS = config("SITE_SEARCH_FILTER_ORGANIZATIONS", None)
SITE_NOTIFICATIONS_ACTIONS_ENABLED = config("SITE_NOTIFICATIONS_ACTIONS_ENABLED", None)
SITE_NOTIFICATIONS_CASES_ENABLED = config("SITE_NOTIFICATIONS_CASES_ENABLED", None)
SITE_NOTIFICATIONS_PLANS_ENABLED = config("SITE_NOTIFICATIONS_PLANS_ENABLED", None)
SITE_NOTIFICATIONS_MESSAGES_ENABLED = config(
    "SITE_NOTIFICATIONS_MESSAGES_ENABLED", None
)
SITE_RECIPIENTS_EMAIL_DIGEST = config("SITE_RECIPIENTS_EMAIL_DIGEST", None)
SITE_CONTACT_PHONENUMBER = config("SITE_CONTACT_PHONENUMBER", None)
SITE_CONTACT_PAGE = config("SITE_CONTACT_PAGE", None)
SITE_GTM_CODE = config("SITE_GTM_CODE", None)
SITE_GA_CODE = config("SITE_GA_CODE", None)
SITE_MATOMO_URL = config("SITE_MATOMO_URL", None)
SITE_MATOMO_SITE_ID = config("SITE_MATOMO_SITE_ID", None)
SITE_SITEIMPROVE_ID = config("SITE_SITEIMPROVE_ID", None)
SITE_COOKIE_INFO_TEXT = config("SITE_COOKIE_INFO_TEXT", None)
SITE_COOKIE_LINK_TEXT = config("SITE_COOKIE_LINK_TEXT", None)
SITE_COOKIE_LINK_URL = config("SITE_COOKIE_LINK_URL", None)
SITE_KCM_SURVEY_LINK_TEXT = config("SITE_KCM_SURVEY_LINK_TEXT", None)
SITE_KCM_SURVEY_LINK_URL = config("SITE_KCM_SURVEY_LINK_URL", None)
SITE_OPENID_CONNECT_LOGIN_TEXT = config("SITE_OPENID_CONNECT_LOGIN_TEXT", None)
SITE_OPENID_DISPLAY = config("SITE_OPENID_DISPLAY", None)
SITE_REDIRECT_TO = config("SITE_REDIRECT_TO", None)
SITE_ALLOW_MESSAGES_FILE_SHARING = config("SITE_ALLOW_MESSAGES_FILE_SHARING", None)
SITE_HIDE_CATEGORIES_FROM_ANONYMOUS_USERS = config(
    "SITE_HIDE_CATEGORIES_FROM_ANONYMOUS_USERS", None
)
SITE_HIDE_SEARCH_FROM_ANONYMOUS_USERS = config(
    "SITE_HIDE_SEARCH_FROM_ANONYMOUS_USERS", None
)
SITE_DISPLAY_SOCIAL = config("SITE_DISPLAY_SOCIAL", None)
SITE_THEME_STYLESHEET = config("SITE_THEME_STYLESHEET", None)
SITE_EHERKENNING_ENABLED = config("SITE_EHERKENNING_ENABLED", None)


# Authentication configuration variables
# NOTE variables are namespaced with `DIGID_OIDC`, but some model field names also have `oidc_...` in them
DIGID_OIDC_CONFIG_ENABLE = config("DIGID_OIDC_CONFIG_ENABLE", False)
DIGID_OIDC_BSN_CLAIM = config("DIGID_OIDC_BSN_CLAIM", None)
DIGID_OIDC_OIDC_RP_CLIENT_ID = config("DIGID_OIDC_OIDC_RP_CLIENT_ID", None)
DIGID_OIDC_OIDC_RP_CLIENT_SECRET = config("DIGID_OIDC_OIDC_RP_CLIENT_SECRET", None)
DIGID_OIDC_OIDC_RP_SIGN_ALGO = config("DIGID_OIDC_OIDC_RP_SIGN_ALGO", None)
DIGID_OIDC_OIDC_RP_SCOPES_LIST = config("DIGID_OIDC_OIDC_RP_SCOPES_LIST", None)
DIGID_OIDC_OIDC_OP_DISCOVERY_ENDPOINT = config(
    "DIGID_OIDC_OIDC_OP_DISCOVERY_ENDPOINT", None
)
DIGID_OIDC_OIDC_OP_JWKS_ENDPOINT = config("DIGID_OIDC_OIDC_OP_JWKS_ENDPOINT", None)
DIGID_OIDC_OIDC_OP_AUTHORIZATION_ENDPOINT = config(
    "DIGID_OIDC_OIDC_OP_AUTHORIZATION_ENDPOINT", None
)
DIGID_OIDC_OIDC_OP_TOKEN_ENDPOINT = config("DIGID_OIDC_OIDC_OP_TOKEN_ENDPOINT", None)
DIGID_OIDC_OIDC_OP_USER_ENDPOINT = config("DIGID_OIDC_OIDC_OP_USER_ENDPOINT", None)
DIGID_OIDC_OIDC_RP_IDP_SIGN_KEY = config("DIGID_OIDC_OIDC_RP_IDP_SIGN_KEY", None)
DIGID_OIDC_USERINFO_CLAIMS_SOURCE = config("DIGID_OIDC_USERINFO_CLAIMS_SOURCE", None)
DIGID_OIDC_OIDC_OP_LOGOUT_ENDPOINT = config("DIGID_OIDC_OIDC_OP_LOGOUT_ENDPOINT", None)
DIGID_OIDC_OIDC_KEYCLOAK_IDP_HINT = config("DIGID_OIDC_OIDC_KEYCLOAK_IDP_HINT", None)
DIGID_OIDC_OIDC_USE_NONCE = config("DIGID_OIDC_OIDC_USE_NONCE", None)
DIGID_OIDC_OIDC_NONCE_SIZE = config("DIGID_OIDC_OIDC_NONCE_SIZE", None)
DIGID_OIDC_OIDC_STATE_SIZE = config("DIGID_OIDC_OIDC_STATE_SIZE", None)

# NOTE variables are namespaced with `EHERKENNING_OIDC`, but some model field names also have `oidc_...` in them
EHERKENNING_OIDC_CONFIG_ENABLE = config("EHERKENNING_OIDC_CONFIG_ENABLE", False)
EHERKENNING_OIDC_LEGAL_SUBJECT_CLAIM = config(
    "EHERKENNING_OIDC_LEGAL_SUBJECT_CLAIM", None
)
EHERKENNING_OIDC_OIDC_RP_CLIENT_ID = config("EHERKENNING_OIDC_OIDC_RP_CLIENT_ID", None)
EHERKENNING_OIDC_OIDC_RP_CLIENT_SECRET = config(
    "EHERKENNING_OIDC_OIDC_RP_CLIENT_SECRET", None
)
EHERKENNING_OIDC_OIDC_RP_SIGN_ALGO = config("EHERKENNING_OIDC_OIDC_RP_SIGN_ALGO", None)
EHERKENNING_OIDC_OIDC_RP_SCOPES_LIST = config(
    "EHERKENNING_OIDC_OIDC_RP_SCOPES_LIST", None
)
EHERKENNING_OIDC_OIDC_OP_DISCOVERY_ENDPOINT = config(
    "EHERKENNING_OIDC_OIDC_OP_DISCOVERY_ENDPOINT", None
)
EHERKENNING_OIDC_OIDC_OP_JWKS_ENDPOINT = config(
    "EHERKENNING_OIDC_OIDC_OP_JWKS_ENDPOINT", None
)
EHERKENNING_OIDC_OIDC_OP_AUTHORIZATION_ENDPOINT = config(
    "EHERKENNING_OIDC_OIDC_OP_AUTHORIZATION_ENDPOINT", None
)
EHERKENNING_OIDC_OIDC_OP_TOKEN_ENDPOINT = config(
    "EHERKENNING_OIDC_OIDC_OP_TOKEN_ENDPOINT", None
)
EHERKENNING_OIDC_OIDC_OP_USER_ENDPOINT = config(
    "EHERKENNING_OIDC_OIDC_OP_USER_ENDPOINT", None
)
EHERKENNING_OIDC_OIDC_RP_IDP_SIGN_KEY = config(
    "EHERKENNING_OIDC_OIDC_RP_IDP_SIGN_KEY", None
)
EHERKENNING_OIDC_USERINFO_CLAIMS_SOURCE = config(
    "EHERKENNING_OIDC_USERINFO_CLAIMS_SOURCE", None
)
EHERKENNING_OIDC_OIDC_OP_LOGOUT_ENDPOINT = config(
    "EHERKENNING_OIDC_OIDC_OP_LOGOUT_ENDPOINT", None
)
EHERKENNING_OIDC_OIDC_KEYCLOAK_IDP_HINT = config(
    "EHERKENNING_OIDC_OIDC_KEYCLOAK_IDP_HINT", None
)
EHERKENNING_OIDC_OIDC_USE_NONCE = config("EHERKENNING_OIDC_OIDC_USE_NONCE", None)
EHERKENNING_OIDC_OIDC_NONCE_SIZE = config("EHERKENNING_OIDC_OIDC_NONCE_SIZE", None)
EHERKENNING_OIDC_OIDC_STATE_SIZE = config("EHERKENNING_OIDC_OIDC_STATE_SIZE", None)

# NOTE variables are namespaced with `ADMIN_OIDC`, but some model field names also have `oidc_...` in them
ADMIN_OIDC_CONFIG_ENABLE = config("ADMIN_OIDC_CONFIG_ENABLE", default=False)
ADMIN_OIDC_OIDC_RP_CLIENT_ID = config("ADMIN_OIDC_OIDC_RP_CLIENT_ID", None)
ADMIN_OIDC_OIDC_RP_CLIENT_SECRET = config("ADMIN_OIDC_OIDC_RP_CLIENT_SECRET", None)
ADMIN_OIDC_OIDC_RP_SCOPES_LIST = config("ADMIN_OIDC_OIDC_RP_SCOPES_LIST", None)
ADMIN_OIDC_OIDC_RP_SIGN_ALGO = config("ADMIN_OIDC_OIDC_RP_SIGN_ALGO", None)
ADMIN_OIDC_OIDC_RP_IDP_SIGN_KEY = config("ADMIN_OIDC_OIDC_RP_IDP_SIGN_KEY", None)
ADMIN_OIDC_OIDC_OP_DISCOVERY_ENDPOINT = config(
    "ADMIN_OIDC_OIDC_OP_DISCOVERY_ENDPOINT", None
)
ADMIN_OIDC_OIDC_OP_JWKS_ENDPOINT = config("ADMIN_OIDC_OIDC_OP_JWKS_ENDPOINT", None)
ADMIN_OIDC_OIDC_OP_AUTHORIZATION_ENDPOINT = config(
    "ADMIN_OIDC_OIDC_OP_AUTHORIZATION_ENDPOINT", None
)
ADMIN_OIDC_OIDC_OP_TOKEN_ENDPOINT = config("ADMIN_OIDC_OIDC_OP_TOKEN_ENDPOINT", None)
ADMIN_OIDC_OIDC_OP_USER_ENDPOINT = config("ADMIN_OIDC_OIDC_OP_USER_ENDPOINT", None)
ADMIN_OIDC_USERNAME_CLAIM = config("ADMIN_OIDC_USERNAME_CLAIM", None)
ADMIN_OIDC_GROUPS_CLAIM = config("ADMIN_OIDC_GROUPS_CLAIM", None)
# XXX: this needs to be provided as a Mapping[str, list[str]] now instead of Mapping[str, str]!
ADMIN_OIDC_CLAIM_MAPPING = config("ADMIN_OIDC_CLAIM_MAPPING", None)
ADMIN_OIDC_SYNC_GROUPS = config("ADMIN_OIDC_SYNC_GROUPS", None)
ADMIN_OIDC_SYNC_GROUPS_GLOB_PATTERN = config(
    "ADMIN_OIDC_SYNC_GROUPS_GLOB_PATTERN", None
)
ADMIN_OIDC_DEFAULT_GROUPS = config("ADMIN_OIDC_DEFAULT_GROUPS", None)
ADMIN_OIDC_MAKE_USERS_STAFF = config("ADMIN_OIDC_MAKE_USERS_STAFF", None)
ADMIN_OIDC_SUPERUSER_GROUP_NAMES = config("ADMIN_OIDC_SUPERUSER_GROUP_NAMES", None)
ADMIN_OIDC_OIDC_USE_NONCE = config("ADMIN_OIDC_OIDC_USE_NONCE", None)
ADMIN_OIDC_OIDC_NONCE_SIZE = config("ADMIN_OIDC_OIDC_NONCE_SIZE", None)
ADMIN_OIDC_OIDC_STATE_SIZE = config("ADMIN_OIDC_OIDC_STATE_SIZE", None)
ADMIN_OIDC_USERINFO_CLAIMS_SOURCE = config("ADMIN_OIDC_USERINFO_CLAIMS_SOURCE", None)

#
# DigiD SAML
#
DIGID_SAML_CONFIG_ENABLE = config("DIGID_SAML_SAML_CONFIG_ENABLE", default=False)
DIGID_SAML_CERTIFICATE_LABEL = config("DIGID_SAML_CERTIFICATE_LABEL", None)
DIGID_SAML_CERTIFICATE_TYPE = config("DIGID_SAML_CERTIFICATE_TYPE", None)
DIGID_SAML_CERTIFICATE_PUBLIC_CERTIFICATE = config(
    "DIGID_SAML_CERTIFICATE_PUBLIC_CERTIFICATE", None
)
DIGID_SAML_CERTIFICATE_PRIVATE_KEY = config("DIGID_SAML_CERTIFICATE_PRIVATE_KEY", None)
DIGID_SAML_METADATA_FILE_SOURCE = config("DIGID_SAML_METADATA_FILE_SOURCE", None)
DIGID_SAML_WANT_ASSERTIONS_SIGNED = config("DIGID_SAML_WANT_ASSERTIONS_SIGNED", None)
DIGID_SAML_WANT_ASSERTIONS_ENCRYPTED = config(
    "DIGID_SAML_WANT_ASSERTIONS_ENCRYPTED", None
)
DIGID_SAML_ARTIFACT_RESOLVE_CONTENT_TYPE = config(
    "DIGID_SAML_ARTIFACT_RESOLVE_CONTENT_TYPE", None
)
DIGID_SAML_KEY_PASSPHRASE = config("DIGID_SAML_KEY_PASSPHRASE", None)
DIGID_SAML_SIGNATURE_ALGORITHM = config("DIGID_SAML_SIGNATURE_ALGORITHM", None)
DIGID_SAML_DIGEST_ALGORITHM = config("DIGID_SAML_DIGEST_ALGORITHM", None)
DIGID_SAML_ENTITY_ID = config("DIGID_SAML_ENTITY_ID", None)
DIGID_SAML_BASE_URL = config("DIGID_SAML_BASE_URL", None)
DIGID_SAML_SERVICE_NAME = config("DIGID_SAML_SERVICE_NAME", None)
DIGID_SAML_SERVICE_DESCRIPTION = config("DIGID_SAML_SERVICE_DESCRIPTION", None)
DIGID_SAML_TECHNICAL_CONTACT_PERSON_TELEPHONE = config(
    "DIGID_SAML_TECHNICAL_CONTACT_PERSON_TELEPHONE", None
)
DIGID_SAML_TECHNICAL_CONTACT_PERSON_EMAIL = config(
    "DIGID_SAML_TECHNICAL_CONTACT_PERSON_EMAIL", None
)
DIGID_SAML_ORGANIZATION_URL = config("DIGID_SAML_ORGANIZATION_URL", None)
DIGID_SAML_ORGANIZATION_NAME = config("DIGID_SAML_ORGANIZATION_NAME", None)
DIGID_SAML_ATTRIBUTE_CONSUMING_SERVICE_INDEX = config(
    "DIGID_SAML_ATTRIBUTE_CONSUMING_SERVICE_INDEX", None
)
DIGID_SAML_REQUESTED_ATTRIBUTES = config("DIGID_SAML_REQUESTED_ATTRIBUTES", None)
DIGID_SAML_SLO = config("DIGID_SAML_SLO", None)

#
# Eherkenning SAML
#
EHERKENNING_SAML_CONFIG_ENABLE = config("EHERKENNING_SAML_CONFIG_ENABLE", default=False)
EHERKENNING_SAML_CERTIFICATE_LABEL = config("EHERKENNING_SAML_CERTIFICATE_LABEL", None)
EHERKENNING_SAML_CERTIFICATE_TYPE = config("EHERKENNING_SAML_CERTIFICATE_TYPE", None)
EHERKENNING_SAML_CERTIFICATE_PUBLIC_CERTIFICATE = config(
    "EHERKENNING_SAML_CERTIFICATE_PUBLIC_CERTIFICATE", None
)
EHERKENNING_SAML_CERTIFICATE_PRIVATE_KEY = config(
    "EHERKENNING_SAML_CERTIFICATE_PRIVATE_KEY", None
)
EHERKENNING_SAML_METADATA_FILE_SOURCE = config(
    "EHERKENNING_SAML_METADATA_FILE_SOURCE", None
)
EHERKENNING_SAML_WANT_ASSERTIONS_SIGNED = config(
    "EHERKENNING_SAML_WANT_ASSERTIONS_SIGNED", None
)
EHERKENNING_SAML_WANT_ASSERTIONS_ENCRYPTED = config(
    "EHERKENNING_SAML_WANT_ASSERTIONS_ENCRYPTED", None
)
EHERKENNING_SAML_ARTIFACT_RESOLVE_CONTENT_TYPE = config(
    "EHERKENNING_SAML_ARTIFACT_RESOLVE_CONTENT_TYPE", None
)
EHERKENNING_SAML_KEY_PASSPHRASE = config("EHERKENNING_SAML_KEY_PASSPHRASE", None)
EHERKENNING_SAML_SIGNATURE_ALGORITHM = config(
    "EHERKENNING_SAML_SIGNATURE_ALGORITHM", None
)
EHERKENNING_SAML_DIGEST_ALGORITHM = config("EHERKENNING_SAML_DIGEST_ALGORITHM", None)
EHERKENNING_SAML_ENTITY_ID = config("EHERKENNING_SAML_ENTITY_ID", None)
EHERKENNING_SAML_BASE_URL = config("EHERKENNING_SAML_BASE_URL", None)
EHERKENNING_SAML_SERVICE_NAME = config("EHERKENNING_SAML_SERVICE_NAME", None)
EHERKENNING_SAML_SERVICE_DESCRIPTION = config(
    "EHERKENNING_SAML_SERVICE_DESCRIPTION", None
)
EHERKENNING_SAML_TECHNICAL_CONTACT_PERSON_TELEPHONE = config(
    "EHERKENNING_SAML_TECHNICAL_CONTACT_PERSON_TELEPHONE", None
)
EHERKENNING_SAML_TECHNICAL_CONTACT_PERSON_EMAIL = config(
    "EHERKENNING_SAML_TECHNICAL_CONTACT_PERSON_EMAIL", None
)
EHERKENNING_SAML_ORGANIZATION_URL = config("EHERKENNING_SAML_ORGANIZATION_URL", None)
EHERKENNING_SAML_ORGANIZATION_NAME = config("EHERKENNING_SAML_ORGANIZATION_NAME", None)
EHERKENNING_SAML_EH_LOA = config("EHERKENNING_SAML_EH_LOA", None)
EHERKENNING_SAML_EH_ATTRIBUTE_CONSUMING_SERVICE_INDEX = config(
    "EHERKENNING_SAML_EH_ATTRIBUTE_CONSUMING_SERVICE_INDEX", None
)
EHERKENNING_SAML_EH_REQUESTED_ATTRIBUTES = config(
    "EHERKENNING_SAML_EH_REQUESTED_ATTRIBUTES", None
)
EHERKENNING_SAML_EH_SERVICE_UUID = config("EHERKENNING_SAML_EH_SERVICE_UUID", None)
EHERKENNING_SAML_EH_SERVICE_INSTANCE_UUID = config(
    "EHERKENNING_SAML_EH_SERVICE_INSTANCE_UUID", None
)
EHERKENNING_SAML_EIDAS_LOA = config("EHERKENNING_SAML_EIDAS_LOA", None)
EHERKENNING_SAML_EIDAS_ATTRIBUTE_CONSUMING_SERVICE_INDEX = config(
    "EHERKENNING_SAML_EIDAS_ATTRIBUTE_CONSUMING_SERVICE_INDEX", None
)
EHERKENNING_SAML_EIDAS_REQUESTED_ATTRIBUTES = config(
    "EHERKENNING_SAML_EIDAS_REQUESTED_ATTRIBUTES", None
)
EHERKENNING_SAML_EIDAS_SERVICE_UUID = config(
    "EHERKENNING_SAML_EIDAS_SERVICE_UUID", None
)
EHERKENNING_SAML_EIDAS_SERVICE_INSTANCE_UUID = config(
    "EHERKENNING_SAML_EIDAS_SERVICE_INSTANCE_UUID", None
)
EHERKENNING_SAML_OIN = config("EHERKENNING_SAML_OIN", None)
EHERKENNING_SAML_NO_EIDAS = config("EHERKENNING_SAML_NO_EIDAS", None)
EHERKENNING_SAML_PRIVACY_POLICY = config("EHERKENNING_SAML_PRIVACY_POLICY", None)
EHERKENNING_SAML_MAKELAAR_ID = config("EHERKENNING_SAML_MAKELAAR_ID", None)
EHERKENNING_SAML_SERVICE_LANGUAGE = config("EHERKENNING_SAML_SERVICE_LANGUAGE", None)

#
# CMS configuration variables
#

# benefits (ssd)
CMS_CONFIG_SSD_ENABLE = config("CMS_CONFIG_SSD_ENABLE", default=False)
# common extension
CMS_SSD_REQUIRES_AUTH = config("CMS_SSD_REQUIRES_AUTH", None)
CMS_SSD_REQUIRES_AUTH_BSN_OR_KVK = config("CMS_SSD_REQUIRES_AUTH_BSN_OR_KVK", None)
CMS_SSD_MENU_INDICATOR = config("CMS_SSD_MENU_INDICATOR", None)
CMS_SSD_MENU_ICON = config("CMS_SSD_MENU_ICON", None)

# cases
CMS_CONFIG_CASES_ENABLE = config("CMS_CONFIG_CASES_ENABLE", default=False)
# common extension
CMS_CASES_REQUIRES_AUTH = config("CMS_CASES_REQUIRES_AUTH", None)
CMS_CASES_REQUIRES_AUTH_BSN_OR_KVK = config("CMS_CASES_REQUIRES_AUTH_BSN_OR_KVK", None)
CMS_CASES_MENU_INDICATOR = config("CMS_CASES_MENU_INDICATOR", None)
CMS_CASES_MENU_ICON = config("CMS_CASES_MENU_ICON", None)

# collaborations
CMS_CONFIG_COLLABORATE_ENABLE = config("CMS_CONFIG_COLLABORATE_ENABLE", default=False)
# common extension
CMS_COLLABORATE_REQUIRES_AUTH = config("CMS_COLLABORATE_REQUIRES_AUTH", None)
CMS_COLLABORATE_REQUIRES_AUTH_BSN_OR_KVK = config(
    "CMS_COLLABORATE_REQUIRES_AUTH_BSN_OR_KVK", None
)
CMS_COLLABORATE_MENU_INDICATOR = config("CMS_COLLABORATE_MENU_INDICATOR", None)
CMS_COLLABORATE_MENU_ICON = config("CMS_COLLABORATE_MENU_ICON", None)

# inbox
CMS_CONFIG_INBOX_ENABLE = config("CMS_CONFIG_INBOX_ENABLE", default=False)
# common extension
CMS_INBOX_REQUIRES_AUTH = config("CMS_INBOX_REQUIRES_AUTH", None)
CMS_INBOX_REQUIRES_AUTH_BSN_OR_KVK = config("CMS_INBOX_REQUIRES_AUTH_BSN_OR_KVK", None)
CMS_INBOX_MENU_INDICATOR = config("CMS_INBOX_MENU_INDICATOR", None)
CMS_INBOX_MENU_ICON = config("CMS_INBOX_MENU_ICON", None)

# products
CMS_CONFIG_PRODUCTS_ENABLE = config("CMS_CONFIG_PRODUCTS_ENABLE", default=False)
# common extension
CMS_PRODUCTS_REQUIRES_AUTH = config("CMS_PRODUCTS_REQUIRES_AUTH", None)
CMS_PRODUCTS_REQUIRES_AUTH_BSN_OR_KVK = config(
    "CMS_PRODUCTS_REQUIRES_AUTH_BSN_OR_KVK", None
)
CMS_PRODUCTS_MENU_INDICATOR = config("CMS_PRODUCTS_MENU_INDICATOR", None)
CMS_PRODUCTS_MENU_ICON = config("CMS_PRODUCTS_MENU_ICON", None)

# profile app enable
CMS_CONFIG_PROFILE_ENABLE = config("CMS_CONFIG_PROFILE_ENABLE", default=False)
# procile config
CMS_PROFILE_MY_DATA = config("CMS_PROFILE_MY_DATA", None)
CMS_PROFILE_SELECTED_CATEGORIES = config("CMS_PROFILE_SELECTED_CATEGORIES", None)
CMS_PROFILE_MENTORS = config("CMS_PROFILE_MENTORS", None)
CMS_PROFILE_MY_CONTACTS = config("CMS_PROFILE_MY_CONTACTS", None)
CMS_PROFILE_SELFDIAGNOSE = config("CMS_PROFILE_SELFDIAGNOSE", None)
CMS_PROFILE_ACTIONS = config("CMS_PROFILE_ACTIONS", None)
CMS_PROFILE_NOTIFICATIONS = config("CMS_PROFILE_NOTIFICATIONS", None)
CMS_PROFILE_QUESTIONS = config("CMS_PROFILE_QUESTIONS", None)
CMS_PROFILE_SSD = config("CMS_PROFILE_SSD", None)
CMS_PROFILE_NEWSLETTERS = config("CMS_PROFILE_NEWSLETTERS", None)
CMS_PROFILE_APPOINTMENTS = config("CMS_PROFILE_APPOINTMENTS", None)
# profile common extension
CMS_PROFILE_REQUIRES_AUTH = config("CMS_PROFILE_REQUIRES_AUTH", None)
CMS_PROFILE_REQUIRES_AUTH_BSN_OR_KVK = config(
    "CMS_PROFILE_REQUIRES_AUTH_BSN_OR_KVK", None
)
CMS_PROFILE_MENU_INDICATOR = config("CMS_PROFILE_MENU_INDICATOR", None)
CMS_PROFILE_MENU_ICON = config("CMS_PROFILE_MENU_ICON", None)
