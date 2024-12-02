#include "Daty.h"

int main(){
    Date d1, d2;
    int Dni;
    d1.readDate();
    d2.readDate();
    d1.printDate();
    d2.printDate();
    Dni = LiczDni(d1, d2);
    cout<<"Liczba dni "<< Dni<<endl;
}