#include<stdio.h>

//Program to find the factorial of an interger
int factorial() {
    int number,factorial=1;
    
    printf("Please enter the number to be factorialized: ");
    scanf("%d", &number);

    if (number>=0) {
        for (int i=1;i<=number;++i) {
            factorial = factorial*i;
        }
    } else {
        return 0;
    }
        printf("Factorial of %d is %ld \n", number,factorial);
    
}