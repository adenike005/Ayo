# import csv
# import os
# import random
# import string
# import re

# class User:
#     def __init__(self, username, password, address, email):
#         self.username = username
#         self.password = password
#         self.address = address
#         self.email = email

# class Product:
#     def __init__(self, name, price, description, image_url, reviews, category):
#         self.name = name
#         self.price = price
#         self.description = description
#         self.image_url = image_url
#         self.reviews = reviews
#         self.category = category

# class ProductCatalog:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product):
#         self.products.append(product)

#     def load_products_from_csv(self, filename):
#         try:
#             with open(filename, 'r', newline='') as file:
#                 reader = csv.reader(file)
#                 next(reader)  # Skip the header row
#                 for row in reader:
#                     if row:  # Check if the row is not empty
#                         if len(row) == 6:
#                             name, price, description, image_url, reviews, category = row
#                             price = float(price)
#                             reviews = reviews.split(';')
#                             product = Product(name, price, description, image_url, reviews, category)
#                             self.add_product(product)
#                         else:
#                             print(f"Skipping row: {row}. Expected 6 values, got {len(row)}")
#                     else:
#                         print("Skipping empty row.")
#         except FileNotFoundError:
#             print(f"File {filename} not found.")

# class BankSystem:
#     def __init__(self):
#         self.users = {}
#         self.load_users()

#     def load_users(self):
#         if os.path.exists('users.csv'):
#             with open('users.csv', 'r', newline='') as file:
#                 reader = csv.reader(file)
#                 for row in reader:
#                     username, password, address, email = row
#                     self.users[username] = User(username, password, address, email)

#     def save_users(self):
#         with open('users.csv', 'w', newline='') as file:
#             writer = csv.writer(file)
#             for user in self.users.values():
#                 writer.writerow([user.username, user.password, user.address, user.email])

#     def save_cart_to_csv(self, username, shopping_cart):
#         try:
#             with open('total_amount.csv', 'a', newline='') as file:  # Use 'total_amount.csv' instead of 'user.csv'
#                 writer = csv.writer(file)
#                 for item in shopping_cart.items:
#                     writer.writerow([username, item.product.name, item.quantity, item.product.price * item.quantity])
#                 # Save the total amount of the shopping cart
#                 writer.writerow(['', '', 'Total Amount', '', shopping_cart.calculate_total()])
              
#             print("Shopping cart saved to total_amount.csv successfully.")  # Update the print statement
#         except Exception as e:
#             print(f"Error saving shopping cart: {e}")

#     def register(self, username, password, address, email):
#         if not re.match(r"[^@]+@[^@]+\.[^@]+", email) and len(password) < 6:
#             print("Invalid email format. Please enter a valid email address and Password must be at least 6 characters long.")
#             return

#         if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$", password):
#             print("Password must contain a mix of uppercase and lowercase letters, and digits.")
#             return

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
#         if email in [user.email for user in self.users.values()]:
#             new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
#             for user in self.users.values():
#                 if user.email == email:
#                     user.password = new_password
#             self.save_users()
#             print(f"Your password has been reset to: {new_password}")
#         else:
#             print("Email address not found.")

# class ShoppingCartItem:
#     def __init__(self, product, quantity):
#         self.product = product
#         self.quantity = quantity

# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def view_cart(self):
#         if not self.items:
#             print("Your shopping cart is empty.")
#         else:
#             print("Shopping Cart:")
#             total_items = 0
#             for item in self.items:
#                 print(f"- {item.product.name}({item.quantity}) - Total Amount: ${item.product.price * item.quantity:.2f}")
#                 total_items += item.quantity
#             print(f"Total items in cart: {total_items}")
#             print(f"Total amount: ${self.calculate_total():.2f}")  # Format the total amount with two decimal places and add the dollar sign

#     def calculate_total(self):
#         return sum(item.product.price * item.quantity for item in self.items)

#     def add_to_cart(self, product, quantity=1):
#         for item in self.items:
#             if item.product == product:
#                 item.quantity += quantity
#                 break
#         else:
#             self.items.append(ShoppingCartItem(product, quantity))

#     def save_total_to_file(self):
#         total_amount = self.calculate_total()
#         with open('total_amount.csv', 'w') as file:
#             file.write(f"Total amount in shopping cart: ${total_amount}")
#             file.write(f"username: ${User}")
#         print("Total amount saved to total_amount.txt file.")

# def main():
#     bank_system = BankSystem()
#     product_catalog = ProductCatalog()
#     shopping_cart = ShoppingCart()

#     product_catalog.load_products_from_csv('products.csv')

#     while True:
#         print("\nWelcome to the GamGlam Beauty Shop!")
#         print("--------------------------------------")
#         print("1. Register")
#         print("2. Login")
#         print("3. Exit")

#         choice = input("\nEnter your choice (1-3): ")

#         if choice == '1':
#             username = input("Enter a username: ")
#             password = input("Enter a password: ")
#             address = input("Enter Your address: ")
#             email = input("Enter Your Email: ")
#             bank_system.register(username, password, address, email)
#         elif choice == '2':
#             login_attempts = 0
#             while login_attempts < 3:
#                 username = input("Enter your username: ")
#                 password = input("Enter your password: ")
#                 if bank_system.login(username, password):
#                     print("\nLogged in successfully. \n Welcome to the GamGlam Beauty Shop!")
#                     while True:
#                         print("\nWhat would you like to do")
#                         print("\n1. Sell \n2. Buy")
#                         print("3. Logout")
#                         inner_choice = input("\nEnter your choice (1-3): ")

#                         if inner_choice == '1':
#                             product_name = input("Enter the product name: ")
#                             product_price = float(input("Enter the product price: "))
#                             product_description = input("Enter the product description: ")
#                             product_image_url = input("Enter the product image URL: ")
#                             product_reviews = input("Enter product reviews separated by ';': ").split(';')
#                             product_category = input("Enter the product category: ")

#                             new_product = Product(product_name, product_price, product_description, product_image_url, product_reviews, product_category)

#                             product_catalog.add_product(new_product)

#                             with open('products.csv', 'a', newline='') as file:
#                                 writer = csv.writer(file)
#                                 writer.writerow([product_name, product_price, product_description, product_image_url, ';'.join(product_reviews), product_category])

#                             print("Product added successfully.")

#                         elif inner_choice == '2':
#                             print("1. Product Browsing")
#                             print("2. Shopping Cart Management")
#                             print("3. Order Tracking")
#                             print("4. Customer Support")
#                             print("5. Transaction History")
#                             print("6. Logout")
#                             sub_choice = input("Enter your choice (1-5): ")
#                             if sub_choice == '1':
#                                 while True:
#                                     print("\nProduct Browsing")
#                                     print("-------------------------------")
#                                     print("1. Search for products by name")
#                                     print("2. Search for products by category")
#                                     print("3. Search for products by price range")
#                                     print("4. Show all products with details")
#                                     print("5. Go back to the main menu")

#                                     browse_choice = input("Enter your choice (1-5): ")

