#include<stdio.h>
#include<string.h>
struct person
{
        char id[8];
        char name[20];
        int bt_y;
        int bt_m;
        int bt_d;
};

struct person elec_user[20];

int main(){
        int i;
        int y,m,d;
        char uid,uname;

        for(i=0;i<20;i++){
                printf("%d番目の生徒のid:",i+1);
                scanf("%s",&uid);
                strcpy(elec_user[i].id,&uid);
                printf("%d番目の生徒の名前:",i+1);
                scanf("%s",&uname);
                strcpy(elec_user[i].name,&uname);
                printf("生まれた年:");
                scanf("%d",&y);
                elec_user[i].bt_y=y;
                printf("生まれた月:");
                scanf("%d",&m);
                elec_user[i].bt_m=m;
                printf("生まれた日:");
                scanf("%d",&d);
                elec_user[i].bt_d=d;
        }

        for(i=0;i<20;i++){
                printf("学籍番号%sの%sさんは、西暦%d年%d月%d日生まれです。\n",\
                                elec_user[i].id,elec_user[i].name,\
                                elec_user[i].bt_y,elec_user[i].bt_m,elec_user[i].bt_d);
        }
        return(0);
}