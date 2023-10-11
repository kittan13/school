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

struct person user1;

int main(){
        int y,m,d;
        char uid,uname;

        printf("id:");
        scanf("%s",&uid);
        strcpy(user1.id,&uid);
        printf("name:");
        scanf("%s",&uname);
        strcpy(user1.name,&uname);
        printf("生まれた年:");
        scanf("%d",&y);
        user1.bt_y=y;
        printf("生まれた月:");
        scanf("%d",&m);
        user1.bt_m=m;
        printf("生まれた日:");
        scanf("%d",&d);
        user1.bt_d=d;

        printf("学籍番号%sの%sさんは、西暦%d年%d月%d日生まれです。\n",\
                        user1.id,user1.name,user1.bt_y,user1.bt_m,user1.bt_d);
        return(0);
}