#                                     if browse_choice == '1':
#                                         search_name = input("Enter the product name to search: ")
#                                         found = False
#                                         print("Search Results:")
#                                         for product in product_catalog.products:
#                                             if search_name.lower() in product.name.lower():
#                                                 print(f"Name: {product.name}")
#                                                 print(f"Price: ${product.price}")
#                                                 print(f"Description: {product.description}")
#                                                 print(f"Image URL: {product.image_url}")
#                                                 print(f"Reviews: {product.reviews}")
#                                                 print(f"Category: {product.category}")
#                                                 print("--------------------------------")
#                                                 found = True
#                                         if not found:
#                                             print("No products found matching the search criteria.")
                                    
#                                     elif browse_choice == '2':
#                                         search_category = input("Enter the product category to search: ")
#                                         found = False
#                                         print("Search Results:")
#                                         for product in product_catalog.products:
#                                             if search_category.lower() in product.category.lower():
#                                                 print(f"Name: {product.name}")
#                                                 print(f"Price: ${product.price}")
#                                                 print(f"Description: {product.description}")
#                                                 print(f"Image URL: {product.image_url}")
#                                                 print(f"Reviews: {product.reviews}")
#                                                 print(f"Category: {product.category}")
#                                                 print("--------------------------------")
#                                                 found = True
#                                         if not found:
#                                             print("No products found matching the search criteria.")

#                                     elif browse_choice == '3':
#                                         min_price = float(input("Enter the minimum price: "))
#                                         max_price = float(input("Enter the maximum price: "))
#                                         found = False
#                                         print("Search Results:")
#                                         for product in product_catalog.products:
#                                             if min_price <= product.price <= max_price:
#                                                 print(f"Name: {product.name}")
#                                                 print(f"Price: ${product.price}")
#                                                 print(f"Description: {product.description}")
#                                                 print(f"Image URL: {product.image_url}")
#                                                 print(f"Reviews: {product.reviews}")
#                                                 print(f"Category: {product.category}")
#                                                 print("--------------------------------")
#                                                 found = True
#                                         if not found:
#                                             print("No products found matching the price range.")

#                                     elif browse_choice == '4':
#                                         print("All Products:")
#                                         for product in product_catalog.products:
#                                             print(f"Name: {product.name}")
#                                             print(f"Price: ${product.price}")
#                                             print(f"Description: {product.description}")
#                                             print(f"Image URL: {product.image_url}")
#                                             print(f"Reviews: {product.reviews}")
#                                             print(f"Category: {product.category}")
#                                             print("--------------------------------")

#                                     elif browse_choice == '5':
#                                         break  # Exit the product browsing section and go back to the main menu

#                                     else:
#                                         print("Invalid choice. Please enter a number between (1-5).")
#                             elif sub_choice == '2':
#                                 print("1. View Cart")
#                                 print("2. Add to Cart")
#                                 print("3. Save Total to File")
#                                 print("4. Go back to the main menu")
#                                 cart_choice = input("Enter your choice (1-4): ")
#                                 if cart_choice == '1':
#                                     shopping_cart.view_cart()
#                                 elif cart_choice == '2':
#                                     product_name = input("Enter the product name to add to the cart: ")
#                                     product = next((p for p in product_catalog.products if p.name.lower() == product_name.lower()), None)
#                                     if product:
#                                         quantity = int(input("Enter the quantity: "))
#                                         shopping_cart.add_to_cart(product, quantity)
#                                         print(f"{quantity} {product.name}(s) added to the shopping cart.")
#                                     else:
#                                         print("Product not found.")
#                                 elif cart_choice == '3':
#                                     shopping_cart.save_total_to_file()
#                                 elif cart_choice == '4':
#                                     break  # Exit the shopping cart management and go back to the main menu
#                                 else:
#                                     print("Invalid choice. Please enter a number between (1-4).")
#                             elif sub_choice == '3':
#                                 pass
#                             elif sub_choice == '4':
#                                 pass
#                             elif sub_choice == '6':
#                                 bank_system.save_cart_to_csv(username, shopping_cart)
#                                 print("\nLogged out successfully.")
#                                 break
#                             else:
#                                 print("Invalid choice. Please enter a number between (1-6).")
#                         elif inner_choice == '3':
#                             bank_system.save_cart_to_csv(username, shopping_cart)
#                             print("\nLogged out successfully.")
#                             break
#                         else:
#                             print("Invalid choice. Please enter a number between (1-3).")
#                     break
#                 else:
#                     login_attempts += 1
#                     if login_attempts < 3:
#                         print(f"\nInvalid username or password. You have {3 - login_attempts} attempts remaining.")
#                     else:
#                         print("Maximum login attempts reached. You need to reset your password.")
#                         email = input("Enter your email address to reset your password: ")
#                         bank_system.reset_password(email)
#                         break
#         elif choice == '3':
#             print("\nThank you for using the GamGlam Beauty Shop. Goodbye!")
#             break
#         else:
#             print("\nInvalid choice. Please enter a number between 1 and 3.")

# if __name__ == "__main__":
#     main()




 








# import csv
# import random
# import string
# import hashlib

# class User:
#     def __init__(self, username, password, address, email):
#         self.username = username
#         self.password = password
#         self.address = address
#         self.email = email
#         self.shopping_cart = ShoppingCart()

# class Product:
#     def __init__(self, name, price, description, image_url, reviews, category, inventory):
#         self.name = name
#         self.price = price
#         self.description = description
#         self.image_url = image_url
#         self.reviews = reviews
#         self.category = category
#         self.inventory = inventory

# class ShoppingCartItem:
#     def __init__(self, product, quantity):
#         self.product = product
#         self.quantity = quantity

# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def view_cart(self):
#         if not self.items:
#             print("Your shopping cart is empty.")
#         else:
#             print("Shopping Cart:")
#             total_items = 0
#             for item in self.items:
#                 print(f"- {item.product.name}({item.quantity}) - Total Amount: ${item.product.price * item.quantity:.2f}")
#                 total_items += item.quantity
#             print(f"Total items in cart: {total_items}")
#             print(f"Total amount: ${self.calculate_total():.2f}")

#     def calculate_total(self):
#         return sum(item.product.price * item.quantity for item in self.items)

#     def add_to_cart(self, product, quantity=1):
#         for item in self.items:
#             if item.product.name == product.name:
#                 item.quantity += quantity
#                 break
#         else:
#             self.items.append(ShoppingCartItem(product, quantity))
    
    
#     def remove_from_cart(self, product_name):
#         for item in self.items:
#             if item.product.name == product_name:
#                 self.items.remove(item)
#                 print(f"{product_name} removed from the cart.")
#                 return
#         print(f"{product_name} not found in the cart.")

#     def save_total_to_file(self, user):
#         total_amount = self.calculate_total()
#         with open('total_amount.csv', 'w') as file:
#             file.write(f"Total amount in shopping cart: ${total_amount}\n")
#             file.write(f"Username: {user.username}\n")
#             file.write("Product Details:\n")
#             for item in self.items:
#                 file.write(f"- {item.product.name}({item.quantity}) - Total Amount: ${item.product.price * item.quantity:.2f}\n")
#         print("Shopping cart details saved to total_amount.csv file.")

