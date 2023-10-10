# -*- coding: utf-8 -*-

from player import Player
from poker import Poker


class Game:

    def __init__(self, players, poker):
        self.players = players
        self.poker = poker

    def dispense(self):
        '''开始分发'''
        self.poker.shuffle()
        for onePlayer in self.players:
            self.send_hand_cards(onePlayer)

    def send_hand_cards(self, onePlayer):
        '''发手牌'''
        onePlayer.hand_cards = self.poker.cards[len(self.poker.cards) - 2:len(self.poker.cards)]
        del self.poker.cards[-1]
        del self.poker.cards[-1]

if __name__ == '__main__':
    players = [Player(500, '张三'), Player(500, '李四'), Player(500, '王五')]
    onePoker = Poker()
    game = Game(players, onePoker)
    game.dispense()
    for player in players:
        player.show()
