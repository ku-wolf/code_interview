cc=gcc
cflags=-Wall -lm
sources=$(wildcard *.c)
executables=$(sources:.c=)

all: $(sources) $(executables)

$(executables): %: %.c 
	$(cc)  $@.c $(cflags) -o $@

.PHONY: clean
clean: 
	rm $(executables)
