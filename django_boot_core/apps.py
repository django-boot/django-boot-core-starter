from django.apps import AppConfig
from rhazes.context import ApplicationContext


class DjangoBootCoreConfig(AppConfig):
    name = "django_boot_core"

    def ready(self):
        ApplicationContext.initialize(["django_boot_core.services"])
