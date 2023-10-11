#include<stdio.h>
#include<math.h>

double CircleAreaSize(double a){
    return(M_PI*(a*a));
}

int main(){
    double x=10;
    printf("半径%fの円の面積は",x);
    printf("%fである。\n",RectangleAreaSize(x));
    return(0);
}