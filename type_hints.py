from typing import Optional
# 
# Q1. Add type hints to all parameters and return types
#     for the following functions:
#
#     def greet(username):
#         return f"Welcome, {username}!"
#
#     def calculate_tax(price, rate):
#         return price * rate
#
#     def is_admin(role):
#         return role == "admin"
#
#     def deactivate_user(username):
#         print(f"{username} deactivated")

def greet(username: str) -> str:
    return f"Welcome, {username}!"

def calculate_tax(price : float, rate : float) -> float:
    return price * rate

def is_admin(role : str) -> bool:
    return role == "admin"

def deactivate_user(username : str) -> None:
    print(f"{username} deactivated")

# Q2. Write a function called create_product that takes:
#     name: str, price: float, tags: list[str],
#     category: str = "General", description: Optional[str] = None
#     It should return a dict[str, any]
#     Call it twice — once with all arguments, once with only required ones

def create_product(name: str, price: float, tags: list[str], category: str = 'General', description: Optional[str] = None) -> dict[str, any]:


# Q3. Rewrite this class with full type hints on __init__ and all methods:
#
#     class Order:
#         def __init__(self, product, quantity, price_per_unit):
#             self.product = product
#             self.quantity = quantity
#             self.price_per_unit = price_per_unit
#             self.status = "pending"
#
#         def confirm(self):
#             self.status = "confirmed"
#
#         def get_total(self):
#             return self.quantity * self.price_per_unit
#
#         def summarize(self):
#             return f"{self.product} x{self.quantity} — ${self.get_total()}"

# Q4. Write a function called process_payment that takes:
#     amount: float, method: str, reference: Optional[str] = None
#     Returns dict[str, str | bool]
#     If amount <= 0, return {"success": False, "error": "Invalid amount"}
#     Otherwise return {"success": True, "method": method,
#                       "reference": reference or "N/A"}
#     Add error handling with try/except — combine type hints
#     with what you learned in Phase 5 error handling

# Q5. Write a function called build_api_response that takes:
#     status: str, data: dict, message: str,
#     errors: Optional[list[str]] = None
#     Returns dict[str, str | dict | list | None]
#     Build and return the response dict with all four keys
#     Test with a success call (no errors) and a failed call (with errors list)