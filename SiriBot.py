import discord  #importing discord code software
import os
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
#import webrtcvad #importing voice recognition software
#import json #import json module to convert python into json string
#import random #imports random library for shuffling and other reasons

client = discord.Client()
#vad = webrtcvad.Vad(2) #creating VAD object and setting aggressive level of voice recognition (higher the number, picks up more?)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))  #signals that bot is on_ready

client = commands.Bot(command_prefix="$")

@client.command(pass_context = True)
async def join(ctx):  #function makes the bot join the voice channel
   if(ctx.author.voice):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("What's up you dumb whores")
   else:
    await ctx.send("Your dumbass ain't in a voice channel betch!")


@client.command(pass_context = True)
async def leave(ctx):  #function makes the bot disconnect from the voice channel
    await ctx.voice_client.disconnect()
    await ctx.send("I'm out this hoe you dumb shit")

client.run(os.getenv('TOKEN'))  #makes bot go online
