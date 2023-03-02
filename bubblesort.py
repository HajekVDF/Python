"""
Funkce pro řazení čísel v poli pomocí bubble sort algoritmu.

"""


def bubble_sort(arr):
    for x in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr