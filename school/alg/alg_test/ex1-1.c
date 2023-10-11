#include<stdio.h>

int main(){
    int a = 2;
    double b = 38.123;
    b *= (a++) / 2 + a;
    printf("%.3f\n",b);
    return(0);
}