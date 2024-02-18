import csv
import random
import string
import hashlib
from datetime import datetime


class User:
    def __init__(self, username, password, address, email):
        self.username = username
        self.password = password
        self.address = address
        self.email = email
        self.shopping_cart = ShoppingCart()
        self.transaction_history = []  # Add transaction history list to the User class


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
                if len(lines) >= 3:  
                    user.username = lines[1].split(': ')[1].strip()
                    items = lines[3:]
                    for item_line in items:
                        item_details = item_line.strip().split(' - ')
                        if len(item_details) >= 2:  
                            product_name, quantity_info = item_details[0].split('(')
                            quantity = int(quantity_info.split(')')[0])
                            total_amount = float(item_details[1].split('$')[1])
                            product = Product(product_name, total_amount / quantity, '', '', '', '', 0)
                            self.items.append(ShoppingCartItem(product, quantity))
                        else:
                            print("Invalid format in the shopping cart file. Skipping item.")
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
    def __init__(self, datetime, username, products, total_amount):
        self.datetime = datetime
        self.username = username
        self.products = products
        self.total_amount = total_amount


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

    def record_transaction(self, user, products, total_amount):
        transaction = Transaction(datetime.now(), user.username, products, total_amount)
        user.transaction_history.append(transaction)
        print("Transaction recorded successfully!")


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
                    user_type = input("Are you a seller or buyer? Type 'seller' or 'buyer': ")
                    if user_type.lower() == 'seller':
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
                                                print("Payment processed successfully!")
                                                user_manager.record_transaction(user, user.shopping_cart.items, user.shopping_cart.calculate_total())
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

                            # elif inner_choice == '4':
                            #     print("Customer Support:")
                            #     print("Phone: 123-456-7890")
                            #     print("Email: support@company.com")
                            
                            elif inner_choice == '4':
                                print("Customer Support:")
                                print("Phone: 123-456-7890")
                                print("Email: support@company.com")
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

                            elif inner_choice == '5':
                                print("\nTransaction History:")
                                if user.transaction_history:
                                    for transaction in user.transaction_history:
                                        print("\nDate and Time:", transaction.datetime)
                                        print("Username:", transaction.username)
                                        print("Total Amount:", transaction.total_amount)
                                        print("Products Purchased:")
                                        for product in transaction.products:
                                            print(f"- {product.product.name} ({product.quantity})")
                                else:
                                    print("No transaction history available.")

                            elif inner_choice == '6':
                                break
                            else:
                                print("Invalid choice. Please enter a number between (1-6).")
            else:
                print("Invalid username or password.")

        elif choice == '3':
            print("Thank you for using our system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between (1-3).")


if __name__ == "__main__":
    main()

