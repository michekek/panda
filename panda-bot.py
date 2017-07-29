# panda bot
# ---------

# rewrite for a new bot

import discord
import asyncio
import emoji
import time

client = discord.Client()

# bot info
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

where_am_I = "Team 40"
why_am_I_so_sweaty = "It's probably hot where you are"
why_am_I_in_team40 = "Idk you clicked on the invite"


# ErisBot Commands
e1 = "`.music play [URL/Video Title]` - Plays a song." 
e2 = "`.music pause` - Pauses the current song."
e3 = "`.music volume [0 - 100]` - Changes the volume of the music. Requires Admin/DJ."
e4 = "`.music queue [Page number]` - View the music queue and select which page." 
e5 = "`.music skip [number]` - Vote to skip a song."
e6 = "`.music forceskip` - Force skip the song. Requires Admin/DJ." 
e7 = "`.music nowplaying` - View what's playing." 
e8 = "`.music stop` - Stops the player and completely resets everything. Requires Admin/DJ."

# Fredboat Commands:
f1 = "`;;play [url]` - Plays a song, given the url."
f2 = "`;;list` - Displays current songs in playlist."
f3 = "`;;nowplaying` - Shows the song currently playing."
f4 = "`;;skip` - Skips the current song."
f5 = "`;;pause` - Pauses the current song."
f6 = "`;;unpause` - Continues the song."
f7 = "`;;join` - Connects to the voice channel."
f8 = "`;;leave` - Disconnects the bot."
f9 = "`;;repeat` - Changes the repeat mode."
f10 = "`;;fwd [time]` - Forwards the track given a time amount."
f11 = "`;;rew [time]` - Rewinds the track given a time amount."
f12 = "`;;seek [time]` - Sets the track to the given time."
f13 = "`;;split` - Takes a youtube track and splits the track based on the tracklist."

# Panda Commands
p1 = "`!add` - Adds yourself to the queue."
p2 = "`!remove` - Removes yourself from the queue."
p3 = "`!now` - Displays the current performer."
p4 = "`!next` - Displays the next performer."
p5 = "`!queue` - Displays the queue of performers."
p6 = "`!position` - Displays your position."
p7 = "`!clear` - Clears the queue. Requires the role `Admin`, `Moderator` or `DJ` to be used."
p8 = "Use this bot to queue yourself up in order to perform. Respect the order of the queue, and do not deliberately attempt to sabotage performances or you will be restricted from using this text channel and its associated voice channel."

# Vexera Commands
v1 = "`+join` - Connects to the voice channel."
v2 = "`+disconnect` - Disconnects the bot."
v3 = "`+np` - Displays the song currently playing."
v4 = "`+pause` - Pauses the current song."
v5 = "`+play [URL/Video Title]` - Plays a song."
v6 = "`+queue` - Shows the music queue."
v7 = "`+resume` - Continues the paused song."
v8 = "`+search` - Displays a search menu for a song."
v9 = "`+shuffle` - Shuffles the queue."
v10 = "`+skip` - Skips the current song."

AUTHORIZED_CHANNELS = ["316630583490904064", #bots-general
                       "332700371556368384", #bots-testing
                       "316644942078410753" #chat-room
]

# allow only one colour role at a time
@client.event
async def on_message(message):
    if message.channel.id in AUTHORIZED_CHANNELS:
        if message.content.startswith("!colour"):
            msg = message.content.split()
            user_roles = message.author.roles
            team40 = client.get_server(id = "316584649453469698")
            if len(msg) != 2:
                return
            elif msg[1] == "remove":
                for role in user_roles:
                    if role.name.startswith("Colour"):
                        await client.delete_role(team40, role)
                bot_msg = await client.send_message(message.channel, emoji.emojize(":ok_hand:"))
                time.sleep(2)
                await client.delete_message(bot_msg)
            else:
                user_role_names = []
                for role in user_roles:
                    if role.name.startswith("Colour"):
                        await client.send_message(message.channel, "{}, please use `!colour remove` to remove your current colour before adding a new one!".format(message.author.mention))
                        return
                
                placeholder = discord.utils.get(team40.roles, name = "Placeholder role")
                hex_code = msg[1]
                int_colour = int(hex_code, 16)
                new_role = await client.create_role(team40, name = "Colour {}".format(hex_code), colour = discord.Colour(int_colour))
                await client.move_role(team40, new_role, placeholder.position)
                await client.add_roles(message.author, new_role)
                bot_msg = await client.send_message(message.channel, emoji.emojize(":ok_hand:"))
                time.sleep(2)
                await client.delete_message(bot_msg)
                
        elif message.content.startswith("!help"):
            msg = message.content.split()
            if len(msg) == 1:
                await client.send_message(message.channel, "what do you need help with")
            elif msg[1] == "colour" or msg[1] == "colours":
                embed = discord.Embed(description = "", colour = 0x7bb3ff)
                embed.add_field(name = "!colour [hex code]", value = "Gives you a coloured role, provided the hex code is valid", inline = False)
                embed.add_field(name = "!colour remove", value = "Removes the coloured role", inline = False)
                await client.send_message(message.channel, embed = embed)
            elif msg[1] == "color" or msg[1] == "colors":
                await client.send_message(message.channel, "pls spell colour correctly ty")
            else:
                await client.send_message(message.channel, "sry I can't help you with that")

        # panda embed message
#        elif message.content.startswith("fuck"):
#            await client.delete_message(message)
#            embed = discord.Embed(description = "", colour = 0xD37BD6)
#            embed.add_field(name = "Where am I?", value = where_am_I, inline = False)
#            embed.add_field(name = "Why am I so sweaty?", value = why_am_I_so_sweaty, inline = False)
#            embed.add_field(name = "Why am I in team 40?", value = why_am_I_in_team40, inline = False)

#            await client.send_message(message.channel, embed=embed)
    
      
client.run('MzA4NDQ1MjE4MjQ2NjIzMjM0.C-jwew.oSri0Hspnm53oo5Rnuo3Tlz6uWw') # panda token
