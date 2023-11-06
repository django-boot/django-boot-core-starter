from django.test import TestCase
from rhazes.context import ApplicationContext

from django_boot_core.services.config import ApplicationConfiguration
from tests.polls_starter.services import PollService
from tests.services.samples import SampleServiceA


class ApplicationContextTestCase(TestCase):
    def test_application_configuration_bean_exists(self):
        application_configuration: ApplicationConfiguration = (
            ApplicationContext.get_bean(ApplicationConfiguration)
        )
        self.assertIsNotNone(application_configuration)
        foo = application_configuration.read_configuration_variable("foo")
        zoo = application_configuration.read_configuration_variable("zoo")
        self.assertEqual(foo, "bar")
        self.assertEqual(zoo, True)

    def test_di_scan_starters(self):
        self.assertIsNotNone(ApplicationContext.get_bean(PollService))

    def test_di_scan_packages(self):
        self.assertIsNotNone(ApplicationContext.get_bean(SampleServiceA))
