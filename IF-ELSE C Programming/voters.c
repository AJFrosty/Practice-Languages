#include<stdio.h>

//Program to test if someone is eligible to vote
int main()
{
     int age;
     printf("Enter Age of Person : ");
     scanf("%d",&age);
     if(age>17)
          printf("Person is Eligible for Voting \n");
     else
          printf("Person is NOT Eligible for Voting\n");
     return 0;
}