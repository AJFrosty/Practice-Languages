#include<stdio.h>

//Program to see week numer it is
int main() {
    int day;
    char weekdays[][15] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
    char date;

    printf("Please enter the Week Day: ");
    scanf("%d", &day);
    
    if (day>=1  && day<=7) { 
        printf("The Day of the week is %s. \n", weekdays[day-1]);
    } else 
        printf("That is not a day of the week!\n");
}
   