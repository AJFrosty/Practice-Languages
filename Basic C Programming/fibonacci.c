#include<stdio.h>

int main() {
    int num[25];
    int response;
    num[0] = -1;
    num[1] = 1;

    printf("Enter the length of the fibonacci sequence you wish to see: ");
    scanf("%d", &response);

    for (int i=2;i<=response+1;++i) {
        num[i] = num[i-1] + num[i-2];
        printf(" %d",num[i]);
    }
    printf("\n");
    return 0;
}