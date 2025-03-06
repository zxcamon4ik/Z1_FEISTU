CC = gcc
CFLAGS =
TARGET=Tcase
NAME = tmpTest.txt
INPUT ?= -10 10 0.5 2 8 h
SRC = z1.c

bin:
	mkdir -p bin

cases:
	mkdir -p cases/local 
	mkdir -p cases/tests


build: $(SRC)
	@($(CC) $(CFLAGS) -o bin/$(TARGET) $(SRC) -lm)


create: build
	@echo "$(INPUT)" | timeout 5 ./bin/$(TARGET) > cases/local/$(NAME)

clean:
	@(rm -rf cases/local/*.txt)
	@(find bin/ -mindepth 1 -maxdepth 1 -not -name ".gitignore" -exec rm -rf {} +)
	@echo "Clean!" 

run:
	python3 main.py 

.PHONY: bin cases create build run clean  

