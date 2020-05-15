from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WordConfig(AppConfig):
    name = "recitewords.word_book"
    verbose_name = _("word_book")

    def ready(self):
        try:
            import recitewords.users.signals  # noqa F401
        except ImportError:
            pass
