#!/bin/bash

# Да, создаётся 315 файлов, но зато очень удобно работать с ними в дальнейшем

# Выбор числа добавляемых времён
if [ -z "$1" ]; then
    num_of_tests=20;
else
    num_of_tests=$1;
fi

# Очистка файлов для записи (перезадать)
if [ -n "$2" ]; then
    ./clean.sh;
fi

function generate_data {
# Заполняем датасет временами
i=0
while [ $i -lt "$num_of_tests" ]
do
    ../app_files/"$1".exe < ../prog_data/in_files/in_"$2".txt >> ../dataset/"$1"/"$2".txt
    i=$((i+1));
done
}

# можно добавить ветвление, чтобы не всё сразу заполнять, если нужно
# Генерация датасета
for typ in ptrs_Os ptrs_O0 ptrs_O1 ptrs_O2 ptrs_O3 idx_Os idx_O0 idx_O1 idx_O2 idx_O3 mix_Os mix_O0 mix_O1 mix_O2 mix_O3
do
    k=1;
    while [ "$k" -le 10000 ]
    do
        echo -n -e "$typ $k \r"
        generate_data "$typ" "$k"
        if [ "$k" -eq 1 ]; then k=$((k+499));
        else k=$((k+500)); fi
    done
done
