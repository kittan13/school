#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define GU 0
#define CHOKI 1
#define PA 2

int main(){
	int janken_com;
	int janken_hito;
	//毎回乱数が変わるようにします。
	srand((unsigned int)time(NULL));

	//それぞれの手を決めます。
	janken_com = rand()%3;
	printf("あなたの手を入力してください(ぐー=0,ちょき=1,ぱー=2):");
    scanf("%d",&janken_hito);

    //結果を判断します。
    printf("\n私の手は、%dでした。\n結果は、",janken_com);

    //あいこの場合
    if(janken_com == janken_hito)printf("あいこ");

    //コンピュータが勝つ場合
    if((janken_com == GU &&janken_hito ==CHOKI)||(janken_com == CHOKI &&janken_hito == PA)||(janken_com == PA &&janken_hito ==GU))
        printf("私の勝ち");

    //人が勝つ場合
    if((janken_com == GU &&janken_hito ==PA)||(janken_com == CHOKI &&janken_hito == GU)||(janken_com == PA &&janken_hito ==CHOKI))
        printf("あなたの勝ち");

    printf("でした。\n");
    return(0);
}

    