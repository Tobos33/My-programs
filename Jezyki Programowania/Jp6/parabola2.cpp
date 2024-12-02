#include "parabola2.h"
#include <cmath>

int Parabola::counter = 0;
int Point::counter = 0;
/*
Point::Point(){
    x = new float;
    y = new float;
    counter++;
}
*/
Point::Point(float a, float b){
    x = new float;
    y = new float;
    *x = a;
    *y = b;
    counter++;
}

Point::~Point(){
    delete  x;
    delete  y;
    counter--;
}

Point::Point(const Point &p){
    x = new float;
    y = new float;
    *x = *p.x;
    *y = *p.y;
    counter++;
}
/*
Parabola::Parabola(){
    a = new float;
    b = new float;
    c = new float;
    counter++;
}
*/


Parabola::Parabola(Point p1, Point p2, Point p3){
    a = new float;
    b = new float;
    c = new float;
    *a = ((*p1.y - *p2.y)*(*p1.x-*p3.x)/(*p1.x-*p2.x)-*p1.y+*p3.y)/((pow(*p1.x, 2)-pow(*p2.x,2))*(*p1.x-*p3.x)/(*p1.x - *p2.x)-pow(*p1.x,2)+pow(*p3.x,2));
    *b = (*p1.y - *p3.y)/(*p1.x-*p3.x) - (*a)*((pow(*p1.x, 2)-pow(*p3.x, 2))/(*p1.x - *p3.x));
    *c = (*p1.y) - (*b)*(*p1.x) -(*a)*pow(*p1.x, 2);
    counter++;
}

Parabola::Parabola(const Parabola &p){
    a = new float;
    b = new float;
    c = new float;
    *a = *p.a;
    *b = *p.b;
    *c = *p.c;
    counter++;
}

Parabola::~Parabola(){
    delete  a;
    delete  b;
    delete  c;
    counter--;
}


void allow(Point p1, Point p2, Point p3){
    if (pow(*p1.x,2)*(*p2.x-*p3.x)+ pow(*p2.x,2)*(*p3.x-*p1.x) +pow(*p3.x,2)*(*p1.x-*p2.x) == 0){
        cout<<"Nie da sie stworzyc paraboli"<<endl;
        exit(1);
    }
}



float y_value(Parabola P, float x){
    float y = (*P.a)*pow(x, 2) +(*P.b)*x +*P.c;
    return(y);
}


Parabola::Parabola(Point p1, Parabola par){
    a = new float;
    b = new float;
    c = new float;
    *a = 0;
    *b = 2*(*par.a)*(*p1.x) + *par.b;
    *c = *p1.y - (2*(*par.a)*(*p1.x) + *par.b)*(*p1.x);
    counter++;
}