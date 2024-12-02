#include"macierz.h"

float tab[N1][N1];

int main(){


    for(int i = 0; i<N1; i++){
        cout<<"Podaj "<<i+1<<" rząd pierwszej macierzy "<<N1<<" na "<<N1<<endl;
        for(int j = 0; j<N1; j++){
            cin>>tab[i][j];
        }

    }
    Macierz macierz1(tab);

    for(int i = 0; i<N1; i++){
        cout<<"Podaj "<<i+1<<" rząd drugiej macierzy "<<N1<<" na "<<N1<<endl;
        for(int j = 0; j<N1; j++){
            cin>>tab[i][j];
        }

    }
    Macierz macierz2(tab);
    Macierz macierz3;
    Macierz macierz4;
    Macierz macierz5;
    //cout<<macierz1;
    //cout<<macierz2;
    macierz3 = macierz1 + macierz2;
    cout<<"dodawanie"<<endl<<macierz3;
    macierz4 = macierz2 - macierz1;
    cout<<"odejmowanie"<<endl<<macierz4;
    macierz5 = macierz1*macierz2;
    cout<<"mnożenie"<<endl<<macierz5;
    //cout<<macierz1;
    //cout<<macierz2;
}