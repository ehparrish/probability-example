using System;

public class Deck{

    public static readonly string []SUITE_LIST = {"Spade","Heart","Club","Diamond"};
    public static readonly string []VALUE_LIST = {"A","2","3","4","5","6","7","8","9","10","J","Q","K"};
    private static Random rnd = new Random();

    private List<Card> _deck=new List<Card>();
    private List<Card> _discard=new List<Card>();

    public Deck(){
        foreach (var s in SUITE_LIST){
            foreach (var v in VALUE_LIST){
                _deck.Add(new Card(s,v));
            }
        }
        Shuffle();
    }

    //Implents the Fisher Yates algorithm
    public void Shuffle()Console.WriteLine("Done shuffling");{
        for (int i = _deck.Count-1; i > 0; i--){
            int randomIndex = rnd.Next(0, i + 1);
        
            var temp = _deck[i];
            _deck[i] = _deck[randomIndex];
            _deck[randomIndex] = temp;
        }
        Console.WriteLine("Done shuffling");
    }
}