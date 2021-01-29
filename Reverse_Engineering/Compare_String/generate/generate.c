#include <stdio.h>
#include <string.h>
#include <stdint.h>



int main(int argc, char const *argv[])
{
    uint8_t size = 28;
    uint8_t flagarr[32] = {45, 53, 63, 48, 119, 110, 47, 114, 47, 110, 49, 45, 106, 50, 91, 51, 100, 110, 44, 113, 50, 100, 91, 51, 45, 105, 47, 121};
    
    for(int i = 0; i < size; i++){
        flagarr[i] += 4;
    }


    printf("Hey there! Help me recover the flag!\n> ");
    
    uint8_t buffer[size+1];
    fgets(buffer,size+1,stdin);

    if(strcmp(buffer,flagarr) == 0) {
        printf("Correct! you got the flag!\n");
    }
    else {
        printf("Sorry, but that wasn't the flag.\n");
    }

    return 0;
}