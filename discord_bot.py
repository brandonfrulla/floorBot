import discord
import requests

client = discord.Client()
File_object = open(".botPw", "r")

url = "https://api.opensea.io/api/v1/collection/"
slugs = { 
            'galaxyfc' : "galaxy-fight-club",
            'hgalaxy': "hero-galaxy-heroes",
            'horde': "edenhorde-official",
            'pixel': "pixelmongen1",
            'furu': "karafuru",
            'cdogs': "cooldogsofficial",
            'nfh': "nfh",
            'doodles': "doodles-official",
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
            'cworld':"creatureworld",
            'mfers': "mfers",
            'asuna': "livesofasuna",
            'wow': "world-of-women-nft",
            'bakc': "bored-ape-kennel-club",
            '888': "888innercircle",
            'ntoo': "neotokyo-outer-identities",
            'dfella': "deadfellaz",
            'frenz': "alienfrensnft",
            'veef': "veefriends",
            'bossb': "bossbeauties",
            'abomb': "adam-bomb-squad"
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
            await message.channel.send("Include a slug ticker!\n\nTo ask for help, call '/f help'")
        else:
            if(_list[1].lower() == 'help'):
                reply = format("Acceptable command slugs: \n\n{slugs}".format(slugs = list(slugs.keys())))
                await message.channel.send(reply)
            elif (_list[1].lower() in slugs.keys()):
                newUrl = url + slugs.get(_list[1]) 
                response = requests.request("GET", newUrl)
                floor = response.json()['collection']['stats']['floor_price']
                # collection = json['collection']
                # stats = collection['stats']
                # floor = stats['floor_price']
                reply = format("{slug} Floor: {fl}".format(slug = str.upper(_list[1]), fl = floor))
                await message.channel.send(reply)
            else:
                await message.channel.send(format("I don't know that slug yet, add it to my dictionary via pull request here! \n{link}".format(link = 'https://github.com/brandonfrulla/floorBot/blob/main/discord_bot.py')))

client.run(File_object.read())
