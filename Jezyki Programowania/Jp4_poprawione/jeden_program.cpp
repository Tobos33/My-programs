#include "parabola.h"
#include <cmath>

int Parabola::counter = 0;
int Point::counter = 0;

Point::Point(){
    x = 0;
    y = 0;
    counter++;
}

Point::Point(float &a, float &b){
    x = a;
    y = b;
    counter++;
}

Parabola::Parabola(){
    a = 0;
    b = 0;
    c = 0;   
    counter++;
}

Parabola::Parabola(Point p1, Point p2, Point p3){
    a = ((p1.y - p2.y)*(p1.x-p3.x)/(p1.x-p2.x)-p1.y+p3.y)/((pow(p1.x, 2)-pow(p2.x,2))*(p1.x-p3.x)/(p1.x - p2.x)-pow(p1.x,2)+pow(p3.x,2));
    b = (p1.y - p3.y)/(p1.x-p3.x) - a*((pow(p1.x, 2)-pow(p3.x, 2))/(p1.x - p3.x));
    c = p1.y - b*p1.x -a*pow(p1.x, 2);
    counter++;
}

void allow(Point p1, Point p2, Point p3){
    if (pow(p1.x,2)*(p2.x-p3.x)+ pow(p2.x,2)*(p3.x-p1.x) +pow(p3.x,2)*(p1.x-p2.x) == 0){
        cout<<"Nie da sie stworzyc paraboli"<<endl;
        exit(1);
    }
}



float y_value(Parabola P, float x){
    float y = P.a*pow(x, 2) +P.b*x +P.c;
    return(y);
}



Parabola::Parabola(Point p1, Parabola &par){
    a = 0;
    b = 2*par.a*p1.x + par.b;
    c = p1.y - (2*par.a*p1.x + par.b)*p1.x;
    counter++;
}


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