#include<stdio.h>

double RoundHalfUp(double a){
    int b;
    b = (a+0.5);
    return b;
    //return(int)(a+0.5);
}

int main(){
    double x = 3.14,y=2.81828;
    printf("%fを小数点以下第一位で七捨八入すると%fである。\n",x,RoundHalfUp(x));
    printf("%fを小数点以下第一位で七捨八入すると%fである。\n",y,RoundHalfUp(y));
    return(0);
}