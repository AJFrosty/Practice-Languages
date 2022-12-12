#include<stdio.h>

//Program to test if an interger is odd or even
int main () {
    int a;
    
    printf("Please insert a number: ");
    scanf("%d", &a);

    if (a%2 == 0) 
        printf("The number %d is Even \n", a);
    else
        printf("The number %d is Odd \n", a);
    
}