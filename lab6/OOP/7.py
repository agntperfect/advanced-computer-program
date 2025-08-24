class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}" by {self.author}'


book1 = Book("Python Basics", "John Doe")
book2 = Book("OOP in Depth", "Jane Smith")

print(book1) 
print(book2)