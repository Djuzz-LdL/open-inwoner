from pathlib import Path

from django.core.exceptions import ValidationError
from django.test import TestCase

from django_setup_configuration.exceptions import ConfigurationRunFailed
from django_setup_configuration.test_utils import execute_single_step
from zgw_consumers.constants import APITypes

from open_inwoner.openklant.constants import KlantenServiceType
from open_inwoner.openklant.models import (
    ESuiteKlantConfig,
    KlantenSysteemConfig,
    OpenKlant2Config,
)
from open_inwoner.openzaak.tests.factories import ServiceFactory

from ...bootstrap.openklant import (
    ESuiteKlantConfigurationStep,
    KlantenSysteemConfigurationStep,
    OpenKlant2ConfigurationStep,
)

KLANTEN_SERVICE_API_ROOT = "https://openklant.local/klanten/api/v1/"
CONTACTMOMENTEN_SERVICE_API_ROOT = "https://openklant.local/contactmomenten/api/v1/"

BASE_DIR = Path(__file__).parent / "files"
ESUITEKLANT_CONFIG_STEP_FULL_YAML = str(BASE_DIR / "esuiteklant_config_step_full.yaml")
KLANTENSYSTEEM_CONFIG_STEP_FULL_YAML = str(
    BASE_DIR / "klantensysteem_config_step_full.yaml"
)
OPENKLANT2_CONFIG_STEP_FULL_YAML = str(BASE_DIR / "openklant2_config_step_full.yaml")


class ESuiteKlantConfigurationStepTestCase(TestCase):
    def test_configure(self):
        kc = ServiceFactory(
            slug="klanten-service",
            api_root=KLANTEN_SERVICE_API_ROOT,
            api_type=APITypes.kc,
        )
        cmc = ServiceFactory(
            slug="contactmomenten-service",
            api_root=CONTACTMOMENTEN_SERVICE_API_ROOT,
            api_type=APITypes.cmc,
        )
        execute_single_step(
            ESuiteKlantConfigurationStep, yaml_source=ESUITEKLANT_CONFIG_STEP_FULL_YAML
        )

        config = ESuiteKlantConfig.get_solo()

        self.assertEqual(config.klanten_service, kc)
        self.assertEqual(config.contactmomenten_service, cmc)

        self.assertEqual(config.register_bronorganisatie_rsin, "837194569")
        self.assertEqual(config.register_channel, "email")
        self.assertEqual(config.register_type, "bericht")
        self.assertEqual(config.register_employee_id, "1234")
        self.assertEqual(config.use_rsin_for_innNnpId_query_parameter, True)

    def test_configure_with_bad_service_identifiers(self):
        kc = ServiceFactory(
            slug="klanten-service-different-from-yaml",
            api_root=KLANTEN_SERVICE_API_ROOT,
            api_type=APITypes.kc,
        )
        cmc = ServiceFactory(
            slug="contactmomenten-service-different-from-yaml",
            api_root=CONTACTMOMENTEN_SERVICE_API_ROOT,
            api_type=APITypes.cmc,
        )

        with self.assertRaises(ConfigurationRunFailed) as exc:
            execute_single_step(
                ESuiteKlantConfigurationStep,
                yaml_source=ESUITEKLANT_CONFIG_STEP_FULL_YAML,
            )

        self.assertEqual(
            str(exc.exception),
            (
                "Unable to retrieve `klanten_service` and/or `contactmomenten_service`"
                ". Try first configuring the `zgw_consumers` configuration steps, and."
                " ensure that both the `identifier` and `api_type` fields match."
            ),
        )

    def test_configure_with_bad_api_type_for_klanten_service(self):
        kc = ServiceFactory(
            slug="klanten-service",
            api_root=KLANTEN_SERVICE_API_ROOT,
            api_type=APITypes.orc,
        )
        cmc = ServiceFactory(
            slug="contactmomenten-service",
            api_root=CONTACTMOMENTEN_SERVICE_API_ROOT,
            api_type=APITypes.cmc,
        )

        with self.assertRaises(ConfigurationRunFailed) as exc:
            execute_single_step(
                ESuiteKlantConfigurationStep,
                yaml_source=ESUITEKLANT_CONFIG_STEP_FULL_YAML,
            )

        self.assertEqual(
            str(exc.exception),
            (
                "Found klanten service with identifier `klanten-service`, but expected"
                " `api_type` to equal `kc` and got `orc`"
            ),
        )

    def test_configure_with_bad_api_type_for_contactmomenten_service(self):
        kc = ServiceFactory(
            slug="klanten-service",
            api_root=KLANTEN_SERVICE_API_ROOT,
            api_type=APITypes.kc,
        )
        cmc = ServiceFactory(
            slug="contactmomenten-service",
            api_root=CONTACTMOMENTEN_SERVICE_API_ROOT,
            api_type=APITypes.orc,
        )

        with self.assertRaises(ConfigurationRunFailed) as exc:
            execute_single_step(
                ESuiteKlantConfigurationStep,
                yaml_source=ESUITEKLANT_CONFIG_STEP_FULL_YAML,
            )

        self.assertEqual(
            str(exc.exception),
            (
                "Found contactmomenten service with identifier "
                "`contactmomenten-service`, but expected `api_type` to equal `cmc`"
                " and got `orc`"
            ),
        )

    def test_idempotent_configure(self):
        kc = ServiceFactory(
            slug="klanten-service",
            api_root=KLANTEN_SERVICE_API_ROOT,
            api_type=APITypes.kc,
        )
        cmc = ServiceFactory(
            slug="contactmomenten-service",
            api_root=CONTACTMOMENTEN_SERVICE_API_ROOT,
            api_type=APITypes.cmc,
        )

        def assert_values():
            config = ESuiteKlantConfig.get_solo()

            self.assertEqual(config.klanten_service, kc)
            self.assertEqual(config.contactmomenten_service, cmc)

            self.assertEqual(config.register_bronorganisatie_rsin, "837194569")
            self.assertEqual(config.register_channel, "email")
            self.assertEqual(config.register_type, "bericht")
            self.assertEqual(config.register_employee_id, "1234")
            self.assertEqual(config.use_rsin_for_innNnpId_query_parameter, True)

        execute_single_step(
            ESuiteKlantConfigurationStep, yaml_source=ESUITEKLANT_CONFIG_STEP_FULL_YAML
        )

        assert_values()

        config = ESuiteKlantConfig.get_solo()
        config.register_bronorganisatie_rsin = "800000009"
        config.register_channel = "not-email"
        config.register_type = "not-bericht"
        config.register_employee_id = "4321"
        config.use_rsin_for_innNnpId_query_parameter = False
        config.save()

        execute_single_step(
            ESuiteKlantConfigurationStep, yaml_source=ESUITEKLANT_CONFIG_STEP_FULL_YAML
        )

        assert_values()


