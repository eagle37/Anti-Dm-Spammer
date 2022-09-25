"""Made by Eagle[.]#0831 Don't you dare skid this"""
import discord
from discord.ext import commands
client = commands.Bot(command_prefix="$", self_bot=True, intents=discord.Intents.all())
token = input("Enter Your Account Token => ")
cd = commands.CooldownMapping.from_cooldown(5, 6, commands.BucketType.user)


@client.event
async def on_message(message):
  if not message.guild:
    bucket = cd.get_bucket(message)
    retry = bucket.update_rate_limit()
    if retry:
      await message.channel.send("Blocking you for spamming | Made By Eagle[.]#0831")
      await message.author.block()
      print("Blocked", message.author, "For spamming Dms")
client.run(token, bot=False)
