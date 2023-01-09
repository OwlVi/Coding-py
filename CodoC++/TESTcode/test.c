#include <math.h>
#include <stdio.h>

int cmp_n(double d1, double d2, size_t n) {
    return fabs(trunc(pow(10, n) * d1) - trunc(pow(10, n) * d2)) < 1.0;
}

int main() {
    double pi = 4;
    size_t o = 0;
    struct {
      double pi;
      size_t n;
    } oracle[] = {
       { 3.14, 2 },
       { 3.141, 3 }
    };
    for (int i = 0; i < 100000; i++) {
        int den = i * 2 + 3;
        //(4 - 4/3 + 4/5 -4/7 + 4/9 -......)
        pi += ((i % 2) ? 4.0 : -4.0) / den;
        int special = 0;
        if(
            o < sizeof(oracle) / sizeof(*oracle) &&
            cmp_n(pi, oracle[o].pi, oracle[o].n)
        ) {
            special = 1;
            o++;
        }
        
    }
    printf("pi = %.10f\n", pi);
}