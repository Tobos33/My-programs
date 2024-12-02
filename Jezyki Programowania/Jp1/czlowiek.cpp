#include "Czlowiek.h"

void Czlowiek::Dodaj(){
    cout<<"Podaj Imie"<<endl;
    cin>>Imie;
    cout<<"Podaj Nazwisko"<<endl;
    cin>>Nazwisko;
    cout<<"Podaj Rok"<<endl;
    cin>>Rok;
    cout<<"Podaj Grupa"<<endl;
    cin>>Grupa;
}

void Czlowiek::Wypisz(){
    cout<<Imie<<"   "<<Nazwisko<<"   "<<Rok<<"   "<<Grupa<<endl;
    //cout<<Nazwisko<<endl;
    //cout<<Rok<<endl;
    //cout<<Grupa<<endl;
}