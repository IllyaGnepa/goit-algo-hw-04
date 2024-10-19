import timeit
import random

# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Функція для вимірювання часу виконання
def measure_time(algorithm, arr):
    return timeit.timeit(lambda: algorithm(arr.copy()), number=100)

# Генеруємо дані
n = 1000  # розмір масиву
sorted_arr = list(range(n))
reverse_arr = sorted_arr[::-1]
random_arr = [random.randint(0, n) for i in range(n)]

# Вимірювання часу
print("Merge Sort:")
print("Sorted array:", measure_time(merge_sort, sorted_arr))
print("Reverse array:", measure_time(merge_sort, reverse_arr))
print("Random array:", measure_time(merge_sort, random_arr))

print("\nInsertion Sort:")
print("Sorted array:", measure_time(insertion_sort, sorted_arr))
print("Reverse array:", measure_time(insertion_sort, reverse_arr))
print("Random array:", measure_time(insertion_sort, random_arr))

print("\nTimsort (sorted function):")
print("Sorted array:", measure_time(sorted, sorted_arr))
print("Reverse array:", measure_time(sorted, reverse_arr))
print("Random array:", measure_time(sorted, random_arr))

# Timsort є набагато ефективнішим на практиці завдяки адаптивності. 
# Він автоматично використовує сортування вставками для невеликих частин масиву та сортування злиттям для більших фрагментів, що робить його швидким як для випадкових, так і для частково відсортованих масивів.
