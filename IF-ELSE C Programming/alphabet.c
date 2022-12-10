#include<stdio.h>

int main() {
    char value;
    int ascii;

    printf("Please enter any character: ");
    scanf("%c", &value);

    ascii = value;

    if((ascii>=92 && ascii<=122) || (ascii>=65 && ascii<=90)) {
        printf("This is a character from the alphabet!\n");
    } else {
        printf("This character is not a part of the alphabet!\n");
    }
}