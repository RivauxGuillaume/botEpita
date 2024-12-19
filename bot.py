from discord import app_commands, Intents, Client

TOKEN = "MTMxOTI4MjU2OTAxNTIwMTg5NA.GK-W0n.giKff4Giiv6JrdtmKOEdvzEJ0iZzY7uH91yi04"

intents = Intents.default()
client = Client(intents = intents)
intents.message_content = True
tree = app_commands.CommandTree(client)

@client.event
async def on_message(message):
    print(message.content)
    if message.content == 'ping':
        await message.channel.send('pong')


@client.event
async def on_ready():
    print(str(client.user) + " : message")
    await tree.sync()


@tree.command(name = "plus", description = "simple addition")
async def addition_cmd(ctx,a:int,b:int):
    await ctx.response.send_message(f"The calculation result is:\n{a+b}" )

client.run(TOKEN)

