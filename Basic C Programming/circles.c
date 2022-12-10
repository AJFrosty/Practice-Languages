#include <stdio.h>

// Program to get the area and circumference of a circle

int main () {
    float radius, circum, area;

    printf("What is the length of the radius of your circle?\n");
    scanf("%f", &radius);

    circum = 2*radius*22/7;
    area = radius*radius*22/7;

    printf("The circumference of the circle is %0.2f\n",circum );
    printf("The area of the circle is %0.2f\n", area); 

}