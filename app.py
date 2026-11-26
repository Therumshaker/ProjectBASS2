
books = []  

def add_book():
    title = input("Въведи заглавие на книгата: ").strip()
    if title == "":
        print("Заглавието не може да е празно!")
    else:
        books.append(title)
        print("Книгата е добавена.")


def show_books():
    if len(books) == 0:
        print("Няма добавени книги.")
    else:
        print("Списък с книги:")
        number = 1
        for book in books:
            print(number, ". ", book, sep="")
            number += 1


def search_book():
    word = input("Въведи заглавие за търсене: ").strip().lower()
    found = False
    for book in books:
        if word in book.lower():
            print("Намерена книга:", book)
            found = True
    if not found:
        print("Няма такава книга.")


def delete_book():
    title = input("Въведи заглавие за изтриване: ").strip().lower()
    for book in books:
        if book.lower() == title:
            books.remove(book)
            print("Книгата е изтрита.")
            return
    print("Няма такава книга.")


def sort_books():
    books.sort(key=str.lower)
    print("Книгите са сортирани по азбучен ред.")
    show_books()


def count_books():
    print("Брой книги:", len(books))


def show_help():
    print("\nНалични команди:")
    print("add    - добавяне на книга")
    print("show   - показване на всички книги")
    print("search - търсене по заглавие")
    print("delete - изтриване на книга")
    print("sort   - сортиране по азбучен ред")
    print("count  - показване на броя на книгите")
    print("help   - помощ")
    print("exit   - изход\n")


print("Добре дошъл в приложението за книги!")
show_help()

while True:
    command = input("Въведи команда: ").strip().lower()

    if command == "add":
        add_book()
    elif command == "show":
        show_books()
    elif command == "search":
        search_book()
    elif command == "delete":
        delete_book()
    elif command == "sort":
        sort_books()
    elif command == "count":
        count_books()
    elif command == "help":
        show_help()
    elif command == "exit":
        print("Довиждане!")
        break
    else:
        print("Непозната команда! Напиши help за помощ.")
