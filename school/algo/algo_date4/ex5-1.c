#include<stdio.h>

int main(){
	int birthmonth;
	printf("あなたの生まれた月を入力してください。:");
	scanf("%d",&birthmonth);

	printf("\n%d月は、",birthmonth);
	switch((birthmonth%12)/3){
		//四季に変換する。春は3-5月、夏は6-8月、秋は9-11月、冬は12-2月。
		case 0:
			printf("冬です。\n");
			//break;
		case 1:
			printf("春です。\n");
			//break;
		case 2:
			printf("夏です。\n");
			//break;
		case 3:
			printf("秋です。\n");
			//break;
		default:
			printf("理解できません。\n");
	}
	return(0);
}
