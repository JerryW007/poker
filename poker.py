# -*- coding: utf-8 -*-

import random

class Item:
    '''每张牌'''
    def __init__(self, num, suit):
        self.num = num # 点数
        self.suit = suit # 花色    
    
    
    def show(self):
        reverse_symbol = {'A':'∀','K':'ʞ'}
        num = self.num
        suit = self.suit
        if num == 10:
            SHOW_MODEL = f'┏-------┓\n' \
                f'|{num}     |\n' \
                f'|       |\n' \
                f'|   {suit}   |\n' \
                f'|       |\n' \
                f'|     {num}|\n' \
                f'┗-------┛\n' 
        else:
            SHOW_MODEL = f'┏-------┓\n' \
                    f'|{num}      |\n' \
                    f'|       |\n' \
                    f'|   {suit}   |\n' \
                    f'|       |\n' \
                    f'|      {num}|\n' \
                    f'┗-------┛\n' 
        return SHOW_MODEL
    

class Poker:
            
    def __init__(self):
        self.cards = []
        for suit in ['♠','♥','♣','♦']:
            for i in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']:
                self.cards.append(Item(i,suit))
    
    def shuffle(self):
        '''洗牌'''
        temp = []
        while len(self.cards) > 0:
            index = random.randint(0,len(self.cards)-1)
            temp.append(self.cards[index])
            del self.cards[index]       
        self.cards = temp
            
if __name__ == '__main__':
    poker = Poker()
    poker.shuffle()
    for i in poker.cards:
        print(f'花色:{i.suit},点数:{i.num}')