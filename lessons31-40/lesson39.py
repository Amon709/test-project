# Функции


# Функции - это блок кода, который можно вызвать множество раз.
# Функция может принимать аргументы и возвращать значение.


# Синтаксис функции

# def <имя_функции>(аргументы):
#     <тело функции>
#     return <значение>


# Пример функции

def division(x, y):
    return x / y

division_result_1 = division(10, 2)
division_result_2 = division(10, 4)

print(division_result_1)
print(division_result_2)


# Преимущества использования функций

# 1. Повторное использование кода
# 2. Упрощение структуры программы
# 3. Повышение читаемости
# 4. Лёгкость сопровождения и отладки
# 5. Снижение сложности
# 6. Гибкость и расширяемость
# 7. Инкапсуляция логики


# Аргументы функций могут быть обязательными и необязательными

# Пример функции с необязательным аргументом

def division(x, y=2):
    return x / y

print(division(10))
print(division(10, 4))


# Ключевое слово return

# Ключевое слово return используется для выхода из функции
# и возвращения результата выполнения функции
# в основную программу.

# По-умолчанию любая функция возвращает None


def division(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x / y

print(division(10, 4))
print(division(10, "4"))


def check_number(num):
    if num > 0:
        return "Число положительное"
    elif num < 0:
        return "Число отрицательное"

    return "Число равно нулю"

print(check_number(0))


# Правила написания названия функций

# 1. Строчные буквы: Используйте только строчные буквы.
# 2. Snake_case: Разделяйте слова с помощью символа подчеркивания (_).
# 3. Без специальных символов: Избегайте пробелов и специальных символов.
# 4. Глаголы: Начинайте названия с глаголов для отражения действий.
# 5. Описательность: Название должно четко описывать назначение функции.