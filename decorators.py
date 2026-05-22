# Q1. Write a decorator called logger that:
#     - Prints "Calling: {function_name}" before the function runs
#     - Prints "Done: {function_name}" after it runs
#     - Uses @wraps and passes through *args, **kwargs
#     Apply it to two different functions and test both

# Q2. Write a decorator called validate_positive that:
#     - Checks the first argument passed to the decorated function
#     - If it's <= 0, returns {"error": "Value must be positive"}
#     - Otherwise runs the function normally
#     Apply it to a function called calculate_discount(price, percent)
#     Test with a valid price and an invalid one (negative)

# Q3. Write a decorator called timer that:
#     - Records the time before and after the function runs
#     - Prints "{function_name} completed in {time} seconds"
#     - Returns the function's result unchanged
#     Apply it to a function that loops 1,000,000 times
#     and returns the final count

# Q4. Write a decorator with arguments called require_role(role):
#     - Takes a role string as argument
#     - The wrapper checks if user["role"] matches the required role
#     - If not, returns {"error": "Access denied. Requires: {role}"}
#     - If yes, runs the function normally
#     Apply it to two functions: one requiring "admin", one requiring "editor"
#     Test each with a matching and non-matching user dict

# Q5. Stack two decorators on one function:
#     Use the logger from Q1 and require_role from Q4
#     Apply both to a function called manage_products(user, action)
#     that returns "{user['username']} performed: {action}"
#     Test with an admin user and a viewer user
#     Observe the order the decorators run