#     def load_cart_from_file(self, user):
#         try:
#             with open('total_amount.csv', 'r') as file:
#                 lines = file.readlines()
#                 if lines:
#                     user.username = lines[1].split(': ')[1].strip()
#                     items = lines[3:]
#                     for item_line in items:
#                         item_details = item_line.split(' - ')
#                         if len(item_details) >= 4:  # Ensure there are enough elements
#                             product_name = item_details[1].split('(')[0].strip()
#                             quantity = int(item_details[1].split('(')[1].split(')')[0].strip())
#                             product_price = float(item_details[3].split(': ')[1].strip())
#                             product = Product(product_name, product_price, '', '', '', '', 0)
#                             self.items.append(ShoppingCartItem(product, quantity))
#                         else:
#                             print("Invalid format in the shopping cart file. Skipping item.")
#                     # print("Shopping cart loaded from total_amount.csv file.")
#         except FileNotFoundError:
#             pass

# class UserManager:
#     def __init__(self):
#         self.users = {}
#         self.load_users()

#     def load_users(self):
#         try:
#             with open('users.csv', 'r') as file:
#                 reader = csv.DictReader(file)
#                 for row in reader:
#                     user = User(row['username'], row['password'], row['address'], row['email'])
#                     user.shopping_cart.load_cart_from_file(user)
#                     self.users[row['email']] = user
#         except FileNotFoundError:
#             pass

#     def save_users(self):
#         with open('users.csv', 'w', newline='') as file:
#             fieldnames = ['username', 'password', 'address', 'email']
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()
#             for user in self.users.values():
#                 writer.writerow({'username': user.username, 'password': user.password, 'address': user.address, 'email': user.email})

#     def register(self, username, password, address, email):
#         if len(password) < 6 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password) or not any(char in string.punctuation for char in password):
#             print("Password must be at least 6 characters long and contain a mix of letters, numbers, and special characters.")
#             return False

#         if '@gmail.com' not in email:
#             print("Email must be a Gmail address.")
#             return False

#         if email in self.users:
#             print("Email already exists. Please choose another one.")
#             return False

#         user = User(username, self.hash_password(password), address, email)
#         user.shopping_cart.load_cart_from_file(user)
#         self.users[email] = user
#         self.save_users()
#         print("Registration successful!")
#         return True

#     def login(self, email, password):
#         max_attempts = 3
#         login_attempts = 0
#         while login_attempts < max_attempts:
#             if email in self.users:
#                 if self.check_password(password, self.users[email].password):
#                     print("Login successful!")
#                     return True
#                 else:
#                     login_attempts += 1
#                     if login_attempts < max_attempts:
#                         print(f"\nInvalid username or password. You have {max_attempts - login_attempts} attempts remaining.")
#                     else:
#                         print("Maximum login attempts reached. You need to reset your password.")
#                         email = input("Enter your email address to reset your password: ")
#                         self.reset_password(email)
#                         break
#             else:
#                 print("Email not found.")
#                 return False

#     def reset_password(self, email):
#         if email in self.users:
#             new_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))
#             self.users[email].password = self.hash_password(new_password)
#             self.save_users()
#             print(f"Your password has been reset to: {new_password}")
#             return True
#         print("Email address not found.")
#         return False

#     def hash_password(self, password):
#         return hashlib.sha256(password.encode()).hexdigest()

#     def check_password(self, password, hashed_password):
#         return self.hash_password(password) == hashed_password

# class ProductManager:
#     def __init__(self):
#         self.products = []
#         self.load_products()

#     def load_products(self):
#         try:
#             with open('products.csv', 'r') as file:
#                 reader = csv.DictReader(file)
#                 for row in reader:
#                     self.products.append(Product(row['name'], float(row['price']), row['description'], row['image_url'], row['reviews'], row['category'], int(row['inventory'])))
#         except FileNotFoundError:
#             pass

#     def save_products(self):
#         with open('products.csv', 'w', newline='') as file:
#             fieldnames = ['name', 'price', 'description', 'image_url', 'reviews', 'category', 'inventory']
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()
#             for product in self.products:
#                 writer.writerow({'name': product.name, 'price': product.price, 'description': product.description, 'image_url': product.image_url, 'reviews': product.reviews, 'category': product.category, 'inventory': product.inventory})

#     def add_product(self, name, price, description, image_url, reviews, category, inventory):
#         self.products.append(Product(name, price, description, image_url, reviews, category, inventory))
#         self.save_products()
#         print("Product added successfully!")

#     def browse_products(self):
#         print("\nProduct Browsing")
#         print("-------------------------------")
#         print("1. Search for products by name")
#         print("2. Search for products by category")
#         print("3. Search for products by price range")
#         print("4. Show all products with details")
#         print("5. Go back to the main menu")

#     def search_by_name(self):
#         name = input("Enter the product name: ")
#         found = False
#         for product in self.products:
#             if name.lower() in product.name.lower():
#                 print(f"\nName: {product.name}")
#                 print(f"Price: {product.price}")
#                 print(f"Description: {product.description}")
#                 print(f"Category: {product.category}")
#                 print(f"Inventory: {product.inventory}")
#                 found = True
#         if not found:
#             print("Product not found.")

#     def search_by_category(self):
#         category = input("Enter the product category: ")
#         found = False
#         for product in self.products:
#             if category.lower() in product.category.lower():
#                 print(f"\nName: {product.name}")
#                 print(f"Price: {product.price}")
#                 print(f"Description: {product.description}")
#                 print(f"Category: {product.category}")
#                 print(f"Inventory: {product.inventory}")
#                 found = True
#         if not found:
#             print("Product not found.")

#     def search_by_price_range(self):
#         min_price = float(input("Enter the minimum price: "))
#         max_price = float(input("Enter the maximum price: "))
#         found = False
#         for product in self.products:
#             if min_price <= product.price <= max_price:
#                 print(f"\nName: {product.name}")
#                 print(f"Price: {product.price}")
#                 print(f"Description: {product.description}")
#                 print(f"Category: {product.category}")
#                 print(f"Inventory: {product.inventory}")
#                 found = True
#         if not found:
#             print("Product not found.")

#     def show_all_products(self):
#         print("\nAll Products:")
#         for product in self.products:
#             print("\nName:", product.name)
#             print("Price:", product.price)
#             print("Description:", product.description)
#             print("Category:", product.category)
#             print("Inventory:", product.inventory)
#             print("-------------------------------")

# def main():
#     user_manager = UserManager()
#     product_manager = ProductManager()

#     while True:
#         print("\nWelcome!")
#         print("1. Register")
#         print("2. Login")
#         print("3. Exit")

#         choice = input("Enter your choice (1-3): ")

#         if choice == '1':
#             username = input("Enter your username: ")
#             password = input("Enter your password: ")
#             address = input("Enter your address: ")
#             email = input("Enter your email: ")
#             user_manager.register(username, password, address, email)

