import discord
from random import randint
client = discord.Client()

insults = ["'<@' + user + '>' + ' can suck a fat one'", "'Hey ' + '<@' + user + '>' + ', I fucked your mom'", "'<@' + user + '>' + 'likes dick in their ass'", "'<@' + user + '>' + ' thinks Community is a good show'", "'<@' + user + '>' + 'plays Legion jungle'", "'<@' + user + '>' + ' thinks Hannah Marchi is hot'", "'<@' + user + '>' + ' is gay'", "'<@' + user + '>' + ' jerks it to Roadhog fanfics'", "'<@' + user + '>' + ' spits on the wiener'", "'<@' + user + '>' + ', your parents must be brothers'", "'<@' + user + '>' + ', nigga u gay'", "'<@' + user + '>' + ' is a filthy casual'", "'<@' + user + '>' + ' can go fuck themselves'", "'<@' + user + '>' + ' mains Roy'", "'<@' + user + '>' + ' is a fucking faggot'", "'<@' + user + '>' ', do you get to the Cloud District very often? Oh, what am I saying, of course you dont'"]
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('~insult'):
        for user in message.raw_mentions:
            msg = eval(insults[randint(0,len(insults)-1)]).format(message)
            await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('MzM0OTA4MTc1MzkwMDgxMDI0.DEiDfw.oRpBBOvUePjb5Sg-8kL-6yWB828')
