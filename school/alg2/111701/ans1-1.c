#include<stdio.h>



int func1(int n)
{
    int i,m=1;
    if(n>0){
        for(i=1;i<=n;i++){
            m=m*i;
        }
    }
    return(m);
}

int main(){
    int ans=0;
    ans =func1(3);
    printf(ans);
}
