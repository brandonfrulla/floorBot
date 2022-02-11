import discord
import requests

client = discord.Client()
File_object = open(".botPw", "r")

url = "https://api.opensea.io/api/v1/collection/"
slugs = { 'doodles': "doodles-official",
            'bayc': "boredapeyachtclub",
            'wabc': "wicked-ape-bone-club",
            'mayc': "mutant-ape-yacht-club",
            'clonex': "clonex",
            'azuki' : "azuki",
            'ccats': "cool-cats-nft",
            'meebits': "meebits",
            'kongz': "cyberkongz",
            'meka':"mekaverse",
            'hape':"hapeprime",
            'cworld':"creatureworld"
}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('/f'):

        slug = message.content
        _list = slug.split(" ")

        if (len(_list)<2):
            await message.channel.send("Include a slug ticker, you whore.\n\nTo ask for help, call '/f help'")
        else:
            if(_list[1] == 'help'):
                await message.channel.send(slugs.keys())
            elif (_list[1] in slugs.keys()):
                newUrl = url + slugs.get(_list[1]) 
                response = requests.request("GET", newUrl)
                json = response.json()
                collection = json['collection']
                stats = collection['stats']
                floor = stats['floor_price']
                await message.channel.send(floor)
            else:
                await message.channel.send("I don't know that slug yet")
            
client.run(File_object.read())
