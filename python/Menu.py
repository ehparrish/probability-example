import GameRunner

GAMES = ['Coin Flip', 'Dice Roll', 'Card Game']

def print_menu(score, points):
    print("You can play:")
    for i, game in enumerate(GAMES):
        if (score >= points[i]):
            print(f"{i+1}. {game} ({points[i]} points)")
    print("0. Quite while you are ahead!")
    print("Please enter the number for your choice: ")

def main():
    player_points = 10
    runner = GameRunner.GameRunner()

    print("Welcome to the Probability Game!");
    choice = -1;
    while (choice != 0 and player_points > 0 and player_points < 100):
        points = [runner.coinPoints, runner.dicePoints, runner.cardPoints]
        print(f'\nYou have {player_points} points.')
        print_menu(player_points, points)
        try:
            choice = int(input())
            if choice < 0 or choice > len(points) or player_points < points[choice-1]:
                raise ValueError
        except:
            print("Please enter a valid choice")
            choice = -1
            continue
        if choice == 0:
            print(f"You quit with {player_points} points.")
        elif choice == 1:
            print("\nCoin Game")
            player_points = runner.play_coin_game(player_points)
        elif choice == 2:
            print("\nDice Game")
            player_points = runner.play_dice_game(player_points)
        elif choice == 3:
            print("\nCard Game")
            player_points = runner.play_card_game(player_points)
    
    if player_points == 0:
        print("Oh no! You lost it all!  Better luck next time!")
    elif  player_points >= 100:
        print("Wow!  You broke the bank!  Congratulations!")

if __name__ == "__main__":
    main()
