#include <iostream>
using namespace std;

class Date{
    int year, month, day;

    public:
    void readDate() {cin>>year>>month>>day;}
    void printDate() {cout<<year<<" "<<month<<" "<<day<<endl;}
    /*int Rokprzes(Date) {
        int lata;
        lata = year % 4;
        return lata;
    };*/
    friend int LiczDni(Date, Date);
};

int LiczDni(Date, Date);
