#include "parabola.h"
#include <cmath>

Point::Point(){
    x = 0;
    y = 0;
}

Point::Point(float a, float b){
    x = a;
    y = b;
}

Parabola::Parabola(){
    a = 0;
    b = 0;
    c = 0;   
}

Parabola::Parabola(Point p1, Point p2, Point p3){
    a = ((p1.y - p2.y)*(p1.x-p3.x)/(p1.x-p2.x)-p1.y+p3.y)/((pow(p1.x, 2)-pow(p2.x,2))*(p1.x-p3.x)/(p1.x - p2.x)-pow(p1.x,2)+pow(p3.x,2));
    b = (p1.y - p2.y)/(p1.x-p2.x) - a*(pow(p1.x, 2)-pow(p2.x, 2)/(p1.x - p2.x));
    c = p1.y - b*p1.x -a*pow(p1.x, 2);
}

void allow(Point p1, Point p2, Point p3){
    if (pow(p1.x,2)*(p2.x-p3.x)+ pow(p2.x,2)*(p3.x-p1.x) +pow(p3.x,2)*(p1.x-p2.x) == 0){
        cout<<"Nie da sie stworzyc paraboli"<<endl;
        exit(1);
    }
}