
'''<<------------------------------------------------------------------SEASOON-6------------------------------------------------------------------>>'''

'''1.Create a Python dictionary called insta_followers that stores the number of followers for 5 Instagram influencers 
(use their usernames as keys and follower counts as values). Print the dictionary.'''
insta_followers = {"virat_kholi":273,"leo_missi":511,"premanand_jii":900,"aventica_desani":560,"ashish":320}
print(insta_followers)
'''2.Add a new influencer to your insta_followers dictionary and update the follower count for one existing influencer. 
Then, delete one influencer from the dictionary and print the updated dictionary.'''
insta_followers = {"virat_kholi":273,"leo missi":511,"premanand_jii":900,"aventica_desani":560,"ashish":320}
insta_followers["dipika"] = 678# adding one influencer
insta_followers["virat_kkholi"] = 678# updating one influencer
del insta_followers["ashish"]# deleting one influencer
print(insta_followers)

'''3.Given a dictionary called food_prices with 5 Zomato food items as keys and their prices as values, write code to display
 all items that cost more than ₹200.'''
food_price = {"pizza":250,"manchurian":250,"rasmali":430,"burger":125,"franki":300,"pulav":200}
for food, price in food_price.items():

    if price>200:
        print("The cost of this iteams are more than 200:--",price)

'''4.Create two sets: flipkart_users and myntra_users, each containing 5 unique usernames. Find and print the set of users 
who have accounts on both platforms using set intersection.'''
flipkart_users = {"ashish","mahii","udisha","krishna","akasha","priya","divy","jasmine"}
myntra_users = {"prakash","mahii","sidhi","krishna","vikash","priya","priyanka","jasmine"}
final = flipkart_users.intersection(myntra_users)
print(final)
'''5.Write a function get_unique_artists(spotify_playlist1, spotify_playlist2) that takes two sets of artist names and returns a 
set of all unique artists across both playlists (set union).<br><br><em><strong>Hint:</strong> Use the union() method or the | operator for sets.</em>'''
def get_unique_artists(spotify_playlist1,spotify_playlist2):
    return spotify_playlist1,spotify_playlist2
spotify_playlist1 = {"jaya kishori","arjit singh","kanahiya mittal","shidu mosseiala"}
spotify_playlist2 = {"jaya kishori","neha kakkar","prakash mali","avantika desani"}
final = get_unique_artists(spotify_playlist1,spotify_playlist2)
print(final)
