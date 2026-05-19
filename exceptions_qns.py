# Q1. Create three custom exception classes:
#     - InvalidAgeError (inherits from Exception)
#     - InvalidEmailError (inherits from Exception)
#     - InvalidPasswordError (inherits from Exception)
#
#     Write a function called validate_user(email, age, password) that:
#     - Raises InvalidEmailError if "@" not in email
#     - Raises InvalidAgeError if age < 18
#     - Raises InvalidPasswordError if len(password) < 8
#     - Returns {"valid": True} if everything passes
#
#     Test with try/except catching each specific exception
#     and one valid call that passes all checks

class InvalidAgeError(Exception):
    pass

class InvalidEmailError(Exception):
    pass

class InvalidPasswordError(Exception):
    pass

def validate_user(email, age, password):
    if "@" not in email:
        raise InvalidEmailError("Invalid email format")

    if age < 18:
        raise InvalidAgeError("Must be 18 or above!")
    
    if len(password) < 8:
        raise InvalidPasswordError("Password must be at least 8 characters long")
    
    return {"valid": True}

print()
print("Question 01:")
print('-' * 24)

# valid data
try:
    result = validate_user('john@abc.com', 35, 'abi489ginia')
except InvalidEmailError as e:
    print(f"Error: {str(e)}")
except InvalidAgeError as e:
    print(f"Error: {str(e)}")
except InvalidPasswordError as e:
    print(f"Error: {str(e)}")
else:
    print(f"{result}")

# invalid email
try:
    result = validate_user('johnabc.com', 35, 'abi489ginia')
except InvalidEmailError as e:
    print(f"Error: {str(e)}")
except InvalidAgeError as e:
    print(f"Error: {str(e)}")
except InvalidPasswordError as e:
    print(f"Error: {str(e)}")
else:
    print(f"{result}")

# invalid age
try:
    result = validate_user('john@abc.com', 17, 'abi489ginia')
except InvalidEmailError as e:
    print(f"Error: {str(e)}")
except InvalidAgeError as e:
    print(f"Error: {str(e)}")
except InvalidPasswordError as e:
    print(f"Error: {str(e)}")
else:
    print(f"{result}")

# shorter password
try:
    result = validate_user('john@abc.com', 35, 'hia')
except InvalidEmailError as e:
    print(f"Error: {str(e)}")
except InvalidAgeError as e:
    print(f"Error: {str(e)}")
except InvalidPasswordError as e:
    print(f"Error: {str(e)}")
else:
    print(f"{result}")


