#include<stdio.h>
#include<math.h>

//Program to find simple interest and compound interest
int main() {
    float p,r,t,si,com;
    int response;

    printf("Are you doing:\n1. Simple Interest\n2. Compund Interest\n");
    scanf("%d", &response);

    if (response == 1) { 
        printf("Please insert Principle, Rate and Time \n[NB: Separate each value with a Comma (\",\")\n");
        scanf("%f,%f,%f", &p,&r,&t);

    si = (p*t*r)/100;
    printf("The simple interest is: $%-.2f \n", si);
    }
    else {
        printf("Please insert Principle, Rate and Time \n[NB: Separate each value with a Comma (\",\")\n");
        scanf("%f,%f,%f", &p,&r,&t);

        com = p*pow((1+r/100),t);
        printf("The compound interest is: $%0.2f \n", com);
    }
}