class Book:
    def __init__(self, title, author,isbn):
        self._title = title
        self._author = author
        self._isbn = isbn

    def __str__(self):
        return f"{self._title} + {self._author} + {self._isbn}"
    
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        self._title = title
    
    def get_author(self):
        return self._author
    
    def set_author(self, author):
        self._author = author
        
    def get_isbn(self):
        return self._isbn
    
    def set_isbn(self, isbn):
        self._isbn = isbn
        
class Fiction(Book):
    def __init__(self,title, author,isbn, genre):
        super().__init__(title, author, isbn)
        self._genre = genre
    
    def __str__(self):
        return f"{super().__str__ ()}- Fiction ({self._genre})"
    
class NonFiction(Book):
    def __init__(self, title, author, isbn,topic):
        super().__init__(title, author, isbn)
        self._topic = topic
        
    def __str__(self):
        return f"{super().__str__()} - NonFiction ({self._topic})"   
    
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self,book):
        self.books.append(book)
        print( "Added book")
            
    def remove_book(self,title):
        for book in self.books:
            if book.get_title() == title:
                self.books.remove(book)
                print( "Removed book")
                return
            print("Book not found")
        
    def display_books(self):
        if self.books:
            print("Book available")
            for book in self.books:
                print(f"{book}")
        else:
            print("Book not available")

def add_fiction_book():
    title=input("Enter title")
    author = input("Enter author")
    isbn = input("Enter ISBN")
    genre = input("Enter genre")
    return Fiction(title, author, isbn, genre)

def add_non_fiction_book():
    title=input("Enter title")
    author = input("Enter author")
    isbn = input("Enter ISBN")
    topic = input("Enter topic")
    return NonFiction(title, author, isbn, topic)

def main():
    library = Library()
    menu = {
        '1': lambda: library.add_book(add_fiction_book()),
        '2': lambda: library.add_book(add_non_fiction_book()),
        '3':library.display_books,
        '4':exit
    }
    
    while True:
        print("1. Add Fiction Book")
        print("2. Add Nonfiction Book")
        print("3. Display Books")
        print("4. Exit")
        
        choice = input("Choose an option")
    
        try:
            action = menu[choice]
            if callable(action):
                action()
            else:
                print('Invalid')
        except KeyError:
            print('Invalid error')

if __name__ == "__main__":
    main()