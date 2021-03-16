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
                await ctx.send('보고 싶은 항목의 번호를 입력하세요. (1번을 보고 싶다면 1 입력)\n\n1. 디스코드란 무엇인가\n2. 키보드 콤보 - 디스코드 단축키\n3. eon28이 소개한 봇\n4. 디스코드 오류 해결법\n5. 이모지, 이모티콘\n6. 배지 badges\n7. 프로필 꾸미기 rich presence\n8. 디스코드 문의하기 \n9. HypeSquad 배지 얻기')

            if str(reaction.emoji) == '📂':
                await ctx.send('보고 싶은 항목의 번호를 입력하세요. (1번을 보고 싶다면 1 입력)\n\n1. 개발자 모드\n2. 디스코드 파트너 \n3. 공개 서버 기능\n4. 디스코드 웹후크')

            if str(reaction.emoji) == '🖍':
                await ctx.send('보고 싶은 항목의 번호를 입력하세요. (1번을 보고 싶다면 1 입력)\n\n1. 기울기 \n2. 굵은 글씨\n3. 밑줄\n4. 취소선\n5. 마크다운 효과 제거\n6. 공백 만들기')
            
            if str(reaction.emoji) == '📝':
                await ctx.send('보고 싶은 항목의 번호를 입력하세요. (1번을 보고 싶다면 1 입력)\n\n1. single_line_highlight\n2. multi_line_highlight\n3. code_block\n4. spoiler_tags\n5. single_line_block_quotes\n6. multi_line_block_quotes\n7. color embed')
            
            if str(reaction.emoji) == '🖌':
                await ctx.send('글자 색깔 꾸미기')
            
            if str(reaction.emoji) == '⚒':
                await ctx.send('서버 꾸미기')
            
        except asyncio.TimeoutError:
            await ctx.send('시간이 초과되었습니다.\n시간 제한은 60초입니다.')
    
def setup(bot):
    bot.add_cog(Category(bot))