class OpenKlant2ConfigurationStepTestCase(TestCase):
    def test_configure(self):
        kc = ServiceFactory(
            slug="klanten-service",
            api_root=KLANTEN_SERVICE_API_ROOT,
            api_type=APITypes.kc,
        )

        execute_single_step(
            OpenKlant2ConfigurationStep, yaml_source=OPENKLANT2_CONFIG_STEP_FULL_YAML
        )

        config = OpenKlant2Config.get_solo()

        self.assertEqual(config.service, kc)
        self.assertEqual(config.mijn_vragen_kanaal, "formulier")

        self.assertEqual(config.mijn_vragen_organisatie_naam, "De Gemeente")
        self.assertEqual(
            config.mijn_vragen_actor, "e412c6f6-bc31-4fd4-b883-0fb5e88d3f5b"
        )
        self.assertEqual(config.interne_taak_gevraagde_handeling, "Vraag beantwoorden")
        self.assertEqual(
            config.interne_taak_toelichting, "Vraag via OIP, graag beantwoorden"
        )


class KlantenSysteemConfigurationStepTest(TestCase):
    def test_configure_success(self):
        kc = ServiceFactory(
            slug="klanten-service",
            api_root=KLANTEN_SERVICE_API_ROOT,
            api_type=APITypes.kc,
        )
        cmc = ServiceFactory(
            slug="contactmomenten-service",
            api_root=CONTACTMOMENTEN_SERVICE_API_ROOT,
            api_type=APITypes.cmc,
        )
        esuite_config = ESuiteKlantConfig.get_solo()
        esuite_config.klanten_service = kc
        esuite_config.contactmomenten_service = cmc
        esuite_config.save()

        execute_single_step(
            KlantenSysteemConfigurationStep,
            yaml_source=KLANTENSYSTEEM_CONFIG_STEP_FULL_YAML,
        )

        config = KlantenSysteemConfig.get_solo()
        self.assertEqual(config.primary_backend, KlantenServiceType.ESUITE.value)
        self.assertTrue(config.register_contact_via_api)
        self.assertEqual(config.register_contact_email, "oip-test@test.nl")
        self.assertTrue(config.send_email_confirmation)

    def test_configure_missing_api_services(self):
        with self.assertRaises(ValidationError):
            execute_single_step(
                KlantenSysteemConfigurationStep,
                yaml_source=KLANTENSYSTEEM_CONFIG_STEP_FULL_YAML,
            )
