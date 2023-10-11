#include<stdio.h>
#include<math.h>

int main(){
	double a,b,c,d;
	a = pow(10,11);
	b = 1;
	c = a+b;
	d = a-b;
	printf("%fと%fの和は%fで、差は%fです。\n",a,b,c,d);
	return(0);
}
