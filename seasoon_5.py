'''<<------------------------------------------------------SEASOON-5-------------------------------------------------------------------------------------->>'''

'''1.Create a list called playlist_ids with 5 song IDs (as integers) that you might see in a Spotify playlist, and print the list.'''
# playlist_ids = [12576,10345,25408,56898,34907]
# print(playlist_ids)
'''2.Add two more song IDs to your playlist_ids list using both append() and extend(), then print the updated list. 
<br><br><em><strong>Hint:</strong> Use append() for a single ID and extend() for adding multiple IDs at once.</em>'''
# playlist_ids = [12576,10345,25408,56898,34907]
# playlist_ids.append(6489)
# playlist_ids.extend([45678,32789,4536,23723,2533])
# print(playlist_ids)

'''3.Simulate removing the last played song from your playlist_ids list using pop(), and display the removed ID along with the remaining playlist.'''
# playlist_ids = [12576,10345,25408,56898,34907]
# playlist_ids.pop()
# print(playlist_ids)

'''4.Create a tuple called insta_filters with 4 Instagram filter names (as strings). Try to change the first filter name
 and observe what error you get.<br><br><em><strong>Hint:</strong> Tuples are immutable. Note down the error message.</em>'''
# insta_filter = ("Juno","Slumber","Crema","Ludwig","Aden")
# insta_filter[0] = "moon" 
# print(insta_filter)
'''5.Write a short Python script that takes a scenario (like a list of recent Zomato orders vs a tuple of fixed IPL team names) and
 prints which one should use a list and which should use a tuple, explaining your choice in a comment'''
zomato_order = ["pizza","burger","sandwitch","pav-bhaji","manchurian","pulav","dhokla","rashmali"]
ipl_team =("KKR","RCB","GT","RR","CSK","LSG","MI","DC","PBKS","SRH")
print("Recent zomatos order are :--",zomato_order)#we have use list for zomatoes order because the data is not fixed if we want to remove or add some item
# then we can easily change using list .
print("IPL Teams are :--",ipl_team)# we have use tuple for ipl teams because the data are fixed and can not be change so the best option is to use tuple .
