#include<stdio.h>
#include<stdlib.h>
#include<time.h>



int main(){
    
    int GU = 0;
    int CHOKI = 1;
    int PA = 2;

    srand((unsigned int)time(NULL));

    int hito;
    int com = rand()%3;

    printf("あなたの手を入力してください(ぐー＝０、ちょき＝１、ぱー＝２)：");
    scanf("%d",&hito);

    printf("私の手は、%dでした。\n結果は、",com);

    if(hito == com){
        printf("あいこ");
    }else if((hito==GU && com==CHOKI) ||
               (hito==CHOKI && com==PA) ||
               (hito==PA && com==GU)){
                printf("あなたの勝ち");
    }else if((hito==CHOKI && com==GU) ||
              (hito==PA && com==CHOKI) ||
              (hito==GU && com==PA)){
                printf("私の勝ち");
    }
              
    printf("でした\n");
    return(0);
}