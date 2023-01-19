#include<stdio.h>

//Program to test if the inserted character is a Vowel or not
int main() {
    char value;

    printf("Enter the letter to test to see if it is a Vowel or a Consonant: ");
    scanf("%c", &value);

    if (value == 'a' || value == 'A' || value == 'e' || value == 'E'|| value == 'i' || value == 'I'|| value == 'o' || value == 'O' || value == 'u' || value == 'U') {
        printf("%c is a Vowel \n", value);
    } else {
        printf("%c is a Consonant \n", value);
    }
}