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

/*Generator::~Generator(){
    delete [] tab;
}*/

Histogram::Histogram(){
    histo = new int[span];
}

/*Histogram::~Histogram(){
    delete [] histo;
}*/


void generacja(Generator gen){
    gen.tab[0] = (double)gen.seed;
    for(int i = 0; i < gen.N; i++){
        gen.tab[i+1] = (double)((gen.w1*((int)gen.tab[i]+gen.w2)) % gen.w3);}

}

void skalowanie(Generator gen){
    if(gen.w1 >= gen.w2 && gen.w1 >= gen.w2){
        for(int i = 0; i <= gen.N; i++){
            gen.tab[i] /= gen.w1;
        }}
    else if(gen.w2 >= gen.w1 && gen.w2 >= gen.w3){
        for(int i = 0; i <= gen.N; i++){
            gen.tab[i] /= gen.w2;
        }}
    if(gen.w3 >= gen.w2 && gen.w3 >= gen.w1){
        for(int i = 0; i < gen.N; i++){
            gen.tab[i] /= gen.w3;
        }}
}

void Histogram::fill(Generator gen){
    for(int i = 0; i< span; i++){
        histo[i] = 0;
    }
    for(int i = 0; i < gen.N; i++){
        for(int j = 0; j < span; j++){
            if(gen.tab[i] <= (double)(j+1)/span){
                histo[j] ++;
                break;
            }
        }
    }
};

void Histogram::printhisto(){
    cout<<"---------------- Histogram liczb losowych ----------------"<<endl<<endl<<"  ";
    for(int i = 0; i < span; i++){
        cout<<(double)i/span<<"0 - "<<(double)(i+1)/span<<"   ";
        for(int j = 0; j < histo[i]; j++){
            cout<<"*";
        }
        cout<<endl;
    }
    cout<<"----------------------------------------------------------"<<endl;
};