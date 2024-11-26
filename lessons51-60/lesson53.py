# * Решение практической части — Чтение данных формата .json

import json
from catalog_actions import show_all_books, add_new_book, search_book_by_author, save_books

with open("lesson53_library.json", "r", encoding="utf-8") as file:
    books = json.load(file)

while True:
    print("Выберите действие:\n"
          "1. Показать все книги\n"
          "2. Добавить новую книгу\n"
          "3. Найти книги по автору\n"
          "4. Сохранить изменения\n"
          "5. Выход\n")

    selected_action = input("Введите номер действия: ")

    if selected_action == "1":
        show_all_books(books)

    elif selected_action == "2":
        add_new_book(books)

    elif selected_action == "3":
        search_book_by_author(books)

    elif selected_action == "4":
        save_books(books)

    elif selected_action == "5":
        print("\nПрограмма завершена.")
        break

    else:
        print("\nНекорректный ввод. Попробуйте ещё раз.")
        continue

    print("\n--------------------------------------------------\n")