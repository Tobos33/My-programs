#include "wektory.h"
#include <stdexcept>
int main(){
    float x, y, z;
    cout<<"Podaj wspolrzedne punktu"<<endl;
    cin>>x>>y>>z;
    try{
        x= x+y+z;
    }
    catch(std::logic_error & )
    {
        std::cout<<"zle parametry"<<endl;
    }
    Punkt p1(x,y,z);
    cout<<"Podaj wspolrzedne punmktu"<<endl;
    cin>>x>>y>>z;
    Punkt p2(x,y,z);
    p1.Przedstaw();
    p2.Przedstaw();
    Wektor w(p1,p2);
    w.Przedstaw();
    float L;
    L = w.Dlugosc();
    cout<<"Dlugosc wektora jest rowna"<<L<<endl;
}