# Q1. Write a function called safe_divide(a, b) that:
#     - Tries to divide a by b
#     - Catches ZeroDivisionError and returns "Cannot divide by zero"
#     - Catches TypeError and returns "Both inputs must be numbers"
#     - Returns the result if successful
#     Test with: (10, 2), (10, 0), (10, "five")

def safe_divide(a, b):
    try:
        a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Both inputs must be numbers"
    else:
        return a / b

print()
print("Question 01:")
print('-' * 24)
print(f"{safe_divide(10, 2)}")
print(f"{safe_divide(10, 0)}")
print(f"{safe_divide(10, "five")}")

# Q2. Write a function called get_user(users, username) that:
#     - Accepts a dict of users and a username to look up
#     - Tries to access users[username]
#     - Catches KeyError and returns "User not found"
#     - Returns the user data if found
#     Test with an existing and non-existing username

users = {
    "jdoe": "John Doe",
    "asmith": "Alice Smith",
    "bwayne": "Bruce Wayne"
}

def get_user(users, username):
    try:
        users[username]
    except KeyError:
        return "User not found"
    else:
        return f"{username} - {users[username]} found!"

print()
print("Question 02:")
print('-' * 24)
print(f"{get_user(users, 'izzy')}")
print(f"{get_user(users, 'jdoe')}")

# Q3. Write a function called create_account(username, password) that:
#     - Raises ValueError if username is empty
#     - Raises ValueError if password is shorter than 8 characters
#     - Otherwise returns {"success": True, "username": username}
#     Wrap the calls in try/except and print the result
#     Test with valid and invalid inputs

def create_account(username, password):
    if not username:
        raise ValueError("Username is empty")
    elif len(password) < 8:
        raise ValueError("Password should 8 characters or more!")
    return {"success": True, "username": username}

print()
print("Question 03:")
print('-' * 24)

# Valid Inputs
try:
    create_account('izzy', 'hgabjhd63y68qu3')
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"{create_account('izzy', 'hgabjhd63y68qu3')}")

# No Username
try:
    create_account('', 'hgabjhd63y68qu3')
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"{create_account('', 'hgabjhd63y68qu3')}")

# Short password

try:
    create_account('izzy', 'qu3')
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"{create_account('izzy', 'qu3')}")



# Q4. Write a function called process_order(product, quantity, price) that:
#     Uses the full try/except/else/finally structure:
#     - try: validate that quantity and price are greater than 0
#       raise ValueError if not
#       compute total = quantity * price
#     - except ValueError as e: return {"success": False, "error": str(e)}
#     - else: return {"success": True, "total": total}
#     - finally: print "process_order() called" every time
#     Test with valid and invalid inputs

def process_order(product, quantity, price):
    try:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        total = quantity * price
    except ValueError as e:
        return {"success": False, "error": str(e)}
    else:
        return {"success": True, "total": total}
    finally:
        print("process_order() called")

print()
print("Question 04:")
print('-' * 24)

print(f"{process_order('apples', 12, 3.99)}")
print(f"{process_order('oranges', -5, 3.99)}")
print(f"{process_order('bananas', 12, -2.5)}")


# Q5. Combine error handling with OOP:
#     Add error handling to this BankAccount class:
#     - deposit(amount): raise ValueError if amount <= 0
#     - withdraw(amount): raise ValueError if amount <= 0
#                         raise ValueError if amount > balance

class BankAccount:
    def __init__(self, owner, opening_balance):
        self.name = owner
        self.balance = opening_balance
        print(f"Account created ✅. Balance: ${self.balance:,}")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        self.balance += amount
        print(f"Deposit of ${amount:,} is successful! Your current balance is ${self.balance:,}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        if amount > self.balance:
            raise ValueError("Withdrawal amount can not be higher than account balance")
        self.balance -= amount
        print(f"Withdrawal of ${amount:,} is successful! Your current balance is ${self.balance:,}")

print()
print("Question 05:")
print('-' * 24)

#     Wrap all method calls in try/except when testing
#     and print a clean error message for each failure case
#     Test: deposit valid, deposit negative,
#           withdraw valid, withdraw more than balance

my_account = BankAccount('Imran', 350)

# deposit valid
try:
    my_account.deposit(4550)
except ValueError as e:
    print(f"Error: {str(e)}")

# deposit negative
try:
    my_account.deposit(-15)
except ValueError as e:
    print(f"Error: {str(e)}")

# withdraw valid

try:
    my_account.withdraw(50)
except ValueError as e:
    print(f"Error: {str(e)}")

# withdraw negative

try:
    my_account.withdraw(-35)
except ValueError as e:
    print(f"Error: {str(e)}")

# withdraw more than balance

try:
    my_account.withdraw(15000)
except ValueError as e:
    print(f"Error: {str(e)}")