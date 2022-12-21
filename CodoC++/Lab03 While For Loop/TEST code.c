#include <stdio.h>
#include <stdlib.h>

int main()
{
   char bitnum[10] ;
   fgets(bitnum,10,stdin);

   int i = atoi(bitnum);

   for ( i ; i > 0 ; i--){
      printf("%d\n",i);
      
   }
}