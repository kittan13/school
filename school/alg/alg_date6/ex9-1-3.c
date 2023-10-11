#include<stdio.h>
#include<math.h>

double TriangleAreaSize(double a){
    return((sqrt(3)/4)*a*a);
}

int main(){
    double x=10;
    printf("各辺の長さが%fの正三角形の面積は",x);
    printf("%fである。\n",TriangleAreaSize(x));
    return(0);
}