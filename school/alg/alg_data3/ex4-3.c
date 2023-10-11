#include<stdio.h>

int main(){
       int a;

        printf("数字を入力してください:");
        scanf("%d,&a");

        printf("%dは、",a);
        if((a % 2 )!= 0)
                printf("奇数");
        else
                printf("偶数");
        printf("です。\n");
        return(0);
}
