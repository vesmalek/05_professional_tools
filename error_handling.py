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

# Q4. Write a function called process_order(product, quantity, price) that:
#     Uses the full try/except/else/finally structure:
#     - try: validate that quantity and price are greater than 0
#       raise ValueError if not
#       compute total = quantity * price
#     - except ValueError as e: return {"success": False, "error": str(e)}
#     - else: return {"success": True, "total": total}
#     - finally: print "process_order() called" every time
#     Test with valid and invalid inputs

# Q5. Combine error handling with OOP:
#     Add error handling to this BankAccount class:
#     - deposit(amount): raise ValueError if amount <= 0
#     - withdraw(amount): raise ValueError if amount <= 0
#                         raise ValueError if amount > balance
#     Wrap all method calls in try/except when testing
#     and print a clean error message for each failure case
#     Test: deposit valid, deposit negative,
#           withdraw valid, withdraw more than balance