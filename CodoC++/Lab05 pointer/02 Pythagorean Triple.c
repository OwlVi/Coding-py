#include <stdio.h>
#include <stdlib.h>

int main(){
    char input_n[50];
    fgets(input_n,sizeof(input_n),stdin);
    int n = atoi(input_n);
    Pythagorean(n);
    if (Pythagorean == 0){
        printf("No triple found.");
    }
}
