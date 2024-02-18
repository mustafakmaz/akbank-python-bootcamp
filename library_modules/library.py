class Library:
    def __init__(self):
        try:
            self.library_books = open("books.txt", "a+")
        except Exception as e:
            print(f"File operation error: {e}")

    def read_book_file(self):
        try:
            self.library_books.seek(0)
            self.books = self.library_books.read()
            self.books = self.books.splitlines()
            return self.books
        except Exception as e:
            print(f"File operation error: {e}")
        
    def list_books(self):
        self.all_books = self.read_book_file()
        for i, item in enumerate(self.all_books):
            splitted_book_info = item.split(",")
            print(f"\nName:{splitted_book_info[0]}\nAuthor:{splitted_book_info[1]}\nDate:{splitted_book_info[2]}\nPages:{splitted_book_info[3]}")

    def add_book(self, book_name, author, date, page):
        self.all_books = self.read_book_file()
        self.new_book = book_name + "," + author + "," + date + "," + page
        self.new_book = self.new_book.splitlines()
        self.all_books = self.all_books + self.new_book
        try:
            self.library_books.truncate(0)
            for book in self.all_books:
                self.library_books.write(f"{book}\n")
            print(f"{book_name} book is added to the system.")
        except Exception as e:
            print(f"File operation error: {e}")
        
    def delete_book(self, deleted_book):
        self.all_books = self.read_book_file()
        for i, item in enumerate(self.all_books):
            splitted_book_info = item.split(",")
            if splitted_book_info[0] == deleted_book:
                self.all_books.pop(i)
                try:
                    self.library_books.truncate(0)
                    for book in self.all_books:
                        self.library_books.write(f"{book}\n")
                except Exception as e:
                    print(f"File operation error: {e}")
                print(f"{deleted_book} book is deleted from the system.")
                return 0
                
        print("\nBook not found.")

    def search_book(self, searched_book):
        self.all_books = self.read_book_file()
        for i, item in enumerate(self.all_books):
            splitted_book_info = item.split(",")
            if splitted_book_info[0] == searched_book:
                print("\nBook found!")
                print(f"\nName:{splitted_book_info[0]}\nAuthor:{splitted_book_info[1]}\nDate:{splitted_book_info[2]}\nPages:{splitted_book_info[3]}")
                return 0

        print("\nBook not found.")

    def __del__(self):
        self.library_books.close()
        del self.library_books
