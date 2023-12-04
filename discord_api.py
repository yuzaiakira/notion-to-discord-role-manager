import discord

from notion_api import get_user_data
from config import TEXT_CHANNEL_ID

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 

client = discord.Client(intents=intents)


async def update_discord_roles(member, notion_roles, channel, message):
    guild = message.guild
    roles_to_assign = []

    for role_name in notion_roles:  # Replace with actual role names
        role = discord.utils.get(guild.roles, name=role_name)
        if role:
            if guild.me.top_role < role:
                await channel.send(f"I do not have permission to assign that role! {role_name}")
            else:    
                roles_to_assign.append(role)
        else:
            await channel.send(f"The role '{role_name}' does not exist.")
    
    await member.edit(roles=roles_to_assign)
    await channel.send(f"Roles updated successfully for {member.name}")
    
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message: discord.message.Message):
    # block bot message
    if message.author.bot:
        return
    
    # Check if the message starts with a '!update_role' command and specific  text channel
    if message.content.startswith('!update_role') and message.channel.id == TEXT_CHANNEL_ID:
        channel = client.get_channel(TEXT_CHANNEL_ID)

        async for user_data in get_user_data():
            member = message.guild.get_member(user_data['user_id'])

            if member:
                try:
                    await update_discord_roles(member, user_data['roles'], channel, message)
                except Exception as e:
                    await channel.send(f"something went wrong while updating roles for '{member.name}'.")
            
                
            
                
               