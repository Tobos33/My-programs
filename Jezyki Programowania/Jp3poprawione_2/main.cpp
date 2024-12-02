#include "wektory.h"

int main(){
    float x, y, z;
    cout<<"Podaj wspolrzedne punktu"<<endl;
    cin>>x;
    test();
    cin>>y;
    test();
    cin>>z;
    test();
    Punkt p1( x, y, z);
    cout<<"Podaj wspolrzedne punktu"<<endl;
    cin>>x;
    test();
    cin>>y;
    test();
    cin>>z;
    test();
    Punkt p2(x,y,z);
    p1.Przedstaw();
    p2.Przedstaw();
    Wektor w(p1,p2);
    w.Przedstaw();
    float L;
    L = w.Dlugosc();
    cout<<"Dlugosc wektora jest rowna "<<L<<endl;
}