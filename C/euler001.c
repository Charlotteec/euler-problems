#include <stdio.h>

int main(){
int i, s;
s=0;
  for(i=0;i<1000;i++){
      if(i%3==0||i%5==0){
        s=s+i;
      }
  }
printf("hello??\n");
printf("%i ",s);
return 0;

}

