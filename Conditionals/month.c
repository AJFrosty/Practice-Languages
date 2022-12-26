#include<stdio.h>

//Program that takes Month number and output the number of days

int main() {
    int month;
    char months[][15] = {"January","February","March","April","May","June","July","August","September","October","November","December"};
    char days[][5] = {"31","28","31","30","31","30","31","31","30","31","30","31"};

    printf("Please enter the month number: ");
    scanf("%d", &month);

    if (month<13 && month>0)
        printf("The number of days in the month of %s is %s \n", months[month-1], days[month-1]);
    else
        printf("That's not a month number!\n"); 
        
}