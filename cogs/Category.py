import discord
from discord.ext import commands
import asyncio
from discord import Embed
from EZPaginator import Paginator


class Category(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="카테고리")
    async def Category(self, ctx):
        embed = discord.Embed(
            title="KDD - 카테고리",
            description="KDD의 카테고리입니다. 이모지를 클릭하여 원하는 카테고리를 열어보세요.\n\n:pushpin: 기본적인 디스코드 팁\n📂 디스코드 서버 팁\n🖍 글자 강조하기\n📝 채팅 꾸미기\n🖌 글자 색깔 꾸미기\n⚒ 서버 꾸미기",
            colour=0x00FFFF,
            inline=False,
        )

        r = ["📌", "📂", "🖍", "📝", "🖌", "⚒"]
        m = await ctx.send(embed=embed)
        for i in r:
            await m.add_reaction(i)

        def checks(reaction, user):
            return user == ctx.author and str(reaction.emoji) in r

        try:
            reaction, user = await self.bot.wait_for(
                "reaction_add", timeout=60.0, check=checks
            )

            if str(reaction.emoji) == "📌":
                pageinfo = discord.Embed(
                    title="기본적인 디스코드 팁",
                    description="``이모지``로 페이지를 넘겨 정보를 확인해보세요.\n\n**1페이지**. 디스코드란 무엇인가\n\n**2페이지**. 키보드 콤보 - 디스코드 단축키\n\n**3페이지**. eon28이 소개한 봇\n\n**4페이지**. 디스코드 오류 해결법\n\n**5페이지**. 이모지, 이모티콘\n\n**6페이지**. 배지 badges\n\n**7페이지**. 프로필 꾸미기 rich presence\n\n**8페이지**. 디스코드 문의하기 \n\n**9페이지**. HypeSquad 배지 얻기",
                    color=0x00FFFF,
                    inline=False,
                    timestamp=ctx.message.created_at,
                )
                page1 = Embed(
                    title="디스코드란?",
                    description="디스코드란?\n디스코드는 게이머를 위한 메신저이다.\n\n#기본 정보\n\n개발자 - Discord lnc.\n발매 - 2015년 3월 "
                    "6일\n\n#특징\n● 뛰어난 성능과 무료 사용을 토대로 급부상하고 있는 메신저 프로그램\n● 한국에서는 주로 온라인 게임을 즐기는 "
                    "사람들이 많이 이용하는 편\n● 뛰어난 성능과 간편함\n● 단순한 보이스 채팅말고도 텍스트 채팅과 정보 공유, "
                    "관리 기능 등을 지원\n● 게임 내에서 자체적으로 보이스톡 시스템을 지원하더라도 Discord를 병용하거나 Discord만을 이용하는 "
                    "경우도 많은 "
                    "편",
                    color=0x00FFFF,
                    timestamp=ctx.message.created_at,
                )
                page1.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/655651598671937586"
                    "/655654221173227531/hgfhfhf.PNG"
                )
                page1.set_footer(text="1/9 페이지")

                page2 = Embed(
                    title="키보드 콤보 (디스코드 단축키)",
                    description="키보드 콤보 (디스코드 단축키) - 디스코드에서 사용할 수 있는 단축키 모음\n\nI.설명\n디스코드 프로그램에서 Ctrl+/를 동시에 누르면 키보드 콤보라는 작은 화면이 뜨게 됩니다.\n키보드 콤보는 디스코드 내에서 사용할 수 있는 단축키입니다.\n게임을 하거나 다른 작업, 디스코드 내에서 작업할 때도 편리하게 사용할 수 있겠죠?\nII. DDR 화살표 소리\nCtrl+/ (키보드 콤보)에서 상하좌우 화살표 키를 누르면 오른쪽 위의 DDR 화살표에 불이 들어오면서 소리가 난다\n\n\nIII. 이스터에그\nCtrl+/ (키보드 콤보)에서 HH -> NK 를 입력하면 순옥살이 나간다.\n\n참고영상\nhttps://www.youtube.com/watch?v=5ZvzS3aAXEA&app=desktop",
                    color=0x00FFFF,
                    timestamp=ctx.message.created_at,
                )
                page2.add_field(
                    name="이미지",
                    value="[키보드 콤보 목록](https://cdn.discordapp.com/attachments/649570312723234827/663283154848579585/dsffdsfdsfdsfdsfs.PNG) \n[상하좌우 키](https://cdn.discordapp.com/attachments/649570312723234827/663283217801019403/dsasddad.PNG)",
                )
                page2.set_footer(text="2/9 페이지")

                page3 = Embed(
                    title="Eon28(김만찬)이 소개한 봇",
                    description="[여기](https://blog.naver.com/PostList.nhn?blogId=alscks140&categoryNo=42&parentCategoryNo=42&skinType=&skinId=&from=menu)를 클릭하여 자세히 알아보세요.",
                    color=0x00FFFF,
                    timestamp=ctx.message.created_at,
                )
                page3.set_footer(text="3/9 페이지")

                page4 = Embed(
                    title="디스코드 오류 해결법",
                    description="1. 디스코드 알림음이 들리지 않습니다.\n> (정확하지는 않지만 해결이 되었던 방법) \n> 껐다 키면 해결이 됩니다.\n\n2. 화면 공유가 되지 않습니다.\n> 화면 공유를 하는 사람의 컴퓨터 운영체제가 \n> 윈도우 7이면 소리가 안들립니다.",
                    color=0x00FFFF,
                    timestamp=ctx.message.created_at,
                )
                page4.set_footer(text="4/9 페이지")

                page5 = Embed(
                    title="디스코드 이모지",
                    description="이모지, 이모티콘 - 다들 알고 있는 이모티콘이다.\n> I. 설명\n디스코드에서 사용하는 이모티콘이다.\n이모지라고도 불리고 이모티콘이라고도 불린다.\n\n> II. 사용방법\n채팅 입력칸 우측에 이모지 버튼이 있어 이모지를 전송할 수 있다.\n누르게 되면 사용할 수 있는 (글로벌) 이모지, 서버 이모지를 골라 사용할 수 있다.\n상단에 검색창도 있어 검색을 통해 빠르게 이모지/이모티콘을 사용할 수 있다.\n자신이 많이 사용하는 이모지/이모티콘이 있다면 :(이름): 형태로 이모티콘을 채팅을 통해 사용할 수 있다.\n추가로 이모지/이모티콘을 통해 채팅에 반응을 추가 할 수 있다.",
                    color=0x00FFFF,
                    timestamp=ctx.message.created_at,
                )
                page5.set_footer(text="5/9 페이지")
                pages = [pageinfo, page1, page2, page3, page4, page5]

                msg = await ctx.send(embed=pageinfo)

                page = Paginator(
                    bot=self.bot, message=msg, embeds=pages, use_extend=True, only=ctx.author
                )
                await page.start()

            if str(reaction.emoji) == "📂":
                await ctx.send(
                    "보고 싶은 항목의 번호를 입력하세요. (1번을 보고 싶다면 1 입력)\n\n1. 개발자 모드\n2. 디스코드 파트너 \n3. 공개 서버 기능\n4. 디스코드 웹후크"
                )

            if str(reaction.emoji) == "🖍":
                await ctx.send(
                    "보고 싶은 항목의 번호를 입력하세요. (1번을 보고 싶다면 1 입력)\n\n1. 기울기 \n2. 굵은 글씨\n3. 밑줄\n4. 취소선\n5. 마크다운 효과 제거\n6. 공백 만들기"
                )

            if str(reaction.emoji) == "📝":
                await ctx.send(
                    "보고 싶은 항목의 번호를 입력하세요. (1번을 보고 싶다면 1 입력)\n\n1. single_line_highlight\n2. multi_line_highlight\n3. code_block\n4. spoiler_tags\n5. single_line_block_quotes\n6. multi_line_block_quotes\n7. color embed"
                )

            if str(reaction.emoji) == "🖌":
                await ctx.send("글자 색깔 꾸미기")

            if str(reaction.emoji) == "⚒":
                await ctx.send("서버 꾸미기")

        except asyncio.TimeoutError:
            await ctx.send("시간이 초과되었습니다.\n시간 제한은 60초입니다.")


def setup(bot):
    bot.add_cog(Category(bot))
