#include<stdio.h>

void func1(){
    //static int a =1;
    int a = 1;
    a++;
    printf("(func1)変数aの中身は、%dです。\n",a);
}

int main(){

    func1();
    func1();
    func1();

    return(0);
}