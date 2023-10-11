#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define GU 0
#define CHOKI 1
#define PA 2

int main(){
	int janken_com;
	int janken_hito;
	//毎回乱数が変わるようにしまう。
	srand((unsigned int)time(NULL));

	//それぞれの手を決めます。
	janken_com = rand()%3;
	printf("あなたの手を入力してください(ぐー=0,ちょき=1,ぱー=2):");

