# # Define the main application class
# class ECommerceApp:
#     def __init__(self):
#         self.users = {}  # Store user information
#         self.products = {}  # Store product catalog
#         self.shopping_carts = {}  # Store user shopping carts
#         self.orders = {}  # Store user orders

#     # User Registration functionality
#     def register_user(self, username, email, password):
#         # Implement user registration logic, including email verification
#         pass

#     # Product Management functionality
#     def add_product(self, product_id, name, price, description, category):
#         # Add a product to the catalog
#         pass

#     def browse_products(self, category=None, search=None):
#         # Browse products based on category or search query
#         pass

#     # Shopping Cart Management functionality
#     def add_to_cart(self, user_id, product_id, quantity=1):
#         # Add products to the user's shopping cart
#         pass

#     def remove_from_cart(self, user_id, product_id):
#         # Remove products from the user's shopping cart
#         pass

#     def view_cart(self, user_id):
#         # View the contents of the user's shopping cart
#         pass

#     # Secure Payment Processing functionality
#     def process_payment(self, user_id):
#         # Integrate with payment gateway to process secure payments
#         pass

#     # Order Tracking functionality
#     def track_order(self, user_id, order_id):
#         # Track the status of a user's order
#         pass

#     # Customer Support functionality
#     def contact_customer_support(self, user_id, issue):
#         # Contact customer support for assistance
#         pass

#     # User Authentication functionality
#     def login(self, username, password):
#         # Authenticate user login credentials
#         pass

#     def logout(self, user_id):
#         # Log out the user
#         pass

#     # Data Security measures
#     def encrypt_data(self, data):
#         # Encrypt sensitive data
#         pass

#     def decrypt_data(self, data):
#         # Decrypt encrypted data
#         pass

# # Main function to run the application
# def main():
#     # Initialize the e-commerce application
#     app = ECommerceApp()

#     # Implement the application logic based on user interactions
#     # This may involve handling user inputs, calling appropriate methods, and displaying outputs


# if __name__ == "__main__":
#     main()

# import os
# import random
# import string

# class User:
#     def __init__(self, username, password, address, email):
#         self.username = username
#         self.password = password
#         self.address = address
#         self.email = email

# class BankSystem:
#     def __init__(self):
#         self.users = {}
#         self.load_users()

#     def load_users(self):
#         if os.path.exists('users.txt'):
#             with open('users.txt', 'r') as file:
#                 for line in file:
#                     user_data = line.strip().split(',')
#                     if len(user_data) == 4:
#                         username, password, address, email = user_data
#                         self.users[username] = User(username, password, address, email)
#                     else:
#                         print(f"Issue with user data: {line.strip()}")

#     def save_users(self):
#         with open('users.txt', 'w') as file:
#             for user in self.users.values():
#                 file.write(f"{user.username},{user.password},{user.address},{user.email}\n")

#     def register(self, username, password, address, email):
#         if username not in self.users:
#             self.users[username] = User(username, password, address, email)
#             self.save_users()
#             print("Registration successful!")
#         else:
#             print("Username already exists. Please choose another one.")

#     def login(self, username, password):
#         if username in self.users and self.users[username].password == password:
#             print("Login successful!")
#             return True
#         else:
#             print("Invalid username or password.")
#             return False

#     def reset_password(self, email):
#         for user in self.users.values():
#             if user.email == email:
#                 new_password = input("Enter your new password: ")
#                 user.password = new_password
#                 self.save_users()
#                 print("Your password has been reset.")
#                 return True
#         print("Email address not found.")
#         return False

#     def handle_wrong_password(self, username):
#         print("Invalid password. Would you like to reset your password?")
#         choice = input("Enter 'yes' to reset password or 'no' to continue login: ").lower()
#         if choice == 'yes':
#             email = input("Enter your email address: ")
#             self.reset_password(email)
#         elif choice == 'no':
#             return
#         else:
#             print("Invalid choice.")

# class Product:
#     def __init__(self, name, price, description):
#         self.name = name
#         self.price = price
#         self.description = description

#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Price: ${self.price}")
#         print(f"Description: {self.description}")
#         print()

# class ProductCatalog:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product):
#         self.products.append(product)

