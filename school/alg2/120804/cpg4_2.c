#include <stdio.h>
#include <stdlib.h>

void insert_sort( int *a, int n )
{
  int i, j, q;
  for ( i = 2; i <= n; i++ ) {
    q = a[i]; j = i;
    while ( a[j-1] > q ) {
      a[j] = a[j-1];
      j--;
    }
    a[j] = q;
  }
}

int main( int argc, char *argv[ ] )
{
  FILE *fp;
  int *a, n, i;
  n = atoi(argv[1]);
  a = (int *)malloc(sizeof(int)*(n+1));
  a[0] = -1;
  if((fp = fopen(argv[2], "r")) == NULL){
    printf("Can't open %s.\n", argv[2]);
    exit(1);
  }
  for (i = 1; i <= n; i++) {
    fscanf(fp, "%d\n", &a[i]);
  }
  fclose(fp);
  insert_sort(a, n);
  for (i = 1; i <= n; i++) printf("%d\n", a[i]);
}