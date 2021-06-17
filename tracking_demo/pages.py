from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Tracker(Page):
    @staticmethod
    def live_method(player, data):
        player.store_tracking_data(data)


page_sequence = [Tracker]
