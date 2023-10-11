#include<stdio.h>

void printc(char *c){
    while(*c!=0)printf("%c",*c++ +1);
}

int main(){
    char a[] = "Ryukoku Univrsity";

    printc(a);
    return(0);
}