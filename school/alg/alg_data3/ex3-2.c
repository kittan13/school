#include<stdio.h>
#include<math.h>

int main(){
	double a,b,c,d;
	a = sqrt(10001);
	b = sqrt(9999);
	c = a - b;
	d = 2/(a+b);
	printf("%.23fと%.23fの差は%.23fです。\n",a,b,c);
	printf("%.23fと%.23fの差は%.23fです。\n",a,b,d);
	return(0);
}
