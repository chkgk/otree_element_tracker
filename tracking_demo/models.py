from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

# django models for BigInteger
from django.db import models as django_models

author = 'Christian König gen. Kersting'

doc = """
Demo of element hover tracking using oTree 2.6b0
"""


class Constants(BaseConstants):
    name_in_url = 'tracking_demo'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def store_tracking_data(self, id_in_group, payload):
        HoverEvent.objects.create(
            player=self.get_player_by_id(id_in_group),
            element_id=payload["element_id"],
            enter_time=payload["enter_time"],
            leave_time=payload["leave_time"]
        )

class Player(BasePlayer):
    pass


class HoverEvent(models.ExtraModel):
    player = models.Link(Player)
    element_id = models.StringField()
    enter_time = django_models.BigIntegerField()
    leave_time = django_models.BigIntegerField()

def custom_export(players):
    yield ["session", "participant_code", "round_number", "id_in_group", "element_id", "enter_time", "leave_time"]
    for e in HoverEvent.objects.all():
        yield [
            e.player.session.code,
            e.player.participant.code,
            e.player.round_number,
            e.player.id_in_group,
            e.element_id,
            e.enter_time,
            e.leave_time
        ]