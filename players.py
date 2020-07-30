from enum import Enum
from typing import List

from cards import Hand, Card


PositionEnum = Enum("PlayersEnum", ['N', 'E', 'S', 'W'])

POSITIONS = list(PositionEnum)

TEAMS = [(PositionEnum.N, PositionEnum.S),
         (PositionEnum.W, PositionEnum.E)]

class Player:

    def __init__(self, position: PositionEnum, hand: Hand):
        self.position = position
        self.hand = hand

    def play_card(self, card: Card):
        self.hand.play_card(card)

    def get_legal_actions(self, trick):
        pass

    def __str__(self):
        return self.position.name

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self) -> int:
        return hash(self.position)

class Team:

    def __init__(self, p0: Player, p1: Player):
        self.players = [p0, p1]
        self.teammate = {p0.position: p1, p1.position: p0}

    def __str__(self):
        return f"{self.players[0]}{self.players[1]}"

    def has_player(self, p: Player) -> bool:
        """

        :param p:
        :return:
        """
        return p in self.players

    def get_players(self) -> List[Player]:
        """

        :return:
        """
        return self.players

    def get_teammate(self, p: Player) -> Player:  # todo [ORIYAN] Possibly remove?
        """

        :param p:
        :return:
        """
        assert (p in self.players)
        return self.teammate[p.position]
