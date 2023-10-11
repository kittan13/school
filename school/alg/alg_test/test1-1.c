#include<stdio.h>

int main(){
    int a = 3, b = 2;
    double c = 9.123;
    c *= (a++) / 2 + b;
    switch(a){
        case 2:
            printf("%.2f\n",c);
            break;
        case 3:
        case 4:
            printf("%.3f\n",c);
            break;
        default:
            printf("%.4f\n",c);
    }
    return(0);
};