#include <iostream>
#include <cmath>
using namespace std;

class wektor;

class Punkt {
    float mX, mY, mZ;
    public:
    Punkt();
    Punkt(float, float, float);
    ~Punkt(){};
    void Przedstaw(){
    cout<<"Wspolrzedne punktu"<<endl<<"x = "<<mX<<"   "<<"y = "<<mY<<"   "<<"z = "<<mZ<<endl;
};
    friend class Wektor;
};


class Wektor {
    float mA, mB, mC;
    public:
    Wektor();
    Wektor(Punkt, Punkt);
    ~Wektor(){};
    void Przedstaw(){
        cout<<"Skladowe wektora:"<<endl<<"skladowa x = "<<mA<<"   "<<"skladowa y = "<<mB
        <<"   "<<"skladowa z = "<<mC<<endl;
    };
    float Dlugosc(){
        float L = 0;
        L = sqrt(pow(mA, 2) + pow(mB, 2) + pow(mC, 2));
        return L;
    };
};

