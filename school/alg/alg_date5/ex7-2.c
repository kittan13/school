#include<stdio.h>
//最初から条件を満たさない場合

int main(){
    int i=1;
    while(i>11){
        i=i+1;
        printf("iの値は%dです。\n",i);
    }
    return(0);
}