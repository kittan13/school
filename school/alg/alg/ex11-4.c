#include<stdio.h>

struct complex
{
    double real;
    double imaginary;
};

struct complex complex_add(strucu complex func_a,struct complex func_b){
    struct complex func_c;
    func_c.real = func_a.real + func_b.real;
    func_c.imaginary = func_a.imaginary + func_b.imaginary;
    return func_c;
}

void print_complex(char message[],struct complex a){
    printf("%s = %3lfi\n",message,a.real,a.imaginary);
}

int main(){
    struct complex a,b,c;

    a.real = 10; a.imaginary = 5;
    b.real = 20; b.imaginary = 3;
}
