class Library:
    def __init__(self, library_name, library_books = [], library_authors = []):
        self.library_name = library_name
        self.library_books = []
        self.library_authors = []
    
    def __len__(self):
        return len(self.library_books)
    
    def __repr__(self):
        return f"<Library {self.library_name} have {self.library_books.__len__()} books and {self.library_authors.__len__()} authors>"
    
    def __str__(self):
        return f"Library {self.library_name} have {self.library_books.__len__()} books and {self.library_authors.__len__()} authors"
    
    def new_book(self, name, year, book_author):
        self.name = name
        self.year = year
        self.book_author = book_author
        
        self.library_books.append((name, year, book_author))
        self.book_author.books.append((self.name, self.year))
        
        if self.book_author not in self.library_authors:
            self.library_authors.append(self.book_author)
            
        Book.count += 1

        return Book(name, year, book_author)

    def group_by_author(self, author):
        self.author = author
        
        result_author = []
        
        for book in self.library_books:
            if book[2] == self.author:
                result_author.append(book)               
        return result_author
    
    def group_by_year(self, year):
        self.year = year
        
        result_year = []
        
        for book in self.library_books:
            if book[1] == self.year:
                result_year.append(book)            
        return result_year        


class Book:
    count = 0
    
    def __init__(self, name, year, author, count = 0):
        self.name = name
        self.year = year
        self.author = author
        
    def __str__(self):
        return f"{self.name}, {self.year} by {self.author.name}"
    
    def __repr__(self):
        return f"<{self.name}, {self.year} by {self.author.name}>"

class Author:
    def __init__(self, name, country, birthday, books = []):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []
    
    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"<{self.name}>"
        
        

library_1 = Library("Heroes")

orwell = Author("George Orwell", "England", "25 June 1903")
remarque = Author("Erich Maria Remarque", "German", "22 June 1898")

animal_farm = Book("Animal Farm", 1945, orwell)
_1984 = Book("1984", 1949, orwell)
time_to_love = Book("A Time to Love and a Time to Die", 1958, remarque)
western_front = Book("All Quiet on the Western Front", 1929, remarque)

animal_farm = library_1.new_book(animal_farm.name, animal_farm.year, animal_farm.author)
library_1.new_book(_1984.name, _1984.year, _1984.author)
library_1.new_book(time_to_love.name, time_to_love.year, time_to_love.author)
library_1.new_book(western_front.name, western_front.year, western_front.author)


print(len(library_1))

print(library_1.group_by_author(orwell))
print(library_1.group_by_author(remarque))
print(library_1.group_by_year(1949))
print(library_1.group_by_year(1929))

print(orwell.books)

print(library_1)

print(animal_farm)

print(Book.count)

