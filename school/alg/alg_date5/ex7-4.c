#include<stdio.h>

int main(){
    int i=0;
    while(i<10){
        i++;
        int j=0;
        while(j<10){
            j++;
            printf("iの値は%dで、jの値は%dです。\n",i,j);
        }
    }
    return(0);
}