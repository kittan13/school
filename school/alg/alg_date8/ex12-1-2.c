#include<stdio.h>

int a = 1;
void func1(){
    a=3;
    printf("(func1)変数aの中身は、%dです。\n",a);
}

int main(){
    int a;
    a=2;
    printf("(main)変数aの中身は、%dです。\n",a);

    func1();

    return(0);
}