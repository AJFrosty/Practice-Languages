#include<stdio.h>

int main() {
    int year;

    printf("Please enter a year: ");
    scanf("%d", &year);

    if (year%4 == 0 && year%100) 
        if (year%400 == 0) 
            printf("The year %d is a Leap Year!", year);
        
    else if (year%4 == 0 && year%100 != 0) 
        printf("The year %d is a Leap Year!", year);
    else 
        printf("The year %d is not a Leap Year!", year);
    
}