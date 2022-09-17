# Вычислить число c заданной точностью d

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Какое-то неправильное число!")
    return number


def division(num1, num2):
    return num1 / num2


num1 = InputNumbers("Введите 1 число: ")
num2 = InputNumbers("Введите 2 число: ")
n = int(InputNumbers("Введите точность (количество знаков после запятой): "))
rezult = round(division(num1, num2), n)

print(f"Результат деления: {rezult}")