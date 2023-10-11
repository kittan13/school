#include<stdio.h>

double RoundHalfUp(double a){
    int b;
    b = a;
    double c;
    c = a-b;
    int d;
    if (c > 0)
        d=a+1;
    else
        d=a;
    return d;
}

int main(){
    double x = 314,y=271828;
    printf("%fを10の位で四捨五入すると%fである。\n",x,RoundHalfUp(x));
    printf("%fを10の位で四捨五入すると%fである。\n",y,RoundHalfUp(y));
    return(0);
}