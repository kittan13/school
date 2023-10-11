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
    
    

    if(0=hito || 1=hito || 2=hito){
        printf("私の手は、%dでした。\n結果は、",com);

        int result = (com-hito+3)%3;

        if(hito==com){
            printf("あいこ");
        }else if(hito!=com){
            switch (result){
                case 1:
                    printf("あなたの勝ち");
                    break;
        
                case 2:
                    printf("あなたの負け");
                    break;
            }
        }
                
        printf("でした\n");
    }else{
        printf("0から2で入力してください。");
    }

    return(0);
}