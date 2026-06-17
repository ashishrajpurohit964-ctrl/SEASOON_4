
'''<<<-----------------------------------------------------------------------SEASOON:--3--------------------------------------------------------------------------------------------->>>'''
'''1.Declare four variables in Python: your age as an int, your height in centimeters as a float, your name as a str, and whether you have a Spotify account as a bool. 
Print each variable and use the type() function to display its data type'''
# a = 23
# b = 7.99
# n = "Ashish"
# ac = True
# print(f" Your age is :--{a},{type(a)}")
# print(f" Your hight is :--{b},{type(b)}")
# print(f" Your name is :--{n},{type(n)}")
# print(f" You have a spotify account:--{ac},{type(ac)}")

'''2.Write a function total_cart_amount(prices) that takes a list of product prices as strings (like ['199.99', '49', '350.75']) and 
returns the total as a float. Print the result for a sample Flipkart-style cart.<br><br><em><strong>Hint:</strong> Use float() to convert each string before summing.</em>'''

# def total_cart_amount(price):
#         total = 0.0
#         for i in price:
#                 total+=float(total)
                # return total----------------------------------------------------->>>>>>DOUT
# cart = ['199.99', '49', '350.75']

# print(total_cart_amount((cart)))

'''3.Create a script that asks the user to input their cricket score as a string, converts it to an int, and prints 'Half-century!' if the score is 50 or more, otherwise prints 'Keep going!'.
<br><br><em><strong>Constraint:</strong> Use input(), int(), and if-else.</em>'''

# cricket_score = input("Enter your cricket score:--")
# n = int(cricket_score)
# if n >=50:
#     print("Hlaf-century!")
# else:
#     print("keep going!")

'''4.Given the variable is_premium = 'True' (as a string), write code to correctly convert it to a boolean value and print its type.<br><br><em><strong>Hint:</strong> The bool() 
function alone won’t work as expected. Think about string comparison.</em>'''

# is_premium = "True"
# print(type(is_premium))
# b = bool(is_premium)
# print(type(b))