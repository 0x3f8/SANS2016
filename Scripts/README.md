These are scripts I used to solve some of the challenges

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


**getAllItemsFromDungeonOnline.exp**

This experimental expect script will connect to the dungeon server and retrieve all items TK GDT command then performing inventory/drop.

Current Issues:

- Dropping the Axe causes the troll to appear and murder you.  Using NT doesn't fix this
- Dropping the skeleton causes its ghose to appear, but the script keeps going
- Several other items cause issues
- At some point items don't get dropped and then inventory begins to stack, making it difficult to verify item index number

*I've discovered another way to find item descriptions and will be posting an update soon*

```
expect getAllRoomsFromDungeonOnline.exp > someTextFile
```

Then read the text file

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

