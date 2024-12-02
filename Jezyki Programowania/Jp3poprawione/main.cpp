#include "wektory.h"

int main(){
    float x, y, z, a, b, c, liczba;
    cout<<"Podaj wspolrzedne punktu"<<endl;
    cin>>x;
    test(x);
    cin>>y;
    test(y);
    cin>>z;
    if (!z){
        cout<<"Podany zły typ zmiennej ";
        return 1;
    }
    Punkt p1( x, y, z);
    cout<<"Podaj wspolrzedne punktu"<<endl;
    cin>>x;
    test(x);
    cin>>y;
    test(y);
    cin>>z;
    test(z);
    Punkt p2(x,y,z);
    cin>>liczba;
    p1.Przedstaw();
    p2.Przedstaw();
    Wektor w(p1,p2);
    w.Przedstaw();
    float L;
    L = w.Dlugosc();
    cout<<"Dlugosc wektora jest rowna "<<L<<endl;
}