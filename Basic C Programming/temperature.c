#include<stdio.h>

int main () {
    float cel,fahren;

    printf("Please insert the temperature in degrees Celsius: ");
    scanf("%f", &cel);

    fahren = (1.8*cel)+32;
    printf("The temperature %0.2f of degrees Celsius in Degrees Fahrenheit is: %0.2f \n", cel, fahren);
}