#     def browse_products(self):
#         if not self.products:
#             print("No products available.")
#         else:
#             print("Available Products:")
#             for i, product in enumerate(self.products, 1):
#                 print(f"{i}. {product.name} - ${product.price}")

#     def get_product_by_index(self, index):
#         if 0 < index <= len(self.products):
#             return self.products[index - 1]
#         else:
#             return None

# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_to_cart(self, product, quantity=1):
#         for _ in range(quantity):
#             self.items.append(product)

#     def view_cart(self):
#         if not self.items:
#             print("Your shopping cart is empty.")
#         else:
#             print("Shopping Cart:")
#             for item in self.items:
#                 print(f"- {item.name} - ${item.price}")

#     def calculate_total(self):
#         return sum(item.price for item in self.items)

#     def save_total_to_file(self):
#         total_amount = self.calculate_total()
#         with open('total_amount.txt', 'w') as file:
#             file.write(f"Total amount in shopping cart: ${total_amount}")
#         print("Total amount saved to total_amount.txt file.")

# def main():
#     bank_system = BankSystem()
#     catalog = ProductCatalog()
#     shopping_cart = ShoppingCart()

#     # Adding sample products
#     catalog.add_product(Product("Laptop", 999, "A powerful laptop for work and gaming."))
#     catalog.add_product(Product("Smartphone", 699, "A high-performance smartphone with great camera quality."))
#     catalog.add_product(Product("Headphones", 99, "Wireless headphones with noise cancellation feature."))

#     while True:
#         print("\nWelcome to the GamGlam Beauty Shop!")
#         print("--------------------------------------")
#         print("1. Register")
#         print("2. Login")
#         # print("3. Reset Password")
#         print("3. Exit")

#         choice = input("Enter your choice (1-3): ")

#         if choice == '1':
#             username = input("Enter a username: ")
#             password = input("Enter a password: ")
#             address = input("Enter Your address: ")
#             email = input("Enter Your Email: ")
#             bank_system.register(username, password, address, email)
#         elif choice == '2':
#             username = input("Enter your username: ")
#             password = input("Enter your password: ")
#             if bank_system.login(username, password):
#                 while True:
#                     print("\nWhat would you like to do?")
#                     print("1. Browse Products")
#                     print("2. View Cart")
#                     print("3. Checkout")
#                     print("4. Logout")
#                     inner_choice = input("Enter your choice (1-4): ")

#                     if inner_choice == '1':
#                         catalog.browse_products()
#                     elif inner_choice == '2':
#                         shopping_cart.view_cart()
#                     elif inner_choice == '3':
#                         total_amount = shopping_cart.calculate_total()
#                         if total_amount > 0:
#                             print(f"Total amount in your cart: ${total_amount}")
#                             print("Proceed to secure payment processing.")
#                             # Implement payment processing logic here (not provided in this example)
#                             shopping_cart.save_total_to_file()  # Save the total amount to a file
#                             shopping_cart.items = []  # Clear the cart after successful purchase
#                             print("Purchase successful! Thank you for shopping with us.")
#                         else:
#                             print("Your cart is empty. Add items before checking out.")
#                     elif inner_choice == '4':
#                         print("Logged out successfully.")
#                         break
#                     else:
#                         print("Invalid choice. Please enter a number between 1 and 4.")
#                 break
#             else:
#                 bank_system.handle_wrong_password(username)
#         elif choice == '3':
#             email = input("Enter your email address: ")
#             bank_system.reset_password(email)
#         elif choice == '4':
#             print("Thank you for using the GamGlam Beauty Shop. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 4.")


# if __name__ == "__main__":
#     main()





# import os

# class User:
#     def __init__(self, username, password, address, email):
#         self.username = username
#         self.password = password
#         self.address = address
#         self.email = email

# class BankSystem:
#     def __init__(self):
#         self.users = {}
#         self.load_users()

#     def load_users(self):
#         if os.path.exists('users.txt'):
#             with open('users.txt', 'r') as file:
#                 for line in file:
#                     user_data = line.strip().split(',')
#                     if len(user_data) == 4:
#                         username, password, address, email = user_data
#                         self.users[username] = User(username, password, address, email)
#                     else:
#                         print(f"Issue with user data: {line.strip()}")

