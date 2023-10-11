#include<stdio.h>

int a = 1;
void func1(){
    printf("(func1)変数aの中身は、%dです。\n",a);
}

int main(){
    a=2;
    printf("(main)変数aの中身は、%dです。\n",a);

    func1();

    return(0);
}