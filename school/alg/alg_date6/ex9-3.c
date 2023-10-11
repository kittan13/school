#include <stdio.h>

unsigned long gcd(unsigned long a, unsigned long b)
{
  if (b == 0) {
    return a;
  } else if ((a % b) == 0) {
    return b;
  } else {
    return gcd(b, a % b);
  }
}

int main(void)
{
  unsigned long a, b;
  unsigned long ret;

  printf("二つの数字を入力してください: ");
  scanf("%lu%lu", &a, &b);

  ret = gcd(a, b);
  printf("最大公約数 = %lu\n", ret);
  printf("最小公倍数 = %lu\n", (a * b) / ret);
  return 0;
}