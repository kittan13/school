#include<stdio.h>

int main(){
    int rank = 2;

    switch (rank){
        case 1:
            printf("Gold!\n");
            break;
        case 2:
            printf("Silver\n");
            break;
        case 3:
            printf("Bronze\n");
        default:
            printf("No medal\n");
        break;
    }
    printf("です！\n");
}