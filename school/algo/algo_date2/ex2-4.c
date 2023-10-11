#include <stdio.h>

int main() {
        char id[] = "My student ID is y**----";
        id[0] = '2';
        id[1] = '1';
        id[2] = '0';
        id[3] = '2';
        id[4] = '3';
        id[5] = '1';
        printf ("%s.\n", id);
        return(0);
}
