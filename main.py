import asyncio
import os
import platform
import random
import time
from collections import Counter

import discord
import pytz
from discord.ext import commands

from keep_alive import keep_alive

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
intents.reactions = True

client = commands.Bot(command_prefix="$", intents=intents)

# Bot Status


def local_datetime(datetime_obj):
    utcdatetime = datetime_obj.replace(tzinfo=pytz.utc)
    tz = "Africa/Nairobi"
    return utcdatetime.astimezone(pytz.timezone(tz))


__games__ = [
    (discord.ActivityType.playing, "with iamksm"),
    (discord.ActivityType.playing, "with Bloody Actor"),
    (discord.ActivityType.watching, "over {guilds} Server"),
    (discord.ActivityType.watching, "over {members} Members"),
    (discord.ActivityType.watching, "The 254 Millennnial Talk"),
    (discord.ActivityType.listening, "to Podcasts"),
    (discord.ActivityType.listening, "to $ commands"),
]
__gamesTimer__ = 60 * 60  # 60 minutes


@client.event
async def on_ready():
    print("Bot's Ready")
    while True:
        guildCount = len(client.guilds)
        memberCount = len(list(client.get_all_members()))
        randomGame = random.choice(__games__)
        await client.change_presence(
            activity=discord.Activity(
                type=randomGame[0],
                name=randomGame[1].format(guilds=guildCount, members=memberCount),
            )
        )
        await asyncio.sleep(__gamesTimer__)


@client.command()
async def hello(ctx):
    await ctx.send("Hello " + str(ctx.author.display_name) + ", What's up?")


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)


@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 804285695404670986:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == "warzone":
            role = discord.utils.get(guild.roles, name="Warzone")

        elif payload.emoji.name == "apex":
            role = discord.utils.get(guild.roles, name="Apex Legends")

        elif payload.emoji.name == "civ6":
            role = discord.utils.get(guild.roles, name="Civilization 6")

        elif payload.emoji.name == "gta5":
            role = discord.utils.get(guild.roles, name="GTA 5")

        elif payload.emoji.name == "thedivision":
            role = discord.utils.get(guild.roles, name="The Division")

        elif payload.emoji.name == "amongus":
            role = discord.utils.get(guild.roles, name="Among Us")

        elif payload.emoji.name == "leagueoflegends":
            role = discord.utils.get(guild.roles, name="League of Legends")

        elif payload.emoji.name == "brawlhalla":
            role = discord.utils.get(guild.roles, name="Brawlhalla")

        elif payload.emoji.name == "nfspayback":
            role = discord.utils.get(guild.roles, name="NFS:Payback")

        elif payload.emoji.name == "pubglite":
            role = discord.utils.get(guild.roles, name="PUBG Lite")

        elif payload.emoji.name == "pubgmobile":
            role = discord.utils.get(guild.roles, name="PUBG Mobile")

        elif payload.emoji.name == "overwatch":
            role = discord.utils.get(guild.roles, name="Overwatch")

        elif payload.emoji.name == "codmobile":
            role = discord.utils.get(guild.roles, name="COD Mobile")

        elif payload.emoji.name == "genshin":
            role = discord.utils.get(guild.roles, name="Genshin Impact")

        elif payload.emoji.name == "thecrew":
            role = discord.utils.get(guild.roles, name="The Crew")

        elif payload.emoji.name == "valorant":
            role = discord.utils.get(guild.roles, name="Valorant")

        elif payload.emoji.name == "rainbowsix":
            role = discord.utils.get(guild.roles, name="Rainbow Six Siege")

        elif payload.emoji.name == "csgo":
            role = discord.utils.get(
                guild.roles, name="Counter Strike Global Offensive"
            )

        elif payload.emoji.name == "fifa":
            role = discord.utils.get(guild.roles, name="FIFA")

        elif payload.emoji.name == "starwars":
            role = discord.utils.get(guild.roles, name="Starwars Battlefront II")

        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role:
            member = payload.member
            if member:
                await member.add_roles(role)
                print("done")
            else:
                print("Member Not found.")
        else:
            print("Role not found.")

    elif message_id == 836847840503267368:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == "roblox":
            role = discord.utils.get(guild.roles, name="Roblox")

        elif payload.emoji.name == "fortnite":
            role = discord.utils.get(guild.roles, name="Fortnite")

        elif payload.emoji.name == "eurotruck":
            role = discord.utils.get(guild.roles, name="EuroTruck Simulator 2")

        elif payload.emoji.name == "destiny2":
            role = discord.utils.get(guild.roles, name="Destiny 2")

        elif payload.emoji.name == "minecraft":
            role = discord.utils.get(guild.roles, name="Minecraft")

        elif payload.emoji.name == "paladins":
            role = discord.utils.get(guild.roles, name="Paladins")

        elif payload.emoji.name == "chess":
            role = discord.utils.get(guild.roles, name="Chess")

        elif payload.emoji.name == "warframe":
            role = discord.utils.get(guild.roles, name="Warframe")

        elif payload.emoji.name == "clashofclans":
            role = discord.utils.get(guild.roles, name="Clash of Clans")

        elif payload.emoji.name == "WorldofWarships":
            role = discord.utils.get(guild.roles, name="World of Warships")

        elif payload.emoji.name == "WarThunder":
            role = discord.utils.get(guild.roles, name="War Thunder")

        elif payload.emoji.name == "payday2":
            role = discord.utils.get(guild.roles, name="PayDay 2")

        elif payload.emoji.name == "RedDead":
            role = discord.utils.get(guild.roles, name="Red Dead Redemption")

        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role:
            member = payload.member
            if member:
                await member.add_roles(role)
                print("done")
            else:
                print("Member Not found.")
        else:
            print("Role not found.")

    elif message_id == 756039914549805116:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == "254millennialtalk":
            role = discord.utils.get(guild.roles, name="254 millennial fans")

        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role:
            member = payload.member
            if member:
                await member.add_roles(role)
                print("done")
            else:
                print("Member Not found.")
        else:
            print("Role not found.")

    elif message_id == 844992614084116480:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == "PC":
            role = discord.utils.get(guild.roles, name="PC")

        elif payload.emoji.name == "PS4":
            role = discord.utils.get(guild.roles, name="PS4")

        elif payload.emoji.name == "XBox":
            role = discord.utils.get(guild.roles, name="XBox")

        elif payload.emoji.name == "Mobile":
            role = discord.utils.get(guild.roles, name="Mobile")

        elif payload.emoji.name == "Nintendo":
            role = discord.utils.get(guild.roles, name="Nintendo")

        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role:
            member = guild.get_member(payload.user_id)
            # member = payload.member

            if member:
                await member.add_roles(role)
                print("done")
            else:
                print("Member Not found.")
        else:
            print("Role not found.")


