#include <stdio.h>

void swap_a(int a, int b){
        int tmp;
        tmp = a;
        a = b;
        b = tmp;
}

void swap_b(int *a, int *b){
        int tmp;
        tmp = *a;
        *a = *b;
        *b = tmp;
}

void swap_c(int *a, int *b){
        int *tmp;
        tmp = a;
        a = b;
        b = tmp;
}

void swap_print(int a, int b){
        printf("a = %d, b = %d\n",a, b);
}

int main(){
        int data[2] = {100, 200};
        swap_print(data[0],data[1]);

        printf("値渡しで関数に引数を受け渡した場合．");
        swap_a(data[0], data[1]);
        swap_print(data[0],data[1]);

        printf("参照渡しで関数に引数を受け渡した場合-1.");
        swap_b(&data[0],&data[1]);
        swap_print(data[0],data[1]);

        printf("参照渡しで関数に引数を受け渡した場合-2.");
        swap_c(&data[0],&data[1]);
        swap_print(data[0],data[1]);

        return(0);
}