#         elif choice == '2':
#             email = input("Enter your email: ")
#             password = input("Enter your password: ")
#             if user_manager.login(email, password):
#                 user = user_manager.users[email]
                
#                 while True:
#                     # Check if the user is a seller or buyer
#                     user_type = input("Are you a seller or buyer? Type 'seller' or 'buyer': ")
#                     if user_type.lower() == 'seller':
#                         # Seller functionality
#                         name = input("Enter the product name: ")
#                         price = float(input("Enter the product price: "))
#                         description = input("Enter the product description: ")
#                         image_url = input("Enter the product image URL: ")
#                         reviews = input("Enter the product reviews: ")
#                         category = input("Enter the product category: ")
#                         inventory = int(input("Enter the product inventory: "))
#                         product_manager.add_product(name, price, description, image_url, reviews, category, inventory)
#                         print("Product added successfully!")
#                     else:
#                         # Buyer functionality
#                         while True:
#                             print("\nWhat would you like to do")
#                             print("\n1. Product Browsing")
#                             print("2. Shopping Cart Management")
#                             print("3. Order Tracking")
#                             print("4. Customer Support")
#                             print("5. Transaction History")
#                             print("6. Logout")

#                             inner_choice = input("\nEnter your choice (1-6): ")

#                             if inner_choice == '1':
#                                 product_manager.browse_products()
#                                 browse_choice = input("\nEnter your choice (1-5): ")
#                                 if browse_choice == '1':
#                                     product_manager.search_by_name()
#                                 elif browse_choice == '2':
#                                     product_manager.search_by_category()
#                                 elif browse_choice == '3':
#                                     product_manager.search_by_price_range()
#                                 elif browse_choice == '4':
#                                     product_manager.show_all_products()
#                                 elif browse_choice == '5':
#                                     continue
#                                 else:
#                                     print("Invalid choice. Please enter a number between (1-5).")

#                             elif inner_choice == '2':
#                                 user.shopping_cart.view_cart()
#                                 print("1. Add to Cart")
#                                 print("2. View cart")
#                                 print("3. Remove cart")
#                                 print("4. Go back to the main menu")
#                                 cart_choice = input("Enter your choice (1-2): ")
#                                 if cart_choice == '1':
#                                     product_name = input("Enter the product name to add to cart: ")
#                                     quantity = int(input("Enter the quantity: "))
#                                     selected_product = None
#                                     for product in product_manager.products:
#                                         if product.name == product_name:
#                                             selected_product = product
#                                             break
#                                     if selected_product:
#                                         user.shopping_cart.add_to_cart(selected_product, quantity)
#                                         user.shopping_cart.save_total_to_file(user)
#                                         user_manager.save_users()
#                                         print("Product added to cart.")
#                                     else:
#                                         print("Product not found.")
                                        
#                                 elif cart_choice == '2':
#                                     user.shopping_cart.view_cart()
                                    
#                                 elif cart_choice == '3':
#                                     product_name = input("Enter the product name to remove from the cart: ")
#                                     user.shopping_cart.remove_from_cart(product_name)
#                                     user.shopping_cart.save_total_to_file(user)
#                                     user_manager.save_users()
                                    
#                                 elif cart_choice == '4':
#                                     continue
#                                 else:
#                                     print("Invalid choice. Please enter 6a number between (1-4).")

#                             elif inner_choice == '6':
#                                 print("Logged out successfully.")
#                                 break

#                     logout_choice = input("Would you like to logout? (yes/no): ")
#                     if logout_choice.lower() == 'yes':
#                         break
#                     elif logout_choice.lower() == 'no':
#                         continue
#                     else:
#                         print("Invalid choice. Please enter 'yes' or 'no'.")

#         elif choice == '3':
#             print("Goodbye!")
#             break

#         else:
#             print("Invalid choice. Please enter a number between 1 and 3.")

# if __name__ == "__main__":
#     main()


# import csv
# import random
# import string
# import hashlib
# from datetime import datetime  # Import the datetime module

# class User:
#     def __init__(self, username, password, address, email):
#         self.username = username
#         self.password = password
#         self.address = address
#         self.email = email
#         self.shopping_cart = ShoppingCart()
        

# class Product:
#     def __init__(self, name, price, description, image_url, reviews, category, inventory):
#         self.name = name
#         self.price = price
#         self.description = description
#         self.image_url = image_url
#         self.reviews = reviews
#         self.category = category
#         self.inventory = inventory

# class ShoppingCartItem:
#     def __init__(self, product, quantity):
#         self.product = product
#         self.quantity = quantity

# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def view_cart(self):
#         if not self.items:
#             print("Your shopping cart is empty.")
#         else:
#             print("Shopping Cart:")
#             total_items = 0
#             for item in self.items:
#                 print(f"- {item.product.name}({item.quantity}) - Total Amount: ${item.product.price * item.quantity:.2f}")
#                 total_items += item.quantity
#             print(f"Total items in cart: {total_items}")
#             print(f"Total amount: ${self.calculate_total():.2f}")

#     def calculate_total(self):
#         return sum(item.product.price * item.quantity for item in self.items)

#     def add_to_cart(self, product, quantity=1):
#         for item in self.items:
#             if item.product.name == product.name:
#                 item.quantity += quantity
#                 break
#         else:
#             self.items.append(ShoppingCartItem(product, quantity))

#     def remove_from_cart(self, product_name, quantity=None):
#         for item in self.items:
#             if item.product.name == product_name:
#                 if quantity:
#                     if item.quantity > quantity:
#                         item.quantity -= quantity
#                     else:
#                         self.items.remove(item)
#                 else:
#                     self.items.remove(item)
#                 print(f"{product_name} removed from the cart.")
#                 return
#         print(f"{product_name} not found in the cart.")

#     def save_total_to_file(self, user):
#         total_amount = self.calculate_total()
#         with open('total_amount.csv', 'w') as file:
#             file.write(f"Total amount in shopping cart: ${total_amount}\n")
#             file.write(f"Username: {user.username}\n")
#             file.write("Product Details:\n")
#             for item in self.items:
#                 file.write(f"- {item.product.name}({item.quantity}) - Total Amount: ${item.product.price * item.quantity:.2f}\n")
#         print("Shopping cart details saved to total_amount.csv file.")

#     def load_cart_from_file(self, user):
#         try:
#             with open('total_amount.csv', 'r') as file:
#                 lines = file.readlines()
#                 if len(lines) >= 3:  # Ensure minimum lines required
#                     user.username = lines[1].split(': ')[1].strip()
#                     items = lines[3:]
#                     for item_line in items:
#                         item_details = item_line.strip().split(' - ')
#                         if len(item_details) >= 2:  # Ensure there are enough elements
#                             product_name, quantity_info = item_details[0].split('(')
#                             quantity = int(quantity_info.split(')')[0])
#                             total_amount = float(item_details[1].split('$')[1])
#                             product = Product(product_name, total_amount / quantity, '', '', '', '', 0)
#                             self.items.append(ShoppingCartItem(product, quantity))
#                         else:
#                             print("Invalid format in the shopping cart file. Skipping item.")
#                     # print("Shopping cart loaded from total_amount.csv file.")
#         except FileNotFoundError:
#             print("Shopping cart file not found.")
#         except Exception as e:
#             print(f"Error loading shopping cart: {str(e)}")


