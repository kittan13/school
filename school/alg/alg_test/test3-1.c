#include<stdio.h>

int func3(int *a){
    *a=1109;
    
    return *a;

};

int main(){
    int a = 100;
    func3(&a);
    printf("%d\n",a);
    a = 200;
    func3(&a);
    printf("%d\n",a);
    return(0);
};