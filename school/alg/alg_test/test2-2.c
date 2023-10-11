#include<stdio.h>

int main(){
    int a;
    printf("得点を入力してください：");
    scanf("%d",&a);

    if(90<=a){
        printf("評価はＳです。\n");
    }else if(80 <= a <= 89){
        printf("評価はAです。\n");
        break;
    }
    return(0);
}