import discord
import asyncio
import re
import random
import os.path
import linecache
from random import randint

# creates a bot object that has access to Discord's events
bot = discord.Client()

#--------------------------------------------
# Events 
#--------------------------------------------

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
    print("creating arrays...")
    storedKoan = []
    storedQuote = []
    storedFortune = []
    print('------------------')
    channel = discord.Object(id='278559327789514753')
    yield from bot.send_message(channel,'QB is online!')

@bot.event
@asyncio.coroutine
def on_message(message):
    storedKoan = []
    storedQuote = []
    storedFortune = []

    msg_content = message.content

    # User responses fuuko
    if (message.author.id == '278701369765003264'):
        if (re.match('Achoo!')):
            msg = ('{0.author.mention}, bless you!').format(message)
            yield from bot.send_message(message_channel, msg)

    if message.author == bot.user:
        # prevents the bot from responding to itself
        return
    
    if (re.match('\!koan', message.content.lower())):
            # magic eight ball check
            msg = ('{0.author.mention}, %s' % random_line("koan.txt", storedKoan)).format(message)
            yield from bot.send_message(message.channel, msg)
            

    if (re.match('\!fortune', message.content.lower())):        
	    # fortunes!
	    msg = ('{0.author.mention}, %s' % random_line("fortune.txt",storedFortune)).format(message)
	    yield from bot.send_message(message.channel, msg)
	    

    if (re.match('\!quote', message.content.lower())):
	    #quotes!
	    msg = ('{0.author.mention}, %s' % random_line("quotes.txt", storedQuote)).format(message)
	    yield from bot.send_message(message.channel, msg)

# implement later    
#    if (re.match('?(you|he|she|it|it\'s)[\,\ ]? (.+) a big', message.content.lower())):
#            #bane?
#            msg = ('{0.author.mention},for you').format(message)
#            yield from bot.send_message(message.channel, msg)

#--------------------- tl notes ------------------------------------------------------------
    if (re.match('sasuga', message.content.lower())):
            msg = ('{0.author.mention}, TL NOTE: sasuga means sausage').format(message)
            yield from bot.send_message(message.channel, msg)

    if (re.match('keikaku', message.content.lower())):
            msg = ('{0.author.mention}, TL NOTE: keikaku means plan').format(message)
            yield from bot.send_message(message.channel, msg)

    if (re.match('kawaii', message.content.lower())):
            msg = ('{0.author.mention}, TL NOTE: kawaii means scary').format(message)
            yield from bot.send_message(message.channel, msg)

    if (re.match('kowai', message.content.lower())):
            msg = ('{0.author.mention}, TL NOTE: kowai means cute').format(message)
            yield from bot.send_message(message.channel, msg)

    if (re.match('hawaii', message.content.lower())):
            msg = ('{0.author.mention}, TL NOTE: hawaii means cute').format(message)
            yield from bot.send_message(message.channel, msg)

#-------------------------------------------------------------------------------------------

    #--------- Admin commands-----------------------------------

    # commands in this section should only be executed if called by a specific user (hopefully the bot's owner)
    if (message.author.id == '270058815171461121'):
        if (message.content == '!kill'):
            # disconnects fromt the discord server and ends the script
            yield from bot.send_message(message.channel, 'Goodbye!')
            yield from bot.close()
            exit()
   
    #stringo's admin command
    if (message.author.id == '232684662244376576'):
        if (message.content == '!timecube'):
            # disconnects fromt the discord server and ends the script
            yield from bot.send_message(message.channel, 'Goodbye!')
            yield from bot.close()
            exit()
    #-----------------------------------------------------------

def Random_Message(response_list):
    # pulls a random response from the global list and returns it as a string
    random = randint(0,(len(response_list)-1))
    return response_list[random]

def random_line(afile, storage):
    # now a clusterfuck of stackoverflow answers!
    # less random, but now offers unique answers!
#    if len(storage) >= 10:
    # NOTE: I have no clue if using storage.append would modify storage or the arg, so I'm using if statements to be safe
#        if storage == storedKoan:
#            storedKoan.pop(0)
#        if storage == storedFortune:
#            storedFortune.pop(0)
#        if storage == storedQuote:
#            storedQuote.pop(0)

    line_num = 0
    selected_line = ''
    with open(afile) as fp:
       while 1:
         line = fp.readline()
         if not line: break
         line_num += 1
         if random.uniform(0, line_num) < 1:
             selected_line = line
    return selected_line.strip()

#                 if line != storage[i]:
                 # NOTE: I have no clue if using storage.append would modify storage or the arg, so I'm using if statements to be safe
#                     if storage == storedKoan:
#                         storedKoan.append(line)
#                     if storage == storedFortune:
#                         storedFortune.append(line)
#                     if storage == storedQuote:
#                         storedquote.append(line)
def main():
    print('\nLoading scripts...')
    #checks for files
    if os.path.isfile('fortune.txt') is False:
      print('\nfortunes.txt not found! exiting')
      exit()
    if os.path.isfile('quotes.txt') is False:
      print('quotes.txt not found! exiting')
      exit()
    if os.path.isfile('koan.txt') is False:
      print('\nkoan.txt not found! exiting')
      exit()

    print('\nAttempting to log in...')
    # Bot token, do not change this. This allows the bot to login to the discord server
    bot.run("Mjg1NzkyMDM1NTY5NDAxODU3.C5Xrfw.99-cZmqDLQKcI_Zhpf04d90BwTE")

main()
