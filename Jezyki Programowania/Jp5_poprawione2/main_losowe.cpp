#include "losowe.h"


int main(){
    int a,c,m,seed,N;
    cout<<"Podaj stale"<<endl;;
    cout<<"a: ";
    cin>>a;
    cout<<"c: ";
    cin>>c;
    cout<<"m: ";
    cin>>m;
    cout<<"seed: ";
    cin>>seed;
    cout<<"N: ";
    cin>>N;
    Generator gen(N, a, c, m, seed);
    generacja(gen);
    skalowanie(gen);
    gen.PrintGenerator();
    Histogram h1;
    h1.fill(gen);
    h1.printhisto();

    return 0;
}