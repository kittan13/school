#include<stdio.h>

int main(){
    int i;
    int j;
    for(i=1;i<=10;i++){
        for(j=1;j<=10;j++){
            printf("iの値は%dで、jの値は%dです。\n",i,j);
        }
    }
    return(0);
}