#     def save_users(self):
#         with open('users.txt', 'w') as file:
#             for user in self.users.values():
#                 file.write(f"{user.username},{user.password},{user.address},{user.email}\n")

#     def register(self, username, password, address, email):
#         if username not in self.users:
#             self.users[username] = User(username, password, address, email)
#             self.save_users()
#             print("Registration successful!")
#         else:
#             print("Username already exists. Please choose another one.")

#     def login(self, username, password):
#         if username in self.users and self.users[username].password == password:
#             print("Login successful!")
#             return True
#         else:
#             print("Invalid username or password.")
#             return False

# class Product:
#     def __init__(self, name, category, price, description, image_url, reviews=[]):
#         self.name = name
#         self.category = category
#         self.price = price
#         self.description = description
#         self.image_url = image_url
#         self.reviews = reviews

#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Category: {self.category}")
#         print(f"Price: ${self.price}")
#         print(f"Description: {self.description}")
#         print(f"Image URL: {self.image_url}")
#         if self.reviews:
#             print("Customer Reviews:")
#             for review in self.reviews:
#                 print(f"- {review}")
#         else:
#             print("No reviews yet.")
#         print()

# class ProductCatalog:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product):
#         self.products.append(product)

#     def search_by_name(self, name):
#         results = [product for product in self.products if name.lower() in product.name.lower()]
#         self._display_search_results(results)

#     def search_by_category(self, category):
#         results = [product for product in self.products if category.lower() in product.category.lower()]
#         self._display_search_results(results)

#     def search_by_price_range(self, min_price, max_price):
#         results = [product for product in self.products if min_price <= product.price <= max_price]
#         self._display_search_results(results)

#     def _display_search_results(self, results):
#         if results:
#             print("Search Results:")
#             for product in results:
#                 product.display()
#         else:
#             print("No matching products found.")

#     def browse_products(self):
#         if not self.products:
#             print("No products available.")
#         else:
#             print("Available Products:")
#             for product in self.products:
#                 product.display()

# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_to_cart(self, product, quantity=1):
#         for _ in range(quantity):
#             self.items.append(product)

#     def view_cart(self):
#         if not self.items:
#             print("Your shopping cart is empty.")
#         else:
#             print("Shopping Cart:")
#             for item in self.items:
#                 print(f"- {item.name} - ${item.price}")

#     def calculate_total(self):
#         return sum(item.price for item in self.items)

#     def save_total_to_file(self):
#         total_amount = self.calculate_total()
#         with open('total_amount.txt', 'w') as file:
#             file.write(f"Total amount in shopping cart: ${total_amount}")
#         print("Total amount saved to total_amount.txt file.")

# def main():
#     bank_system = BankSystem()
#     catalog = ProductCatalog()
#     shopping_cart = ShoppingCart()

#     # Adding sample products
#     catalog.add_product(Product("Laptop", "Electronics", 999, "A powerful laptop for work and gaming.", "laptop.jpg", ["Great product!", "Fast delivery."]))
#     catalog.add_product(Product("Smartphone", "Electronics", 699, "A high-performance smartphone with great camera quality.", "smartphone.jpg", ["Excellent phone.", "Long battery life."]))
#     catalog.add_product(Product("Headphones", "Electronics", 99, "Wireless headphones with noise cancellation feature.", "headphones.jpg"))

#     while True:
#         print("\nWelcome to the GamGlam Beauty Shop!")
#         print("--------------------------------------")
#         print("1. Register")
#         print("2. Login")
#         print("3. Browse Products")
#         print("4. Search Products by Name")
#         print("5. Search Products by Category")
#         print("6. Search Products by Price Range")
#         print("7. View Cart")
#         print("8. Checkout")
#         print("9. Exit")

#         choice = input("Enter your choice (1-9): ")

