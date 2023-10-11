#include <stdio.h>
#include <stdlib.h>
void quick_sort( int *a, int left, int right )
{
  int i, j, p, t;
  p = a[(left + right)/2];
  i = left; j = right;
  while ( i <= j ) {
    while ( a[i] < p ) i++;
    while ( a[j] > p ) j--;
    if ( i <= j ) {
      t = a[i]; a[i] = a[j]; a[j] = t;
      i++; j--;
    }
  }
  if ( left < j ) quick_sort(a, left, j);
  if ( i < right ) quick_sort(a, i, right);
}

int main( int argc, char *argv[ ] )
{
  FILE *fp;
  int *a, n, i;
  n = atoi(argv[1]);
  a = (int *)malloc(sizeof(int)*(n+1));
  a[0] = -1;
  if ( (fp = fopen(argv[2], "r")) == NULL ) {
    printf("Can't open %s.\n", argv[2]);
    exit(1);
  }
  for ( i = 1; i <= n; i++ ) {
    fscanf(fp, "%d\n", &a[i]);
  }
  fclose(fp);
  quick_sort(a, 1, n);
  for ( i = 1; i <= n; i++ ) printf("%d\n", a[i]);
}