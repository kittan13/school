#include<stdio.h>

double RectangleAreaSize(double a,double b){
    return(a*b);
}

int main(){
    double x=10,y=20;
    printf("各辺の長さが%fと%fの長方形の面積は",x,y);
    printf("%fである。\n",RectangleAreaSize(x,y));
    return(0);
}