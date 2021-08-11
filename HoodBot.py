from inspect import getmembers
import discord
import asyncio
import modulefinder
from operator import add, ipow
import os
import time


from discord.utils import get
from discord.ext import commands
from discord import channel, message
from discord import *
from discord.ext.commands.core import *
from discord.raw_models import *
from discord.user import ClientUser
from discord.role import *
from discord import *
from discord.message import *


# TOKEN
token = 'ODc0NTgwNDcxMzc4NDk3NTY2.YRJCiQ.kMbKr9ElaZ8ZLy5HMVFpt6BnTZ0'

# clear the terminal


def cls():
    os.system("cls")


cls()

# id's
# Client (My bot)
bot = commands.Bot(command_prefix=".")

# on start type "Bot is on"


@bot.event
async def on_ready():
    print("> Bot in on .imcool :)")

# start ~~~~~~~~~~~~~~~~~~~~~

# .boost command send "תנו בוסט לשרת"


@bot.command()
async def boost(ctx):
    await ctx.send("תנו בוסט לשרת")

# .clear <number-of-massages-to-clear> command


@bot.command(pass_context=True)
async def clear(ctx, limit: int = None):
    passed = 0
    failed = 0
    limit += 1
    async for msg in ctx.message.channel.history(limit=limit):
        if 1 > 0:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1
    cls()
    print(f"[Complete] Removed {passed} messages with {failed} fails")

# slap command [On beta]


@bot.command()
async def slap(ctx, member: discord.Member, *, reason='no reason'):
    await ctx.send('{} just got slapped for {}'.format(member, reason))

# addrole


@bot.command()
@has_role("A+")
async def addrole(ctx, member: discord.Member, role2):
    role = discord.utils.get(ctx.guild.roles, name=role2)
    try:
        await member.add_roles(role)
        await ctx.send(f"""The command was successful add the role {role} was added""")
    except:
        await ctx.send(f"""Sorry the command failed to add the role {role}""")
        await ctx.send("If you don't know what the fuck r you doing type .addrole_h")

# mute [only gives the role mute does not removes the roles, does not removes the role mute after a time]


@bot.command(pass_context=True)
@commands.has_role('A+')
async def mute(ctx, member: discord.Member, timelong):
    role = get(ctx.guild.roles, name='member')
    await member.remove_roles(member, role)
    mute = discord.utils.get(ctx.guild.roles, name="🔇-Muted-🔇")
    await member.add_roles(mute)
    await bot.say("{} has been muted from chat".format(member.name))
    time.wait(timelong)
    await member.add_roles(role)

# mute 2 [beta]


@bot.command(pass_context=True)
@commands.has_role('A+')
async def mute2(ctx, member: discord.Member, timelong):
    role = get(ctx.guild.roles, name='member')
    await member.remove_roles(member, role)
    mute = discord.utils.get(ctx.guild.roles, name="🔇-Muted-🔇")
    await member.add_roles(mute)
    await bot.say("{} has been muted from chat".format(member.name))
    time.wait(timelong)
    await member.add_roles(role)


@bot.command()
@has_permissions(ban_members=True, kick_members=True)
async def addrole_h(ctx):
    await ctx.send(".addrole @who_to_add_to the-role then the role but be careful write it with out a @ just the name for example @Test X Test V")

# I'm cool yes i know


@bot.command()
async def imcool(ctx):
    await ctx.send("Ziki is cool")
    while True:
        role = discord.utils.get(ctx.guild.roles, name="🔧-Main Developer-🔧")
        await role.edit(color=0xf16f6f, reason="red")
        await asyncio.sleep(3)
        await role.edit(color=0x6f76f1, reason="blue")
        await asyncio.sleep(3)
        await role.edit(color=0xf1e86f, reason="yellow")
        await asyncio.sleep(3)
        await role.edit(color=0x9f6ff1, reason="purple")
        await asyncio.sleep(3)
        await role.edit(color=0x6ff17e, reason="green")
        await asyncio.sleep(3)
        await role.edit(color=0x6feff1, reason="cyan")
        await asyncio.sleep(3)


# end ~~~~~~~~~~~~~~~~~~~~~~~
# Run the bot on the server.
try:
    bot.run(token)
except:
    print("> Bot is off and dailed to lunch.")