# class UserManager:
#     def __init__(self):
#         self.users = {}
#         self.load_users()


#     def load_users(self):
#         try:
#             with open('users.csv', 'r') as file:
#                 reader = csv.DictReader(file)
#                 for row in reader:
#                     user = User(row['username'], row['password'], row['address'], row['email'])
#                     user.shopping_cart.load_cart_from_file(user)
#                     self.users[row['email']] = user
#         except FileNotFoundError:
#             pass

#     def save_users(self):
#         with open('users.csv', 'w', newline='') as file:
#             fieldnames = ['username', 'password', 'address', 'email']
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()
#             for user in self.users.values():
#                 writer.writerow({'username': user.username, 'password': user.password, 'address': user.address, 'email': user.email})

#     def register(self, username, password, address, email):
#         if len(password) < 6 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password) or not any(char in string.punctuation for char in password):
#             print("Password must be at least 6 characters long and contain a mix of letters, numbers, and special characters.")
#             return False

#         if '@gmail.com' not in email:
#             print("Email must be a Gmail address.")
#             return False

#         if email in self.users:
#             print("Email already exists. Please choose another one.")
#             return False

#         user = User(username, self.hash_password(password), address, email)
#         user.shopping_cart.load_cart_from_file(user)
#         self.users[email] = user
#         self.save_users()
#         print("Registration successful!")
#         return True

#     def login(self, email, password):
#         max_attempts = 3
#         login_attempts = 0
#         while login_attempts < max_attempts:
#             if email in self.users:
#                 if self.check_password(password, self.users[email].password):
#                     print("Login successful!")
#                     return True
#                 else:
#                     login_attempts += 1
#                     if login_attempts < max_attempts:
#                         print(f"\nInvalid username or password. You have {max_attempts - login_attempts} attempts remaining.")
#                     else:
#                         print("Maximum login attempts reached. You need to reset your password.")
#                         email = input("Enter your email address to reset your password: ")
#                         self.reset_password(email)
#                         break
#             else:
#                 print("Email not found.")
#                 return False

#     def reset_password(self, email):
#         if email in self.users:
#             new_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))
#             self.users[email].password = self.hash_password(new_password)
#             self.save_users()
#             print(f"Your password has been reset to: {new_password}")
#             return True
#         print("Email address not found.")
#         return False

#     def hash_password(self, password):
#         return hashlib.sha256(password.encode()).hexdigest()

#     def check_password(self, password, hashed_password):
#         return self.hash_password(password) == hashed_password
    
    
# class ProductManager:
#     def __init__(self):
#         self.products = []
#         self.load_products()

#     def load_products(self):
#         try:
#             with open('products.csv', 'r') as file:
#                 reader = csv.DictReader(file)
#                 for row in reader:
#                     self.products.append(Product(row['name'], float(row['price']), row['description'], row['image_url'], row['reviews'], row['category'], int(row['inventory'])))
#         except FileNotFoundError:
#             pass

#     def save_products(self):
#         with open('products.csv', 'w', newline='') as file:
#             fieldnames = ['name', 'price', 'description', 'image_url', 'reviews', 'category', 'inventory']
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()
#             for product in self.products:
#                 writer.writerow({'name': product.name, 'price': product.price, 'description': product.description, 'image_url': product.image_url, 'reviews': product.reviews, 'category': product.category, 'inventory': product.inventory})

#     def add_product(self, name, price, description, image_url, reviews, category, inventory):
#         self.products.append(Product(name, price, description, image_url, reviews, category, inventory))
#         self.save_products()
#         print("Product added successfully!")

#     def browse_products(self):
#         print("\nProduct Browsing")
#         print("-------------------------------")
#         print("1. Search for products by name")
#         print("2. Search for products by category")
#         print("3. Search for products by price range")
#         print("4. Show all products with details")
#         print("5. Go back to the main menu")

#     def search_by_name(self):
#         name = input("Enter the product name: ")
#         found = False
#         for product in self.products:
#             if name.lower() in product.name.lower():
#                 print(f"\nName: {product.name}")
#                 print(f"Price: {product.price}")
#                 print(f"Description: {product.description}")
#                 print(f"Category: {product.category}")
#                 print(f"Inventory: {product.inventory}")
#                 found = True
#         if not found:
#             print("Product not found.")

#     def search_by_category(self):
#         category = input("Enter the product category: ")
#         found = False
#         for product in self.products:
#             if category.lower() in product.category.lower():
#                 print(f"\nName: {product.name}")
#                 print(f"Price: {product.price}")
#                 print(f"Description: {product.description}")
#                 print(f"Category: {product.category}")
#                 print(f"Inventory: {product.inventory}")
#                 found = True
#         if not found:
#             print("Product not found.")

#     def search_by_price_range(self):
#         min_price = float(input("Enter the minimum price: "))
#         max_price = float(input("Enter the maximum price: "))
#         found = False
#         for product in self.products:
#             if min_price <= product.price <= max_price:
#                 print(f"\nName: {product.name}")
#                 print(f"Price: {product.price}")
#                 print(f"Description: {product.description}")
#                 print(f"Category: {product.category}")
#                 print(f"Inventory: {product.inventory}")
#                 found = True
#         if not found:
#             print("Product not found.")

#     def show_all_products(self):
#         print("\nAll Products:")
#         for product in self.products:
#             print("\nName:", product.name)
#             print("Price:", product.price)
#             print("Description:", product.description)
#             print("Category:", product.category)
#             print("Inventory:", product.inventory)
#             print("-------------------------------")

# def main():
#     user_manager = UserManager()
#     product_manager = ProductManager()

#     while True:
#         print("\nWelcome!")
#         print("1. Register")
#         print("2. Login")
#         print("3. Exit")

#         choice = input("Enter your choice (1-3): ")

#         if choice == '1':
#             username = input("Enter your username: ")
#             password = input("Enter your password: ")
#             address = input("Enter your address: ")
#             email = input("Enter your email: ")
#             user_manager.register(username, password, address, email)

#         elif choice == '2':
#             email = input("Enter your email: ")
#             password = input("Enter your password: ")
#             if user_manager.login(email, password):
#                 user = user_manager.users[email]
                
