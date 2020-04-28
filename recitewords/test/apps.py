from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TestConfig(AppConfig):
    name = "recitewords.test"
    verbose_name = _("Test")

    def ready(self):
        try:
            import recitewords.users.signals  # noqa F401
        except ImportError:
            pass
