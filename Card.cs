/*This is the template for a Card object. It is responsible for tracking
the suite and value of the Card.*/
using System;

public class Card{

    private string _suite;
    private string _value;

    public Card (string s, string v){
        _suite = s;
        _value = v;
    }

    //Display suite then value
    public string Display(string padding=""){
        return _suite+padding+_value;
    }
    //dispaly value then suite
    public string DisplayReverse(string padding=""){
        return _value+padding+_suite;
    }
}