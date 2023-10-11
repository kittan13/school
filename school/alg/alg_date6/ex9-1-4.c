#include<stdio.h>


int main(){
    double X1,X2,Y1,Y2;
    printf("座標2点を入力してください。\n");
    printf("X1 = ");
    scanf("%lf",&X1);
    printf("Y1 = ");
    scanf("%lf",&Y1);
    printf("X2 = ");
    scanf("%lf",&X2);
    printf("Y2 = ");
    scanf("%lf",&Y2);

    double a,b;
    a=(Y2-Y1)/(X2-X1);
    b=Y1-a*X1;

    printf("求めたい式は\ny=(%lf)x+(%lf)\nです。",a,b);
    return(0);
    }