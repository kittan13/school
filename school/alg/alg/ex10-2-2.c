#include<stdio.h>

int main(){
        int i,j;
        int data[10][10];
        int *p;
        int counter = 0;

        for(j=0;j<10;j++){
                for(i=0;i<10;i++){
                        data[j][i]=100+counter;
                        counter++;
                }
        }
        for(p = &data[0][0]; *p != data[9][9]; p++);
        printf("アドレス%pの中身は、%dです。\n", p, *p);
        p=&data[0][0];
        printf("data[4][4]の中身%d\n",data[4][4]);
        printf("data[5][5]の中身%d\n",*(p+55));
        return(0);
}