@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 804285695404670986:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == "warzone":
            role = discord.utils.get(guild.roles, name="Warzone")

        elif payload.emoji.name == "apex":
            role = discord.utils.get(guild.roles, name="Apex Legends")

        elif payload.emoji.name == "civ6":
            role = discord.utils.get(guild.roles, name="Civilization 6")

        elif payload.emoji.name == "gta5":
            role = discord.utils.get(guild.roles, name="GTA 5")

        elif payload.emoji.name == "thedivision":
            role = discord.utils.get(guild.roles, name="The Division")

        elif payload.emoji.name == "amongus":
            role = discord.utils.get(guild.roles, name="Among Us")

        elif payload.emoji.name == "leagueoflegends":
            role = discord.utils.get(guild.roles, name="League of Legends")

        elif payload.emoji.name == "brawlhalla":
            role = discord.utils.get(guild.roles, name="Brawlhalla")

        elif payload.emoji.name == "nfspayback":
            role = discord.utils.get(guild.roles, name="NFS:Payback")

        elif payload.emoji.name == "pubglite":
            role = discord.utils.get(guild.roles, name="PUBG Lite")

        elif payload.emoji.name == "pubgmobile":
            role = discord.utils.get(guild.roles, name="PUBG Mobile")

        elif payload.emoji.name == "overwatch":
            role = discord.utils.get(guild.roles, name="Overwatch")

        elif payload.emoji.name == "codmobile":
            role = discord.utils.get(guild.roles, name="COD Mobile")

        elif payload.emoji.name == "genshin":
            role = discord.utils.get(guild.roles, name="Genshin Impact")

        elif payload.emoji.name == "thecrew":
            role = discord.utils.get(guild.roles, name="The Crew")

        elif payload.emoji.name == "valorant":
            role = discord.utils.get(guild.roles, name="Valorant")

        elif payload.emoji.name == "rainbowsix":
            role = discord.utils.get(guild.roles, name="Rainbow Six Siege")

        elif payload.emoji.name == "csgo":
            role = discord.utils.get(
                guild.roles, name="Counter Strike Global Offensive"
            )

        elif payload.emoji.name == "fifa":
            role = discord.utils.get(guild.roles, name="FIFA")

        elif payload.emoji.name == "starwars":
            role = discord.utils.get(guild.roles, name="Starwars Battlefront II")

        elif payload.emoji.name == "fortnite":
            role = discord.utils.get(guild.roles, name="Fortnite")

        elif payload.emoji.name == "eurotrack":
            role = discord.utils.get(guild.roles, name="EuroTruck Simulator 2")

        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role:
            member = guild.get_member(payload.user_id)
            # member = payload.member

            if member:
                await member.remove_roles(role)
                print("done")
            else:
                print("Member Not found.")
        else:
            print("Role not found.")

    elif message_id == 836847840503267368:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == "roblox":
            role = discord.utils.get(guild.roles, name="Roblox")

        elif payload.emoji.name == "fortnite":
            role = discord.utils.get(guild.roles, name="Fortnite")

        elif payload.emoji.name == "eurotruck":
            role = discord.utils.get(guild.roles, name="EuroTruck Simulator 2")

        elif payload.emoji.name == "destiny2":
            role = discord.utils.get(guild.roles, name="Destiny 2")

        elif payload.emoji.name == "minecraft":
            role = discord.utils.get(guild.roles, name="Minecraft")

        elif payload.emoji.name == "paladins":
            role = discord.utils.get(guild.roles, name="Paladins")

        elif payload.emoji.name == "chess":
            role = discord.utils.get(guild.roles, name="Chess")

        elif payload.emoji.name == "warframe":
            role = discord.utils.get(guild.roles, name="Warframe")

        elif payload.emoji.name == "clashofclans":
            role = discord.utils.get(guild.roles, name="Clash of Clans")

        elif payload.emoji.name == "WorldofWarships":
            role = discord.utils.get(guild.roles, name="World of Warships")

        elif payload.emoji.name == "WarThunder":
            role = discord.utils.get(guild.roles, name="War Thunder")

        elif payload.emoji.name == "payday2":
            role = discord.utils.get(guild.roles, name="PayDay 2")

        elif payload.emoji.name == "RedDead":
            role = discord.utils.get(guild.roles, name="Red Dead Redemption")
            
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role:
            member = guild.get_member(payload.user_id)
            # member = payload.member

            if member:
                await member.remove_roles(role)
                print("done")
            else:
                print("Member Not found.")
        else:
            print("Role not found.")

    elif message_id == 756039914549805116:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == "254millennialtalk":
            role = discord.utils.get(guild.roles, name="254 millennial fans")

        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role:
            member = guild.get_member(payload.user_id)
            # member = payload.member

            if member:
                await member.remove_roles(role)
                print("done")
            else:
                print("Member Not found.")
        else:
            print("Role not found.")

    elif message_id == 844992614084116480:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == "PC":
            role = discord.utils.get(guild.roles, name="PC")

        elif payload.emoji.name == "PS4":
            role = discord.utils.get(guild.roles, name="PS4")

        elif payload.emoji.name == "XBox":
            role = discord.utils.get(guild.roles, name="XBox")

        elif payload.emoji.name == "mobile":
            role = discord.utils.get(guild.roles, name="Mobile")

        elif payload.emoji.name == "Nintendo":
            role = discord.utils.get(guild.roles, name="Nintendo")

        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role:
            member = guild.get_member(payload.user_id)
            # member = payload.member

            if member:
                await member.remove_roles(role)
                print("done")
            else:
                print("Member Not found.")
        else:
            print("Role not found.")


