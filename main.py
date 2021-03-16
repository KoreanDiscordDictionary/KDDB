import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(command_prefix=['kdd ', 'KDD ', 'kdd', 'KDD'], help_command=None)

startup_extensions = ['cogs.Quiz']

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('불러오기에 실패 하였습니다. 에러 파일 : {}\n에러 내용 : {}'.format(extension,exc))

@bot.event
async def on_ready():
    print('Korean Discord Dictionary Bot On Ready.')

@bot.command(name = '리로드')
async def reload(ctx):
    for i in startup_extensions:
        bot.reload_extension(i)
    await ctx.send('리로드가 완료되었습니다.')
    

bot.run('Nzg4NjQ5MTAzNTcxNDE5MTY2.X9mktg.jPBPg2DmXSMSfg3fpRd_KRD8sM4')