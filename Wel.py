import csv
import os
import random
import string
import re

class User:
    def __init__(self, username, password, address, email):
        self.username = username
        self.password = password
        self.address = address
        self.email = email

class Product:
    def __init__(self, name, price, description, image_url, reviews, category):
        self.name = name
        self.price = price
        self.description = description
        self.image_url = image_url
        self.reviews = reviews
        self.category = category

# class ProductCatalog:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product):
#         self.products.append(product)

#     def load_products_from_csv(self, filename):
#         with open(filename, 'r', newline='') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 name, price, description, image_url, reviews, category = row
#                 price = float(price)
#                 reviews = reviews.split(';')
#                 product = Product(name, price, description, image_url, reviews, category)
#                 self.add_product(product)

#     def save_products_to_csv(self, filename):
#         with open(filename, 'w', newline='') as file:
#             writer = csv.writer(file)
#             for product in self.products:
#                 writer.writerow([product.name, product.price, product.description, product.image_url, ';'.join(product.reviews), product.category])


class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    # def load_products_from_csv(self, filename):
    #     with open(filename, 'r', newline='') as file:
    #         reader = csv.reader(file)
    #         next(reader)  # Skip the header row
    #         for row in reader:
    #             name, price, description, image_url, reviews, category = row
    #             price = float(price)
    #             reviews = reviews.split(';')
    #             product = Product(name, price, description, image_url, reviews, category)
    #             self.add_product(product)
    
    def load_products_from_csv(self, filename):
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    if row:  # Check if the row is not empty
                        if len(row) == 6:
                            name, price, description, image_url, reviews, category = row
                            price = float(price)
                            reviews = reviews.split(';')
                            product = Product(name, price, description, image_url, reviews, category)
                            self.add_product(product)
                        else:
                            print(f"Skipping row: {row}. Expected 6 values, got {len(row)}")
                    else:
                        print("Skipping empty row.")
        except FileNotFoundError:
            print(f"File {filename} not found.")


class BankSystem:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        if os.path.exists('users.csv'):
            with open('users.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    username, password, address, email = row
                    self.users[username] = User(username, password, address, email)

    def save_users(self):
        with open('users.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for user in self.users.values():
                writer.writerow([user.username, user.password, user.address, user.email])

    # def register(self, username, password, address, email):
    #     if username not in self.users:
    #         self.users[username] = User(username, password, address, email)
    #         self.save_users()
    #         print("Registration successful!")
    #     else:
    #         print("Username already exists. Please choose another one.")
    def register(self, username, password, address, email):
        # Verify email format using regular expression
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email) and len(password) < 6:
            print("Invalid email format. Please enter a valid email address and Password must be at least 6 characters long.")
            return

        # Verify password length
        # if len(password) < 6:
        #     print("Password must be at least 6 characters long.")
        #     return

        # Verify mixed characters in password
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$", password):
            print("Password must contain a mix of uppercase and lowercase letters, and digits.")
            return

        if username not in self.users:
            self.users[username] = User(username, password, address, email)
            self.save_users()
            print("Registration successful!")
        else:
            print("Username already exists. Please choose another one.")

    def login(self, username, password):
        if username in self.users and self.users[username].password == password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password.")
            return False

    def reset_password(self, email):
        if email in [user.email for user in self.users.values()]:
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            for user in self.users.values():
                if user.email == email:
                    user.password = new_password
            self.save_users()
            print(f"Your password has been reset to: {new_password}")
        else:
            print("Email address not found.")

class ShoppingCart:
    def __init__(self):
        self.items = []

    def view_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.items:
                print(f"- {item.name} - ${item.price}")

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def add_to_cart(self, product, quantity=1):
        for _ in range(quantity):
            self.items.append(product)

    def save_total_to_file(self):
        total_amount = self.calculate_total()
        with open('total_amount.txt', 'w') as file:
            file.write(f"Total amount in shopping cart: ${total_amount}")
        print("Total amount saved to total_amount.txt file.")

def main():
    bank_system = BankSystem()
    product_catalog = ProductCatalog()
    shopping_cart = ShoppingCart()

    # product_catalog.load_products_from_csv('products.csv')
    product_catalog.load_products_from_csv('products.csv')


    while True:
        print("\nWelcome to the GamGlam Beauty Shop!")
        print("--------------------------------------")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == '1':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            address = input("Enter Your address: ")
            email = input("Enter Your Email: ")
            bank_system.register(username, password, address, email)
        elif choice == '2':
            login_attempts = 0
            while login_attempts < 3:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if bank_system.login(username, password):
                    print("\nLogged in successfully. \n Welcome to the GamGlam Beauty Shop!")
                    while True:
                        print("\nWhat would you like to do?")
                        print("1. Product Browsing")
                        print("2. Shopping Cart Management")
                        print("3. Secure Payment Processing")
                        print("4. Order Tracking")
                        print("5. User Authentication")
                        print("6. Data Security")
                        print("7. Customer Support")
                        print("8. Logout")
                        inner_choice = input("\nEnter your choice (1-7): ")

                        if inner_choice == '1':
                            product_catalog.show_all_products()
                        elif inner_choice == '2':
                            # Implement shopping cart management
                            pass
                        elif inner_choice == '8':
                            print("\nLogged out successfully.")
                            break
                        else:
                            print("Invalid choice. Please enter a number between (1-7).")

                    break
                else:
                    login_attempts += 1
                    if login_attempts < 3:
                        print(f"\nInvalid username or password. You have {3 - login_attempts} attempts remaining.")
                    else:
                        print("Maximum login attempts reached. You need to reset your password.")
                        email = input("Enter your email address to reset your password: ")
                        bank_system.reset_password(email)
                        break
        elif choice == '3':
            print("\nThank you for using the GamGlam Beauty Shop. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
