#! /usr/bin/bash

echo "THE PROGRAM BIGINS HERE : "

echo "NAME OF THE PROGRAM : $0"

echo "LIST OF ARGUMENTS PASSED TO PROGRAM : $@"

echo "NUMBER OF ARGUMENTS IN THE PROGRAM : $#"

if [ -z "$1" ]; then
    echo "USAGE : $0 <filename>"
    exit -1
fi

echo "HEADER ROW : head -1 $1"

echo "`tail -n +2 $1 | cat -n `"

Echo "The program end here...Thanks !! "


