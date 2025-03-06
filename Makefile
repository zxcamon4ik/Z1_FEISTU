myUID := $(shell id -u)

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
	@make bin
	@echo "$(INPUT)" | timeout 5 ./bin/$(TARGET) > cases/local/$(NAME)

clean:
	@(rm -rf cases/local/*.txt)
	@(find bin/ -mindepth 1 -maxdepth 1 -not -name ".gitignore" -exec rm -rf {} +)
	@echo "Clean!" 

run:
	python3 main.py 


echo-i-uid:
	@echo $(myUID)


d-run:
	@make bin
	@export myUID=${myUID} && \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose build --build-arg SRC=$(SRC) && \
		docker compose up --build 

d-purge:
	@export myUID=${myUID} &&\
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down --volumes --remove-orphans --rmi local --timeout 0 


.PHONY: bin cases create build run clean d-run echo-i-uid d-purge 

