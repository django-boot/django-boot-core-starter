from django.test import TestCase
from rhazes.context import ApplicationContext

from django_boot_core.services.config import ApplicationConfiguration


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
