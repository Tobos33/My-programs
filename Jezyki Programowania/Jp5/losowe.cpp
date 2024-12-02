#include "losowe.h"
#include "cmath"

Generator::Generator(){
    N = 0;
    w1 = 0;
    w2 = 0;
    w3 = 0;
    long seed = 0;
    tab = {};
}

Generator::Generator(long a, long b, long c, long d, long e){
    N = a;
    w1 = b;
    w2 = c;
    w3 = d;
    tab = new double[N];
    seed = e;
}

Histogram::Histogram(){
    histo ={};
}

void generacja(Generator gen){
    gen.tab[0] = (double)gen.seed;
    for(int i = 0; i < gen.N; i++){
        gen.tab[i+1] = (double)((gen.w1*((int)gen.tab[i]+gen.w2)) % gen.w3);}

}

void skalowanie(Generator gen){
    for(int i = 0; i < gen.N; i++){
        gen.tab[i] = gen.tab[i]/gen.tab[gen.N];
    }
}