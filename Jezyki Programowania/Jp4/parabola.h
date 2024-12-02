#include <iostream>
#include <cmath>
using namespace std;

class Parabola;

class Point {
    float x,y;
    static int counter;
    public:
    Point();
    Point(float,float);
    ~Point(){};
    void print(){cout<<"x="<<x<<"   "<<"y="<<y<<endl;};
    float y_value(Parabola);
    static void number(){cout<<counter<<endl;}
    friend class Parabola;
    friend void allow(Point, Point, Point);
};
void allow(Point, Point, Point);

class Parabola {
    float a,b,c;
    static int counter;
    public:
    Parabola();
    Parabola(Point, Point, Point);
    ~Parabola(){};
    void print(){cout<<a<<"x^2"<<b<<"x"<<c<<endl;};
    void count(Point, Point, Point);
    static void number(){cout<<counter<<endl;};
    friend class Point;
};