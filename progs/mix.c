#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <sys/time.h>

#define MAX_ARRAY_SIZE 10000

void init_array(int *arr, const uint64_t n)
{
    for (uint64_t i = 0; i < n; i++)
        arr[i] = ((i % 92) + 7);
}

uint64_t get_microseconds(void)
{
    struct timeval tv;

    if (gettimeofday(&tv, NULL))
        return (uint64_t) -1;

    return (uint64_t)tv.tv_sec * 1000ULL * 1000ULL + tv.tv_usec;
}

int count_sum(int *arr, const uint64_t n, int temp, int sum)
{
    for (uint64_t i = 0; i < n; i++)
    {
        temp *= *(arr + i);
        sum += temp;
    }
 
  return sum;
}

int a[MAX_ARRAY_SIZE];

int main(void)
{
    FILE *trash;
    uint64_t n, start, end;

    int temp = 1, sum = 0;

    int rc = scanf("%lu", &n);

    init_array(a, n);

    start = get_microseconds();

    for (uint64_t i = 0; i < 300; i++)
        sum = count_sum(a, n, temp, sum);

    end = get_microseconds();

    printf("%lu\n", (end - start));

    a[0] *= sum;

    trash = fopen("../prog_data/trash/trash.txt", "w");
    fprintf(trash, "%d %d", sum, rc);
    fclose(trash);

    return EXIT_SUCCESS;
}
