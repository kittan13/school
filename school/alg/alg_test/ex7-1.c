#include<stdio.h>

int func7(int *a){
    *a=1138;
    return *a;
}

int main(){
    int a = 150;
    func7(&a);
    printf("%d\n",a);
    return(0);
}