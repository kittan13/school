#include<stdio.h>

void func6(){
    static int value = 938;
    value = value + 100;
    printf("%d\n",value);
}

int main(){
    func6();
    func6();
    func6();
    return(0);
};