''''<<------------------------------------------------seasoon:7--------------------------------------------------------------->>'''
'''1.Write a Python script that takes your current Spotify listening time in minutes and checks if it is above 120 minutes; if yes, print '
You are a true music fan!', otherwise print 'Keep listening!'.'''
listening_time = int(input("enter your time in minute:--"))
if listening_time>120:
    print("You are a true music fan")
else:
    print("keep listining...............!!!")

'''2.Create a Python program that asks the user to enter their Zomato order amount and checks if it is above 300; 
if yes, print 'Eligible for free delivery', else print 'Delivery charges apply'.'''
zomato_amount=int(input("enter your zommato amount:-"))
if zomato_amount>300:
    print("you are eligible for free delivery")
else:
    print("you are not eligible for free delivery")

'''3.Build a Python script that takes your Flipkart cart total and applies the following logic: if total > 2000, print 'You get a 10% discount'; 
elif total > 1000, print 'You get a 5% discount'; else print 'No discount available'.'''
a = int(input("enter your product price:--"))
b= int(input("enter your product price:--"))
c = int(input("enter your product price:--"))
d = int(input("enter your product price:--"))
total = a+b+c+d
print(total)
if total > 2000:
    discount = total*10/100
    final_price=total-discount
    print(f"congratulation you have received of 10% discount {discount} and your final price is :--",final_price)
elif total >1000:
    discount = total*5/100
    final_price = total - discount
    print(f"congratulation you have received 5% discount:-{discount}",final_price)

'''4.Write a Python program that asks the user to enter their IPL fantasy team points and uses nested if-else statements to print: 'Champion' if points > 800, 
'Top Performer' if points between 500 and 800, 'Keep Trying' otherwise.<br><br><em><strong>Hint:</strong> Use nested if-else blocks to check the ranges.</em>'''
points = int(input("enter your points :--"))
if points>800:
    print("Top performer")
    if points>=500:
        print("keep trying")
    else:
        print("keep trying")