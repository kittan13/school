#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[ ])
{
  FILE *fp;
  char *fn;
  int i, x;
  fn = argv[1];
  if ( (fp = fopen(fn, "w")) == NULL ) {
   printf("Can't open %s.\n", fn);
    exit(1);
  }
  for ( i = 0; i < 30; i++ ) {
    x = rand( );
    fprintf(fp, "%d\n", x);
  }
  fclose(fp);
}
