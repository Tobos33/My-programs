#include <iostream>
#include <cmath>
using namespace std;

class Parabola;

class Point {
    float x,y;
    static int counter;
    public:
    Point();
    Point(float ,float);
    ~Point(){counter--;};
    void print(){cout<<"x="<<x<<"   "<<"y="<<y<<endl;};
    static void amount(){cout<<"Liczba elementów klasy Point: "<<counter<<endl;};
    friend class Parabola;
    friend void allow(Point, Point, Point);
};
void allow(Point, Point, Point);
float y_value(Parabola, float);


class Parabola {
    float a,b,c;
    static int counter;
    public:
    Parabola();
    Parabola(Point, Parabola );
    Parabola(Point, Point, Point);
    ~Parabola(){counter--;};
    void print(){cout<<a<<"x^2 + ("<<b<<")x + ("<<c<<")"<<endl;};
    void print_tangent(){cout<<b<<"x + ("<<c<<")"<<endl;};
    void count(Point, Point, Point);
    static void amount(){cout<<"Liczba elementów klasy Parabola: "<<counter<<endl;};
    friend class Point;
    friend float y_value(Parabola, float);
};