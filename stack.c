#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#ifndef BUF_SIZE
#define BUF_SIZE 100
#endif

int bof(char *str) {
    char buffer[BUF_SIZE];
    strcpy(buffer, str);
    return 1;
}

int main(int argc, char **argv) {
    char str[517];
    FILE *badfile;
    badfile = fopen("badfile", "r");
    fread(str, sizeof(char), 517, badfile);
    bof(str);
    printf("Returened Properly\n");
    return 1;
}