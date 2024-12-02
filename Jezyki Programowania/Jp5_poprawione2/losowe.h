#include <iostream>
#include <cmath>
using namespace std;

class Generator{
    long N;
    double *tab;
    long w1, w2, w3;
    long seed;
    public:
    Generator();
    Generator(long, long, long, long, long);
    ~Generator(){};
    void PrintGenerator(){for(int i = 0; i < N; i++){cout<<tab[i]<<endl;}};
    friend void generacja(Generator);
    friend void skalowanie(Generator);
    friend class Histogram;
};

void generacja(Generator);
void skalowanie(Generator);


class Histogram{
    int span = 20;
    public:
    int *histo;
    Histogram();
    ~Histogram(){};
    void fill(Generator);
    void printhisto();

};

