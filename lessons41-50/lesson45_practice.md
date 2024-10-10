# Работа с файлами - Запись данных в файлы .txt - Практика

## Цели задания:
1. Закрепить работу с текстовыми файлами в разных режимах (запись, добавление).
2. Научиться логировать ошибки программы в отдельный файл.
3. Попрактиковаться в обработке ошибок с помощью исключений в Python.

## Задание:
Создайте программу, которая имитирует работу кассового аппарата и записывает отчет о проданных товарах в текстовый файл. Программа должна:

1. Принимать от пользователя информацию о проданных товарах: название товара (`product_name`), количество (`quantity`) и цену (`price`).

2. Записывать данные о каждом проданном товаре в файл в формате: Название товара, Количество, Цена.

3. В конце каждой записи добавлять итоговую сумму для каждого товара (количество * цена).

4. Если пользователь ввел некорректные данные (например, отрицательное количество или цену), программа должна записать сообщение об ошибке в отдельный лог-файл.

## Пример работы программы:

### Пример ввода:

```shell
Введите название товара (или "стоп" для завершения): Молоко
Введите количество: 3
Введите цену: 50

Введите название товара (или "стоп" для завершения): Хлеб
Введите количество: -2
Ошибка: Некорректное количество для товара "Хлеб" - -2

Введите название товара (или "стоп" для завершения): Яблоки
Введите количество: 5
Введите цену: 30

Введите название товара (или "стоп" для завершения): стоп
```

### Файл sales_report.txt после выполнения программы:

```commandline
Название товара: Молоко, Количество: 3, Цена: 50, Сумма: 150
Название товара: Яблоки, Количество: 5, Цена: 30, Сумма: 150
```

### Файл error_log.txt после выполнения программы:

```commandline
Ошибка: Некорректное количество для товара "Хлеб" - -2
```

