#include<stdio.h>

void func4(){
    static int value = 909;
    value = value + 100;
    printf("%d\n",value);
}

int main(){
    func4();
    func4();
    func4();
    return(0);
};