import discord

intents = discord.Intents.default()
intents.dm_messages = True
intents.message_content = True

relay = discord.Client(intents=intents)

relay_token = "BOT_TOKEN_HERE"
channel_dupe_id = 0123456789011121314  # Replace with your duplicate channel ID

@relay.event
async def on_ready():
    print(f'Relay bot logged in as {relay.user}!')
    print(f'Relay bot user ID: {relay.user.id}')  # Debug line

@relay.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore messages from other bots

    relay_channel = relay.get_channel(channel_dupe_id)
    if relay_channel:
        formatted_name = f'**{message.author.name}**'
        content = message.content

        print(f"Received message: {content} from {formatted_name} in channel {message.channel.id}")
        print(f'Relaying message: {content}')
        await relay_channel.send(content)
    else:
        print("Relay channel not found")

print("Starting relay bot...")
relay.run(relay_token)
