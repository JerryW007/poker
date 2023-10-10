# -*- coding: utf-8 -*-


class Player:
    
    def __init__(self,money,name):
        self.money = money
        self.name = name
        self.hand_cards = []
    def show(self):
        lines = []
        for i in range(7):
            line = []
            for _,card in enumerate(self.hand_cards):
                line.append(' '*2 + card.show().split('\n')[i])
            lines.append(''.join(line) + '\n')
        for index,_ in enumerate(lines):
            if index == 0:
                lines[index] = self.name + ":" + lines[index]
            else:
                lines[index] = ' '* (len(self.name)*2+1) + lines[index]
        print("".join(lines))