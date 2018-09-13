#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int generate_int_file(char *fname, unsigned int number_of_integers) {
    srand((unsigned int)time(NULL));
    int excluded = rand() % number_of_integers;
    
    FILE *file = NULL;
    file = fopen(fname, "wb");

    if (file != NULL) {
        for (int i = 0; i < number_of_integers + 1; i++){
            if (i == excluded){
               i += 1; 
            }
            fwrite(&i, sizeof(int), 1, file); 
        }
    }
    fclose(file);
    return excluded;
}

int main(int argc, char *argv[]) {
    char *fname;
    unsigned int number_of_ints; 
    if (argc < 3) {
        printf("Gimme some args: file_name, number_of_ints_in_file\n");
        exit(1);
    }
    
    fname = argv[1];
    number_of_ints = (unsigned int)atoi(argv[2]);

    int excluded = generate_int_file(fname, number_of_ints);
    printf("excluded: %u\n", excluded);
    return 0;
}
