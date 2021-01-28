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
        if database.userInfo(user.id) is None:
            database.addUser(user.id)
            await ctx.send(f"{ctx.author.mention} liked {user.mention}'s cut. They got their first like!")
        else:
            database.addLike(user.id)
            likes = str(database.userInfo(user.id))
            clean = likes.replace("(", "").replace(")", "").replace("'", "").replace(",", "")
            await ctx.send(f"{ctx.author.mention} liked {user.mention}'s cut. They now have {clean} likes.")



client.run(TOKEN)