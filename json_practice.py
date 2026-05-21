import json

# Q1. Create a Python dictionary representing a product with at least
#     5 keys including a nested dict for "seller" (name, location)
#     and a list for "tags"
#     Convert it to a JSON string using json.dumps() with indent=4
#     Print the result and print its type to confirm it's a string

product = {
    'name': 'tomato',
    'price': '3.99',
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

# Q4. Write a function called parse_payment_response(json_string) that:
#     - Parses the JSON string
#     - Catches json.JSONDecodeError if the string is invalid
#     - Catches KeyError if expected fields are missing
#     - If "status" is "success", returns "Payment confirmed. Ref: {ref_id}"
#     - If "status" is "failed", returns "Payment failed: {reason}"
#     Test with a success response, a failed response, broken JSON,
#     and a valid JSON missing a required field

# Q5. Create a list of at least 3 user dicts, each with:
#     username, email, role, is_active
#     Write it to a file called users.json using json.dump()
#     Then read it back using json.load()
#     Loop through the loaded data and print only active users
#     in this format: "ismail (admin) — ismail@mail.com"