dead_chat = [
    "dead chat",
    "ded chat",
    "chat dead",
    "dead server",
    "boring server",
]

images = [
    "https://media1.tenor.com/images/f7ad58f17084a81fde2da96ddaa94edd/tenor.gif?itemid=18146171",
    "https://media1.tenor.com/images/e2726f8433b913452d9a2f6768c49913/tenor.gif?itemid=4781301",
    "https://media1.tenor.com/images/55b71cfa4bb363418b3833eaf1ee477d/tenor.gif?itemid=4941248",
    "https://media1.tenor.com/images/939041d7709c44d052e4ddd1ca2f66a0/tenor.gif?itemid=13295259",
    "https://media1.tenor.com/images/1f1378bacd3e8cd1c51bf829f4c08f4d/tenor.gif?itemid=22075897",
    "https://media1.tenor.com/images/1771637ecbf5a19e226b951f3c133f42/tenor.gif?itemid=9304816",
]


@client.event
async def on_message(message):
    empty_array = []
    modmail_channel = discord.utils.get(
        client.get_all_channels(), name="👨-moderator-only"
    )

    if message.author == client.user:
        return
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("[" + message.author.display_name + "]")

            for file in files:
                await modmail_channel.send(file.url)

        else:
            await modmail_channel.send(
                "[" + message.author.mention + "] " + message.content
            )

    elif str(message.channel) == "👨-moderator-only" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("[" + message.author.mention + "]")

            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            await member_object.send("[" + message.author.mention + "]" + mod_message)

    elif str(message.content) in dead_chat:
        dead_chat_replies = [
            f"{message.author.mention}, Get a life Bruh",
            f"{message.author.mention}, Try uninstalling discord",
            f"{message.author.mention}, You can always leave you know",
            f"{message.author.mention}, Sorry Sire, how should we {(len(list(client.get_all_members()))) - 1 } members entertain you 😒",
            f"{message.author.mention}, You need Jesus",
            images,
        ]
        reply = random.choice(dead_chat_replies)
        if reply is images:
            embed = discord.Embed(title=message.author.display_name)
            embed.set_image(url=random.choice(reply))
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(reply)

    await client.process_commands(message)


