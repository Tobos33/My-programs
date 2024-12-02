#include "macierz.h"


Macierz::Macierz(){
    mac = new float *[N1];
    for(int i = 0; i<N1; i++){
        *(mac + i) = new float[N1];
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
Macierz::Macierz(const Macierz& m){
    mac = new float *[N1];
    for(int i = 0; i<N1; i++){
        mac[i] = new float[N1];
        for(int j = 0; j<N1; j++){
            mac[i][j] = m.mac[i][j];
        }
    } 
}

Macierz::~Macierz(){

}

Macierz operator+(Macierz m1, Macierz m2){
    Macierz macierz1;

    for(int i = 0; i<N1; i++){
        for(int j = 0; j<N1;j++ ){
            macierz1.mac[i][j] = m1.mac[i][j] + m2.mac[i][j];
        }
    }
    //Macierz &macierz2 = macierz1;
    return macierz1;
    
}

Macierz operator-(Macierz m1, Macierz m2){ 
    Macierz macierz1;

    for(int i = 0; i<N1; i++){
        for(int j = 0; j<N1;j++ ){
            macierz1.mac[i][j] = m1.mac[i][j] - m2.mac[i][j];
        }
    }
    //Macierz &macierz2 = macierz1;
    return macierz1;
}

Macierz operator*(Macierz m1, Macierz m2){ 
    Macierz macierz1;
    for(int i = 0; i<N1; i++){
        for(int j = 0; j<N1;j++ ){
            macierz1.mac[i][j] = 0;
        }
    }

    for(int i = 0; i<N1; i++){
        for(int j = 0; j<N1;j++ ){
            for(int k = 0; k<N1; k++){
            macierz1.mac[i][j] += (m1.mac[i][k]*m2.mac[k][j]);
            }
            
        }
        
    }
    //Macierz &macierz2 = macierz1;
    return macierz1;
}

ostream& operator<<(ostream& out, Macierz& m){
    out<<endl;
    for(int i = 0; i<N1; i++){
        out<<"| ";
        for(int j = 0; j<N1; j++)
            out<<m.mac[i][j]<<" "; 
        out<<"|"<<endl;
    }
    out<<endl;
    
    return out;  
}

Macierz& Macierz::operator=(const Macierz& m){
    if(&m == this) return *this;
    delete [] mac;
    mac = new float *[N1];
    for(int i = 0; i<N1; i++){
        *(mac + i) = new float[N1];
    }
    mac = m.mac;
    cout<<"przypisanie"<<endl;
    return *this;
}




