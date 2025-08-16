class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: रु {self.price:.2f}")
        print("-" * 30)
    
    def update_price(self, new_price):
        self.price = new_price
        print(f"Price updated to रु {self.price:.2f}")


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1815)

print("Book Information:")
book1.display_info()

print("Updating price...")
book1.update_price(2250)
print("\nUpdated Book Information:")
book1.display_info()

book2 = Book("To Kill a Mockingbird", "Harper Lee", 2000)
print("Second Book Information:")
book2.display_info()

book2.update_price(1850)
print("After price update:")
book2.display_info()