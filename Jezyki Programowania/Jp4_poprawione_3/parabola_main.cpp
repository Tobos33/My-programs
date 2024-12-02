#include "parabola.h"

int main(){
    float *x,*y;
    x = new float;
    y = new float;
    cout<<"Podaj trzy punkty"<<endl;
    cout<<"Punkt pierwszy"<<endl;
    cin>>*x>>*y;
    Point p1(*x,*y);
    cout<<"Punkt drugi"<<endl;
    cin>>*x>>*y;
    Point p2(*x,*y);
    cout<<"Punkt trzeci"<<endl;
    cin>>*x>>*y;
    Point p3(*x,*y);
    allow(p1, p2, p3);
    p1.print();
    p2.print();
    p3.print();
    Parabola par(p1, p2, p3);
    par.print();
    cout<<"Podaj wartość odciętej, dla punktu styczności"<<endl;
    cin>>*x;
    *y = y_value(par, *x);
    Point tangent_p(*x,*y);
    cout<<"Punkt styczności: ";
    tangent_p.print();
    Parabola tangent(tangent_p, par);
    tangent.print_tangent();
    tangent_p.amount();
    tangent.amount();
}