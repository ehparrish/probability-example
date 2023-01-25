import Coin
import Die
import Deck

class GameRunner:
    def __init__(self):
        self.coin = Coin.Coin()
        self.die = Die.Die()
        self.deck = Deck.Deck()
        self.coinPoints = 1;
        self.dicePoints = 2;
        self.cardPoints = 5;

    def play_coin_game(self, points):
        return points

    def play_dice_game(self, points):
        return points

    def play_card_game(self, points):
        play_again = 'Y'
        self.deck.shuffle_all()
        while play_again != 'N':
            print("\nDealing card")
            first_card = self.deck.draw_and_discard()
            print(first_card.display_reverse(" of "))
            second_card = self.deck.draw_and_discard()
            print(second_card.display_reverse(" of "))
            print("Do you think the next card will be higher (>), lower (<), or the same (=) ?")
            print("Enter >, <, or = : ")
            choice = GameRunner.get_compare()
            print("Next Card!")
            print(second_card.display_reverse(' of '))
            win = False
            if (choice == '<' and Deck.Deck.compare(first_card, second_card) == Deck.Comparator.LESS):
                win = True
            elif (choice == '=' and Deck.Deck.compare(first_card, second_card) == Deck.Comparator.EQUAL):
                win = True
            elif (choice == '>' and Deck.Deck.compare(first_card, second_card) == Deck.Comparator.GREATER):
                win = True

            if win:
                points += self.cardPoints
                print("You win!  You now have {points} points!")
            else:
                points -= self.cardPoints
                print("You lose!  You now have {points} pionts!")

            if points < self.cardPoints:
                play_again = 'N'
                print("Sorry. You don't have enough points to keep playing.")
            else:
                print("Would you like to play again?  Y or N: ")
                play_again = GameRunner.get_y_or_n()

        return points

    def get_compare():
        choice = input()
        while choice not in ('>', '=', '<'):
            print("Please enter >, <, or =: ")
        return choice

    def get_y_or_n():
        choice = input().upper()
        while choice not in ('Y', 'N'):
            print("Please enter Y or N: ")
            choice = input().upper()
        return choice

