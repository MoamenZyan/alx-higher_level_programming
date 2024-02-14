#!/bin/bash

files=$(ls)
for i in $files;
do
    touch /home/moamenzyan/ALX/alx-higher_level_programming/0x0D-SQL_introduction/$i
    cat $i > /home/moamenzyan/ALX/alx-higher_level_programming/0x0D-SQL_introduction/$i
done
