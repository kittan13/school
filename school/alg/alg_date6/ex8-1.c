#include<stdio.h>

//関数は呼び出される前にせんげんする必要がある（変数も同様）
//とりあえず宣言だけしておけば、プログラムの後ろでもいい。
void baisu(int kazu,int waru){
    if(kazu%waru == 0) //waruで割ったあまりで倍数か否かを確認
        printf("%dは%dの倍数です。\n",kazu,waru);
    else
        printf("%dは%dの倍数ではありません。\n",kazu,waru);
}

int main(){
    //いろんな数が倍数か否か調べましょう。
    int a;

    a=15;
    baisu(a,3);  // まるかっこの中は引数と呼び、関数内に引き渡される。    
    baisu(10,5);  //引数は、関数の宣言時に指定した型で引き渡す必要がある。

    a+=10;  //a = a+10のことです。
    baisu(a,10000);

    a++;  // A =a+!の事です。
    baisu(a,5);
    return(0);
}
