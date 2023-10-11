#include<stdio.h>
#include<stdlib.h>
#include<time.h>



int main(){
    
    int GU = 0;
    int CHOKI = 1;
    int PA = 2;
    
    int counter = 1;

    srand((unsigned int)time(NULL));

    int hito;
    int com = rand()%3;

    int make(){
        (hito==CHOKI && com==GU) ||
        (hito==PA && com==CHOKI) ||
        (hito==GU && com==PA);
        printf("私の勝ち");
    };

    int aiko(){
        hito==com;
        printf("あいこ\n");
    };
    
    int kati(){
        (hito==GU && com==CHOKI) ||
        (hito==CHOKI && com==PA) ||
        (hito==PA && com==GU);
    };

    printf("あなたの手を入力してください(ぐー＝０、ちょき＝１、ぱー＝２)：");
    scanf("%d",&hito);

    printf("私の手は、%dでした。\n結果は、",com);

    if(aiko){
        printf("あいこです\n");
        while(make || aiko){
            printf("あなたの手を入力してください(ぐー＝０、ちょき＝１、ぱー＝２)：");
            scanf("%d",&hito);
            counter++;
            int com = rand()%3;
            printf("私の手は、%dでした。\n結果は、",com);
            if(make){
                printf("私の勝ち\n");
            }else{
                printf("あいこ\n");
            }
        }
    }else if(make){
        printf("あなたの負けです\n");
    }else{
        printf("あなたの勝ち\n");
        printf("あなたが勝つまで%d回かかりました/n",counter);
    }
    return(0);
}




   /* if((hito==GU && com==CHOKI) ||
       (hito==CHOKI && com==PA) ||
       (hito==PA && com==GU)){
        printf("あなたの勝ち")
       }




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
*/