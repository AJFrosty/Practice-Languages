#include<stdio.h>

int main() {
    char fname[25],lname[25],mname[25],abbrev;

    printf("Please insert your first name, middle name (if you have 2 use only 1), last name: ");
    scanf("%s %s %s", fname,mname,lname);

    printf("Your abbreviated name is: %c.%c %s \n", fname[0],mname[0],lname);
}