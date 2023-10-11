#include<stdio.h>

double RoundHalfUp(double a){
    int b;
    b = (a/25 + 0.5);
    int c;
    c = 25*b;
    return c;
}

int main(){
    double x = 314,y=271828;
    printf("%fを10の位で四捨五入すると%fである。\n",x,RoundHalfUp(x));
    printf("%fを10の位で四捨五入すると%fである。\n",y,RoundHalfUp(y));
    return(0);
}