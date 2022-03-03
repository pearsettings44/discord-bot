import discord

client = discord.Client()

@client.event
async def on_ready():
    # Let know when bot is online.
    print("Bot is now online and ready to serve!")

@client.event
async def on_message(message):
    # The bot is listening to any messages.

    # Prevents bot to respond to himself, avoiding an infitine loop.
    if message.author == client.user:
        return

    if message.content == "Anastacia?":
        await message.channel.send("Daddy?")
    
    if message.content == "omg":
        await message.channel.send("xd")
    
    if message.content == "I love you more" or message.content == "i love you more":
        await message.channel.send("thats a lie!")

client.run("TOKEN")