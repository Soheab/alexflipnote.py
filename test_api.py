import asyncio

import alexflipnote

alex = alexflipnote.Client()


async def lmao():
    lol = "https://cdn.discordapp.com/avatars/150665783268212746/48003cb74f0c32bcdd3cd18c1a2bfe2c.png?size=1024"
    lol2 = "https://google.com/"
    #return print(await alex.amiajoke(lol))
    print(await alex.achievement("ahahahahah"))
    print(await alex.amiajoke(lol))
    print(await alex.challenge("ah yes"))
    print(await alex.trash(
        "https://cdn.discordapp.com/avatars/150665783268212746/48003cb74f0c32bcdd3cd18c1a2bfe2c.png?size=1024",
        "https://cdn.discordapp.com/avatars/374913578655809548/970b349e16461d81e15f2b81296a43d6.png?size=1024"
    ))
    print((await alex.steam('alexflipnote')))
    print(await alex.captcha('ah yes'))
    print(await alex.color('666666'))
    print(await alex.colourify(
        "https://cdn.discordapp.com/avatars/150665783268212746/48003cb74f0c32bcdd3cd18c1a2bfe2c.png?size=1024",
        "666666", "123456"
    ))
    print(await alex.sadcat())
    print(await alex.cats())
    print(await alex.birb())
    print(await alex.drake('ah', 'yes'))
    print(await alex.pornhub('ah', 'yes'))
    print(await alex.supreme('ah yes', dark=True))
    print(await alex.facts('ah yes'))
    print(await alex.fml())
    print(await alex.ship(
        "https://cdn.discordapp.com/avatars/150665783268212746/48003cb74f0c32bcdd3cd18c1a2bfe2c.png?size=1024",
        "https://cdn.discordapp.com/avatars/374913578655809548/970b349e16461d81e15f2b81296a43d6.png?size=1024"
    ))
    print(await alex.salty("https://cdn.discordapp.com/avatars/150665783268212746/48003cb74f0c32bcdd3cd18c1a2bfe2c.png?size=1024"))
    print(await alex.dogs())
    print(await alex.didyoumean('ah', 'yes'))
    print(await alex.filter('gay', "https://cdn.discordapp.com/avatars/150665783268212746/48003cb74f0c32bcdd3cd18c1a2bfe2c.png?size=1024"))
    print(await alex.calling('ah yes'))
    print(dict(await alex.github_colours()).get('Python'))
    print(await alex.colour_image('666666'))
    print(await alex.colour_image_gradient('666666'))
    print(await alex.scroll('ah yes'))
    print(await alex.bad("https://cdn.discordapp.com/avatars/374913578655809548/970b349e16461d81e15f2b81296a43d6.png?size=1024"))

    sess = await alex.close()
    if sess is None:
        print('SESSION IS CLOSED')
    else:
        print("SESSION IS __NOT__ CLOSED")
asyncio.get_event_loop().run_until_complete(lmao())
