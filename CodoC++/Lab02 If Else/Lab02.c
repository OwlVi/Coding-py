#include <stdio.h>
#include <stdlib.h>
int main()
{   
    float p,oney;
    int percents;
    // input
    char stamp[10] ,money[10];
    fgets(stamp, 10 ,stdin);
    int istamp = atoi(stamp);

    fgets(money , 10 ,stdin);
    float imoney = atof(money);
    // process
    if (istamp >= 9 ){
        percents = 40 ;
        p = 0.4*imoney;
        imoney = imoney - p;
        istamp = istamp - 9;
    } else if (istamp >= 6){
        percents = 30 ;
        p = 0.3*imoney;
        imoney = imoney - p;
        istamp = istamp - 6;

    }else if (istamp >= 3){
        percents = 20 ;
        p = 0.2*imoney;
        imoney = imoney - p;
        istamp = istamp - 3;
    }else if (istamp = 2){
        percents = 15 ;
        p = 0.15*imoney;
        imoney = imoney - p;
        istamp = istamp - 2;
    } else {
        percents = 10*istamp ;
        p = 0.10*imoney*istamp;
        imoney = imoney - p;
        istamp = istamp-istamp;
    }
    // output
    printf("You get %d percents discount.\n",percents);
    printf("Total amount due is %.2f Baht.\n",imoney);
    printf("And you have %d stickers left.\n",istamp);
}