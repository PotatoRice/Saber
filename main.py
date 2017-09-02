import discord
from random import randint
client = discord.Client()

voteObjects = []
saberInsults = ["Saber sucks", "saber sucks", "fuck saber", "Fuck saber", "Fuck Saber"]
insults = ["'<@' + user + '>' + ' can suck a fat one'", "'Hey ' + '<@' + user + '>' + ', I fucked your mom'", "'<@' + user + '>' + ' likes dick in their ass'", "'<@' + user + '>' + ' thinks Community is a good show'", "'<@' + user + '>' + 'plays Legion jungle'", "'<@' + user + '>' + ' thinks Hannah Marchi is hot'", "'<@' + user + '>' + ' is gay'", "'<@' + user + '>' + ' jerks it to Roadhog fanfics'", "'<@' + user + '>' + ' spits on the wiener'", "'<@' + user + '>' + ', your parents must be brothers'", "'<@' + user + '>' + ', nigga u gay'", "'<@' + user + '>' + ' is a filthy casual'", "'<@' + user + '>' + ' can go fuck themselves'", "'<@' + user + '>' + ' mains Roy'", "'<@' + user + '>' + ' is a fucking faggot'", "'<@' + user + '>' ', do you get to the Cloud District very often? Oh, what am I saying, of course you dont'"]
axelPics = ["\"https://cdn.discordapp.com/attachments/291077390187364352/352696468450050049/20160523_213317.jpg\"","\"http://imgur.com/0OabyTQ\"", "\"https://cdn.discordapp.com/attachments/291077390187364352/352692689109647361/Axel_Trap.png\""]
davisPics = ["\"http://i.imgur.com/sk9CSqW.png\"","\"https://partymmr.com/wp-content/uploads/2017/03/dota-2-memes-am-finish-farming-945x751.png\""]
chrisPics = ["\":EZ:\""]
ericPics = ["\"https://www.youtube.com/watch?v=3KquFZYi6L0&ab_channel=UrielMatt\""]
votes = {}
class Vote:
    yes = 0
    no = 0
    '''
    async def __init__(self, name):
        self.name = name
        self.voters = []
        right so i have no idea how to do an init method within this async/await bullshit, so I'm leaving this out.
        We just run Vote.start at the same time we initialize, and it's all good... I think.
        '''
    '''
    "Let me explain"
    Ok so we have a dictionary called votes that keeps track of the name and number of each vote. This is important
    because otherwise we have no way to associate user input of a vote name with the vote object it actually refers to.
    Voters is a dictionary that keeps tracks of who voted and what their response was. This way we can limit users to one
    vote, allow them to change their vote, check who voted for what, etc.
    '''
    async def start(self, message, name):
        self.name = name
        votes[self.name] = n;
        self.voters = {}
        await client.send_message(message.channel, 'New vote: ' + name)
        
    
    async def addVote(self, message, yesno):
        if message.author in self.voters:
             await client.send_message(message.channel, "You already voted for " + str(self.name) + ", asshole.")
        else:
            if yesno == 'yes':
                self.voters[message.author] = 'yes'
                self.yes += 1
                await client.send_message(message.channel, "Current votes for: " + str(self.name) + "\nYes: " + str(self.yes) + "\nNo: " + str(self.no))
            elif yesno == 'no':
                self.voters[message.author] = 'no'
                self.no += 1
                await client.send_message(message.channel, "Current votes for: " + str(self.name) + "\nYes: " + str(self.yes) + "\nNo: " + str(self.no))
    async def printVote(self, message):
        await client.send_message(message.channel, "Current votes for: " + str(self.name) + "\nYes: " + str(self.yes) + "\nNo: " + str(self.no))


async def axel(message):
    msg = eval(axelPics[randint(0,len(axelPics)-1)]).format(message)
    await client.send_message(message.channel, msg)

async def davis(message):
    msg = eval(davisPics[randint(0,len(davisPics)-1)]).format(message)
    await client.send_message(message.channel, msg)
    
async def chris(message):
    msg = eval(chrisPics[randint(0,len(chrisPics)-1)]).format(message)
    await client.send_message(message.channel, msg)

async def eric(message):
    msg = eval(ericPics[randint(0,len(ericPics)-1)]).format(message)
    await client.send_message(message.channel, msg)
    

async def insult(message, mentions):
    for user in mentions:
        msg = eval(insults[randint(0,len(insults)-1)]).format(message)
        await client.send_message(message.channel, msg)

n = 0
@client.event
async def on_message(message):
    words = message.content.split()
    if message.author == client.user:
        return
    if message.content.startswith('~hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if ("Nico" in message.content) or ("nico" in message.content):
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=96zCe-jIPYU")
    if (saberInsults[0] in message.content) or (saberInsults[1] in message.content) or (saberInsults[2] in message.content) or (saberInsults[3] in message.content) or (saberInsults[4] in message.content): 
        msg = 'Hey {0.author.mention}, fuck you too'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('~insult'):
        await insult(message, message.raw_mentions)
    if message.content.startswith('~axel'):
        await axel(message)
    if message.content.startswith('~davis'):
        await davis(message)
    if message.content.startswith('~chris'):
        await chris(message)
    if message.content.startswith('~eric'):
        await eric(message)
    if message.content.startswith('~vote'):
        if message.content.startswith('~vote new'):
            voteName = words[2]
            if voteName in votes:
                await client.send_message(message.channel, 'Sorry, that vote already exists. Dumbass')
            else:
                global n
                voteObjects.append(Vote())
                await voteObjects[n].start(message, voteName)
                n += 1
        else:
            voteName = words[1]
            if voteName in votes:
                voteNumber = votes[voteName]
                if words[2] == "yes":
                    await voteObjects[voteNumber].addVote(message, 'yes')
                elif words[2] == "no":
                    await voteObjects[voteNumber].addVote(message, 'no')
                elif words[2] == "print":
                    await voteObjects[voteNumber].printVote(message)
                else:
                    await client.send_message(message.channel, 'Error, vote input not recognized. Please enter in the form of "~vote (votename) (yes/no)"')
            
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('MzM0OTA4MTc1MzkwMDgxMDI0.DEiDfw.oRpBBOvUePjb5Sg-8kL-6yWB828')