#                 while True:
#                     # Check if the user is a seller or buyer
#                     user_type = input("Are you a seller or buyer? Type 'seller' or 'buyer': ")
#                     if user_type.lower() == 'seller':
#                         # Seller functionality
#                         name = input("Enter the product name: ")
#                         price = float(input("Enter the product price: "))
#                         description = input("Enter the product description: ")
#                         image_url = input("Enter the product image URL: ")
#                         reviews = input("Enter the product reviews: ")
#                         category = input("Enter the product category: ")
#                         inventory = int(input("Enter the product inventory: "))
#                         product_manager.add_product(name, price, description, image_url, reviews, category, inventory)
#                         print("Product added successfully!")
#                     else:
#                         # Buyer functionality
#                         while True:
#                             print("\nWhat would you like to do")
#                             print("\n1. Product Browsing")
#                             print("2. Shopping Cart Management")
#                             print("3. Backup")
#                             print("4. Customer Support")
#                             print("5. Transaction History")
#                             print("6. Logout")

#                             inner_choice = input("\nEnter your choice (1-6): ")

#                             if inner_choice == '1':
#                                 product_manager.browse_products()
#                                 browse_choice = input("\nEnter your choice (1-5): ")
#                                 if browse_choice == '1':
#                                     product_manager.search_by_name()
#                                 elif browse_choice == '2':
#                                     product_manager.search_by_category()
#                                 elif browse_choice == '3':
#                                     product_manager.search_by_price_range()
#                                 elif browse_choice == '4':
#                                     product_manager.show_all_products()
#                                 elif browse_choice == '5':
#                                     continue
#                                 else:
#                                     print("Invalid choice. Please enter a number between (1-5).")

#                             elif inner_choice == '2':
#                                 user.shopping_cart.view_cart()
#                                 print("1. Add to Cart")
#                                 print("2. View cart")
#                                 print("3. Remove cart")
#                                 print("4. Go back to the main menu")
#                                 cart_choice = input("Enter your choice (1-2): ")
#                                 if cart_choice == '1':
#                                     product_name = input("Enter the product name to add to cart: ")
#                                     quantity = int(input("Enter the quantity: "))
#                                     selected_product = None
#                                     for product in product_manager.products:
#                                         if product.name == product_name:
#                                             selected_product = product
#                                             break
#                                     if selected_product:
#                                         user.shopping_cart.add_to_cart(selected_product, quantity)
#                                         user.shopping_cart.save_total_to_file(user)
#                                         user_manager.save_users()
#                                         print("Product added to cart.")
                                        
#                                         pay_choice = input("Do you want to proceed to pay? (yes/no): ")
#                                         if pay_choice.lower() == 'yes':
#                                            card_number = input("Enter your bank card number: ")
#                                            pin_code = input("Enter your PIN code: ")
#                                            last_four_digits = input("Enter the last 4 digits of your ATM card: ")
#                                            if len(card_number) != 16 or not card_number.isdigit():
#                                                print("Invalid card number. Please enter a valid 16-digit card number.")
#                                            elif len(pin_code) != 4 or not pin_code.isdigit():
#                                                print("Invalid PIN code. Please enter a valid 4-digit PIN code.")
#                                            elif len(last_four_digits) != 4 or not last_four_digits.isdigit():
#                                                print("Invalid last 4 digits. Please enter a valid 4-digit number.")
#                                            else:
#                                                print("Processing payment...")
#                                                print("Payment processed successfully!")
#                                                print("Payment processed successfully!")

                                           
#                                         else:
#                                          print("Payment cancelled.")




#                                     else:
#                                         print("Product not found.")
                                        
#                                 elif cart_choice == '2':
#                                     user.shopping_cart.view_cart()
                                    
#                                 elif cart_choice == '3':
#                                     product_name = input("Enter the product name to remove from the cart: ")
#                                     quantity = int(input("Enter the quantity to remove (Enter 0 to remove all): "))
#                                     user.shopping_cart.remove_from_cart(product_name, quantity)
#                                     user.shopping_cart.save_total_to_file(user)
#                                     user_manager.save_users()
                                    
#                                 elif cart_choice == '4':
#                                     continue
#                                 else:
#                                     print("Invalid choice. Please enter a number between (1-4).")
                                    
#                             elif inner_choice == '3':
#                                 print("\nBackup:")
#                                 print("Date and Time\t\tActivity")
#                                 print("---------------------------------------------")
                                
#                                 current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                                 print(f"{current_time}\tLogged in")
#                                 choice = input("\nPress Enter to see more activities or type 'q' to quit backup: ")
#                                 if choice.lower() == 'q':
#                                     break
#                                 current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                                 print(f"{current_time}\tSimulated activity")
#                                 print("\nProduct to Purchase:")
#                                 print("Name: ", selected_product.name)
#                                 print("Price: ", selected_product.price)
#                                 print("Description: ", selected_product.description)
#                                 print("Category: ", selected_product.category)
#                                 print("Inventory: ", selected_product.inventory)
                                
#                             elif inner_choice == '4':
#                                 print("Customer Support:")
#                                 print("Phone: 123-456-7890")
#                                 print("Email: support@company.com")
#                                 print("Customer Support Bot:")
#                                 print("How can we assist you today?")
#                                 print("You exist keyword to terminate")
                                
#                                 while True:
#                                     user_input = input("You: ")
#                                     if "order" in user_input:
#                                         print("Bot: Please provide your order details, and we will assist you accordingly.")
#                                     elif "refund" in user_input:
#                                         print("Bot: Our refund policy allows for returns within 30 days of purchase.")
#                                     elif "complaint" in user_input:
#                                          print("Bot: We apologize for any inconvenience. Please provide details of your complaint.")
#                                     elif "thank" in user_input:
#                                         print("Bot: You're welcome! Is there anything else I can assist you with?")
#                                     elif "bye" in user_input:
#                                         print("Bot: Goodbye! If you have any further questions, feel free to ask.")

#                                         break
#                                     elif "exist" in user_input:
#                                         print("Bot: Terminating customer support bot.")
#                                         break
#                                     else:
#                                         print("Bot: I'm sorry, I didn't understand that. How else can I assist you?")

#                             elif inner_choice == "5":
#                                 print("\nTransaction History:")
#                             elif inner_choice == '6':
#                                 print("Logged out successfully.")
#                                 break

#                     logout_choice = input("Would you like to logout? (yes/no): ")
#                     if logout_choice.lower() == 'yes':
#                         break
#                     elif logout_choice.lower() == 'no':
#                         continue
#                     else:
#                         print("Invalid choice. Please enter 'yes' or 'no'.")

#         elif choice == '3':
#             print("Goodbye!")
#             break

#         else:
#             print("Invalid choice. Please enter a number between 1 and 3.")

# if __name__ == "__main__":
#     main()

import csv
import random
import string
import hashlib
from datetime import datetime  # Import the datetime module

class User:
    def __init__(self, username, password, address, email):
        self.username = username
        self.password = password
        self.address = address
        self.email = email
        self.shopping_cart = ShoppingCart()
        self.transaction_history = []

class Product:
    def __init__(self, name, price, description, image_url, reviews, category, inventory):
        self.name = name
        self.price = price
        self.description = description
        self.image_url = image_url
        self.reviews = reviews
        self.category = category
        self.inventory = inventory

class ShoppingCartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def view_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart:")
            total_items = 0
            for item in self.items:
                print(f"- {item.product.name}({item.quantity}) - Total Amount: ${item.product.price * item.quantity:.2f}")
                total_items += item.quantity
            print(f"Total items in cart: {total_items}")
            print(f"Total amount: ${self.calculate_total():.2f}")

    def calculate_total(self):
        return sum(item.product.price * item.quantity for item in self.items)

    def add_to_cart(self, product, quantity=1):
        for item in self.items:
            if item.product.name == product.name:
                item.quantity += quantity
                break
        else:
            self.items.append(ShoppingCartItem(product, quantity))

    def remove_from_cart(self, product_name, quantity=None):
        for item in self.items:
            if item.product.name == product_name:
                if quantity:
                    if item.quantity > quantity:
                        item.quantity -= quantity
                    else:
                        self.items.remove(item)
                else:
                    self.items.remove(item)
                print(f"{product_name} removed from the cart.")
                return
        print(f"{product_name} not found in the cart.")

    def save_total_to_file(self, user):
        total_amount = self.calculate_total()
        with open('total_amount.csv', 'w') as file:
            file.write(f"Total amount in shopping cart: ${total_amount}\n")
            file.write(f"Username: {user.username}\n")
            file.write("Product Details:\n")
            for item in self.items:
                file.write(f"- {item.product.name}({item.quantity}) - Total Amount: ${item.product.price * item.quantity:.2f}\n")
        print("Shopping cart details saved to total_amount.csv file.")

    def load_cart_from_file(self, user):
        try:
            with open('total_amount.csv', 'r') as file:
                lines = file.readlines()
                if len(lines) >= 3:  # Ensure minimum lines required
                    user.username = lines[1].split(': ')[1].strip()
                    items = lines[3:]
                    for item_line in items:
                        item_details = item_line.strip().split(' - ')
                        if len(item_details) >= 2:  # Ensure there are enough elements
                            product_name, quantity_info = item_details[0].split('(')
                            quantity = int(quantity_info.split(')')[0])
                            total_amount = float(item_details[1].split('$')[1])
                            product = Product(product_name, total_amount / quantity, '', '', '', '', 0)
                            self.items.append(ShoppingCartItem(product, quantity))
                        else:
                            print("Invalid format in the shopping cart file. Skipping item.")
                    # print("Shopping cart loaded from total_amount.csv file.")
        except FileNotFoundError:
            print("Shopping cart file not found.")
        except Exception as e:
            print(f"Error loading shopping cart: {str(e)}")

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        try:
            with open('users.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    user = User(row['username'], row['password'], row['address'], row['email'])
                    user.shopping_cart.load_cart_from_file(user)
                    self.users[row['email']] = user
        except FileNotFoundError:
            pass

    def save_users(self):
        with open('users.csv', 'w', newline='') as file:
            fieldnames = ['username', 'password', 'address', 'email']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in self.users.values():
                writer.writerow({'username': user.username, 'password': user.password, 'address': user.address, 'email': user.email})

    def register(self, username, password, address, email):
        if len(password) < 6 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password) or not any(char in string.punctuation for char in password):
            print("Password must be at least 6 characters long and contain a mix of letters, numbers, and special characters.")
            return False

        if '@gmail.com' not in email:
            print("Email must be a Gmail address.")
            return False

        if email in self.users:
            print("Email already exists. Please choose another one.")
            return False

        user = User(username, self.hash_password(password), address, email)
        user.shopping_cart.load_cart_from_file(user)
        self.users[email] = user
        self.save_users()
        print("Registration successful!")
        return True

    def login(self, email, password):
        max_attempts = 3
        login_attempts = 0
        while login_attempts < max_attempts:
            if email in self.users:
                if self.check_password(password, self.users[email].password):
                    print("Login successful!")
                    return True
                else:
                    login_attempts += 1
                    if login_attempts < max_attempts:
                        print(f"\nInvalid username or password. You have {max_attempts - login_attempts} attempts remaining.")
                    else:
                        print("Maximum login attempts reached. You need to reset your password.")
                        email = input("Enter your email address to reset your password: ")
                        self.reset_password(email)
                        break
            else:
                print("Email not found.")
                return False

    def reset_password(self, email):
        if email in self.users:
            new_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))
            self.users[email].password = self.hash_password(new_password)
            self.save_users()
            print(f"Your password has been reset to: {new_password}")
            return True
        print("Email address not found.")
        return False

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password, hashed_password):
        return self.hash_password(password) == hashed_password

