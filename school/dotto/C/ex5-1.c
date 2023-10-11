#include<stdio.h>

int main(){
    int a =0;
    int counter =0;

    if((counter%2)==0){
        while(a<=30){
            counter++;
            a+=counter;
            printf("counter=%d、a=%dの時は足す\n",counter,a);
        }
    }else{
        while(a<=30){
            counter++;
            a-=counter;
            printf("counter=%d、a=%dの時は引く\n",counter,a);
        }
    }
    printf("30を超えたのは%dのときである",counter);
    return(0);
}