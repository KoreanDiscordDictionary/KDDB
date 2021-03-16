import discord
from discord.ext import commands
from pymongo import MongoClient
import random
import string

coll = MongoClient('mongodb://localhost:27017/').KDDB.quiz

class Quiz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.coll = coll

    @commands.group(name = '퀴즈')
    async def quiz(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title = 'KDDB - 퀴즈 도움말', description = '`KDD 퀴즈 출제 <퀴즈 제목>` - 퀴즈를 출제합니다.\n`KDD 퀴즈 삭제` - 자신이 등록한 퀴즈를 삭제합니다.\n`KDD 퀴즈 목록` - 퀴즈 목록을 보고 퀴즈를 풀 수 있습니다.\n', color = 0x7289DA)
            await ctx.send(embed=embed)
    
    @quiz.command(name = '출제')
    async def Appearance_quiz(self, ctx, *, title=None):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        if title == None:
            await ctx.send('퀴즈 출제 명령어의 올바른 사용법은 `KDD 퀴즈 출제 <퀴즈 제목>`입니다.')
        else:
            
            leng = 10
            string_pool = string.ascii_letters
            result = ""
            for i in range(leng):
                result += random.choice(string_pool)
            ranom = random.randint(1, 1000)
            await ctx.send(f"{title} 퀴즈의 설명은 무엇인가요?")
            desc = await self.bot.wait_for("message", check=check)
            des = desc.content

            des = des.rstrip()

            await ctx.send('선택지는 몇개인가요? (1개이면 1을 입력, 2개이면 2를 입력)')
            num = await self.bot.wait_for("message", check=check)
            num = num.content

            await ctx.send('정답은 몇 번인가요?')
            answer = await self.bot.wait_for("message", check=check)
            answer = answer.content
            ranom = str(ranom)
            self.coll.insert_one({
                "_id": str(result + ranom),
                "title": str(title),
                "des": str(des),
                "num": int(num),
                "answer": int(answer)
            })
            await ctx.send(f'퀴즈 등록을 완료했습니다.\n등록하신 퀴즈의 아이디는 `{result + ranom}`입니다.')
                
           

def setup(bot):
    bot.add_cog(Quiz(bot))