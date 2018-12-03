#include <stdio.h>
int fib(int i)
{
    if(i == 0){
        return 0;
    }else if( i == 1){
        return 1;
    }else{
        return fib(i-1) + i;
    }
}

int main()
{
   int s = fib(1);
   printf("%d",fib(10));
   return 0;
}


