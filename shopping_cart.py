# shopping_cart.py
import os
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


subtotal_price = 0
selected_ids = []

while True:
    selected_id = input("Please input a product identifier, or write DONE if you are finished with your order: ").lower()
    if selected_id == "done":
        break
    if int(selected_id) > len(products) or int(selected_id) <=0:
        print("OOPS! Invalid ID, try again.")
    else:
        selected_ids.append(selected_id)

print("------------------------------------")
print("TK's Delicatessen")
print("------------------------------------")
print("Website: www.tkdeli.com")
print("Phone Number: 1-201-340-5039")
print("------------------------------------")

#datetime
from datetime import datetime  
now = datetime.now()
 
dt_string = now.strftime("%m/%d/%y %H:%M:%S")
print("CHECKOUT TIME:", dt_string)
print("-----------------------------")
print("SELECTED PRODUCTS:")


for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    subtotal_price = subtotal_price + matching_product["price"]
    print("... ",matching_product["name"], "(" + str(to_usd(matching_product["price"])) + ")")


#Totals
from dotenv import load_dotenv

load_dotenv()


tax_rate = (os.getenv("TAX_RATE", default = 0.0875))
print(tax_rate)

tax = subtotal_price * float(tax_rate)
total = subtotal_price + tax

# Bottom of receipt
print("-----------------------------") 
print ("SUBTOTAL:", to_usd(subtotal_price))
print ("SALES TAX:", to_usd(tax))
print ("TOTAL:", to_usd(total))
print("-----------------------------")
receiptask = input("Would you like an email copy of your receipt? (Yes/No):")
if receiptask == "Yes":
    customeremail = input("Please enter your email address:")
    #an attempt was made
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="Please set env var called 'SENDGRID_API_KEY'")
    SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="Please set env var called 'SENDER_ADDRESS'")
print("-----------------------------")

print("Thanks for shopping, please come back soon!")