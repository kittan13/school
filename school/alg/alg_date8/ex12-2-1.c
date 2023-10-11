#include<stdio.h>

void my_rand(){
    static int a =1;
    a=a*214013+2531011;
    printf("(my_rand)変数aの中身は、%dです。\n",a);
}

int main(){

    my_rand();
    my_rand();
    my_rand();
    my_rand();
    my_rand();
    my_rand();
    my_rand();
    my_rand();
    my_rand();
    my_rand();

    return(0);
}