import json

# Q1. Create a Python dictionary representing a product with at least
#     5 keys including a nested dict for "seller" (name, location)
#     and a list for "tags"
#     Convert it to a JSON string using json.dumps() with indent=4
#     Print the result and print its type to confirm it's a string

product = {
    'name': 'tomato',
    'price': 3.99,
    'in_stock': True,
    'quantity': 10,
    'seller': {
        'name': 'Issam',
        'location': 'Mbweni, Zanzibar',
        'tags': ['groceries', 'fruit', 'fresh']
    }
}

json_string = json.dumps(product, indent=4)

print()
print("Question 01:")
print(json_string)
print(type(json_string))

# Q2. Take this JSON string and parse it into a Python dict:
#     json_str = '{"order_id": 201, "customer": "Ismail", "items": [{"product": "shirt", "qty": 2}, {"product": "shoes", "qty": 1}], "paid": true, "notes": null}'
#     After parsing:
#     a) Print the customer name
#     b) Print the first item's product name
#     c) Print whether it's paid (confirm it's a Python bool, not a string)
#     d) Print the notes value and confirm it came back as None

json_str = '{"order_id": 201, "customer": "Ismail", "items": [{"product": "shirt", "qty": 2}, {"product": "shoes", "qty": 1}], "paid": true, "notes": null}'

my_order = json.loads(json_str)

print()
print("Question 02:")
print(my_order['customer'])
print(my_order['items'][0]['product'])
print(my_order['paid'])
print(type(my_order['paid']))
print(my_order['notes'])

# Q3. Write a function called build_api_response(success, data, message)
#     that builds and returns a JSON string in this structure:
#     {
#         "success": true/false,
#         "message": "...",
#         "data": { ... }
#     }
#     Call it twice — once with success=True and real data,
#     once with success=False and empty data {}
#     Print both results with indent=4

def build_api_response(success, data, message):
    response = {
        'success': success,
        'message': message,
        'data': data
    }

    return json.dumps(response, indent=4)

print()
print("Question 03:")
print(build_api_response(True, {'username': 'izzy', 'location': 'Oregon, US'}, 'OK!'))
print()
print(build_api_response(False, {}, 'NOT OK!'))

# Q4. Write a function called parse_payment_response(json_string) that:
#     - Parses the JSON string
#     - Catches json.JSONDecodeError if the string is invalid
#     - Catches KeyError if expected fields are missing
#     - If "status" is "success", returns "Payment confirmed. Ref: {ref_id}"
#     - If "status" is "failed", returns "Payment failed: {reason}"
#     Test with a success response, a failed response, broken JSON,
#     and a valid JSON missing a required field

def parse_payment_response(json_string):
    try:
        result = json.loads(json_string)
    except json.JSONDecodeError:
        return "Error: Invalid JSON"

    try:
        status = result['status']
        if status == 'success':
            return f"Payment confirmed. Ref: {result['ref_id']}"
        elif status == 'failed':
            return f"Payment failed: {result['reason']}"
    except KeyError as e:
        return f"Error: Missing field {e}"

# Test data
success = '{"status": "success", "ref_id": "HGAD7368QBFADI"}'
failed = '{"status": "failed", "reason": "Insufficient balance"}'
broken = '{"status": "success", ref_id: missing_quotes}'
missing_field = '{"status": "success"}'

print()
print("Question 04:")

print(parse_payment_response(success))
print(parse_payment_response(failed))
print(parse_payment_response(broken))
print(parse_payment_response(missing_field))

# Q5. Create a list of at least 3 user dicts, each with:
#     username, email, role, is_active
#     Write it to a file called users.json using json.dump()
#     Then read it back using json.load()
#     Loop through the loaded data and print only active users
#     in this format: "ismail (admin) — ismail@mail.com"

users = [
    {'username': 'Farid', 'email': 'farid@abc.com', 'role': 'admin', 'is_active': True},
    {'username': 'Hassan', 'email': 'hassan@abc.com', 'role': 'viewer', 'is_active': False},
    {'username': 'Khalid', 'email': 'khalid@abc.com', 'role': 'support', 'is_active': True}
]

# writing to file
with open("users.json", "w") as f:
    json.dump(users, f, indent=4)

with open("users.json", "r") as f:
    loaded = json.load(f)


print()
print("Question 05:")
for user in loaded:
    if user['is_active'] == True:
        print(f"{user['username']} ({user['role']}) — {user['email']}")

