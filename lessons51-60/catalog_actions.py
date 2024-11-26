def show_all_books(books):
    print("\nВсе книги в каталоге:")

    if len(books) == 0:
        print("Каталог пуст")
    else:
        for book in books:
            print(f"- {book["title"]} - {book["author"]} ({book["year"]})")


def add_new_book(books):
    print("\nДобавление новой книги")
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Введите год публикации: ")

    new_book = {"title": title, "author": author, "year": year}

    books.append(new_book)

    print("\nКнига добавлена!")


def search_book_by_author(books):
    print("\nПоиск по автору")
    author = input("Введите имя автора: ")

    author_books = [book for book in books if book["author"] == author]

    print(f"\nКниги автора {author}:")

    if len(author_books) == 0:
        print("Ничего не найдено")
    else:
        for book in author_books:
            print(f"- {book["title"]} - {book["author"]} ({book["year"]})")


def save_books(books):
    with open("lesson53_library.json", "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4, ensure_ascii=False)

    print("\nДанные успешно сохранены!")