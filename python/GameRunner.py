import Coin
import Die
import Deck

class GameRunner:
    def __init__(self):
        self.__coin = Coin()
        self.__die = Die()
        self.__deck = Deck()
        self.coinPoints = 1;
        self.dicePoints = 2;
        self.cardPoints = 5;

    def play_coin_game(self):
        pass

    def play_dice_game(self):
        pass

    def play_card_game(self):
        pass
