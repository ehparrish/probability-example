import Coin
import Die
import Deck

class GameRunner:
    def __init__(self):
        self.__coin = Coin.Coin()
        self.__die = Die.Die()
        self.__deck = Deck.Deck()
        self.coinPoints = 1;
        self.dicePoints = 2;
        self.cardPoints = 5;

    def play_coin_game(self, points):
        return points

    def play_dice_game(self, points):
        return points

    def play_card_game(self, points):
        return points
