import itertools

from django.test import TestCase

import requests_mock

from open_inwoner.accounts.tests.factories import UserFactory
from open_inwoner.openklant.api_models import Klant
from open_inwoner.openklant.services import eSuiteKlantenService
from open_inwoner.openklant.tests.data import KLANTEN_ROOT, MockAPIReadData
from open_inwoner.utils.test import DisableRequestLogMixin


class eSuiteServiceTestCase(TestCase, DisableRequestLogMixin):
    maxDiff = None

    def setUp(self):
        super().setUp()
        self.data = MockAPIReadData()
        self.data.setUpServices()
        self.service = eSuiteKlantenService()
        self.user = UserFactory()

    def test_create_klant_can_only_specify_one_identifier(self):
        identifiers = {
            "vestigingsnummer": "123",
            "user_bsn": "123",
            "user_kvk_or_rsin": "123",
        }

        # Test all pairs
        for id1, id2 in itertools.combinations(identifiers.keys(), 2):
            with self.subTest(f"{id1} with {id2}"):
                test_ids = {id1: "123", id2: "123"}
                with self.assertRaises(ValueError):
                    self.service.create_klant(**test_ids)

        # Test all three
        with self.subTest("all identifiers"):
            with self.assertRaises(ValueError):
                self.service.create_klant(**identifiers)

    def test_create_klant_bsn(self):
        with requests_mock.mock() as m:
            m.post(
                f"{KLANTEN_ROOT}klanten",
                json=self.data.klant_bsn,
            )

            klant = self.service.create_klant(user_bsn="123456789")

        self.assertIsInstance(klant, Klant)
        self.assertEqual(
            m.request_history[0].json(),
            {"subjectIdentificatie": {"inpBsn": "123456789"}},
        )
        self.assertEqual(
            klant,
            Klant(
                url="https://klanten.nl/api/v1/klant/aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
                bronorganisatie="123456789",
                klantnummer="12345678",
                website_url="",
                voornaam="John",
                voorvoegsel_achternaam="van der",
                achternaam="Doe",
                telefoonnummer="0612345678",
                emailadres="foo@example.com",
                toestemming_zaak_notificaties_alleen_digitaal=False,
                bedrijfsnaam="",
            ),
        )

    def test_create_klant_kvk(self):
        with requests_mock.mock() as m:
            m.post(
                f"{KLANTEN_ROOT}klanten",
                json=self.data.klant_kvk,
            )

            klant = self.service.create_klant(user_kvk_or_rsin="87654321")

        self.assertIsInstance(klant, Klant)
        self.assertEqual(
            m.request_history[0].json(),
            {"subjectIdentificatie": {"innNnpId": "87654321"}},
        )
        self.assertEqual(
            klant,
            Klant(
                url="https://klanten.nl/api/v1/klant/aaaaaaaa-aaaa-aaaa-aaaa-ffffffffffff",
                bronorganisatie="123456789",
                klantnummer="87654321",
                website_url="",
                voornaam="",
                voorvoegsel_achternaam="",
                achternaam="",
                telefoonnummer="0687654321",
                emailadres="foo@bar.com",
                toestemming_zaak_notificaties_alleen_digitaal=False,
                bedrijfsnaam="AcmeCorp B.V.",
            ),
        )

    def test_create_klant_vestigingsnummer(self):
        with requests_mock.mock() as m:
            m.post(
                f"{KLANTEN_ROOT}klanten",
                json=self.data.klant_vestiging,
            )

            klant = self.service.create_klant(vestigingsnummer="123456789000")

        self.assertIsInstance(klant, Klant)
        self.assertEqual(
            m.request_history[0].json(),
            {"subjectIdentificatie": {"vestigingsNummer": "123456789000"}},
        )
        self.assertEqual(
            klant,
            Klant(
                url="https://klanten.nl/api/v1/klant/bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
                bronorganisatie="123456789",
                klantnummer="11111111",
                website_url="",
                voornaam="",
                voorvoegsel_achternaam="",
                achternaam="",
                telefoonnummer="0612345678",
                emailadres="foo@bar.com",
                toestemming_zaak_notificaties_alleen_digitaal=False,
                bedrijfsnaam="AcmeCorp B.V.",
            ),
        )
