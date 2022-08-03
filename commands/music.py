import asyncio
import json, os

from main import discord, commands, bot, tasks
from discord.ext import commands
from pytube import YouTube
from youtubesearchpython import VideosSearch


queuelist = []
filestodelete = []

class PlayMusic(commands.Cog):

    def _init_(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_role("DJ")
    async def join(self, context):
        channel = context.author.voice.channel
        await channel.connect()
    
    @commands.command()
    @commands.has_role("DJ")
    async def leave( self, context):
        await context.voice_client.disconnect()
    
    @commands.command()
    @commands.has_role("DJ")
    async def pause(self, context):
        voice = context.voice_client
        if voice.is_playing() == True:
            voice.pause()
        else:
            await context.send("Bot is not playing Audio!")

    @commands.command()
    @commands.has_role("DJ")
    async def resume(self, context):
        voice = context.voice_client
        if voice.is_playing() == True:
            await context.send("Bot is playing Audio!")
        else:
            voice.resume()
    
    @commands.command(aliases = ["skip"])
    @commands.has_role("DJ")
    async def stop(self, context):
        voice = context.voice_client
        if voice.is_playing() == True:
            voice.stop()
        else:
            await context.send("Bot is not playing Audio!")

    
    @commands.command()
    @commands.has_role("DJ")
    async def clear(self, context):
        voice = context.voice_client
        for file in queuelist:
            os.remove(f"{file}.mp4")
        queuelist.clear()

        for file in filestodelete:
            os.remove(f"{file}.mp4")
        filestodelete.clear()
    
    @tasks.loop(minutes = 120)
    async def clear_loop(self, context):
    
        for file in queuelist:
            os.remove(f"{file}.mp4")
        queuelist.clear()

        for file in filestodelete:
            os.remove(f"{file}.mp4")
        filestodelete.clear()

        print("Cleared the queue")

    
    @commands.command()
    @commands.has_role("Owner")
    async def clear_loop_start(self, context):
        self.clear_loop.start(context)

    @commands.command()
    @commands.has_role("Owner")
    async def clear_loop_stop(self, context):
        self.clear_loop.stop()

    @commands.command()
    async def viewqueue(self, context):
        await context.send(f"Queue: ** {str(queuelist)} **")

    @commands.command()
    @commands.has_role("DJ")
    async def play(self, context, *, searchword):
        ydl_opts = {}
        voice = context.voice_client

        #Get the Title
        if searchword[0:4] == "http" or searchword[0:3] == "www":
            yt = YouTube(searchword)


        elif searchword[0:4] != "http" or searchword[0:3] != "www":
            videosSearch = VideosSearch(searchword, limit= 1)
            json_formatted_str = json.dumps(videosSearch.result(), indent=3) #dumps turns the python object into a json formatted string
            videoInfo = json.loads(json_formatted_str) #loads turns out json formatted string into a python dictionary where we can retrieve our data

            videoLink = videoInfo["result"] [0] ["link"]

            yt = YouTube(videoLink)

        title = yt.title                            # type: ignore
        yt = yt.streams.get_highest_resolution()    # type: ignore
        def download(yt):
            yt.download()
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, download, yt)
        
        #Playing and Queueing Audio
        if voice.is_playing():
            queuelist.append(title)
            await context.send(f"Added to Queue: ** {title} **")
        else:
            voice.play(discord.FFmpegPCMAudio(f"{title}.mp4"), after = lambda e : check_queue())
            await context.send(f"Playing ** {title} ** :musical_note:")
            filestodelete.append(title)
            await bot.change_presence(activity=discord.Activity(type = discord.ActivityType.listening, name = title))
        
        def check_queue():
            try:
                if queuelist[0] != None:
                    voice.play(discord.FFmpegPCMAudio(f"{queuelist[0]}.mp4"), after = lambda e : check_queue())
                    coro = bot.change_presence(activity=discord.Activity(type = discord.ActivityType.listening, name = queuelist[0]))
                    fut = asyncio.run_coroutine_threadsafe(coro, bot.loop)
                    fut.result()
                    filestodelete.append(queuelist[0])
                    queuelist.pop(0)
            except IndexError:
                for file in filestodelete:
                    os.remove(f"{file}.mp4")
                filestodelete.clear()

def setup(bot):
    bot.add_cog(PlayMusic(bot))