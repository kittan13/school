#include <stdio.h>
#include <stdlib.h>

void select_sort( int *a, int n )
{
  int i, j, min, t;
  for ( i = 1; i < n; i++ ) {
    min = i;
    for (j = i+1; j <= n; j++) {
      if (a[j] < a[min]) min = j;
    }
    t = a[min]; a[min] = a[i]; a[i] = t;
  }
}

int main( int argc, char *argv[ ] )
{
  FILE *fp;
  int *a, n, i;
  n = atoi(argv[1]);
  a = (int *)malloc(sizeof(int)*(n+1));
  a[0] = -1;
  if ( ( fp = fopen( argv[2], "r") ) == NULL ) {
    printf("Can't open %s.\n", argv[2]);
    exit(1);
  }
  for ( i = 1; i <= n; i++ ) {
    fscanf(fp, "%d\n", &a[i]);
  }
  fclose(fp);
  select_sort(a, n);
  for (i = 1; i <= n; i++) printf("%d\n", a[i]);
}