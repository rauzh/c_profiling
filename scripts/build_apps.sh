#!/bin/bash

if [ -f "../app_files/*" ]; then
    rm ../app_files/*
fi

# Os
gcc -std=c99 -Wall -Werror -Wpedantic -o ../app_files/ptrs_Os.exe -Os ../progs/ptrs.c -lm
gcc -std=c99 -Wall -Werror -Wpedantic -o ../app_files/mix_Os.exe -Os ../progs/mix.c -lm
gcc -std=c99 -Wall -Werror -Wpedantic -o ../app_files/idx_Os.exe -Os ../progs/idx.c -lm

# O0
gcc -std=c99 -Wall -Werror -Wpedantic -o ../app_files/ptrs_O0.exe -O0 ../progs/ptrs.c -lm
gcc -std=c99 -Wall -Werror -Wpedantic -o ../app_files/mix_O0.exe -O0 ../progs/mix.c -lm
gcc -std=c99 -Wall -Werror -Wpedantic -o ../app_files/idx_O0.exe -O0 ../progs/idx.c -lm

# O1
gcc -std=c99 -Wall -Werror -Wpedantic -o ../app_files/ptrs_O1.exe -O1 ../progs/ptrs.c -lm
gcc -std=c99 -Wall -Werror -Wpedantic -o ../app_files/mix_O1.exe -O1 ../progs/mix.c -lm
gcc -std=c99 -Wall -Werror -Wpedantic -o ../app_files/idx_O1.exe -O1 ../progs/idx.c -lm

# O2
gcc -std=c99 -Wall -Werror -Wpedantic -o ../app_files/ptrs_O2.exe -O2 ../progs/ptrs.c -lm
gcc -std=c99 -Wall -Werror -Wpedantic -o ../app_files/mix_O2.exe -O2 ../progs/mix.c -lm
gcc -std=c99 -Wall -Werror -Wpedantic -o ../app_files/idx_O2.exe -O2 ../progs/idx.c -lm

# O3
gcc -std=c99 -Wall -Werror -Wpedantic -o ../app_files/ptrs_O3.exe -O3 ../progs/ptrs.c -lm
gcc -std=c99 -Wall -Werror -Wpedantic -o ../app_files/mix_O3.exe -O3 ../progs/mix.c -lm
gcc -std=c99 -Wall -Werror -Wpedantic -o ../app_files/idx_O3.exe -O3 ../progs/idx.c -lm
