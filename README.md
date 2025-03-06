<p align="center" style="margin-top: 120px">

  <h1 align="center">Z1_tester :wheelchair: </h1>
It was created out of laziness to check every test case manually—so now testing is a breeze!

## Run Tester :runner:
```shell
make run
```
>### By default, the tester uses z1.c located in the root of the project. If you want to test a different C file, specify its path with the SRC argumen also with docker. For example:

>```shell
>make run SRC=path/to/file
>```

## Clean Directories  :broom:
```shell
make clean
```

## Run in Docker :whale:
```shell
make d-run
```

## Purge Docker :wastebasket:
```shell
make d-purge 
``` 