# Who is Command
@client.command()
async def whois(ctx, member: discord.Member):
    embed = discord.Embed(
        title=member.name, description=member.mention, color=discord.Color.red()
    )
    embed.add_field(
        name="Name and Tag",
        value="{}#{}".format(member.name, member.discriminator),
        inline=True,
    )
    embed.add_field(name="User ID", value=member.id, inline=True)
    embed.add_field(
        name="Account Creation Date",
        value=local_datetime(member.created_at).strftime(
            "%A, %B %d %Y @ %H:%M:%S %p %Z"
        ),
        inline=False,
    )
    embed.add_field(
        name="Joined Server On",
        value=local_datetime(member.joined_at).strftime(
            "%A, %B %d %Y @ %H:%M:%S %p %Z"
        ),
        inline=False,
    )

    # import pdb; pdb.set_trace()
    # if member in ctx.author.friends:
    #   # print("{} is on my friends list!".format(member.name))
    #   embed.add_field(name = "Are you Friends?" , value = member.is_friend(), inline = True)

    all_activities = []
    spotify = None
    for activity in member.activities:
        activity_name = activity.name
        if "spotify" in activity_name.lower():
            spotify = activity
        all_activities.append(activity_name)
    activities = "\n".join(all_activities) if all_activities else None
    embed.add_field(name="Activities", value=activities, inline=True)

    if spotify:
        embed.add_field(
            name="Spotify", value=f"{spotify.artist} - {spotify.title}", inline=True
        )

    roles = sorted([role for role in member.roles], reverse=True)
    mentions = [str(role.mention) for role in roles]
    del roles
    embed.add_field(name="Top Role", value=member.top_role, inline=False)
    embed.add_field(name="Roles", value=" , ".join(mentions), inline=False)

    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(
        icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}"
    )

    await ctx.send(embed=embed)


player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winning_conditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

# TicTacToe Game


@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
            ":white_large_square:",
        ]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send(
            "A game is already in progress! Finish it before starting a new one."
        )


# placing No.s in the TicTacToe game
@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                check_winner(winning_conditions, mark)
                print(count)
                if gameOver:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send(
                    "Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile."
                )
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the #tictactoe command.")


# Check Winner
def check_winner(winning_conditions, mark):
    global gameOver
    for condition in winning_conditions:
        if (
            board[condition[0]] == mark
            and board[condition[1]] == mark
            and board[condition[2]] == mark
        ):
            gameOver = True


# Error Handling
@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send(
            "Please make sure to mention/ping players (ie. <@688534433879556134>)."
        )


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")


# Server info.


