#include <stdio.h>

int main(){
    char input_n[10];
    printf("Enter n: ");
    fgets(input_n,sizeof(input_n),stdin);
    int n = atoi(input_n),count = 0,i,j;
    long double lcm = 1,Pi = 4,sum = 0;
    for (i = 1; i <= n ; i += 2){
        if (i%2){
            Pi = Pi - (4.0/i);
        }else{
            Pi = Pi + (4.0/i);
        }
    }
    printf("%.10Lf",Pi);
}