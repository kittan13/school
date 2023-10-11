#include <stdio.h>

int main (void){

int year;

printf("変換したい西暦を入力してください。(1912年以降)：");
scanf("%d", &year);


if(year>=1912&&year<=1925){
printf("%d年は大正%d年です。\n", year, year-1911);
}
else if(year>=1926&&year<=1988){
printf("%d年は昭和%d年です。\n", year, year-1925);
}
else if(year>=1989&&year<=2018){
printf("%d年は平成%d年です。\n", year, year-1988);
}
else if(year==2019||year==2020){
printf("%d年は令和%d年です。\n", year, year-2018);
}
return(0);
}