/*This is the temple for a Coin object. It is resposible to knowing if heads is showing,
flipping the coin and displaying the value.*/

using System;

public class Coin{

    private bool _headsUp;
    private static Random rnd = new Random();
    
    public Coin(){
        this.Flip();
    }
    public bool Flip(){
        _headsUp = (rnd.Next(0,2)>0);    
        return _headsUp;
    } 

    public string Display(){
        if (_headsUp){
            return "HEADS";
        }
        else
            return "TAILS";
    }
}