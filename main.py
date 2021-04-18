import discord
import asyncio
import jishaku
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(
    command_prefix=["kdd ", "KDD ", "kdd", "KDD"],
    help_command=None,
    intents=discord.Intents.all(),
)

startup_extensions = ["jishaku", "cogs.Quiz", "cogs.Category"]

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            print(f"{extension}를 불러왔습니다.")
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print(f"불러오기에 실패 하였습니다. 에러 파일 : {extension}\n에러 내용 : {exc}")


@bot.event
async def on_ready():
    print(f"{bot.user.name} On Ready.")


@bot.command(name="리로드")
async def reload(ctx):
    for i in startup_extensions:
        bot.reload_extension(i)
    await ctx.send("리로드가 완료되었습니다.")


bot.run("ODMzMTc1OTQyMDgzMTE3MDc2.YHuhkA.g0ZwduEmno5un67PP_UF8wO1MXU")  # KDDB 봇
