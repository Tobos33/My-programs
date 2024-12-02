#include "Daty.h"

int LiczDni(Date d1, Date d2){
    int IleDni = 0;
    if(d1.year >= d2.year){
        IleDni = IleDni + (d1.year - d2.year)*365;
        if(d1.month > d2.month){
            IleDni = IleDni + (d1.month - d2.month)*30 + (30 - d1.day) + (30 - d2.day);}
        else if (d1.month == d2.month){
            if (d1.day >= d2.day)
                IleDni = IleDni + d1.day - d2.day;
            else
                IleDni = IleDni + d2.day - d1.day;}
        else if (d2.month > d1.month){
            IleDni = IleDni + (d2.month - d1.month)*30; + (30 - d1.day) + (30 - d2.day);}}
    else{
        IleDni = IleDni + (d2.year - d1.year)*365;
        if(d1.month > d2.month){
            IleDni = IleDni + (d1.month - d2.month)*30;}
        else if (d1.month == d2.month){
            if (d1.day >= d2.day)
                IleDni = IleDni + d1.day - d2.day;
            else
                IleDni = IleDni + d2.day - d1.day;}
        else if (d2.month > d1.month){
            IleDni = IleDni + (d2.month - d1.month)*30;}}
    return IleDni;
    /*if (abs(d1.year - d2.year) > 4){
        IleDni = IleDni + (abs(d1.year - d2.year) - Rokprzes(d1.year))%4;
    }*/

}
