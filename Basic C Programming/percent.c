#include<stdio.h>

int main () {
    float grades[5];
    float response, total, average;
// Average Calculation
    for (int i=0;i<5;++i) {
        printf("Please enter the grade #%i for the Student:\n", i+1);
        scanf("%f", &response);
            if (response<101 && response>0){
                grades[i] = response;
            } else {
                printf("Be for real and insert logical grades!!!");
            }
        }
    for (int y=0;y<5;y++) {
        total = total + grades[y];
    }
    average = total/5;
    printf("The Avergae percentage of this student's grades is: %0.2f\n", average);

// Grading Scheme
    if (average>80) {
        printf("This student receives an A+\n");
    } else if (average>=65 && average<=80) {
        printf("This student receives a B\n");
    } else if (average>=42 && average<=50) {
        printf("This student receive a C\n");
    } else {
        printf("This student receives an F\n");
    }
}