@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    member_count = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Info", description=description, color=discord.Color.red()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=False)
    embed.add_field(name="Member Count", value=member_count, inline=True)

    if ctx.guild.premium_subscribers:
        names = ctx.guild.premium_subscribers
        mentions = [str(name.mention) for name in names]
        del names
        embed.add_field(
            name="Current Server Boosters", value="\n".join(mentions), inline=False
        )

    embed.add_field(
        name="Server Creation Date",
        value=local_datetime(ctx.guild.created_at).strftime(
            "%A, %B %d %Y @ %H:%M:%S %p %Z"
        ),
        inline=False,
    )

    if ctx.guild.system_channel:
        embed.add_field(
            name="Standard Channel", value=f"#{ctx.guild.system_channel}", inline=True
        )
        embed.add_field(
            name="AFK Voice Timeout",
            value=f"{int(ctx.guild.afk_timeout / 60)} min",
            inline=True,
        )
        embed.add_field(name="Guild Shard", value=ctx.guild.shard_id, inline=True)

    embed.set_footer(text="Bot by iamksm")
    await ctx.send(embed=embed)


@client.command(aliases=["uptime", "up"])
async def status(ctx):
    """Info about the bot"""
    client.startTime = time.time()
    timeUp = time.time() - client.startTime
    hours = timeUp / 3600
    minutes = (timeUp / 60) % 60
    seconds = timeUp % 60

    client.commands_used = Counter()

    __version__ = "1.8.1"
    client.botVersion = __version__

    client.AppInfo = await client.application_info()
    admin = client.AppInfo.owner

    users = 0
    channel = 0
    if len(client.commands_used.items()):
        commandsChart = sorted(
            client.commands_used.items(), key=lambda t: t[1], reverse=False
        )
        topCommand = commandsChart.pop()
        commandsInfo = "{} (Top-Command: {} x {})".format(
            sum(client.commands_used.values()), topCommand[1], topCommand[0]
        )
    else:
        commandsInfo = str(sum(client.commands_used.values()))
    for guild in client.guilds:
        users += len(guild.members)
        channel += len(guild.channels)

    embed = discord.Embed(color=ctx.me.top_role.colour)
    embed.set_footer(text="Bot Created by iamksm#8749")
    embed.set_thumbnail(url=ctx.me.avatar_url)
    embed.add_field(name="Bot Admin", value=admin, inline=False)
    embed.add_field(
        name="Uptime",
        value="{0:.0f} Hours, {1:.0f} Minutes and {2:.0f} Seconds\n".format(
            hours, minutes, seconds
        ),
        inline=False,
    )
    embed.add_field(name="Observed users", value=users, inline=True)
    embed.add_field(name="Observed servers", value=len(client.guilds), inline=True)
    embed.add_field(name="Watched channel", value=channel, inline=True)
    embed.add_field(name="Commands executed", value=commandsInfo, inline=True)
    embed.add_field(name="Bot Version", value=client.botVersion, inline=True)
    embed.add_field(name="Discord.py Version", value=discord.__version__, inline=True)
    embed.add_field(name="Python Version", value=platform.python_version(), inline=True)

    embed.add_field(
        name="Operating system",
        value=f"{platform.system()} {platform.release()} {platform.version()}",
        inline=False,
    )
    await ctx.send("**:information_source:** Information about this bot:", embed=embed)


@client.command()
async def ping(ctx):
    """Measure the Response Time"""
    ping = ctx.message
    pong = await ctx.send("**:ping_pong:** Pong!")
    delta = pong.created_at - ping.created_at
    delta = int(delta.total_seconds() * 1000)
    await pong.edit(
        content=f":ping_pong: Pong! ({delta} ms)\n*Discord WebSocket latency: {round(client.latency, 5)} ms*"
    )
    time.sleep(1)


@client.command(aliases=["activities"])
async def games(ctx, *scope):
    """Shows which games are currently being played on the server"""
    games = Counter()
    for member in ctx.guild.members:
        for activity in member.activities:
            if not member.bot:
                if isinstance(activity, discord.Game):
                    games[str(activity)] += 1
                elif isinstance(activity, discord.Activity):
                    games[activity.name] += 1
    msg = ":chart: Games currently being played on this server\n"
    msg += "```js\n"
    msg += "{!s:40s}: {!s:>3s}\n".format("Name", "Number")
    chart = sorted(games.items(), key=lambda t: t[1], reverse=True)
    for index, (name, amount) in enumerate(chart):
        if len(msg) < 1950:
            msg += "{!s:40s}: {!s:>3s}\n".format(name, amount)
        else:
            amount = len(chart) - index
            msg += f"+ {amount} Others"
            break
    msg += "```"
    await ctx.send(msg)


keep_alive()
client.run(os.getenv("TOKEN"))