#         if choice == '1':
#             username = input("Enter a username: ")
#             password = input("Enter a password: ")
#             address = input("Enter Your address: ")
#             email = input("Enter Your Email: ")
#             bank_system.register(username, password, address, email)
#         elif choice == '2':
#             username = input("Enter your username: ")
#             password = input("Enter your password: ")
#             if bank_system.login(username, password):
#                 break
#         elif choice == '3':
#             catalog.browse_products()
#         elif choice == '4':
#             name = input("Enter the name to search: ")
#             catalog.search_by_name(name)
#         elif choice == '5':
#             category = input("Enter the category to search: ")
#             catalog.search_by_category(category)
#         elif choice == '6':
#             min_price = float(input("Enter the minimum price: "))
#             max_price = float(input("Enter the maximum price: "))
#             catalog.search_by_price_range(min_price, max_price)
#         elif choice == '7':
#             shopping_cart.view_cart()
#         elif choice == '8':
#             total_amount = shopping_cart.calculate_total()
#             if total_amount > 0:
#                 print(f"Total amount in your cart: ${total_amount}")
#                 print("Proceed to secure payment processing.")
#                 # Implement payment processing logic here (not provided in this example)
#                 shopping_cart.save_total_to_file()  # Save the total amount to a file
#                 shopping_cart.items = []  # Clear the cart after successful purchase
#                 print("Purchase successful! Thank you for shopping with us.")
#             else:
#                 print("Your cart is empty. Add items before checking out.")
#         elif choice == '9':
#             print("Thank you for using the GamGlam Beauty Shop. Goodbye!")
#             break

# if __name__ == "__main__":
#     main()







import os
import random
import string

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
        # print()

class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def browse_products(self):
        if not self.products:
            print("No products available.")
        else:
            print("Available Products:")
            for i, product in enumerate(self.products, 1):
                print(f"\n{i}. {product.name} - ${product.price}")

    def show_all_products(self):
        if not self.products:
            print("No products available.")
        else:
            print("\nAll Products with Details:")
            for i, product in enumerate(self.products, 1):
                print(f"{i}. {product.name} - ${product.price}")
                print(f"   Description: {product.description}")
                print(f"   Image URL: {product.image_url}")
                print(f"   Category: {product.category}")
                print("   Reviews:")
                for review in product.reviews:
                    print(f"   - {review}")

    def search_by_name(self, name):
        found_products = [product for product in self.products if name.lower() in product.name.lower()]
        if found_products:
            print("Found Products:")
            for product in found_products:
                print(f"- {product.name} - ${product.price}")
        else:
            print("No products found with that name.")

    def search_by_category(self, category):
        found_products = [product for product in self.products if category.lower() in product.category.lower()]
        if found_products:
            print("Found Products:")
            for product in found_products:
                print(f"- {product.name} - ${product.price}")
        else:
            print("No products found in that category.")

    def search_by_price_range(self, min_price, max_price):
        found_products = [product for product in self.products if min_price <= product.price <= max_price]
        if found_products:
            print("Found Products:")
            for product in found_products:
                print(f"- {product.name} - ${product.price}")
        else:
            print("No products found in that price range.")
            
    def get_product_by_index(self, index):
        if 0 < index <= len(self.products):
            return self.products[index - 1]
        else:
            return None

class BankSystem:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        if os.path.exists('users.txt'):
            with open('users.txt', 'r') as file:
                for line in file:
                    user_data = line.strip().split(',')
                    if len(user_data) == 4:
                        username, password, address, email = user_data
                        self.users[username] = User(username, password, address, email)
                    else:
                        print(f"Issue with user data: {line.strip()}")

    def save_users(self):
        with open('users.txt', 'w') as file:
            for user in self.users.values():
                file.write(f"{user.username},{user.password},{user.address},{user.email}\n")

    def register(self, username, password, address, email):
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

    # def add_to_cart(self, product, quantity=1):
    #     for _ in range(quantity):
    #         self.items.append(product)

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

# # Define max_attempts outside main()
max_attempts = 3

