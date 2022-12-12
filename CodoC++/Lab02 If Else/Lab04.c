#include <stdio.h>
#include <stdlib.h>
int main (){
    // input
    char number[100];
    fgets(number, 100 ,stdin);
    float tax,inumber = atof(number);
    //process
    if (inumber >= 0){
        if (inumber > 300000.0){
            tax = ((inumber-300000.0)*0.1) + (300000.0*0.05);
            printf("%.2f",tax);
        }else{
            tax = inumber*0.05;
            printf("%.2f",tax);
        }
    }else{
        printf("Error: Salary must be greater or equal to 0");
    }
}