'''<<------------------------------------------------------SEASOON_9---------------------------------------------------------------->>'''

'''1.Define a function called calculate_final_price(price, discount_rate) that returns the final price after applying 
the discount rate to the given price.'''
def calculate_final_price(price,discount_rate):
    discount = discount_rate/100
    final_price = price-discount
    return final_price
price = 1500
discount_rate = 25
final = calculate_final_price(price,discount_rate)
print(final)
'''2.Create a function called get_delivery_charge(amount, city='Ahmedabad') that returns 0 if city is 'Ahmedabad', 
otherwise returns 50 as a delivery charge.<br><br><em><strong>Hint:</strong> Use a default argument for the city parameter.</em>'''
def get_delivery_charge(amount,city):
    if city == "Ahmedabad "and "ahmedabad":
        return 0
    else:
        return 50
amount = int(input("Enter your amount value :--"))
city = input("Enter your city name :--")
final = get_delivery_charge(amount,city)
print(final)
'''3.Write a function called format_price(price, currency='INR') that returns a string like '₹500' if currency is 'INR', or '$500' 
if currency is 'USD'.'''
def format_price(price,currency="INR"):
    if currency == "INR":
        return 500
    elif currency=="USD":
        return "$500"
price = int(input("Enter your price:--"))
currency=input("Enter your currancy name:--")
final = format_price(price,currency)
print(final)
    
'''4.Build a function called apply_coupon(price, coupon_code=None) that returns the price after a 10% discount if coupon_code is 
'ZOMATO10', otherwise returns the original price.<br><br><em><strong>Constraint:</strong> Use a default argument for coupon_code.</em>'''
def apply_coupon(price,coupan_code=None):
    if coupan_code == "Zomato10":
        discount = 10/100
        price1 = price - discount
        return price1
    else:
        return price
price = int(input("Enter your price:--"))
coupan_code = input("Enter coupan code :--")
final = apply_coupon(price,coupan_code=None)
print(final)