def main():
    bank_system = BankSystem()
    product_catalog = ProductCatalog()
    shopping_cart = ShoppingCart()

    # Adding sample products
    product_catalog.add_product(Product("Laptop", 999, "A powerful laptop for work and gaming.", "laptop_image_url", ["Great laptop!", "Fast processing."], "Electronics"))
    product_catalog.add_product(Product("Smartphone", 699, "A high-performance smartphone with great camera quality.", "smartphone_image_url", ["Awesome phone!", "Great camera."], "Electronics"))
    product_catalog.add_product(Product("Headphones", 99, "Wireless headphones with noise cancellation feature.", "headphones_image_url", ["Amazing sound quality!", "Comfortable to wear."], "Electronics"))
    product_catalog.add_product(Product("Laptop", 999, "A powerful laptop for work and gaming.", "laptop_image_url", ["Great laptop!", "Fast processing."], "Electronics"))
    product_catalog.add_product(Product("Smartphone", 699, "A high-performance smartphone with great camera quality.", "smartphone_image_url", ["Awesome phone!", "Great camera."], "Electronics"))
    product_catalog.add_product(Product("Headphones", 99, "Wireless headphones with noise cancellation feature.", "headphones_image_url", ["Amazing sound quality!", "Comfortable to wear."], "Electronics"))
    product_catalog.add_product(Product("Headphones", 99, "Wireless headphones with noise cancellation feature.", "headphones_image_url", ["Amazing sound quality!", "Comfortable to wear."], "Electronics"))
    product_catalog.add_product(Product("Laptop", 999, "A powerful laptop for work and gaming.", "laptop_image_url", ["Great laptop!", "Fast processing."], "Electronics"))
    product_catalog.add_product(Product("Smartphone", 699, "A high-performance smartphone with great camera quality.", "smartphone_image_url", ["Awesome phone!", "Great camera."], "Electronics"))
    product_catalog.add_product(Product("Headphones", 99, "Wireless headphones with noise cancellation feature.", "headphones_image_url", ["Amazing sound quality!", "Comfortable to wear."], "Electronics"))
    product_catalog.add_product(Product("Laptop", 999, "A powerful laptop for work and gaming.", "laptop_image_url", ["Great laptop!", "Fast processing."], "Electronics"))
    product_catalog.add_product(Product("Smartphone", 699, "A high-performance smartphone with great camera quality.", "smartphone_image_url", ["Awesome phone!", "Great camera."], "Electronics"))
    product_catalog.add_product(Product("Headphones", 99, "Wireless headphones with noise cancellation feature.", "headphones_image_url", ["Amazing sound quality!", "Comfortable to wear."], "Electronics"))
    product_catalog.add_product(Product("Laptop", 999, "A powerful laptop for work and gaming.", "laptop_image_url", ["Great laptop!", "Fast processing."], "Electronics"))
    product_catalog.add_product(Product("Smartphone", 699, "A high-performance smartphone with great camera quality.", "smartphone_image_url", ["Awesome phone!", "Great camera."], "Electronics"))
    product_catalog.add_product(Product("Headphones", 99, "Wireless headphones with noise cancellation feature.", "headphones_image_url", ["Amazing sound quality!", "Comfortable to wear."], "Electronics"))
    product_catalog.add_product(Product("Headphones", 99, "Wireless headphones with noise cancellation feature.", "headphones_image_url", ["Amazing sound quality!", "Comfortable to wear."], "Electronics"))
    product_catalog.add_product(Product("Laptop", 999, "A powerful laptop for work and gaming.", "laptop_image_url", ["Great laptop!", "Fast processing."], "Electronics"))
    product_catalog.add_product(Product("Smartphone", 699, "A high-performance smartphone with great camera quality.", "smartphone_image_url", ["Awesome phone!", "Great camera."], "Electronics"))
    product_catalog.add_product(Product("Headphones", 99, "Wireless headphones with noise cancellation feature.", "headphones_image_url", ["Amazing sound quality!", "Comfortable to wear."], "Electronics"))
    product_catalog.add_product(Product("Laptop", 999, "A powerful laptop for work and gaming.", "laptop_image_url", ["Great laptop!", "Fast processing."], "Electronics"))
    product_catalog.add_product(Product("Smartphone", 699, "A high-performance smartphone with great camera quality.", "smartphone_image_url", ["Awesome phone!", "Great camera."], "Electronics"))
    product_catalog.add_product(Product("Headphones", 99, "Wireless headphones with noise cancellation feature.", "headphones_image_url", ["Amazing sound quality!", "Comfortable to wear."], "Electronics"))
    product_catalog.add_product(Product("Laptop", 999, "A powerful laptop for work and gaming.", "laptop_image_url", ["Great laptop!", "Fast processing."], "Electronics"))
    product_catalog.add_product(Product("Smartphone", 699, "A high-performance smartphone with great camera quality.", "smartphone_image_url", ["Awesome phone!", "Great camera."], "Electronics"))
    product_catalog.add_product(Product("Headphones", 99, "Wireless headphones with noise cancellation feature.", "headphones_image_url", ["Amazing sound quality!", "Comfortable to wear."], "Electronics"))
    product_catalog.add_product(Product("Headphones", 99, "Wireless headphones with noise cancellation feature.", "headphones_image_url", ["Amazing sound quality!", "Comfortable to wear."], "Electronics"))
    product_catalog.add_product(Product("Laptop", 999, "A powerful laptop for work and gaming.", "laptop_image_url", ["Great laptop!", "Fast processing."], "Electronics"))
    product_catalog.add_product(Product("Smartphone", 699, "A high-performance smartphone with great camera quality.", "smartphone_image_url", ["Awesome phone!", "Great camera."], "Electronics"))
    product_catalog.add_product(Product("Headphones", 99, "Wireless headphones with noise cancellation feature.", "headphones_image_url", ["Amazing sound quality!", "Comfortable to wear."], "Electronics"))

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
            while login_attempts < max_attempts:
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
                            while True:
                                print("\n1. Search for products by name")
                                print("2. Search for products by category")
                                print("3. Search for products by price range")
                                print("4. Show all products with details")
                                print("5. Go back to the main menu")
                               
                                search_choice = input("\nEnter your choice (1-5): ")

                                if search_choice == '1':
                                    name = input("\nEnter the product name: ")
                                    product_catalog.search_by_name(name)
                                elif search_choice == '2':
                                    category = input("Enter the category: ")
                                    product_catalog.search_by_category(category)
                                elif search_choice == '3':
                                    min_price = float(input("\nEnter the minimum price: "))
                                    max_price = float(input("\nEnter the maximum price: "))
                                    product_catalog.search_by_price_range(min_price, max_price)
                                elif search_choice == '4':
                                    product_catalog.show_all_products()
                                    
                                elif search_choice == '5':
                                    break  # Go back to the main menu
                                
                                else:
                                    print("\nInvalid choice. Please enter a number between 1 and 6.")
                        elif inner_choice == '2':
                            while True:
                                print("1. View Cart")
                                print("2. Add cart")
                                print("3. Checkout")
                                print("4. Remove cart")
                                print("5. Exit")
                                choice = input("\nEnter your choice (1-5): ")
                                if choice == '1':
                                   shopping_cart.view_cart()
                                   
                                elif choice == '2':
                                  while True:
                                    #   index = int(input("Enter the index of the product you want to add to the cart: "))
                                    #   product = product_catalog.get_product_by_index(index)
                                    #   if product:
                                    #       shopping_cart.add_item(product)
                                    #       print(f"{product.name} added to cart.")
                                    #   else:
                                    #       print("Invalid product index.")
                                    index = int(input("\nEnter the product number to add to your cart (0 to stop): "))
                                    if index == 0:
                                      break
                                    product = ProductCatalog.get_product_by_index(index)
                                    if product:
                                      quantity = int(input("Enter the quantity: "))
                                      shopping_cart.add_to_cart(product, quantity)
                                      print(f"{quantity} {product.name}(s) \nadded to your cart.")
                                    else:
                                       print("\nInvalid product number.")
                                       
                                elif choice == '3':
                                    total_amount = shopping_cart.calculate_total()
                                    if total_amount > 0:
                                         print(f"\nTotal amount in your cart: ${total_amount}")
                                         print("\nProceed to secure payment processing.")
                                         shopping_cart.save_total_to_file()
                                         shopping_cart.items = [] 
                                         print("\nPurchase successful! Thank you for shopping with us.")
                                    else:
                                        print("\nYour cart is empty. Add items before checking out.")
                                        
                                elif choice == '5':
                                    break
                           
                            
                        elif inner_choice == '8':
                            print("\nLogged out successfully.")
                            break
                        else:
                            print("Invalid choice. Please enter a number between (1-7).")

                    break
                else:
                    login_attempts += 1
                    if login_attempts < max_attempts:
                        print(f"\nInvalid username or password. You have {max_attempts - login_attempts} attempts remaining.")
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