# Q2. Create a custom exception called InsufficientFundsError
#     that accepts balance and amount in __init__
#     and builds a detailed message automatically:
#     "Cannot withdraw $500. Current balance: $100. Shortfall: $400."
#
#     Write a BankAccount class with:
#     - __init__(self, owner, balance=0)
#     - withdraw(self, amount) that raises InsufficientFundsError if needed
#     - deposit(self, amount) that raises ValueError if amount <= 0
#
#     Test both failure cases and print the exception's message cleanly

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.shortfall = balance - amount
        super().__init__(
            f"Cannot withdraw ${amount:,}. Current balance: ${balance:,}. Shortfall: ${self.shortfall:,}."
        )

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print(f"Account created ✅. Balance: ${self.balance:,}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError
        
        if amount <= 0:
            raise ValueError("Withdrawal unsuccessful! Amount must be greater than zero")
        
        self.balance -= amount
        print(f"${amount:,} Withdrawal successful ✅. Current balance: ${self.balance:,}")
        
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit unsuccessful! Amount must be greater than zero")
        
        self.balance += amount
        print(f"${amount:,} Deposit successful ✅. Current balance: ${self.balance:,}")

print()
print("Question 02:")
print('-' * 24)

my_account = BankAccount('Mohammed', 1500)

try:
    my_account.deposit(500)
except ValueError as e:
    print(f"Error: {str(e)}")

try:
    my_account.deposit(-500)
except ValueError as e:
    print(f"Error: {str(e)}")

try:
    my_account.withdraw(700)
except ValueError as e:
    print(f"Error: {str(e)}")

try:
    my_account.withdraw(-500)
except ValueError as e:
    print(f"Error: {str(e)}")


# Q3. Build an exception hierarchy:
#     - AppError(Exception) — base
#     - ProductError(AppError) — base for product issues
#     - OutOfStockError(ProductError)
#     - InvalidPriceError(ProductError)
#
#     Write a function called process_product(name, price, stock) that:
#     - Raises InvalidPriceError if price <= 0
#     - Raises OutOfStockError if stock == 0
#     - Returns a product dict if everything is valid
#
#     Then demonstrate catching:
#     a) The specific error (OutOfStockError)
#     b) The parent (ProductError) — show it catches both product errors
#     c) The base (AppError) — show it catches everything app-level

class AppError(Exception):
    pass

class ProductError(AppError):
    pass

class OutOfStockError(ProductError):
    pass

class InvalidPriceError(ProductError):
    pass

def process_product(name, price, stock):
    if price <= 0:
        raise InvalidPriceError("Price must be greater than zero")
    
    if stock == 0:
        raise OutOfStockError(f"{name} is out of stock!")
    
    return {'name': name, 'price': price, 'stock': stock}

print()
print("Question 03:")
print('-' * 24)

try:
    result = process_product('spinach', 2.50, 0)
except OutOfStockError as e:
    print(f"Error: {str(e)}")
else:
    print(f"{str(result)}")

# ProductError
try:
    result = process_product('spinach', -1, 5)
except ProductError as e:
    print(f"Error: {str(e)}")
else:
    print(f"{str(result)}")

try:
    result = process_product('spinach', 5.50, 0)
except ProductError as e:
    print(f"Error: {str(e)}")
else:
    print(f"{str(result)}")

# AppError
try:
    result = process_product('spinach', -1, 5)
except AppError as e:
    print(f"Error: {str(e)}")
else:
    print(f"{str(result)}")


# Q4. Combine raise with re-raise:
#     Write a function called get_product(products, product_id) that:
#     - Raises KeyError if product_id not in products
#
#     Write a second function called fetch_product(products, product_id) that:
#     - Calls get_product inside a try block
#     - Catches the KeyError, logs "Product lookup failed: {e}"
#     - Re-raises it so the caller also sees the error
#
#     Wrap the fetch_product call in a try/except
#     and show the error propagating through both functions

my_products = ['12', '13', '15', '24']

def get_product(products, product_id):
    if product_id not in products:
        raise KeyError(f"{product_id} not in products.")
    return product_id
    
def fetch_product(products, product_id):
    try:
        result = get_product(products, product_id)
    except KeyError as e:
        print(f"Product lookup failed: {e}")
        raise
    else:
        return result

print()
print("Question 04:")
print('-' * 24)

prod_id = '17' 

try:
    result = fetch_product(my_products, prod_id)
except KeyError as e:
    print(f"Error: {str(e)}")
else:
    print(f"Found! {prod_id} is in {my_products}")


prod_id_2 = '12' 

try:
    result = fetch_product(my_products, prod_id_2)
except KeyError as e:
    print(f"Error: {str(e)}")
else:
    print(f"Found! {prod_id_2} is in {my_products}")

# Q5. Combine everything — OOP, error handling, custom exceptions:
#     Create these exceptions: OrderError(Exception),
#     InvalidQuantityError(OrderError), PaymentError(OrderError)
#
#     Create a class called Order with:
#     - __init__(self, product, quantity, price_per_unit)
#       raise InvalidQuantityError if quantity <= 0
#     - method pay(self, amount_paid)
#       raise PaymentError if amount_paid < self.total
#     - property or method total(self) returning quantity * price_per_unit
#     - __str__ returning "Order: {product} x{quantity} — ${total}"
#
#     Test creating a valid order and paying correctly
#     Test creating an order with invalid quantity
#     Test paying with insufficient amount

class OrderError(Exception):
    pass

class InvalidQuantityError(OrderError):
    pass

class PaymentError(OrderError):
    pass

class Order:
    def __init__(self, product, quantity, price_per_unit):
        if quantity <= 0:
            raise InvalidQuantityError("Order failed! Quantity must be greater than zero")
        self.product = product
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.total = quantity * price_per_unit

    def pay(self, amount_paid):
        if amount_paid < self.total:
            raise PaymentError(f"Payment unsuccessful. Shortfall ${(self.total - amount_paid):,}")
        print(f"${amount_paid:,} paid successfully!")
        
    def __str__(self):
        return f"Order: {self.product} x{self.quantity} — ${self.total}"

print()
print("Question 05:")
print('-' * 24)

try:
    my_order = Order('dragon fruit', 3, 10)
except InvalidQuantityError as e:
    print(f"Error: {str(e)}")
else:
    print(f"{my_order} successfully created!")

try:
    my_order.pay(30)
except PaymentError as e:
    print(f"Error: {str(e)}")

try:
    invalid_order = Order('dragon fruit', -2, 10)
except InvalidQuantityError as e:
    print(f"Error: {str(e)}")
else:
    print(f"{my_order} successfully created!")

try:
    my_order.pay(15)
except PaymentError as e:
    print(f"Error: {str(e)}")

