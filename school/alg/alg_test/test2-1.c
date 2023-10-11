#include<stdio.h>

int main(){
    int a;
    printf("得点を入力してください：");
    scanf("%d",&a);

    if(90<=a){
        printf("評価はＳです。\n");
    }else if(80 <= a <= 89){
        printf("評価はAです。\n");
    }else if (70 <= a <= 79){
        printf("評価はBです。\n");
    }else if (60 <= a <= 69){
        printf("評価はCです。\n");
    }else{
        printf("不合格です。\n");
            int b = 60-a;
            if(54 <= a <= 59){
                printf("60点まであと%d点です。\n",b);
            } 
    }
    return(0);
}