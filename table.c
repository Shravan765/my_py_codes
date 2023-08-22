#include <stdio.h>

int main () {
    int num, n;
    printf("\nEnter number : ");
    scanf("%d",&num );
    n = 1;
    while (n< 11)
        {
            printf("\n%d", num);
            printf( " * %d", n); 
            printf(" =  %d", num*n );
            n += 1;
        }
    printf("\n\nDONE.........");

}