class ProductManager:
    def __init__(self):
        self.products = []
        self.load_products()

    def load_products(self):
        try:
            with open('products.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.products.append(Product(row['name'], float(row['price']), row['description'], row['image_url'], row['reviews'], row['category'], int(row['inventory'])))
        except FileNotFoundError:
            pass

    def save_products(self):
        with open('products.csv', 'w', newline='') as file:
            fieldnames = ['name', 'price', 'description', 'image_url', 'reviews', 'category', 'inventory']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for product in self.products:
                writer.writerow({'name': product.name, 'price': product.price, 'description': product.description, 'image_url': product.image_url, 'reviews': product.reviews, 'category': product.category, 'inventory': product.inventory})

    def add_product(self, name, price, description, image_url, reviews, category, inventory):
        self.products.append(Product(name, price, description, image_url, reviews, category, inventory))
        self.save_products()
        print("Product added successfully!")

    def browse_products(self):
        print("\nProduct Browsing")
        print("-------------------------------")
        print("1. Search for products by name")
        print("2. Search for products by category")
        print("3. Search for products by price range")
        print("4. Show all products with details")
        print("5. Go back to the main menu")

    def search_by_name(self):
        name = input("Enter the product name: ")
        found = False
        for product in self.products:
            if name.lower() in product.name.lower():
                print(f"\nName: {product.name}")
                print(f"Price: {product.price}")
                print(f"Description: {product.description}")
                print(f"Category: {product.category}")
                print(f"Inventory: {product.inventory}")
                found = True
        if not found:
            print("Product not found.")

    def search_by_category(self):
        category = input("Enter the product category: ")
        found = False
        for product in self.products:
            if category.lower() in product.category.lower():
                print(f"\nName: {product.name}")
                print(f"Price: {product.price}")
                print(f"Description: {product.description}")
                print(f"Category: {product.category}")
                print(f"Inventory: {product.inventory}")
                found = True
        if not found:
            print("Product not found.")

    def search_by_price_range(self):
        min_price = float(input("Enter the minimum price: "))
        max_price = float(input("Enter the maximum price: "))
        found = False
        for product in self.products:
            if min_price <= product.price <= max_price:
                print(f"\nName: {product.name}")
                print(f"Price: {product.price}")
                print(f"Description: {product.description}")
                print(f"Category: {product.category}")
                print(f"Inventory: {product.inventory}")
                found = True
        if not found:
            print("Product not found.")

    def show_all_products(self):
        print("\nAll Products:")
        for product in self.products:
            print("\nName:", product.name)
            print("Price:", product.price)
            print("Description:", product.description)
            print("Category:", product.category)
            print("Inventory:", product.inventory)
            print("-------------------------------")

class Transaction:
    def __init__(self, username, total_amount, products):
        self.datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.username = username
        self.total_amount = total_amount
        self.products = products

def main():
    user_manager = UserManager()
    product_manager = ProductManager()

    while True:
        print("\nWelcome!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            address = input("Enter your address: ")
            email = input("Enter your email: ")
            user_manager.register(username, password, address, email)

        elif choice == '2':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if user_manager.login(email, password):
                user = user_manager.users[email]

                while True:
                    # Check if the user is a seller or buyer
                    user_type = input("Are you a seller or buyer? Type 'seller' or 'buyer': ")
                    if user_type.lower() == 'seller':
                        # Seller functionality
                        name = input("Enter the product name: ")
                        price = float(input("Enter the product price: "))
                        description = input("Enter the product description: ")
                        image_url = input("Enter the product image URL: ")
                        reviews = input("Enter the product reviews: ")
                        category = input("Enter the product category: ")
                        inventory = int(input("Enter the product inventory: "))
                        product_manager.add_product(name, price, description, image_url, reviews, category, inventory)
                        print("Product added successfully!")
                    else:
                        # Buyer functionality
                        while True:
                            print("\nWhat would you like to do")
                            print("\n1. Product Browsing")
                            print("2. Shopping Cart Management")
                            print("3. Backup")
                            print("4. Customer Support")
                            print("5. Transaction History")
                            print("6. Logout")

                            inner_choice = input("\nEnter your choice (1-6): ")

                            if inner_choice == '1':
                                product_manager.browse_products()
                                browse_choice = input("\nEnter your choice (1-5): ")
                                if browse_choice == '1':
                                    product_manager.search_by_name()
                                elif browse_choice == '2':
                                    product_manager.search_by_category()
                                elif browse_choice == '3':
                                    product_manager.search_by_price_range()
                                elif browse_choice == '4':
                                    product_manager.show_all_products()
                                elif browse_choice == '5':
                                    continue
                                else:
                                    print("Invalid choice. Please enter a number between (1-5).")

                            elif inner_choice == '2':
                                user.shopping_cart.view_cart()
                                print("1. Add to Cart")
                                print("2. View cart")
                                print("3. Remove cart")
                                print("4. Go back to the main menu")
                                cart_choice = input("Enter your choice (1-2): ")
                                if cart_choice == '1':
                                    product_name = input("Enter the product name to add to cart: ")
                                    quantity = int(input("Enter the quantity: "))
                                    selected_product = None
                                    for product in product_manager.products:
                                        if product.name == product_name:
                                            selected_product = product
                                            break
                                    if selected_product:
                                        user.shopping_cart.add_to_cart(selected_product, quantity)
                                        user.shopping_cart.save_total_to_file(user)
                                        user_manager.save_users()
                                        print("Product added to cart.")

                                        pay_choice = input("Do you want to proceed to pay? (yes/no): ")
                                        if pay_choice.lower() == 'yes':
                                            card_number = input("Enter your bank card number: ")
                                            pin_code = input("Enter your PIN code: ")
                                            last_four_digits = input("Enter the last 4 digits of your ATM card: ")
                                            if len(card_number) != 16 or not card_number.isdigit():
                                                print("Invalid card number. Please enter a valid 16-digit card number.")
                                            elif len(pin_code) != 4 or not pin_code.isdigit():
                                                print("Invalid PIN code. Please enter a valid 4-digit PIN code.")
                                            elif len(last_four_digits) != 4 or not last_four_digits.isdigit():
                                                print("Invalid last 4 digits. Please enter a valid 4-digit number.")
                                            else:
                                                print("Processing payment...")
                                                print("Payment processed successfully!")
                                                transaction = Transaction(user.username, user.shopping_cart.calculate_total(), user.shopping_cart.items)
                                                user.transaction_history.append(transaction)
                                                with open('transaction_history.csv', 'a', newline='') as file:
                                                    writer = csv.writer(file)
                                                    writer.writerow([transaction.datetime, transaction.username, transaction.total_amount, transaction.products])
                                                print("Payment processed successfully!")

                                        else:
                                            print("Payment cancelled.")

                                    else:
                                        print("Product not found.")

                                elif cart_choice == '2':
                                    user.shopping_cart.view_cart()

                                elif cart_choice == '3':
                                    product_name = input("Enter the product name to remove from the cart: ")
                                    quantity = int(input("Enter the quantity to remove (Enter 0 to remove all): "))
                                    user.shopping_cart.remove_from_cart(product_name, quantity)
                                    user.shopping_cart.save_total_to_file(user)
                                    user_manager.save_users()

                                elif cart_choice == '4':
                                    continue
                                else:
                                    print("Invalid choice. Please enter a number between (1-4).")

                            elif inner_choice == '3':
                                print("\nBackup:")
                                print("Date and Time\t\tActivity")
                                print("---------------------------------------------")

                                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                print(f"{current_time}\tLogged in")
                                choice = input("\nPress Enter to see more activities or type 'q' to quit backup: ")
                                if choice.lower() == 'q':
                                    break
                                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                print(f"{current_time}\tSimulated activity")
                                print("\nProduct to Purchase:")
                                print("Name: ", selected_product.name)
                                print("Price: ", selected_product.price)
                                print("Description: ", selected_product.description)
                                print("Category: ", selected_product.category)
                                print("Inventory: ", selected_product.inventory)

                            elif inner_choice == '4':
                                print("Customer Support Bot:")
                                print("How can we assist you today?")
                                print("You exist keyword to terminate")

                                while True:
                                    user_input = input("You: ")
                                    if "order" in user_input:
                                        print("Bot: Please provide your order details, and we will assist you accordingly.")
                                    elif "refund" in user_input:
                                        print("Bot: Our refund policy allows for returns within 30 days of purchase.")
                                    elif "complaint" in user_input:
                                        print("Bot: We apologize for any inconvenience. Please provide details of your complaint.")
                                    elif "thank" in user_input:
                                        print("Bot: You're welcome! Is there anything else I can assist you with?")
                                    elif "bye" in user_input:
                                        print("Bot: Goodbye! If you have any further questions, feel free to ask.")

                                        break
                                    elif "exist" in user_input:
                                        print("Bot: Terminating customer support bot.")
                                        break
                                    else:
                                        print("Bot: I'm sorry, I didn't understand that. How else can I assist you?")

                            elif inner_choice == "5":
                                print("\nTransaction History:")
                                for transaction in user.transaction_history:
                                    print("\nDate and Time:", transaction.datetime)
                                    print("Username:", transaction.username)
                                    print("Total Amount:", transaction.total_amount)
                                    print("Products:", transaction.products)
                            elif inner_choice == '6':
                                print("Logged out successfully.")
                                break

                    logout_choice = input("Would you like to logout? (yes/no): ")
                    if logout_choice.lower() == 'yes':
                        break
                    elif logout_choice.lower() == 'no':
                        continue
                    else:
                        print("Invalid choice. Please enter 'yes' or 'no'.")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
