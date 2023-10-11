#include<stdio.h>

int main(){
    double*p;    //整数型のメモリを示すポインタの宣言
    double x = 1;

    p = &x;   //変数xのポインタをpに代入
    printf("変数xは、メモリ%pに保管されており、中身は%fです。\n",&x,x);
    printf("ポインタpの指すアドレスは%pで、メモリに中身は%fです。\n",p,*p);
    printf("ポインタp自身は、アドレス%pに保管されています。\n",&p);

    *p = 100;
    printf("ポインタpの指すメモリの中身を変更すると、\
            変数xの中身は%fに変わります。\n",x);

    return(0);
}