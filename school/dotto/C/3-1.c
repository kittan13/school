#include<stdio.h>

int main(void){
    int score = 55;

    if(score>=60){
        printf("あなたは%d点！やったね！\n",score);
    }else if(score>=55){
        printf("あなたは%d点！\n次は頑張ろう！\n",score);
    }else{
        printf("あなたは%d点！もっと頑張ろう\n",score);
    }
    return(0);
}