#include<stdio.h>

int x = 9;
void func8(){
    printf("%d\n",x);
}

int main(){
    int x = 54.5;
    printf("%d\n",x);
    {
        int x = 54.5;
        x++;
        printf("%d\n",x);

        x /= 2;
        printf("%d\n",x);

        x -=100;
        printf("%d\n",x);
    }
    func8();
    printf("%d\n",x);
    return(0);
}