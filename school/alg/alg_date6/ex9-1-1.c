#include<stdio.h>

double TrapezoidAreaSize(double a,double b,double c){
    return(((a+b)*c)/2);
}

int main(){
    double x=10,y=20,z=5;
    printf("上底が%f、下底が%f、高さ%fの台形の面積は",x,y,z);
    printf("%fである。\n",RectangleAreaSize(x,y,z));
    return(0);
}