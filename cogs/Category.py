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

        def checks(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['📌', '📂', '🖍', '📝', '🖌', '⚒']
        
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=checks)

            if str(reaction.emoji) == '📌':
                await ctx.send('보고 싶은 항목의 번호를 입력하세요. (1번을 보고 싶다면 1 입력)\n\n1. 디스코드란 무엇인가\n2. 키보드 콤보 - 디스코드 단축키\n3. eon28이 소개한 봇\n4. 디스코드 오류 해결법\n5. 이모지, 이모티콘\n6. 배지 badges\n7. 프로필 꾸미기 rich presence\n8. 디스코드 문의하기 \n9. HypeSquad 배지 얻기')
                desc = await self.bot.wait_for("message", check=check)
                desc = desc.content

                if desc == 1 or '1':
                    await ctx.send('디스코드란?\n디스코드는 게이머를 위한 메신저이다.\n\n#기본 정보\n\n개발자 - Discord lnc.\n발매 - 2015년 3월 6일\n\n#특징\n● 뛰어난 성능과 무료 사용을 토대로 급부상하고 있는 메신저 프로그램\n● 한국에서는 주로 온라인 게임을 즐기는 사람들이 많이 이용하는 편\n● 뛰어난 성능과 간편함\n● 단순한 보이스 채팅말고도 텍스트 채팅과 정보 공유, 관리 기능 등을 지원\n● 게임 내에서 자체적으로 보이스톡 시스템을 지원하더라도 Discord를 병용하거나 Discord만을 이용하는 경우도 많은 편.\nhttps://cdn.discordapp.com/attachments/655651598671937586/655654221173227531/hgfhfhf.PNG')
                
                if desc == 1 or '2':
                    await ctx.send('키보드 콤보 (디스코드 단축키) - 디스코드에서 사용할 수 있는 단축키 모음\n\nI.설명\n디스코드 프로그램에서 Ctrl+/를 동시에 누르면 키보드 콤보라는 작은 화면이 뜨게 됩니다.\n키보드 콤보는 디스코드 내에서 사용할 수 있는 단축키입니다.\n게임을 하거나 다른 작업, 디스코드 내에서 작업할 때도 편리하게 사용할 수 있겠죠?\nhttps://cdn.discordapp.com/attachments/649570312723234827/663283154848579585/dsffdsfdsfdsfdsfs.PNG\n\nII. DDR 화살표 소리\nCtrl+/ (키보드 콤보)에서 상하좌우 화살표 키를 누르면 오른쪽 위의 DDR 화살표에 불이 들어오면서 소리가 난다\nhttps://cdn.discordapp.com/attachments/649570312723234827/663283217801019403/dsasddad.PNG\n\nIII. 이스터에그\nCtrl+/ (키보드 콤보)에서 HH -> NK 를 입력하면 순옥살이 나간다.\n\n참고영상\nhttps://www.youtube.com/watch?v=5ZvzS3aAXEA&app=desktop')


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