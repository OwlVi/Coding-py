#include <stdio.h>
#include <stdlib.h>
int main()
{
    char input_n[12], input_x[2];
    fgets(input_n, 12, stdin);
    fgets(input_x, 2, stdin);
    int n;
    int x;

    n = atoi(input_n);
    x = atoi(input_x);

    printf("%d",n%10);

}