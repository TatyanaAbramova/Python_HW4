# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def get_primmary_factors(n):
    factors = list()
    devisor = 2
    while (n // devisor >= 1):
        if not n % devisor:
            factors.append(devisor)
            n = n // devisor
        else:
            devisor += 1
    return factors
print(list(set(get_primmary_factors(int(input('Введите число: '))))))