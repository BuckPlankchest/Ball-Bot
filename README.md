# Cube-Bot (Affectionately reffered to as "cubey")
## What is it?
A Python 3.4.2+ Discord Bot. Right now, its main use is to listen for messages and respond to certain keywords.

## Requirements
* Python 3.4.2+
* aiohttp library
* websockets library
* [discord.py](https://github.com/Rapptz/discord.py)

All these libraries can be installed with pip. Pip should handle grabbing all the required packages if you grab discord.py.

## Usage

* .kill
Causes the bot to disconnect and the script to exit. This can only be executed if the message comes from a user id

* .fortune
Takes a random line from 'fortune.txt', and responds with a "fortune". 

* .koan
Takes a random line from 'koan.txt', and responds with a koan.

* .quote
Takes a random line from 'quotes.txt', and responds with a quote.

* .yearquote
Takes a random line from 'quotes2.txt' and respons with a quote and random year

## Other helpful things
The discord.py documention might be useful if you want to contribute: https://discordpy.readthedocs.io/en/latest/

New Feature:
The bot now excludes the last 10 quotes, fortunes, or koans, so it won't get duplicates

## Planned features
choice between random and entered nicknames!
the bot changing its nickname periodically!
Being actually functional!
Currency conversions
Calculator
