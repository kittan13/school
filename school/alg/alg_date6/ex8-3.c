#include<stdio.h>
double MaxDouble(double a,double b){
    if(a<b)return(b); //aとbが等しいときはaを返します。
    return(a);
}

double MinDouble(double a,double b){
    if(a>b)return(b);
}

int main(){
    double x=10.5,y=20.5;
    printf("%fと%fは、",x,y);
    printf("%fの方が大きく、%fの方が小さいです。\n",MaxDouble(x,y),MinDouble(x,y));
    return(0);
}