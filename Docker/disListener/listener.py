import discord

listen = discord.Client()

listen_token = "LISENER_BOT_TOKEN_HERE"

# Dictionary to map source channels to their corresponding relay bot IDs. Channelyouwanttoforward: bot ID
channel_to_relay_bot = {
    0123456789011121314: 0123456789011121314,
    0123456789011121314: 0123456789011121314,
    0123456789011121314: 0123456789011121314,
    0123456789011121314: 0123456789011121314,
    0123456789011121314: 0123456789011121314,
    0123456789011121314: 0123456789011121314,
    0123456789011121314: 0123456789011121314,
    0123456789011121314: 0123456789011121314
}

@listen.event
async def on_ready():
    print(f'Listen bot logged in as {listen.user}!')
    print(f'Listen bot user ID: {listen.user.id}')  # Debug line

@listen.event
async def on_message(message):
    if message.author.bot:
        return

    source_channel_id = message.channel.id
    if source_channel_id not in channel_to_relay_bot:
        return  # Ignore messages from channels not in the mapping

    relay_bot_id = channel_to_relay_bot[source_channel_id]
    relay_bot = listen.get_user(relay_bot_id)

    if relay_bot:
        relay_channel = relay_bot.dm_channel
        if relay_channel:
            await relay_channel.send(f"**{message.author.name}**: {message.content}")
            print(f"Relayed message to relay bot: {message.content}")
        else:
            print(f"Relay channel not found for relay bot {relay_bot_id}")
    else:
        print(f"Relay bot not found: {relay_bot_id}")

    # Debug print statements
    print(f"Message Content: {message.content}")
    print(f"Message Channel ID: {message.channel.id}")
    print("Channel to Relay Bot Mapping:")
    for channel_id, relay_bot_id in channel_to_relay_bot.items():
        print(f"Channel ID: {channel_id} => Relay Bot ID: {relay_bot_id}")

print("Starting listen bot...")
listen.run(listen_token)
