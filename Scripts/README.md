These are scripts I used to solve some of the challenges, I may rewrite the expect scripts as pyexpect.  Much cleaner output!

**getAllTextFromDungeonOnline.exp**

This expect script will connect to the dungeon server and retrieve all text from the game.

```
expect getAllTextFromDungeonOnline.exp > someTextFile
```

**getAllRoomsFromDungeonOnline.exp**

This expect script will connect to the dungeon server and retrieve all room descriptions by using the AH GDT command then performing a look.  If you run the script, take note of which index the script starts at. My experience was that the server hung up around room 48 so I cancelled and restarted with the next room in order set

```
expect getAllRoomsFromDungeonOnline.exp > someTextFile
```

**getAllRoomsFromDungeonOnline.py**

Improved script to get all room descriptions.  Uses the DR command to get the room objects, then uses the two description fields without actually visiting the rooms.

```
python getAllRoomsFromDungeonOnline.py
```

**getAllItemsFromDungeonOnline.exp**

This pexpect script will connect to the dungeon server and retrieve all items though debugging (GDT) and Display Text for each object description

Current Issues:
- My python regex-fu is weak. Columns are fixed width so I should be able to pull them all and include details like room numbers.  Later maybe?


```
python getItemsFromDungeonOnline.py
```

**getTweets.py**

This python script can be used to get all of the Twitter clues from santawclaus. You'll need to provide some information in the script to get started.

**Get your own credentials from Twitter**

```
#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""
```

