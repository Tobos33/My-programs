#include "wektory.h"

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

void test(float a){
    if (!a){
        cout<<"Podany zły typ zmiennej ";
        exit(1);
    }
}