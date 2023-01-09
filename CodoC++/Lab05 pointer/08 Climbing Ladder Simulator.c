#include <stdio.h>

int main(){
    char nstrs[] = "---";
    char hstrs[] = "-O-";
    char lstrs[] = "-^-";
    int n,count = 1;

    printf("Input number of stairs: ");
    scanf("%d",&n);
    char staits[n];
    //printf("%s\n",nstrs);

    for (int i = 0 ; i < n ;i++){
        staits[i] = nstrs;
        printf("%s\n",staits[i]);
    }
    /*
    while (1){
        printf("---- round %d ----\n",count);
        for (int i = 0 ; i < n ;i++){
            printf("|%s|\n",staits[i]);
        }
        if (count > n){
            break;
        }






        count++;
    }
    */

}