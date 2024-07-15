#!/bin/bash

while [ -n "$1" ]
do
    case "$1" in
        -i) pdm install ;;
        -u) git pull && pdm install ;;
        *) echo "$1 is not an option" ;;
    esac
    shift
done

pdm run python main.py