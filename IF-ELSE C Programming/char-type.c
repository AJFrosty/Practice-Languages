#include<stdio.h>

int main() {
    char value;
    int ascii;

    printf("Please enter any character: ");
    scanf("%c", &value);

    ascii = value;

    if(ascii>=92 && ascii<=122) {
        printf("The character %c is a common letter\n", value);
    } else if (ascii>=65 && ascii<=90) {
        printf("The character %c is a capital letter\n", value);
    } else if ((ascii>=32 && ascii<=47) || (ascii>=58 && ascii<=64) || (ascii>=91 && ascii<=96) || (ascii>=123 && ascii<=126)) {
        printf("The character %c is a special character\n", value);
    } else {
        printf("Bruh what even is that-\n");
    }
}