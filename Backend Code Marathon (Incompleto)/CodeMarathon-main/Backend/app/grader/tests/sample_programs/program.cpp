/*
Sample program for testing. Receives an integer as an input and prints that
input + 1.
*/


#include <stdio.h>
#define IN_SIZE 1024


int main(){
    char input[IN_SIZE];
    int number;
    int retval = scanf("%d\n", &number);
    if(!retval){
        fprintf(stderr, "No number was scanned!");
        return 1;
    }
    printf("%d\n", number + 1);
    return 0;
}