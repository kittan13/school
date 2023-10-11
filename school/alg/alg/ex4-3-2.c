#include <stdio.h>

int main(int argc, char *argv[]){
        printf("%sは、", argv[1]);
        if(*argv[1] % 2 == 0){
                printf("偶数です。\n");
        }
        else{
                printf("奇数です。\n");
        }
        return(0);
}