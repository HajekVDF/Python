"""
Funkce pro výpis zadaného počtu čísel fibonacciho posloupnosti.

"""


def fibonacci_sequence(n):
    set_nums = [0, 1]
    for i in range(2, n):
        set_nums.append(set_nums[i-1]+set_nums[i-2])
    return set_nums
