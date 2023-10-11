#include<stdio.h>

int main(){
    int i;
    int data[10];
    char *p;

    for(i=0;i<10;i++)data[i] = 100+i;

    for(p=data; *p!=109;p++)
        printf("アドレス%pの中身は、%dです。\n",p,*p);
    p = data;
    printf("data[4]の中身は、%dです。\n",data[4]);
    printf("data[5]の中身は、%dです。\n",*(p+5));

    return(0);
}