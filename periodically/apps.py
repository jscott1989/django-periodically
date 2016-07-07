from __future__ import \
    unicode_literals, print_function, division, absolute_import

from django.apps import AppConfig

from periodically import autodiscover


class PeriodicallyConfig(AppConfig):
    name = 'periodically'

    def ready(self):
        autodiscover()
