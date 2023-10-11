#include<stdio.h>
#include<stdlib.h>
#include<time.h>

struct card{
    int mark;
    int number;
};

void init(struct card a[]){
    printf("%d\n", a[1].mark);
    if((0 <= a[0].mark)| (a[0].mark <= 12)){
        a[0].mark = 1;
        a[0].number += 1;
    }else if((13 <= a[0].mark)| (a[0].mark <= 25)){
        a[0].mark = 2;
        a[0].number -= 12;
    }else if((26 <= a[0].mark)| (a[0].mark <= 38)){
        a[0].mark = 3;
        a[0].number -= 25;
     }else if((39 <= a[0].mark)| (a[0].mark <= 51)){
        a[0].mark = 3;
        a[0].number -= 38;
     }
}

void print_card(struct card a[]){
    for(a[0].number; a[0].number < 13; a[0].number++)
        printf("マーク;%d, 数字;%d\n", a[0].mark, a[0].number);
}

void shuffle(struct card a[]){
    for(int i = 0; i < 3800; i++){
        int *tem;
        int b = a ->number = (rand()% 51) + 1;
        int c = a ->number = (rand()% 51) + 1;
        *tem = b;
        b = c;
        c = *tem;
    }
}

int main(){
    struct card trump[52];
    srand((unsigned int)time(NULL));
    init(trump);
    shuffle(trump);
    print_card(trump);

    return(0);

}