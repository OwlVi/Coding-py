#include <stdio.h>
#include <stdlib.h>
int main()
{
   char s ;
   s = getchar();

   if((s >= 'a') && (s <= 'z')){
    printf("Output: lower case ");
   }else if ((s >= 'A') && (s <= 'Z')){
    printf("Output: upper case ");
   }else if ((s >= '0') && (s <= '9')){
    printf("Output: digit");
   }else {
    printf("Output: others");
   }

}