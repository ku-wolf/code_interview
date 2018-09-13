#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void stall() {
    int stall = 1;
    if (stall) {
        char c = getchar();
        printf("%c", c);
    }
}


long int get_file_size(FILE *file) {
    fseek(file, 0L, SEEK_END);
    long int file_size = ftell(file);
    rewind(file);
    return file_size;
}


void add_to_bucket(unsigned int * const buckets, const unsigned bucket_size, const unsigned num) {
    int index = floor(num / (sizeof(int) * 8));
    seen_ints[index] = seen_ints[index] | (1 << (num % (sizeof(int) * 8)));
}         


int int_bit_size():
    return sizeof(int) * 8;


int read_file_and_process(
    const char *fname, 
    const unsigned int chunk_size, 
    const int arg_count, 
    void * const *args,
    void (processer_func*)(void * const *)) {

    const File * const file = fopen(fname, "rb");
    unsigned int buffer[chunk_size];


    int bytes_read;
    if (file != NULL) {
        while ((bytes_read = fread(buffer, sizeof(int), chunk_size, file)) > 0) {
            for (int i = 0; i < bytes_read; i++){

                args[arg_count - 1] = (void *) &buffer[i];
                (*processor_func)(args)

            }     
        }
    }
   
    fclose(file);
}

int missing_int(const char *fname, const unsigned int number_of_ints, const float memory_amount_in_bytes) {
    const unsigned float max_int_val = pow(2, int_bit_size());
    const unsigned float half_mem = floor(memory_amount_in_bytes / 2);
    
    const unsigned int n_buckets = max_int / half_mem;
    const unsigned int bucket_size = ceil(max_int_val / n_buckets);
    const unsigned int int_vector_size = ceil(bucket_size / int_bit_size());


    const unsigned int chunk_size = half_mem;
    unsigned int * const seen_int_args = malloc(sizeof(unsigned int) * int_vector_size);
    unsigned int * const 

    for (int i = 0; i < int_vector_size; i++) {
         seen_ints[i] = 0;
    }

    const unsigned int add_to_seen_argc = 3;
    void *seen_int_args[] = {
        (void *) int_vector_size,
        (void *) seen_ints,
        (void *) 0
    };

    read_file_and_process(fname, chunk_size, 3, seen_int_args, add_to_seen_ints);
    
    int index;
    int ret = -1;

    for (int i = 0; i < number_of_ints; i++) {
            index = floor(i / (sizeof(int) * 8));
            
            if (!(seen_ints[index] & (1 << (i % (sizeof(int) * 8))))) {
                 ret = i;
            }
        }

   printf("excluded: %u\n", ret);
  
   stall();
   free(seen_ints); 

   return ret;
}

int main(const int argc, const char * const argv[]) {
    if (argc < 2) {
        printf("Gimme file name\n");
        exit(1);
    }

    const char * const fname = argv[1];
    const unsigned int number_of_ints = (unsigned int)atoi(argv[2]);

    stall();
    missing_int(fname, number_of_ints);
    
    return 0;
}
