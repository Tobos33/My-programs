#include <iostream>
#include <cmath>
using namespace std;

class Parabola;

class Point {
    float *x;
    float *y;
    static int counter;
    public:
    //Point();
    Point(float = 0,float = 0);
    Point(const Point &);
    ~Point();
    void print(){cout<<"x="<<*x<<"   "<<"y="<<*y<<endl;};
    static void amount(){cout<<"Liczba elementów klasy Point: "<<counter<<endl;};
    friend class Parabola;
    friend void allow(Point, Point, Point);
};
void allow(Point, Point, Point);
float y_value(Parabola, float);


class Parabola {
    float *a;
    float *b;
    float *c;
    static int counter;
    public:
    //Parabola();
    Parabola(Point = 0, Point = 0, Point = 0);
    Parabola(const Parabola &);
    Parabola(Point, Parabola);
    ~Parabola();
    void print(){cout<<*a<<"x^2 + ("<<*b<<")x + ("<<*c<<")"<<endl;};
    void print_tangent(){cout<<*b<<"x + ("<<*c<<")"<<endl;};
    void count(Point, Point, Point);
    static void amount(){cout<<"Liczba elementów klasy Parabola: "<<counter<<endl;};
    friend class Point;
    friend float y_value(Parabola, float);
};