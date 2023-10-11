#include <stdio.h>
#include <math.h>

int main()
{
	printf("求めたい連立方程式をax^2+bx+c=0とします。\n");
	printf("それぞれの変数を入力してください\n");
	double a, b, c;
	printf("a=");
	scanf("%lf", &a);
	printf("b=");
	scanf("%lf", &b);
	printf("c=");
	scanf("%lf", &c);


	double d;
	d = b*b-4*a*c;

	double answer,answer1,answer2;

	if (d < 0) {
		printf("解なし\n");
	}
	else if (d == 0) {
		answer = (-b + sqrt(d)) / (2 * a);
		printf("x=%lf(重解)\n", answer);
	}
	else {
		answer1 = (-b + sqrt(d)) / (2 * a);
		answer2 = (-b - sqrt(d)) / (2 * a);
		printf("x=%lf,%lf\n", answer1,answer2);
	}
	
	return(0);
}
