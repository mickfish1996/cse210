import random

# TODO: Define the Board class here

class Board():
    def __init__(self):
        self.__piles = []
        self.__prepare()

    def to_string(self):
        piles = "\n--------------------"
        for i in range(len(self.__piles)):
            piles += (f"\n{i}: " + "O " * self.__piles[i])

        piles += "\n--------------------"
        return piles

    def apply(self, move):
        pile = move.get_pile()
        stone = move.get_stones()
        
        if stone >= self.__piles[pile]:
            self.__piles.pop(pile)
        else:
            self.__piles[pile] -= stone


    def is_empty(self):
        size = len(self.__piles)
        if size == 0:
            return True

    def __prepare(self):
        
        piles = random.randint(2,5)
        for i in range(piles):
            stone = random.randint(1,9)
            self.__piles.append(stone)

