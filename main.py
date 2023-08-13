import os
import discord
from discord import app_commands
import sys
import json

secret = json.dump("./secret.json")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

"""on ready"""
@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")
client.run(secret)
