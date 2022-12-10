#include<stdio.h>

int main() {
    int a,b,c;

    printf("Please insert 3 numbers: ");
    scanf("%d,%d,%d", &a,&b,&c);

    if (a>b && a>c) {
        printf("The Greatest Number is %d \n", a);
    } else if (b>a && b>c) {
        printf("The Greatest Number is %d\n", b);
    } else if (c>a && c>b) {
        printf("The Greatest Number is %d\n", c);
    } else {
        printf("Bruh, these are the same numbers-\n");
    }
}