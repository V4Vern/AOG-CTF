#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void xor (char *input){
    unsigned char x[] = {105,203,60,74,180,194,95,26,212,199,241,43,211,170,88,140,10,82,191,229,19,57,200,45,211,23,28};
    for (int i = 0; i < sizeof(x)/sizeof(x[0]); i++) {
        input[i] ^= x[i];
    }
}

int main(int argc, char* argv[]){
    unsigned char user_input[128];
    unsigned char encflag[] = {88, 242, 127, 126, 207, 176, 111, 98, 224, 169, 159, 24, 140, 210, 104, 254, 85, 32, 143, 134, 120, 102, 253, 25, 189, 115, 97};
    
    printf("==============================\n");
    printf("Hi there! Enter the flag below \n");
    printf("==============================\nFlag> ");

    fgets(user_input, sizeof(user_input), stdin);
    user_input[strcspn(user_input, "\r\n")] = 0;

    unsigned int input_length = strlen(user_input);

    if (input_length != 27) {
        printf("Not the flag :(\n");
        return 0;
    }

    xor(user_input);

    for (int i = 0; i < input_length; i++) {
        if (user_input[i] != encflag[i]) {
            printf("Not the flag :(\n");
            return 0;
        }
    }

    printf("You got the flag!\n");
    return 0;
}