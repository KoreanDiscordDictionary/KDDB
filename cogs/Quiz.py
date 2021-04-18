import discord
from discord.ext import commands
from pymongo import MongoClient
import random
import string

coll = MongoClient("mongodb://localhost:27017/").KDDB.quiz
c = MongoClient("mongodb://localhost:27017/").KDDB.user


class Quiz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.coll = coll
        self.c = c

    @commands.group(name="퀴즈")
    async def quiz(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                title="KDDB - 퀴즈 도움말",
                description="`KDD 퀴즈 출제 <퀴즈 제목>` - 퀴즈를 출제합니다.\n`KDD 퀴즈 삭제` - 자신이 등록한 퀴즈를 삭제합니다.\n`KDD 퀴즈 목록` - 퀴즈 목록을 보고 퀴즈를 풀 수 있습니다.\n",
                color=0x7289DA,
            )
            await ctx.send(embed=embed)

    @quiz.command(name="출제")
    async def Questions_quiz(self, ctx, *, title=None):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        if title == None:
            await ctx.send("퀴즈 출제 명령어의 올바른 사용법은 `KDD 퀴즈 출제 <퀴즈 제목>`입니다.")
        else:

            leng = 10
            string_pool = string.ascii_letters
            result = ""
            for i in range(leng):
                result += random.choice(string_pool)
            ranom = random.randint(1, 1000)
            await ctx.send(f"{title} 퀴즈의 설명은 무엇인가요?\n자세한 설명을 적어주세요.\n**줄바꿈 금지**")
            desc = await self.bot.wait_for("message", check=check)
            des = desc.content

            des = des.rstrip()

            await ctx.send("선택지는 몇개인가요? (1개이면 1을 입력, 2개이면 2를 입력)")
            num = await self.bot.wait_for("message", check=check)
            num = num.content

            await ctx.send("정답은 몇 번인가요?")
            answer = await self.bot.wait_for("message", check=check)
            answer = answer.content
            ranom = str(ranom)
            self.coll.insert_one(
                {
                    "_id": str(result + ranom),
                    "title": str(title),
                    "des": str(des),
                    "num": int(num),
                    "answer": int(answer),
                }
            )
            await ctx.send(f"퀴즈 등록을 완료했습니다.\n등록하신 퀴즈의 아이디는 `{result + ranom}`입니다.")

    @quiz.command(name="목록")
    async def quiz_que(self, ctx):
        i = 1
        embed = discord.Embed(
            title="퀴즈 목록", description=" ", color=0x7289DA, inline=False
        )
        for i in self.coll.find({}):
            idd = i["_id"]
            title = i["title"]
            des = i["des"]
            num = i["num"]
            embed.add_field(
                name=f"{title}", value=f"퀴즈 아이디 : {idd}\n\n퀴즈 설명 : {des}\n선택지 : {num}"
            )
        await ctx.send(embed=embed)

    @quiz.command(name="풀기")
    async def solve_quiz(self, ctx, *, quizid: str):
        if self.coll.find_one({"_id": str(quizid)}):
            i = self.coll.find_one({"_id": str(quizid)})

            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

            idd = i["_id"]
            title = i["title"]
            des = i["des"]
            num = i["num"]
            n = ""
            n += str(num) + ","
            for i in range(num - 1):
                n += str(int(num - 1)) + ","
            n = n[:-1]

            embed = discord.Embed(
                title=f"{title}",
                description=f"퀴즈 아이디 : {idd}\n\n퀴즈 설명 : {des}\n선택지 : {n}",
                color=0x7289DA,
                inline=False,
            )
            await ctx.send(embed=embed)
            await ctx.send("정답은 몇 번일까요?")

            answer = await self.bot.wait_for("message", check=check)
            answers = answer.content

            if i["answer"] == answers:
                await ctx.send("퀴즈를 맞추셨습니다. 축하드립니다.")
                if self.c.find_one({"_id": str(ctx.author.id)}):
                    find = {"_id": str(ctx.author.id)}
                    setdata = {"$inc": {"right": 1}}
                    self.c.update_one(find, setdata)
            else:
                await ctx.send("정답이 아닙니다. :cry:")
        else:
            await ctx.send("해당 아이디를 가진 퀴즈가 존재하지 않습니다.")


def setup(bot):
    bot.add_cog(Quiz(bot))
