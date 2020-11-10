#include <stdio.h>

void function() {
    int a; //variable
    int *ret = &a + 3; //pointer ret pointing to Saved Frame Pointer (SFP)
    (*ret) = 4199890; //assign decimal integer address of the 'instruction we want code to redirect' to the SFP
}

void main() {
    int x = 56; //initial value
    function(); //function call
    x = 1; //to be skipped
    printf("%d\n", x); //print initial value
}