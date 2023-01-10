#include<stdio.h>
#include<math.h>

int main(void) {
    int a,b,c,r1,r2;
    float sqrt;
    
    printf("Enter the coefficient of a,b and c, where a/b/c not equal to 0: ");
    scanf("%d %d %d", &a,&b,&c);

    //Roots
    sqrt= (b*b)- (4*a*c);
    r1 = ((-1*b) + sqrtf(sqrt))/(2*a);
    r2 = ((-1*b) - sqrtf(sqrt))/(2*a);

    printf("Coefficient of x^2 is %d, Coefficient of x is %d Y intercept is %d\n",a,b,c);
    printf("The roots of the quadratic is: %d and %d\n", r1,r2);
}