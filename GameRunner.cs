/*This is the template for a GameRunner object. It is responsible for running
all of the games.*/

public class GameRunner{

    private Coin coin = new Coin();
    private int coinPoints = 1;

    
    private string getYN(){
        string choice = Console.ReadLine().ToUpper();
        while (choice != "Y" && choice != "N"){
            Console.Write("Please enter Y or N: ");
            choice = Console.ReadLine().ToUpper();
        } 
        return choice;

    }
    public int CoinGame(int points){
        string playAgain = "Y";
        while (playAgain != "N"){
            Console.WriteLine("\nFlipping coin!");
            bool firstFlip = coin.Flip();
            Console.WriteLine(coin.Display());
            Console.Write("Do you think the next coin flip will be the same? Y or N: ");
            string bet = getYN();
            Console.WriteLine("Flipping again!");
            bool secondFlip = coin.Flip();
            Console.WriteLine(coin.Display());
            if(bet == "Y"){
                if(firstFlip == secondFlip){
                    points += coinPoints;
                    Console.WriteLine($"You win! You now have {points} points!");
                }
                else{
                    points -= coinPoints;
                    Console.WriteLine($"You lose! You now have {points} points!");
                }
            }
            else{
                if(firstFlip != secondFlip){
                    points += coinPoints;
                    Console.WriteLine($"You win! You now have {points} points!");
                }
                else{
                    points -= coinPoints;
                    Console.WriteLine($"You lose! You now have {points} points!");
                }
            }

            if(points < coinPoints){
                playAgain = "N";
                Console.WriteLine("Sorry. You don't have enough points to keep playing.");
            }
            else{
                Console.Write("Would you like to play again? Y or N: ");
                playAgain = getYN();
            }
        }
        return points;
    }
}