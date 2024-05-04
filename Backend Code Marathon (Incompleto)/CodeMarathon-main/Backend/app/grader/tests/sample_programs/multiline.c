/*
Sample program for testing. Receiving and outputting multiple lines. It
receives 2 numbers, prints their adition and their multiplication.
*/


#include <stdio.h>
#define IN_SIZE 1024


int main(){
    char input[IN_SIZE];
    int number1, number2;
    int retval = scanf("%d\n", &number1);
    if(!retval){
        fprintf(stderr, "No number was scanned!");
        return 1;
    }
    int retval2 = scanf("%d\n", &number2);
    if(!retval){
        fprintf(stderr, "No number was scanned!");
        return 1;
    }
    printf("%d\n", number1 + number2);
    printf("%d\n", number1 * number2);
    return 0;
}
