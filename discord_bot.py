import discord
import requests

client = discord.Client()
File_object = open(".botPw", "r")

url = "https://api.opensea.io/api/v1/collection/"
slugs = { 
            'w3' : "worldwidewebbland?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=type&search[stringTraits][0][values][0]=large%20apartment",
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

        slug = message.content.lower()
        _list = slug.split(" ")

        if (len(_list)<2):
            await message.channel.send("Include a slug ticker!\n\nTo ask for help, call '/f help'")
        else:
            if (len(_list) == 2):
                if(_list[1] == 'help'):
                    reply = format("Acceptable command slugs: \n\n{slugs}".format(slugs = list(slugs.keys())))
                    await message.channel.send(reply)
                elif (_list[1] in slugs.keys()):
                    newUrl = url + slugs.get(_list[1]) 
                    floor = requests.request("GET", newUrl).json()['collection']['stats']['floor_price']
                    reply = format("{slug} Floor: {fl}".format(slug = str.upper(_list[1]), fl = floor))
                    await message.channel.send(reply)
                else:
                    await message.channel.send(format("I don't know that slug yet, add it to my dictionary via pull request here! \n{link}".format(link = 'https://github.com/brandonfrulla/floorBot/blob/main/discord_bot.py')))
            elif ((len(_list) == 3) and (str.lower(_list[2]) == "v")):
                newUrl = url + slugs.get(_list[1]) 
                data = requests.request("GET", newUrl).json()['collection']['stats']
                floor = data['floor_price']
                _1dS = data['one_day_sales']
                _1dV = data['one_day_volume']
                _1dC = data['one_day_change']
                _7dS = data['seven_day_sales']
                _7dV = data['seven_day_volume']
                _7dC = data['seven_day_change']
                _30dS = data['thirty_day_sales']
                _30dV = data['thirty_day_volume']
                _30dC = data['thirty_day_change']
                reply = format("{slug} Floor: {fl}\n*\nOne Day Sales: {_1ds}\nOne Day Volume: {_1dv}\nOne Day Change: {_1dc}\n*\nSeven Day Sales: {_7ds}\nSeven Day Volume: {_7dv}\nSeven Day Change: {_7dc}\n*\nThirty Day Sales: {_30ds}\nThirty Day Volume: {_30dv}\nThirty Day Change: {_30dc}".format(slug = str.upper(_list[1]), fl = floor, _1ds = _1dS, _1dv = _1dV ,_1dc = _1dC, _7ds = _7dS, _7dv = _7dV, _7dc = _7dC, _30ds = _30dS, _30dv = _30dV, _30dc = _30dC))
                await message.channel.send(reply)

client.run(File_object.read())
