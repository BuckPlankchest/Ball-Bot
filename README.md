# Ball-Bot
## What is it?
A Python 3.4.2+ Discord Bot. Right now, its main use is to listen for messages and respond to certain keywords.

## Requirements
* Python 3.4.2+
* aiohttp library
* websockets library
* [discord.py](https://github.com/Rapptz/discord.py)

All these libraries can be installed with pip. Pip should handle grabbing all the required packages if you grab discord.py.

## Usage
* ping
Case insenstive. The bot will respond to the ping with a random message.

* !kill
Causes the bot to disconnect and the script to exit. This can only be executed if the message comes from a user id

* !changenick
Makes the bot change it's nickname, randomly from 'nicknames.txt' because of a future plan. Only executable by the owner.

* !fortune
Takes a random line from 'fortune.txt', and responds with a "fortune". 

* !quote
Takes a random line from 'quotes.txt', and responds with a quote.

## Other helpful things
The discord.py documention might be useful if you want to contribute: https://discordpy.readthedocs.io/en/latest/

## Planned features
choice between random and entered nicknames!
the bot changing its nickname periodically!
checking to see if the files are actually there!
Being actually functional!
