#include<stdio.h>

int main()
{


    char star[5];
    fgets(star,5,stdin);

    int star_stamp = atoi(star);
    printf("%d",star_stamp);
    
}