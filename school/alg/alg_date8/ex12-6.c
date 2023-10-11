#include<stdio.h>
int plot[8][8];
char state[3][5] = {"　","〇","●"};

void print_board(){
    int x,y;
    printf("\033[2J");    //画面のクリア
    printf("\033[%d;%dH",0,0);   //左上にカーソル移動
    for(y=0;y<8;y++){
        for(x=0;x<8;x++){
            printf("%s|",state[plot[x][y]]);
        }
        printf("\n");
        printf("--+--+--+--+--+--+--+--+\n");
    }
}

int main(){
    int x,y;

    for(y=0;y<8;y++)for(x=0;x<8;x++)plot[x][y]=0;
    plot[3][3] = plot[4][4] = 1;
    plot[3][4] = plot[4][3] = 2;

    print_board();
}