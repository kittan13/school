#include<stdio.h>

int main(){
    int birthday;
    printf("あなたの生まれた月を教えてください：");
    scanf("%d",&birthday);

    printf("%d月は、",birthday);

    if(0<birthday && birthday<13){
        switch ((birthday%12)/3){
            case 0:
                printf("冬です");
                break;
            case 1:
                printf("春です");
                break;
            case 2:
                printf("夏です");
                break;
            case 3:
                printf("秋です");
                break;
        }
    }else if(birthday>12 || 0>birthday){
        printf("理解できません");
    }
    
    return(0);
}
   
