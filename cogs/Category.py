import discord
from discord.ext import commands
import asyncio

class Category(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '카테고리')
    async def Category(self, ctx):
        embed = discord.Embed(title = 'KDD - 카테고리', description = 'KDD의 카테고리입니다. 이모지를 클릭하여 원하는 카테고리를 열어보세요.\n\n:pushpin: 기본적인 디스코드 팁\n📂 디스코드 서버 팁\n🖍 글자 강조하기\n📝 채팅 꾸미기\n🖌 글자 색깔 꾸미기\n⚒ 서버 꾸미기', colour = 0x00FFFF, inline=False)
        
        m = await ctx.send(embed=embed)
        await m.add_reaction('📌')
        await m.add_reaction('📂')
        await m.add_reaction('🖍')
        await m.add_reaction('📝')
        await m.add_reaction('🖌')
        await m.add_reaction('⚒')

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['📌', '📂', '🖍', '📝', '🖌', '⚒']

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

            if str(reaction.emoji) == '📌':
                await ctx.send('기본적인 디스코드 팁')

            if str(reaction.emoji) == '📂':
                await ctx.send('디스코드 서버 팁')

            if str(reaction.emoji) == '🖍':
                await ctx.send('글자 강조하기')
            
            if str(reaction.emoji) == '📝':
                await ctx.send('채팅 꾸미기')
            
            if str(reaction.emoji) == '🖌':
                await ctx.send('글자 색깔 꾸미기')
            
            if str(reaction.emoji) == '⚒':
                await ctx.send('서버 꾸미기')
            
        except asyncio.TimeoutError:
            await ctx.send('시간이 초과되었습니다.\n시간 제한은 60초입니다.')
    
def setup(bot):
    bot.add_cog(Category(bot))