#include<stdio.h>
#include<string.h>

int main(){
    char filename[FILENAME_MAX];
    char buffer;
    FILE *fp;

    strcpy(filename,"/dev/stdin");
    if((fp = fopen(filename,"r")) == NULL){
        printf("ファイル%sが見つかりません。\n",filename);
        return(-1);
    }

    while((buffer = fgetc(fp))!= EOF){
        printf("%c",buffer);
    }
    fclose(fp);
}