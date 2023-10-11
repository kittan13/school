#include<stdio.h>
#include<string.h>

int main(){
    char filename[FILENAME_MAX];
    char buffer[1024];
    FILE*fp;

    int str(void) {
        printf("ファイル名を入力してEnterボタンを押してください\n");
 
        char Filename[8];
        scanf("%ls", Filename);
 
        return (0);
    }

    strcpy(filename,"Filename");
    if((fp=fopen(filename,"r")) == NULL){
        printf("ファイル%sが見つかりません。\n",filename);
        return(-1);
    }

    while(fscanf(fp,"%s\n",buffer) != EOF){
        printf("%s\n",buffer);
    }
    fclose(fp);
}