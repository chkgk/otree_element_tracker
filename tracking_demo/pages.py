from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Tracker(Page):
    live_method = 'store_tracking_data'

page_sequence = [Tracker]
