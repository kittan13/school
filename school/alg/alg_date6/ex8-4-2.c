#include<stdio.h>

double RoundHalfUp(double a){
    int b;
    b = ((a+5)/10);

    int c;
    c = b*10;

    return c;
}

int main(){
    double x = 31.4,y=27.1828;
    printf("%fを1の位で四捨五入すると%fである。\n",x,RoundHalfUp(x));
    printf("%fを1の位で四捨五入すると%fである。\n",y,RoundHalfUp(y));
    return(0);
}