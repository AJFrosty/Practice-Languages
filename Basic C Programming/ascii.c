#include<stdio.h>

int main() {
    char value;
    int ascii;

    printf("Please enter your singular character: ");
    scanf("%c", &value);
    
    ascii = value;
    printf("The ascii value of %c = %d\n", value,ascii);
}