import discord, dotenv, os
import database
from discord.ext import commands
dotenv.load_dotenv()


TOKEN = os.getenv("TOKEN")

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("Ready to like them cuts.")


@client.command(name="likecut", aliases=["cut", "like"])
async def likeCut(ctx, user: discord.Member):
    if ctx.author.id == user.id:
        await ctx.send(user.mention + ", You can't like your own cut!")
    else:
        if database.addLike(user.id) is None:
            database.addUser(user.id)
        await ctx.send(f"{ctx.author.mention} liked {user.mention}'s cut.")
        



client.run(TOKEN)