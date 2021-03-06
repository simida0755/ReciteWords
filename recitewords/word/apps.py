from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WordConfig(AppConfig):
    name = "recitewords.word"
    verbose_name = _("word")

    def ready(self):
        try:
            import recitewords.users.signals  # noqa F401
        except ImportError:
            pass
