'''<<--------------------------------------------------------LOOPS TOPIC-------------------------------------------------------------------------------->>'''
'''1.Create a Python script that uses a for loop to print the names of 5 favorite food delivery apps (e.g., Zomato, Swiggy, etc.), one per line.'''
favorite_food = ("Zomato","Swiggy","Lapinoz","Dominoz","MC Donels")
for i in favorite_food:
    print(i)
'''2.Given a list of daily step counts for a week, use a while loop to find and print the first day when you crossed 10,000 steps.<br><br><em><strong>Hint:</strong> 
Loop through the list and stop as soon as you find a value greater than 10,000.</em>'''
steps_list = []
day = 1
steps = 0
count = 0
while steps<7:
    step = int(input(f"Enter your  {steps+1} day steps of this week:--"))
    steps_list.append(step)
    steps+=1
    
    while count<len(steps_list):
        if steps_list[count]>10000:
            print("your first day crossed steps day is :--",steps+1)
            break
        count+=1
    else:
        print("no day crossed 10000 steps.")

'''3.Write a Python function that takes a list of IPL team names and prints only those teams whose names are longer than 6 characters, skipping the rest 
using the continue statement.'''
def ipl_team(list_team):
    for i in list_team:
        if len(i)<=6:
            continue
        print(i)
list_team = ["Chennai Super Kings",
    "Mumbai Indians",
    "Royal Challengers Bengaluru",
    "Kolkata Knight Riders",
    "Sunrisers Hyderabad",
    "Rajasthan Royals",
    "Delhi Capitals",
    "Lucknow Super Giants",
    "Gujarat Titans",
    "Punjab Kings"]
final = ipl_team(list_team)
print(final)

'''4.You have a list of song durations (in seconds) from your Spotify playlist. Use a for loop with enumerate to print each song's position (starting from 1)
 and its duration in the format: 'Song 1: 210 seconds'.'''
def song_duration(duration):
    position = 1
    for i in duration:
        print("song",position,":",i,"seconds")
        position = position + 1
song_playlist = [210,356,780,455,460,220,560,640,669]
final = song_duration(song_playlist)
print(final)

'''5.Build a simple shopping cart total calculator: Given a list of item prices from a Flipkart cart, use a loop to sum the prices. If an item price is 0 (out of stock), skip it. 
Stop adding items if the running total crosses ₹2000 using break, and print the final total.<br><br><em><strong>Constraint:</strong> Use both break and continue in your solution.</em>'''
def shopping_cart(iteam_price):
    sum = 0
    for i in iteam_price:
        if i==0:
            continue
        sum = sum + i
        print(sum)
        if sum > 2000:
            break
    print("Final Total = ",sum)
flipkart_cart = [250,500,678,890,789,567,735,648,457,0,890,6000]
final = shopping_cart(flipkart_cart) 
print(final)       
