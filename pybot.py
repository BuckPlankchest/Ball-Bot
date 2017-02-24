import discord
import asyncio
import os.path
import random

bot = discord.Client()

@bot.event
@asyncio.coroutine
# both the above lines are need for python 3.4.2
# this would be different for newer versions of python
def on_ready():

    # event for when the bot is is done preparing the data received from discord
    # prints out the name and id of the bot to the termainal
    # and makes the bot send a ready message to the discord text channel
    print('Login succesful')
    print("Bot username: %s" % bot.user.name)
    print("Bot id: %s" % bot.user.id)
    print('------')
    channel = discord.Object(id='channel_id')
    yield from bot.send_message(channel,'Ohayou!')
    #creates blank lists to store shit
    storedFortune = [None] * 1
    storedNick = [None] * 1
    storedQuote = [None] * 1

@bot.event
@asyncio.coroutine
def on_message(message):

    if message.author == bot.user:
        # prevents the bot from responding to itself
        return

    if (message.content == 'ping'):
        if (message.author.id == 'author_id'):
            # BEEEEEES message
            msg = '{0.author.mention} gnop!'.format(message)
            yield from bot.send_message(message.channel, msg)
        else:
            # other people
            msg = ('{0.author.mention} %s' % Random_Message()).format(message)
            yield from bot.send_message(message.channel, msg)

    if "literally" in message.content:
        # responds if a message contains a substring
        yield from bot.send_message(message.channel, 'literally')
    
    if "!fortune" in message.content:
	#this is the fortune part, here's hoping it works
        yield from bot.send_message(message.channel, randomFortune())

    # admin commands
    # commands in this section should only be executed if called by a specific user (hopefully the bot's owner)
    if (message.author.id == 'admin_id'):
        if (message.content == '!kill'):
            # disconnects fromt the discord server and ends the script
            yield from bot.send_message(message.channel, 'Oyasumi!')
            yield from bot.close()
            exit()

	if (message.content == '!nickChange'):
		# supposed ot force the bot to change nickname
		changeNick()


def Random_Message():
    # pulls a random response from a list and returns it as a string
    # since randint uses the list length as the max value, added more repsonses involves simply adding strings to the list
    # and restarting the script
    r_response_list = ['reponse_1', 'reponse_2', 'reponse_3', 'response_4', 'reponse_5']
    random = randint(0,(len(r_response_list)-1))
    return r_response_list[random]

def main():
    # bot token, do not change this
    # this allows the bot to login to the discord server
    bot.run("bot_token")

def changeNick():
	# for changing nickname
	if storedNick.len > 10:
		storedNick.pop([0])

	for item in storedNick:
		randNick = random.choice(open('nicknames.txt').readlines())
		if randNick not in storedNick:
			client.change_nickname(client.user, randNick())
			storedNick.append(randNick)

def randomFortune() -> str:
	# Man I hope this works
	if storedfortune.len > 10:
		storedFortune.pop([0])

	for item in storedFortune:
		randFortune = random.choice(open('fortune.txt').readlines())
		if randFortune not in storedFortune:
			storedFortune.append(randFortune)

	return randFortune

def randomQuote() -> str:
	#fuck me, I really hope this works
	if storedQuote.len > 10:
		storedFortune.pop([0])

	for item in storedQuote:
		randQuote = random.choice(open('quotes.txt').readlines())
		if randQuote not in storedQuote:
			storedQuote.append(randquote)

	return randQuote

main()

# remember to add cheks to see if the txt fiels exist
# if os.path.isfile('fortunes.txt') is false:
# 	print('fortunes.txt not found! Exiting')
#	exit
#
# if os.path.isfile('quotes.txt') is false:
#	print('quotes.txt not found! Exiting')
#	exit
#
# if os.path.isfile('nicknames.txt') is false:
#	print('nicknames.txt not found! Exiting')
#	exit
