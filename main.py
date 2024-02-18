from library_modules import library

def menu(object):
    print("\nWelcome to the Library Management System (LMS)")
    print("Choose an option.")
    print("1-List all books")
    print("2-Add a book")
    print("3-Delete a book")
    print("4-Search a book")
    print("5-Quit the system")
    user_input = int(input("Your option: "))
    if user_input == 1:
        lib.list_books()
        menu(lib)
    elif user_input == 2:
        book_name = input("Enter book name: ")
        author = input("Enter book author: ")
        date = str(input("Enter book date: "))
        page = str(input("Enter page count: "))
        lib.add_book(book_name, author, date, page)
        menu(lib)
    elif user_input == 3:
        deleted_book = input("Enter the name of to be deleted book: ")
        lib.delete_book(deleted_book)
        menu(lib)
    elif user_input == 4:
        searched_book = input("Enter the name of to be searched book: ")
        lib.search_book(searched_book)
        menu(lib)
    elif user_input == 5:
        print("See you later.")
        exit()
    else:
        print("Not supported. Please choose an appropiate option.")
        menu(lib)

if __name__ == "__main__":
    lib = library.Library()
    menu(lib)
