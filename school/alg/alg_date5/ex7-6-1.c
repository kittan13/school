#include <stdio.h>

int main(void)
{
 int i, n;
 int sum; /* ①合計用変数を準備 */

 i=0;
 sum = 0; /* ②合計用の変数を0クリア */

 while(n != 0){
  //printf("%2d番目の数? ", i+1);
  printf("足す数は? ");
  scanf("%d", &n);

  sum = sum + n; /* ③合計用変数に累計していく */
  i++;
 }

 printf("\n合計は %dです\n", sum);

 return 0;
}