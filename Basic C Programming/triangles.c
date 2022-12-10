#include<stdio.h>
#include<math.h>

int main(void) {
    //Basic Area of a Triangle
    int answer; 
    printf("Which Equation Do you want to use? \n1. Basic (1/2bh) \n2. Heron's Formula \n3. Angle (1/2ab SinC) \n[NB: Only Insert the Number that Corresponds] \n");
    scanf("%d", &answer);

    if (answer == 1)
    {
        float base, height, first_area;
        printf("Please input the Base of the Triangle: ");
        scanf("%f", &base);
        printf("Please input the height of your Triangle: ");
        scanf("%f", &height);

        first_area = 0.5 * base * height;

        printf("The area of the triangle with the base %0.2f and height of %0.2f is %0.2f \n", base, height, first_area);
    }
    else if (answer == 2) {
    //Heron's Formula
        float a,b,c,s,sqrt,sec_area; 
        printf("Enter the length of all 3 sides of the triangle individually: ");
        scanf("%f,%f,%f", &a,&b,&c);
        //Semi Perimter
        s = (a+b+c)/2;
        if (s>a && s>b && s>c) { 
            sqrt = s * (s-a) * (s-b) * (s-c);
            sec_area = sqrtf(sqrt);
            printf("The area of the triangle with sides of %0.1f,%0.1f and %0.1f is %0.1f \n", a,b,c,sec_area);
        } else {
            printf("Cannot Square Root a Negative Number!!! \n");
        }
    }
    else if (answer == 3) {
    // 1/2ab x SinC
        float a,b,angle,third_area;
        printf("Enter the length of Side A and Side B: ");
        scanf("%f,%f", &a,&b);
        printf("State the angle C: ");
        scanf("%f", &angle);

        third_area = 0.5*a*b* sin(angle);

        printf("The area of the triangle with Side a as %0.1f, Side b as %0.1f, and Angle C as %0.1f is: %0.1f \n", a,b,angle,third_area);
    }
    else {
        printf("Please select 1 through 3 please...\n");
    }
    return 0; 
}