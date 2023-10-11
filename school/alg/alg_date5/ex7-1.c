#include<stdio.h>

int main(){
    int a = 0,counter = 0;
    while(a <= 30){
        counter ++;
        if (counter %2 == 0){
            a += counter;
        }
        if (counter %2 == 1){
            a -= counter;
        }
    }
    printf("偶数は足し、奇数は引く時、30を越えるのは%dの時である。/n",counter);
    return(0);
}