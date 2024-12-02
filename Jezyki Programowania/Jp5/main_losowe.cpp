#include "losowe.h"

int main(){
    int a,c,m,seed,N;
    cout<<"Podaj stale";
    cout<<endl<<"a";
    cin>>a;
    cout<<endl<<"c";
    cin>>c;
    cout<<endl<<"m";
    cin>>m;
    cout<<endl<<"seed";
    cin>>seed;
    cout<<endl<<"N";
    cin>>N;
    Generator gen(N, a, c, m, seed);
    generacja(gen);
    skalowanie(gen);
    gen.PrintGenerator();
}