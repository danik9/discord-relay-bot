import discord

intents = discord.Intents.default()
intents.dm_messages = True
intents.message_content = True

relay = discord.Client(intents=intents)

relay_token = "BOT_TOKEN_HERE"
channel_dupe_id = 0123456789011121314  # Replace with your duplicate channel ID
allowed_user_id = 0123456789011121314  # Replace with the allowed user's ID

@relay.event
async def on_ready():
    print(f'Relay bot logged in as {relay.user}!')
    print(f'Relay bot user ID: {relay.user.id}')  # Debug line

@relay.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore messages from other bots

    if isinstance(message.channel, discord.DMChannel) and message.author.id == allowed_user_id:
        relay_channel = relay.get_channel(channel_dupe_id)
        if relay_channel:
            content = message.content

            print(f"Received message: {content} from {message.author.name} in channel {message.channel.id}")
            print(f'Relaying message: {content}')
            await relay_channel.send(content)
        else:
            print("Relay channel not found")
    else:
        print("Ignoring unauthorized or non-DM message")

print("Starting relay bot...")
relay.run(relay_token)
