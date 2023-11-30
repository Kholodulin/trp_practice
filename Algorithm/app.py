import timeit
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

array = random.sample(range(1, 1000), 100)

bubble_sort_time = timeit.timeit(stmt="bubble_sort(array.copy())", globals=globals(), number=1000)
quick_sort_time = timeit.timeit(stmt="quick_sort(array.copy())", globals=globals(), number=1000)
merge_sort_time = timeit.timeit(stmt="merge_sort(array.copy())", globals=globals(), number=1000)
insertion_sort_time = timeit.timeit(stmt="insertion_sort(array.copy())", globals=globals(), number=1000)

print(f"Время выполнения сортировки пузырьком: {bubble_sort_time}")
print(f"Время выполнения быстрой сортировки: {quick_sort_time}")
print(f"Время выполнения сортировки слиянием: {merge_sort_time}")
print(f"Время выполнения сортировки вставками: {insertion_sort_time}")
