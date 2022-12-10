#include<stdio.h>

int main() {
    int a;
    printf("Please enter any number: ");
    scanf("%d", &a);

    if (a>0) {
        printf("The number %d is Positive\n", a);
    } else if (a<0) {
        printf("The number %d is Negative \n", a);
    } else {
        printf("Bruh that's 0...");
    }
}