class Product:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = int(price)


    def product_information(self):

        try:
            display_option = int(input("Enter (1) to display product Brand, (2) for price, (3) for both "))
            
            if display_option == 1:
                print(f"Brand: {self.brand}")
            
            elif display_option == 2:
                print(f"Price: {self.price}")
            
            elif display_option == 3:
                print(f"Name: {self.name}\nPrice: {self.price}")

            else: 
                print("Please respond with 1, 2, or 3")
        
        except ValueError:
            print("Please respond with 1, 2, or 3")



class Book(Product):
    def __init__ (self, brand, price, genre, author):
        
        self.author = author
        self.genre = genre
        super().__init__(brand, price)

    def product_information(self):

        try:
            display_option = int(input("Enter (1) to display product Brand, (2) for price,\n(3) for genre, (4) for author, (5) for all\n\n"))
            
            if display_option == 1:
                print(f"Brand: {self.brand}")

            elif display_option == 2:
                print(f"Price: {self.price}")

            elif display_option == 3:
                print(f"Genre: {self.genre}")
            
            elif display_option == 4:
                print(f"Author: {self.author}")

            elif display_option == 5:
                print(f"Name: {self.brand}\nPrice: {self.price}\nGenre: {self.genre}\nAuthor: {self.author}")
            
            else:
                print("Respond with number 1-5")

        except ValueError:
            print("Answer must be an integer 1-5")


# phone = Product ("Apple", 500)

# book1 = Book("Hunger Games", 40, "dystopian", "Collins")

# book1.product_information()



class Electronic(Product):
    def __init__(self, brand, price, built_in_wifi, type):
        self.built_in_wifi = built_in_wifi
        self.type = type
        super().__init__(brand, price)

    def product_information(self):

        try:
            display_option = int(input("Enter (1) to Display Product Brand, (2) for Price,\n(3) for Built In Wifi, (4) for Type, (5) for All\n\n"))
            
            if display_option == 1:
                print(f"Brand: {self.brand}")

            elif display_option == 2:
                print(f"Price: {self.price}")

            elif display_option == 3:
                print(f"Built In Wifi : {self.built_in_wifi}")
            
            elif display_option == 4:
                print(f"Type: {self.type}")

            elif display_option == 5:
                print(f"Brand: {self.brand}\nPrice: {self.price}\nBuilt in Wifi: {self.built_in_wifi}\nType: {self.type}")
            
            else:
                print("Respond with number 1-5")

        except ValueError:
            print("Answer must be an integer 1-5")


# phone1 = Electronic("SideKick", 150, "no", "Phone")


# phone1.product_information()


class Clothing(Product):

    def __init__(self, brand, price, size, color):
        self.size = size
        self.color = color
        super().__init__(brand, price)

    def product_information(self):

        try:
            display_option = int(input("Enter (1) to Display Product Brand, (2) for Price,\n(3) for Size, (4) for Color, (5) for All\n\n"))
            
            if display_option == 1:
                print(f"Brand: {self.brand}")

            elif display_option == 2:
                print(f"Price: {self.price}")

            elif display_option == 3:
                print(f"Size : {self.size}")
            
            elif display_option == 4:
                print(f"Type: {self.color}")

            elif display_option == 5:
                print(f"Brand: {self.brand}\nPrice: {self.price}\nSize: {self.size}\nColor: {self.color}")
            
            else:
                print("Respond with number 1-5")

        except ValueError:
            print("Answer must be an integer 1-5")


# shirt = Clothing("Pro Club", 8, "Large", "White")

# shirt.product_information()