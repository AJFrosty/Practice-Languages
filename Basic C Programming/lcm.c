#include<stdio.h>

int main() {
    int n1,n2,lcm, factor=1;

    printf("Please insert 2 numbers: ");
    scanf("%d,%d", &n1,&n2);

    lcm = (n1 > n2) ? n1 : n2;  

    while (factor) {
        if (lcm % n1 == 0 && lcm % n2 == 0) {
            printf("LCM of %d and %d is %d\n", n1,n2,lcm);
            factor=0;
        }
        lcm++;
    }

}