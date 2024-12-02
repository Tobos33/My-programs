#include <iostream>
#include <cmath>
#include <string>
using namespace std;
#define N1 2
#define M1
#define N2
#define M2

class Macierz{
    float **mac;
    public:
    Macierz();
    Macierz(float [][N1]);
    Macierz(const Macierz&);
    ~Macierz();
    friend Macierz& operator+(Macierz, Macierz);
    friend Macierz& operator-(Macierz, Macierz);
    friend Macierz& operator*(Macierz, Macierz);
    friend ostream& operator<<(ostream&, Macierz&);
};

Macierz& operator+(Macierz, Macierz);
Macierz& operator-(Macierz, Macierz);
Macierz& operator*(Macierz, Macierz);
ostream& operator<<(ostream&, Macierz&);