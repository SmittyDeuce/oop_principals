class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = int(price)


    def product_information(self):

        try:
            display_option = int(input("Enter (1) to display product name, (2) for price, (3) for both "))
            
            if display_option == 1:
                print(f"Name: {self.name}")
            
            elif display_option == 2:
                print(f"Price: {self.price}")
            
            elif display_option == 3:
                print(f"Name: {self.name}\nPrice: {self.price}")

            else: 
                print("Please respond with 1, 2, or 3")
        
        except ValueError:
            print("Please respond with 1, 2, or 3")



class Book(Product):
    def __init__ (self, name, price, genre, author):
        
        self.author = author
        self.genre = genre
        super().__init__(name, price)


phone = Product ("Apple", 500)

book1 = Book("Hunger Games", 40, "dystopian", "Polk")

book1.product_information()