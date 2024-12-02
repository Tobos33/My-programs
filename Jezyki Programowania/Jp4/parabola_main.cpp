#include "parabola.h"

int main(){
    float x,y;
    cout<<"Podaj trzy punkty"<<endl;
    cout<<"Punkt pierwszy"<<endl;
    cin>>x>>y;
    Point p1(x,y);
    cout<<"Punkt drugi"<<endl;
    cin>>x>>y;
    Point p2(x,y);
    cout<<"Punkt trzeci"<<endl;
    cin>>x>>y;
    Point p3(x,y);
    allow(p1, p2, p3);
    p1.print();
    p2.print();
    p3.print();
    Parabola par(p1, p2, p3);
    par.print();
}