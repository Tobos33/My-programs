#include "wektory.h"
#include <cmath>
#include <string>


Punkt::Punkt(){
    mX = 0;
    mY = 0;
    mZ = 0;
}

Punkt::Punkt(float a, float b, float c){
    mX = a;
    mY = b;
    mZ = c;
}

Wektor::Wektor(){
    mA = 0;
    mB = 0;
    mC = 0;   
}

Wektor::Wektor(Punkt p1, Punkt p2){
    mA = p1.mX - p2.mX;
    mB = p1.mY - p2.mY;
    mC = p1.mZ - p2.mZ;

}

void test(){
    if (!cin){
    cout<<"Podany zły typ zmiennej ";
    exit(1);
    }
}



int main(){
    float x, y, z, a, b, c, liczba;
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