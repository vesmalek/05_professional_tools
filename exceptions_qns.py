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