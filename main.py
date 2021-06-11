import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Fuck You!')

    if message.content.startswith('$bhanu'):
        await message.channel.send('Handsome as Fuck')

    if message.content.startswith('$pk'):
        await message.channel.send('Tidhee I sus')


    

client.run('ODM4ODU0NDE1Nzk2NDA0MjI2.YJBKDQ.-WSrcNx8qwNtR0e7B4Ig9CVsjv0')