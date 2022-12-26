#include<stdio.h>

//Program to find the first 3 index of an interger
int main() {
    int n,p1,p2;

    printf("Please insert the number in which you want raised to the first 3 Powers: ");
    scanf("%i", &n);

    p1 = n*n;
    p2 = n*n*n;
    printf("The first 3 powers of the number %i are: %ld, %ld, and %ld\n", n,n,p1,p2);
}