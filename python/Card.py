
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def Display(self, padding=" "):
        return f"{self.suit}{padding}{self.value}"

    def DisplayReverse(self, padding=" "):
        return f"{self.value}{padding}{self.suit}"

