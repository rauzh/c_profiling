import statistics as s
import numpy as np
'''
Структура обработки:

НА СЛУЧАЙ, ЕСЛИ СЧИТАЕМ ТОЛЬКО ДАННЫЕ ДЛЯ ГРАФИКОВ ПО УСЛОВИЮ:

В датасете имеется 15 папок.
На каждую такую папку выделяется массив "массив-папка" (arr-dir)
В каждой папке 21 файл, ПО УМОЛЧАНИЮ на каждый выделяется
    массив, кторый хранит в себе ср.ар.
Для О2 этот массив также хранит в себе макс и мин, median
для О3 индексов этот массив также хранит медиану и квартили

Получение файлов, форматированных под гнуплот, будет описано ниже

'''

# Заполнение массива-папки
def fill_arr_dir(arr):
    i = 1
    k = 1
    while(i <= 10000):
        with open("../dataset/"+arr[0]+"/"+str(i)+".txt", "r") as f:
            data = [float(row.strip()) for row in f]
            data = sorted(data)
            arr.append([])
            arr[k].append(i)
            arr[k].append(s.fmean(data) / 300)
            if (arr[0][-1] == '2'):
                arr[k].append(max(data) / 300)
                arr[k].append(min(data) / 300)
            if (arr[0] == 'idx_O3'):
                arr[k].append(max(data) / 300)
                arr[k].append(min(data) / 300)
                arr[k].append(data[len(data) // 2] / 300)
                arr[k].append(data[len(data) // 4] / 300)
                arr[k].append(data[len(data) // 4 * 3] / 300)
        if (i == 1): i += 499; k += 1
        else: i += 500; k += 1

# Создание файла по массиву-папке для первого графика
def make_file_1(arr):
	with open("../dataset/edited/1/"+arr[0]+".txt", "w") as f:
		for i in range(1, len(arr)):
			f.write(str(arr[i][0]) + "  " + str(arr[i][1]) + "\n")

# Создание файла по массиву-папке для второго графика
def make_file_2(arr):
	with open("../dataset/edited/2/"+arr[0]+".txt", "w") as f:
		for i in range(1, len(arr)):
			f.write(str(arr[i][0]) + "  " + str(arr[i][1]) + "  " + 
			str(arr[i][2]) + '  ' + str(arr[i][3]) + "\n")
			
# Создание файла по массиву-папке для третьего графика
def make_file_3(arr):
	with open("../dataset/edited/3/"+arr[0]+".txt", "w") as f:
		for i in range(1, len(arr)):
			f.write(str(arr[i][0]) + "  " + str(arr[i][3]) + "  " +
			str(arr[i][5]) + "  " + str(arr[i][4]) + "  " + str(arr[i][6]) + '  ' +
            str(arr[i][2]) + "\n")

def make_file_med(arr):
	with open("../dataset/edited/3/"+arr[0]+"med.txt", "w") as f:
		for i in range(1, len(arr)):
			f.write(str(arr[i][0]) + "  " + str(arr[i][4]) + "\n")


def main():
# Инициализация массивов
	ptrs_O0, mix_O0, idx_O0 = ['ptrs_O0'], ['mix_O0'], ['idx_O0']
	ptrs_O1, mix_O1, idx_O1 = ['ptrs_O1'], ['mix_O1'], ['idx_O1']
	ptrs_O2, mix_O2, idx_O2 = ['ptrs_O2'], ['mix_O2'], ['idx_O2']
	ptrs_O3, mix_O3, idx_O3 = ['ptrs_O3'], ['mix_O3'], ['idx_O3']
	ptrs_Os, mix_Os, idx_Os = ['ptrs_Os'], ['mix_Os'], ['idx_Os']

# Заполнение массивов
	fill_arr_dir(ptrs_O0); fill_arr_dir(ptrs_O1); fill_arr_dir(ptrs_O2)
	fill_arr_dir(ptrs_O3); fill_arr_dir(ptrs_Os)
	
	fill_arr_dir(mix_O0); fill_arr_dir(mix_O1); fill_arr_dir(mix_O2)
	fill_arr_dir(mix_O3); fill_arr_dir(mix_Os)
	
	fill_arr_dir(idx_O0); fill_arr_dir(idx_O1); fill_arr_dir(idx_O2)
	fill_arr_dir(idx_O3); fill_arr_dir(idx_Os)
 
 # Создание файлов для первого графика
	make_file_1(ptrs_O0); make_file_1(ptrs_O1); make_file_1(ptrs_O2)
	make_file_1(ptrs_O3); make_file_1(ptrs_Os)
	
	make_file_1(mix_O0); make_file_1(mix_O1); make_file_1(mix_O2)
	make_file_1(mix_O3); make_file_1(mix_Os)
	
	make_file_1(idx_O0); make_file_1(idx_O1); make_file_1(idx_O2)
	make_file_1(idx_O3); make_file_1(idx_Os)
	
# Cоздание файлов для второго и третьего графиков
	make_file_2(ptrs_O2); make_file_2(idx_O2); make_file_2(mix_O2)
	
	make_file_3(idx_O3); make_file_med(idx_O3)

main()
