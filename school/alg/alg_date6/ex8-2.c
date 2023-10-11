#include<stdio.h>

int baisu(int kazu,int waru); //今回は宣言だけ

int main(){
    if(baisu(10,6))
        printf("倍数です。\n");
    else
        printf("倍数ではありません。\n");
        return(0);
}

int baisu(int kazu,int waru){//前述の宣言と同じ変数のかたを用います。
    if(kazu%waru == 0)return(1);
    return(0);
}