#include "macierz.h"


Macierz::Macierz(){
    for(int i = 0; i<N1; i++){
        mac[i] = new float[N1];
    }
}

Macierz::Macierz(float tab[][N1]){
    mac = new float *[N1];
    
    for(int i = 0; i<N1; i++){
        mac[i] = new float[N1];
        for(int j = 0; j<N1; j++){
            mac[i][j] = tab[i][j];
        }
    }
}
Macierz::Macierz(Macierz& m){
       for(int i = 0; i<N1; i++){
        mac[i] = new float[N1];
        for(int j = 0; j<N1; j++){
            mac[i][j] = m.mac[i][j];
        }
    } 
}

Macierz::~Macierz(){
    for(int i = 0; i<N1; i++){
        delete [] mac[i];
    }
}

Macierz& operator+(Macierz m1, Macierz m2){
    for(int i = 0; i<N1; i++){
        for(int j = 0; j<N1;j++ ){
            m1.mac[i][j] += m2.mac[i][j];
        }
    }
    return m1;
    
}

Macierz& operator-(Macierz m1, Macierz m2){
    for(int i = 0; i<N1; i++){
        for(int j = 0; j<N1;j++ ){
            m1.mac[i][j] -= m2.mac[i][j];
        }
    }
    return m1;
}

ostream& operator<<(ostream& out, Macierz& m){
    string str = "<<m.mac[0]<<";
    for(int i = 1; i<N1; i++){
        out<<"Macierz:("<<m.mac[i]<<endl<<")";
        
    }
    return out;  
}



