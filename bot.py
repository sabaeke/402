토큰 = ""
c = 0
channel = 804986227329466378 
channel_promote = 811899414452633600 #804986242432237598 #홍보 채널 아이디
admin_user = [763246275902308352,806432617671032842,763246275902308352]#제론, 플레
욕설 = '씨발','시발','병신','ㅂㅅ','ㅆㅂ','ㅅㅂ','새끼','ㅅㄲ','지랄','ㅈㄹ','ㅄ','애미'
검열 = '씨발','시발','병신','ㅂㅅ','ㅆㅂ','ㅅㅂ','새끼','ㅅㄲ','지랄','ㅈㄹ','ㅄ','섹스','보지','자지','신음','ㅅㅅ','애미','https://discord.gg/'
섹드립 = '섹스','보지','자지','신음','ㅅㅅ'
join_count = 0
max_count = 5
join_time = 10
delete_count = 0
max_delete = 5
ban_count = 0
max_ban = 5
_time = 10
일반 = """• 도움 - 봇의 명령어를 보여준다
• 링크 - 건강랜드와 봇 공식서버 링크를 보여준다
• 초대 - 봇의 초대 링크를 알 수 있다
• 핑 - 봇의 핑을 알 수 있다
• 계산 - %계산 (계산식)
• 현재시간 - 현재시간을 알려준다
• 번역 - %번역 (국가코드) (번역할 내용)
    (자세한건 `%번역 도움` 참고)
• 코로나 - 코로나 현재 상황을 알려준다
• 유저정보 - 유저정보를 가져온다
    (자세한건 `%유저정보 도움` 참고)
• 서버정보 - 서버의 정보를 보여준다
"""
게임 = """• 가바보 - 명령어 뒤에 가위/바위/보 를 적어 봇과 가위바위보를 할 수 있다
• 따라해 - 명령어 뒤의 글을 따라합니다
• 굴려 숫자 - 주사위를 굴린다
• 뽑아 단어1 단어2... - 단어들 중 하나를 랜덤으로 뽑아준다
"""
관리자 = """
• 밴 유저id 사유 - 유저를 밴 할 수 있다
• 언밴 유저id - 유저를 밴을 해제 할 수 있다
• 킥 유저id 사유 - 유저를 추방 할 수 있다
• 생성 - 무제한 초대링크를 생성합니다
• 역할추가 - %역할추가 @멘션 역할이름
• 역할제거 - %역할제거 @멘션 역할이름
• 클린 숫자 - 숫자 만큼의 메시지를 지울 수 있다
• 로그 - 서버의 로그를 보여주는 채널이 생성 된다
    (자세한건 `%로그 도움` 참고)
• 검열 - 검열 채널이 만들어진다
    (자세한건 `%검열 도움` 참고)
• 테러보호 - `토큰테러, 클린테러, 차단테러`로 부터 서버를 보호합니다
    (테러를 시도하는 유저의 역할 보다 건강이의 권한이 높아야 합니다)
"""
홍보 = """
• `%셋업` 명령어를 사용 하여 만든 `건강랜드` 채널에서만 사용 가능합니다
(채널 이름 바꾸지 마세요)
• 서버 관리자만 사용 가능 하며 쿨타임은 `서버당 1시간` 입니다 

"""
검열설명 = """
• %검열 통합- 욕설 및 섹드립 검열 
• %검열 욕설 - 욕설만 검열 
• %검열 섹드립 - 섹드립만 검열 
셋 중에 하나만 사용해 주세요
"""
import discord
import json
import io
import time
import asyncio
import random
import datetime
import bs4
import os
#import requests
import turtle as t
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import (CommandNotFound, BadArgument, MissingRequiredArgument, CommandOnCooldown, MissingPermissions)
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands import command
from discord.ext.commands.core import cooldown
from discord import Embed, File

def get_nick(client, message):
    with open('owner.json', 'r') as f:
        nickname = json.load(f)
    
    return nickname[str(message.guild.id), str(message.channel.id)]

def get_prefix(client, message):
    with open('prefix.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(intents=intents, command_prefix=get_prefix)

@client.event
async def on_ready():
    print("    디스코드 봇이 정상적으로 로그인 되었습니다.    ")
    print("    >> 다음으로 로그인합니다.")
    print("     : BOT NAME | " + client.user.name)
    print("     : BOT CLIENT ID | " + str(client.user.id))
    print(" ")
    print(" ")
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("부팅 중...현재 명령어 사용 불가")
    await client.change_presence(status=discord.Status.online, activity=game)
    while True:
        user = len(client.users)
        game = discord.Game(str(user) + "명의 유저와 함께하고 있어요!")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
        game = discord.Game("ㅇㅅㅇ")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
        game = discord.Game("봇 테스트중")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)

#================================================ 서버 prefix 변경 ================================================
@client.listen()
async def on_guild_join(guild):
    with open("prefix.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = '.'
    with open("prefix.json", "w") as f:
        json.dump(prefixes, f, indent=4)

    with open("owner.json", "r") as f:
        nickname = json.load(f)
    nickname[str(guild.id)] = ''
    with open("owner.json", "w") as f:
        json.dump(nickname, f, indent=4)

@client.listen()
async def on_guild_remove(guild):
    with open("prefix.json", "r") as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    with open("prefix.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@client.command()
async def 명령어설정(ctx, *, prefix):
    with open("prefix.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open("prefix.json", "w") as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f"Command_Prefix가 `{prefix}` 로 변경되었습니다.")

@client.listen()
async def on_message(msg):
    try:
        if msg.mentions[0] == client.user:
            with open("prefix.json", "r") as f:
                prefixes = json.load(f)
            pre = prefixes[str(msg.guild.id)] 
            await msg.channel.send(f"현재 **{msg.guild}** 서버의 Command_Prefix는 `{pre}` 입니다")
    except:
        pass
    await client.process_commands(msg)

#================================================ Nick Prefix 변경 ================================================
@client.command()
@commands.has_permissions(administrator = True)
async def 닉네임설정(ctx, *, nick):
    with open("owner.json", "r") as f:
        nickname = json.load(f)
    nickname[str(ctx.guild.id)] = nick
    with open("owner.json", "w") as f:
        json.dump(nickname, f, indent=4)
    await ctx.send(f"Nick Prefix가 `{nick}` 로 변경되었습니다.")

#================================================ 봇 및 서버 초대 ================================================
@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def 초대(ctx):
    if ctx.author.bot:
        return
    embed = discord.Embed(title="봇 초대",description="[이곳을 클릭하세요](https://discord.com/oauth2/authorize?client_id=805661063253196871&permissions=8&scope=bot)",color=0x87CEFA)
    embed.set_thumbnail(url=client.user.avatar_url)
    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def 링크(ctx):
    if ctx.author.bot:
        return
    embed = discord.Embed(title="서버링크",description="건강랜드 : [이곳을 클릭하세요](https://discord.gg/jvDYjVT)\n봇 공식서버 (팀 닥터) : [이곳을 클릭하세요](https://discord.gg/2fyY2Gfw2G)",color=0x87CEFA)
    await ctx.send(embed=embed)

#================================================ 편의 기능 ================================================
@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def 핑(ctx):
    m = await ctx.send(embed = discord.Embed(
        title = '핑 측정중.....',
        colour = discord.Colour.dark_orange()
    )) #[1]
    await asyncio.sleep(2)
    ping = round(client.latency * 1000) #[2]
    latency = m.created_at - ctx.message.created_at #[3]
    if ping >= 0 and ping <= 100: #[4]
        pings = "🔵 매우 좋음"
        embed = discord.Embed(title=f"🏓 Pong",color=0x00e2ff, timestamp=ctx.message.created_at)
        embed.add_field(name="Latency", value=f'{latency}ms', inline=True)
        embed.add_field(name="API Latency", value=f'{ping}ms\n{pings}', inline=True)
        embed.set_thumbnail(url="https://i.imgur.com/1Gk4tOj.png")
        await m.edit(embed=embed) #[5]
    elif ping >= 101 and ping <= 200:
        pings = "🟢 좋음" 
        embed = discord.Embed(title=f"🏓 Pong!",color=0x00ff24, timestamp=ctx.message.created_at)
        embed.add_field(name="Latency", value=f'{latency}ms', inline=True)
        embed.add_field(name="API Latency", value=f'{ping}ms\n{pings}', inline=True)
        embed.set_thumbnail(url="https://i.imgur.com/1Gk4tOj.png")
        await m.edit(embed=embed)    
    elif ping >= 201 and ping <= 500:
        pings = "🟡 보통"
        embed = discord.Embed(title=f"🏓 Pong!",color=0xfeff0e, timestamp=ctx.message.created_at)
        embed.add_field(name="Latency", value=f'{latency}ms', inline=True)
        embed.add_field(name="API Latency", value=f'{ping}ms\n{pings}', inline=True)
        embed.set_thumbnail(url="https://i.imgur.com/1Gk4tOj.png")
        await m.edit(embed=embed)      
    elif ping >= 501 and ping <= 1000:
        pings = "🟠 위험"
        embed = discord.Embed(title=f"🏓 Pong!",color=0xff9f0e, timestamp=ctx.message.created_at)
        embed.add_field(name="Latency", value=f'{latency}ms', inline=True)
        embed.add_field(name="API Latency", value=f'{ping}ms\n{pings}', inline=True)
        embed.set_thumbnail(url="https://i.imgur.com/1Gk4tOj.png")
        await m.edit(embed=embed)      
    elif ping >= 1000:
        pings = "🔴 매우 위험"
        embed = discord.Embed(title=f"🏓 Pong!",color=0xff0000, timestamp=ctx.message.created_at)
        embed.add_field(name="Latency", value=f'{latency}ms', inline=True)
        embed.add_field(name="API Latency", value=f'{ping}ms\n{pings}', inline=True)
        embed.set_thumbnail(url="https://i.imgur.com/1Gk4tOj.png")
        await m.edit(embed=embed)

@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def 유저정보(ctx, member: discord.Member):
    user = member
    date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
    roles = [role for role in member.roles]
    embed=discord.Embed(title=user.name+"님의 정보", description=user.name+"님의 정보를 보여드립니다", color=0x00ffee)
    embed.add_field(name="디스코드 닉네임", value=user, inline=True)
    embed.add_field(name="서버 닉네임", value=user.display_name, inline=False)
    embed.add_field(name="계정생성일", value=str(date.year)+"년"+str(date.month)+"월"+str(date.day)+"일", inline=False)
    embed.add_field(name="아이디", value=user.id, inline=False)
    bot = str(user.bot)
    if bot == "True":
        bot = "봇"
    else:
        bot = "사람"
    embed.add_field(name="봇 여부", value=f"{bot}", inline=False)
    embed.add_field(name="역할", value=" ".join([role.mention for role in roles]), inline=False)
    if member.guild_permissions.administrator:
        admin = "O"
    else:
        admin = "X"
    embed.add_field(name="관리자 권한 여부", value=f"{admin}", inline=False)
    sta = str(member.status)
    if sta == "online":
        status = "온라인 🟢"
    elif sta == "dnd":
        status = "다른 용무 중 ⛔"
    elif sta == "idle":
        status = "자리 비움 🟡"
    elif sta == "offline":
        status = "오프라인 ⚪"
    embed.add_field(name="상태", value=f"{status}", inline=False)
    act = str(member.activity)
    if act == "None":
        act = "활동이 없습니다"
    else:
        act = (member.activity)
    embed.add_field(name="활동", value=f"{act}", inline=False)
    jubseok = member.guild.get_member(member.id).is_on_mobile()
    if jubseok == True:
        jubseok = "핸드폰"
    else:
        jubseok = "PC"
    embed.add_field(name="접속 기기", value=f"{jubseok}", inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"요청자: {ctx.author}")
    await ctx.send(embed=embed)

#================================================ 게임 기능 ================================================
@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def 굴려(ctx):
    if ctx.author.bot:
        return
    try:
        number = int(ctx.message.content.split(" ")[1])
        number2 = random.randint(1,number)
        men = ctx.author.mention
        await ctx.send(f"{men}님이 주사위를 돌려 __{number2}__이(가) 나왔습니다")
    except:
        await message.channel.send("명령어 뒤에 숫자를 붙여주세요")
        return

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def 따라해(ctx, msg):
    if ctx.author.bot:
        return
    list = msg.split("해 ")
    try:
        fol = list[0]
        await ctx.send(fol)
    except:
        await ctx.send("명령어 뒤에 글을 적어주세요")
        return

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def 가바보(ctx, msg):
    if ctx.author.bot:
        return
    ran = random.randint(0,4)
    list = msg.split("보 ")
    try:
        rsp=list[0]
    except IndexError:
        return     
    if rsp =='가위' or rsp =='찌':
        if ran == 1:
            embed = discord.Embed(title="가위바위보", description="졌습니다", color=0xFF7F50) #AAFFFF
            embed.add_field(name="유저", value=":v:", inline=True)
            embed.add_field(name="봇", value=":rock:", inline=True)
            await ctx.send(embed=embed)
        elif ran == 2:
            embed = discord.Embed(title="가위바위보", description="비겼습니다", color=0x87CEFA)
            embed.add_field(name="유저", value=":v:", inline=True)
            embed.add_field(name="봇", value=":v:", inline=True)
            await ctx.send(embed=embed)
        else :
            embed = discord.Embed(title="가위바위보", description="이겼습니다", color=0x00FF7F)
            embed.add_field(name="유저", value=":v:", inline=True)
            embed.add_field(name="봇", value=":raised_hand:", inline=True)
            await ctx.send(embed=embed)
    elif rsp =='바위' or rsp =='묵' or rsp =='주먹':
        if ran == 1:
            embed = discord.Embed(title="가위바위보", description="비겼습니다", color=0x87CEFA)
            embed.add_field(name="유저", value=":rock:", inline=True)
            embed.add_field(name="봇", value=":rock:", inline=True)
            await ctx.send(embed=embed)
        elif ran == 2:
            embed = discord.Embed(title="가위바위보", description="이겼습니다", color=0x00FF7F)
            embed.add_field(name="유저", value=":rock:", inline=True)
            embed.add_field(name="봇", value=":v:", inline=True)
            await ctx.send(embed=embed)
        else :
            embed = discord.Embed(title="가위바위보", description="졌습니다", color=0xFF7F50)
            embed.add_field(name="유저", value=":rock:", inline=True)
            embed.add_field(name="봇", value=":raised_hand:", inline=True)
            await ctx.send(embed=embed)
    elif rsp =='보'or rsp =='보자기' or rsp =='빠':
        if ran == 1:
            embed = discord.Embed(title="가위바위보", description="이겼습니다", color=0x00FF7F)
            embed.add_field(name="유저", value=":raised_hand:", inline=True)
            embed.add_field(name="봇", value=":rock:", inline=True)
            await ctx.send(embed=embed)
        elif ran == 2:
            embed = discord.Embed(title="가위바위보", description="졌습니다", color=0xFF7F50)
            embed.add_field(name="유저", value=":raised_hand:", inline=True)
            embed.add_field(name="봇", value=":v:", inline=True)
            await ctx.send(embed=embed)
        else :
            embed = discord.Embed(title="가위바위보", description="비겼습니다", color=0x87CEFA)
            embed.add_field(name="유저", value=":raised_hand:", inline=True)
            embed.add_field(name="봇", value=":raised_hand:", inline=True)
            await ctx.send(embed=embed)
    else :
        await ctx.send("가위, 바위, 보 만쳐주세요")

#================================================ 관리진 전용 ================================================
@client.command()
@commands.has_permissions(administrator = True)
async def 청소(ctx):
    if ctx.author.bot:
        return
    try: 
        number = int(ctx.message.content.split(" ")[1])
        await ctx.message.delete()
        await ctx.message.channel.purge(limit=number)
        a = await ctx.send(embed=discord.Embed(title="청소기능 발동", description =f"{number}개의 메세지가 {ctx.author.mention}님의 의하여 삭제 되었습니다", color=0x00ff00))
        await asyncio.sleep(5)
        await a.delete()
    except:  
            with open("prefix.json", "r") as f:
                prefixes = json.load(f)
            pre = prefixes[str(ctx.guild.id)] 
            await ctx.send(embed=discord.Embed(title="오류 발생!", description =f"{ctx.author.mention}님 명령어를 확인해주세요! \n 올바른 명령어는 `{pre}청소 (숫자)`입니다!", color=0xFF0000))

@client.command(name="킥")
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    if ctx.author.bot:
        return
    await member.kick(reason=reason)
    embed = discord.Embed(title="킥 명령어 작동", color=0xAAFFFF) 
    embed.add_field(name="킥된 유저", value=f"{member.mention}", inline=False)
    embed.add_field(name="명령어 사용자", value=f"{ctx.author.mention}", inline=False)
    embed.add_field(name="사유", value=f"{reason}", inline=False)
    await ctx.send(embed=embed)

@client.command(name="밴")
@commands.has_permissions(administrator = True)
async def ban(ctx, member : discord.Member, *, reason=None):
    if ctx.author.bot:
        return
    await member.ban(reason=reason)
    embed = discord.Embed(title="밴 명령어 작동", color=0xAAFFFF) 
    embed.add_field(name="밴된 유저", value=f"{member.mention}", inline=False)
    embed.add_field(name="명령어 사용자", value=f"{ctx.author.mention}", inline=False)
    embed.add_field(name="사유", value=f"{reason}", inline=False)
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator = True)
async def 언밴(ctx, *, member):
    if ctx.author.bot:
        return
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(title="언밴 명령어 작동", color=0xAAFFFF) 
            embed.add_field(name="언밴된 유저", value=f"{user.mention}", inline=False)
            embed.add_field(name="명령어 사용자", value=f"{ctx.author.mention}", inline=False)
            await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator = True)
async def 생성(ctx):
    if ctx.author.bot:
        return
    link = await ctx.message.channel.create_invite(max_uses=1,unique=False)
    user = ctx.author
    await ctx.send(f"{user.mention}님 요청하신 **{ctx.guild}** 의 링크가 생성되었습니다. \n **링크 : [ {link} ]**")

#================================================ Team Docter전용 ================================================
@client.command()
async def 인증(ctx):
    if ctx.author.bot:
        return
    channel_id = int(ctx.channel.id)
    channel = int(811909469361274940)
    if channel_id == channel:
        await ctx.send("인증되었습니다")
        await ctx.author.add_roles(discord.utils.get(ctx.author.guild.roles, name="유저"))

#================================================ Team Docter 관리진 전용 ================================================
@client.command()
@commands.has_permissions(administrator = True)
async def 공지(ctx):
    if ctx.author.bot:
        return
    user = int(ctx.author.id)
    ment = ctx.message.content[4:]
    for i in admin_user:
        if user == i:
            for server in client.guilds:
                for channel in server.text_channels:
                    channel_id =channel.id
                await client.get_channel(int(channel_id)).send(ment) 

@client.command()
@commands.has_permissions(administrator = True)
async def 정보(ctx):    
    if ctx.author.bot:
        return
    info = f"{str(len(client.guilds))} 서버 | {str(len(client.users))} 유저"
    await ctx.send(info)

@client.command()
async def 닉네임변경(ctx, *, nickname):
    back_name = ctx.message.author.nick
    user = ctx.message.author
    with open("prefix.json", "r") as f:
        prefixes = json.load(f)
        fix = prefixes[str(ctx.guild.id)] 

    with open("owner.json", "r") as f:
        nick = json.load(f)
        pre = nick[str(ctx.guild.id)] 
    if pre == "":
        await ctx.send(embed=discord.Embed(title="오류 발생!", description =f"현재 이 서버에서는 명령어를 사용할 수 없습니다! \n\n 명령어를 사용하시려면 `{fix}닉네임설정`을 해주세요!", color=0xFF0000))
    else:
        await user.edit(nick=f'{pre} ' + nickname)
        embed = discord.Embed(title="닉네임 변경", color=0xffdd00)
        embed.add_field(name=f'변경 전 닉네임', value=f'{back_name}\n', inline=False)
        embed.add_field(name=f'변경 후 닉네임', value=f'{ctx.message.author.display_name}\n\n', inline=False)
        await ctx.send(embed=embed)
        print(f"[ LOG ] {user} 이가 닉네임을 변경하였습니다. 전: {back_name} / 후: {ctx.message.author.display_name}")         

#============================================================================ 로그 / 검열 명령어 /============================================================================
@client.command()
async def 로그(ctx, *, msg):
    if ctx.author.bot:
        return
    list = msg.split("그 ")
    try:
        com=list[0]
    except IndexError:
        return
    if com == "도움":
        embed = discord.Embed(title="로그 명령어 사용법", description="%로그 - 채팅, 통화방 로그 \n%로그 유저(수정중) - 유저 로그",color=0x00FF7F)
        await ctx.send(embed=embed)
        return
    if com == "생성":
        logg = await ctx.guild.create_text_channel('건강이 로그') #서버이름
        await logg.edit(topic="건강이 로그 채널입니다")
        embed = discord.Embed(title="`건강이-로그` 채널이 생성 되었습니다", description="",color=0x00FF7F)
        await ctx.send(embed=embed)
        chan = discord.utils.get(ctx.guild.text_channels, topic = "건강이 로그 채널입니다")
        await client.get_channel(int(chan.id)).send(f"{ctx.author.mention} 채널이 생성되었습니다")
    if com == "유저":
        logg = await ctx.guild.create_text_channel('건강이 유저 로그') #서버이름
        await logg.edit(topic="건강이 유저 로그 채널입니다")
        embed = discord.Embed(title="`건강이-유저-로그` 채널이 생성 되었습니다", description="",color=0x00FF7F)
        await ctx.send(embed=embed)
        chan = discord.utils.get(ctx.guild.text_channels, topic = "건강이 유저 로그 채널입니다")
        await client.get_channel(int(chan.id)).send(f"{ctx.author.mention} 채널이 생성되었습니다")        
    if com == None:
        await ctx.send("테스트")

@client.command()
async def 테러보호(ctx):
    if ctx.author.bot:
        return
    nuk = await ctx.guild.create_text_channel('건강이 테러')
    await nuk.edit(topic="건강이 테러 채널입니다")
    embed = discord.Embed(title="`건강이-테러` 채널이 생성 되었습니다", description="",color=0x00FF7F)
    await ctx.send(embed=embed)
    chan = discord.utils.get(ctx.guild.text_channels, topic = "건강이 테러 채널입니다")
    await client.get_channel(int(chan.id)).send(f"{ctx.author.mention} 채널이 생성되었습니다")   

@client.command()
async def 검열(ctx, *, msg):
    if ctx.author.bot:
        return     
    list = msg.split("열 ")
    try:
        gum = list[0]
    except IndexError:
        return
    if gum == "도움":
        embed = discord.Embed(title="검열 명령어 사용법",description="%검열로 사용 가능합니다",color=0x00FFFF)
        embed.add_field(name= "명령어",value=검열설명 ,inline=False)
        await ctx.send(embed=embed)    
    if gum == "통합":   
        bad_ = await ctx.guild.create_text_channel('건강이 검열') #서버이름
        await bad_.edit(topic = "건강이 검열 채널입니다")
        embed = discord.Embed(title="`건강이-검열` 채널이 생성 되었습니다", description="",color=0x00FF7F)
        await ctx.send(embed=embed)
        await client.get_channel(int(bad_.id)).send(f"{ctx.author.mention} 채널이 생성되었습니다")
        return
    if gum == "욕설":
        bad_ = await ctx.guild.create_text_channel('건강이 검열') #서버이름
        await bad_.edit(topic = "건강이 욕설 검열 채널입니다")
        embed = discord.Embed(title="`건강이-검열` 채널이 생성 되었습니다", description="",color=0x00FF7F)
        await ctx.send(embed=embed)
        await client.get_channel(int(bad_.id)).send(f"{ctx.author.mention} 채널이 생성되었습니다")
        return
    if gum == "섹드립":
        bad_ = await ctx.guild.create_text_channel('건강이 검열') #서버이름
        await bad_.edit(topic = "건강이 섹드립 검열 채널입니다")
        embed = discord.Embed(title="`건강이-검열` 채널이 생성 되었습니다", description="",color=0x00FF7F)
        await ctx.send(embed=embed)
        await client.get_channel(int(bad_.id)).send(f"{ctx.author.mention} 채널이 생성되었습니다")
        return        


# #============================================================================ 검열 기능 ============================================================================
@client.event
async def on_message(message):
    message_contant=message.content
    for i in 검열:
        try:
            채널 = discord.utils.get(message.guild.text_channels, topic = "건강이 검열 채널입니다") #(guild.text_channels,name="건강이-유저-로그")
            channel_id = 채널.id #건강이-검열 의 아이디
            user = message.author   
            user_id = message.author.id
            time_ = time.strftime('%m/%d %I:%M %p',time.localtime(time.time()))
            for Channel in message.guild.channels:
                if i in message_contant:
                    if message.author.guild_permissions.administrator:
                        return
                    if message.author.bot:
                        return None
                    else:
                        await message.delete()
                        embed = discord.Embed(title="경고!!", description="", color=0xFF0000)
                        embed.set_footer(text="바르고 고운말을 사용합시다")
                        await message.channel.send(embed=embed)
                        embed=discord.Embed(title="검열됨",description=f"<#{message.channel.id}> 에서 검열됨", color=0xFA8072)
                        embed.set_author(name=f"{user}", icon_url=message.author.avatar_url)
                        embed.add_field(name= "검열된 메시지",value=message_contant ,inline=False)
                        embed.add_field(name= "검열 단어",value=i ,inline=False)
                        embed.set_footer(text=f"user id: {user_id} • {time_}",icon_url = client.user.avatar_url)
                        await client.get_channel(int(channel_id)).send(embed=embed)         
        except:
            for i in 욕설:
                try:
                    채널 = discord.utils.get(message.guild.text_channels, topic = "건강이 욕설 검열 채널입니다") #(guild.text_channels,name="건강이-유저-로그")
                    channel_id = 채널.id #건강이-검열 의 아이디
                    user = message.author   
                    user_id = message.author.id
                    time_ = time.strftime('%m/%d %I:%M %p',time.localtime(time.time()))
                    for Channel in message.guild.channels:
                        if i in message_contant:
                            if message.author.bot:
                                return None
                            else:
                                await message.delete()
                                embed = discord.Embed(title="경고!!", description="", color=0xFF0000)
                                embed.set_footer(text="바르고 고운말을 사용합시다")
                                await message.channel.send(embed=embed)
                                embed=discord.Embed(title="검열됨",description=f"<#{message.channel.id}> 에서 욕설이 감지됨", color=0xFA8072)
                                embed.set_author(name=f"{user}", icon_url=message.author.avatar_url)
                                embed.add_field(name= "검열된 메시지",value=message_contant ,inline=False)
                                embed.add_field(name= "검열 단어",value=i ,inline=False)
                                embed.set_footer(text=f"user id: {user_id} • {time_}",icon_url = client.user.avatar_url)
                                await client.get_channel(int(channel_id)).send(embed=embed)
                except:
                    for i in 섹드립:
                        try:
                            채널 = discord.utils.get(message.guild.text_channels, topic = "건강이 섹드립 검열 채널입니다") #(guild.text_channels,name="건강이-유저-로그")
                            channel_id = 채널.id #건강이-검열 의 아이디
                            user = message.author   
                            user_id = message.author.id
                            time_ = time.strftime('%m/%d %I:%M %p',time.localtime(time.time()))
                            for Channel in message.guild.channels:
                                if i in message_contant:
                                    if message.author.bot:
                                        return None
                                        await message.delete()
                                        embed = discord.Embed(title="경고!!", description="", color=0xFF0000)
                                        embed.set_footer(text="바르고 고운말을 사용합시다")
                                        await message.channel.send(embed=embed)
                                        embed=discord.Embed(title="검열됨",description=f"<#{message.channel.id}> 에서 섹드립이 감지됨", color=0xFA8072)
                                        embed.set_author(name=f"{user}", icon_url=message.author.avatar_url)
                                        embed.add_field(name= "검열된 메시지",value=message_contant ,inline=False)
                                        embed.add_field(name= "검열 단어",value=i ,inline=False)
                                        embed.set_footer(text=f"user id: {user_id} • {time_}",icon_url = client.user.avatar_url)
                                        await client.get_channel(int(channel_id)).send(embed=embed)
                        except:
                            return
#이미지 로그
    try:
        time_ = time.strftime('%m/%d %I:%M %p',time.localtime(time.time()))
        채널 = discord.utils.get(message.guild.text_channels,topic = "건강이 로그 채널입니다")
        delete_message_channel = message.channel.id #삭제된 메시지의 채널 아이디
        channel_id = 채널.id #건강이-로그 의 아이디
        user = message.author
        user_id = message.author.id
        url = message.attachments[0].url
        if message.author.bot:
            return
        embed=discord.Embed(title="",description=f"<#{message.channel.id}> 에서 이미지가 올라옴", color=0x9370DB)
        embed.set_author(name=f"{user}", icon_url=message.author.avatar_url)
        embed.set_image(url=url)
        embed.set_footer(text=f"user id: {user_id} • {time_}",icon_url = client.user.avatar_url)
        await client.get_channel(int(channel_id)).send(embed=embed)
    except:
        return

#메시지 삭제 로그
@client.event
async def on_message_delete(message):
    try:
        if message.author.bot:
            return
        time_ = time.strftime('%m/%d %I:%M %p',time.localtime(time.time()))
        채널 = discord.utils.get(message.guild.text_channels,topic = "건강이 로그 채널입니다")
        delete_message_channel = message.channel.id #삭제된 메시지의 채널 아이디
        channel_id = 채널.id #건강이-로그 의 아이디
        user = message.author   
        user_id = message.author.id
        embed=discord.Embed(title="",description=f"<#{delete_message_channel}> 에서 메시지가 삭제됨", color=0xFFA500)
        embed.set_author(name=f"{user}", icon_url=message.author.avatar_url)
        embed.add_field(name= "삭제된 메시지",value=message.content ,inline=False)
        embed.add_field(name= "메시지 아이디",value=message.id ,inline=False)
        embed.set_footer(text=f"user id: {user_id} • {time_}",icon_url = client.user.avatar_url)
        await client.get_channel(int(channel_id)).send(embed=embed)
        return
    except:
        return
#메시지 수정 로그
@client.event
async def on_message_edit(message_before, message_after):
    try:
        if message_before.author.bot:
            return
        time_ = time.strftime('%m/%d %I:%M %p',time.localtime(time.time()))
        채널 = discord.utils.get(message_before.guild.text_channels,topic = "건강이 로그 채널입니다")
        delete_message_channel = message_before.channel.id #삭제된 메시지의 채널 아이디
        channel_id = 채널.id #건강이-로그 의 아이디
        user = message_before.author
        user_id = message_before.author.id
        embed=discord.Embed(title="", description=f"<#{delete_message_channel}> 에서 메시지가 수정됨",color=0xFFD700)
        embed.set_author(name=f"{user}", icon_url=message_before.author.avatar_url)
        embed.add_field(name="수정전 메시지" ,value= message_before.content, inline=True)
        embed.add_field(name="수정후 메시지" ,value= message_after.content, inline=True)
        embed.add_field(name= "메시지 아이디",value=message_before.id ,inline=False)
        embed.set_footer(text=f"user id: {user_id} • {time_}",icon_url = client.user.avatar_url)
                #channel=client.get_channel(channel_id)
        await client.get_channel(int(channel_id)).send(embed=embed)
        return
    except:
        return
#퇴장 로그
@client.event
async def on_member_remove(member):
    try:
        채널 = discord.utils.get(member.guild.text_channels,topic = "건강이 로그 채널입니다")
        time_ = time.strftime('%m/%d %I:%M %p',time.localtime(time.time()))
        channel_id = 채널.id 
        user = member.name
        user_id = member.id
        create = member.created_at
        join = member.joined_at
        embed=discord.Embed(title="", description=f"{member.mention}님이 퇴장하셨습니다",color=0xFF0000)
        embed.set_author(name=f"{user}#{member.discriminator}", icon_url=member.avatar_url)
        embed.add_field(name="계정 생성일" ,value=f"{create}", inline=False)
        embed.add_field(name="서버 입장일" ,value=f"{join}", inline=False)
        embed.set_footer(text=f"user id: {user_id} • {time_}",icon_url = client.user.avatar_url)
        await client.get_channel(int(channel_id)).send(embed=embed)
    except: return
#통방 입퇴장 
@client.event
async def on_voice_state_update(member, before, after):
    try:
        채널 = discord.utils.get(member.guild.text_channels,topic = "건강이 로그 채널입니다")
        time_ = time.strftime('%m/%d %I:%M %p',time.localtime(time.time()))
        channel_id = 채널.id 
        user = member.name
        user_id = member.id
    
        if before.channel != after.channel:
            if before.channel is None and after.channel is not None:
                embed=discord.Embed(title="", description=f"{member.mention}님이 {after.channel}에 입장하셨습니다",color=0xFFFAFA)
                embed.set_author(name=f"{user}#{member.discriminator}", icon_url=member.avatar_url)
                embed.add_field(name="입장한 채널" ,value=f"{after.channel}", inline=False)
                embed.add_field(name= "채널 아이디",value=after.channel.id ,inline=False)
                embed.set_footer(text=f"user id: {user_id} • {time_}",icon_url = client.user.avatar_url)
                await client.get_channel(int(channel_id)).send(embed=embed)

            elif before.channel is not None and after.channel is None:
                embed=discord.Embed(title="", description=f"{member.mention}님이 {before.channel}에서 퇴장하셨습니다",color=0xFFFAFA)
                embed.set_author(name=f"{user}#{member.discriminator}", icon_url=member.avatar_url)
                embed.add_field(name="퇴장한 채널" ,value=f"{before.channel}", inline=False)
                embed.add_field(name= "채널 아이디",value=before.channel.id ,inline=False)
                embed.set_footer(text=f"user id: {user_id} • {time_}",icon_url = client.user.avatar_url)
                await client.get_channel(int(channel_id)).send(embed=embed)
    
            else:
                embed=discord.Embed(title="", description=f"{member.mention}님이 음성방을 이동하였습니다",color=0xFFFAFA)
                embed.set_author(name=f"{user}#{member.discriminator}", icon_url=member.avatar_url)
                embed.add_field(name="이동 전 채널" ,value=f"{before.channel}", inline=True)
                embed.add_field(name="이동 후 채널" ,value=f"{after.channel}", inline=True)
                embed.set_footer(text=f"user id: {user_id} • {time_}",icon_url = client.user.avatar_url)
                await client.get_channel(int(channel_id)).send(embed=embed)
    except: return
#입장 로그
@client.event
async def on_member_join(member):
    try:
        채널 = discord.utils.get(member.guild.text_channels,topic = "건강이 로그 채널입니다")
        time_ = time.strftime('%m/%d %I:%M %p',time.localtime(time.time()))
        channel_id = 채널.id 
        user = member.name
        user_id = member.id
        create = member.created_at
        embed=discord.Embed(title="", description=f"{member.mention}님이 입장하셨습니다",color=0x00FF7F)
        embed.set_author(name=f"{user}#{member.discriminator}", icon_url=member.avatar_url)
        embed.add_field(name="계정 생성일" ,value=f"{create}", inline=True)
        embed.set_footer(text=f"user id: {user_id} • {time_}",icon_url = client.user.avatar_url)
        await client.get_channel(int(channel_id)).send(embed=embed)
    except: 
        return

#============================================================================ 테러 방어 ============================================================================
    #토큰 테러 보호
    global join_count
    global max_count
    global _time
    join_count = join_count + 1
    if join_count >= max_count:
        for invite in await member.guild.invites():
            await invite.delete()
        channel_id = discord.utils.get(member.guild.text_channels,topic = "건강이 테러 채널입니다")
        채널 = channel_id
        time_ = time.strftime('%m/%d %I:%M %p',time.localtime(time.time()))
        await client.get_channel(int(채널)).send(f"@everyone 토큰테러가 감지되었습니다\n시간: {time_}")
    await asyncio.sleep(_time)
    join_count = 0
        
@client.event
async def on_guild_channel_delete(channel):
    async for entry in channel.guild.audit_logs(limit=1):
        user = '{0.user}'.format(entry) #print('{0.user} did {0.action} to {0.target}'.format(entry)) 
    global delete_count,max_delete,_time
    delete_count = delete_count + 1
    for user_id in channel.guild.members:
        if user_id.name+'#'+user_id.discriminator  == user:
            break
    if delete_count >= max_delete:
        await channel.guild.ban(user_id)
        channel_id = discord.utils.get(channel.guild.text_channels,topic = "건강이 테러 채널입니다")
        time_ = time.strftime('%m/%d %I:%M %p',time.localtime(time.time()))
        await client.get_channel(int(channel_id.id)).send(f"@everyone 클린테러가 감지되었습니다\n시간: {time_}")
    await asyncio.sleep(_time)
    delete_count = 0 

@client.event
async def on_member_ban(guild,user):
    async for entry in guild.audit_logs(limit=1):
        user = '{0.user}'.format(entry) #print('{0.user} did {0.action} to {0.target}'.format(entry))      
    global ban_count,max_ban,_time
    ban_count = ban_count + 1
    for user_id in guild.members:
        if user_id.name+'#'+user_id.discriminator  == user:
            break
    if ban_count >= max_ban:
        await guild.ban(user_id)
        channel_id = discord.utils.get(guild.text_channels,topic = "건강이 테러 채널입니다")
        time_ = time.strftime('%m/%d %I:%M %p',time.localtime(time.time()))
        await client.get_channel(int(channel_id.id)).send(f"@everyone 차단테러가 감지되었습니다\n시간: {time_}")
    await asyncio.sleep(_time)

#================================================ error log ================================================
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print(f'잘못된 명령어가 입력되었습니다.')
        await ctx.send(f"잘못된 명령어가 입력되었습니다.")
    if isinstance(error, commands.CommandOnCooldown):
        minute=int(error.retry_after)//60
        hour=minute//60
        # if minute <= 1:
        #     realminute=str(int(error.retry_after)) + '초'
        # else:
        #     realminute=str(minute) + '분'
        # if hour <= 1:
        #     realhour='1시간 이내'
        # else:
        #     realhour=str(hour) + '시간'
        if hour <= 1:
            realminute=str(int(error.retry_after)) + '초'
            realhour=str(minute) + '분'
        else:
            realminute=str(minute) + '분'
            realhour=str(hour) + '시간'
        await ctx.send(embed=discord.Embed(title=f"명령어 쿨타임!", description=f"{ctx.message.author.mention}님의 다음 명령어 사용까지 남은시간 \n\n **약 {realhour} (약 {realminute})**", color=0xFF0000)) 
    else:
        embed = discord.Embed(title="오류!!", description="오류가 발생했습니다.", color=0xFF0000)
        embed.add_field(name="상세", value=f"```{error}```")
        await ctx.send(embed=embed)

@ban.error
async def ban_error(ctx, error):
    with open("prefix.json", "r") as f:
        prefixes = json.load(f)
        pre = prefixes[str(ctx.guild.id)] 
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=discord.Embed(title="오류 발생!", description =f"{ctx.author.mention}님은 이 명령어를 사용할 권한이 없습니다!", color=0xFF0000))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(title="오류 발생!", description =f"{ctx.author.mention}님 명령어를 확인해주세요! \n 올바른 명령어는 `{pre}밴 (유저멘션)`입니다!", color=0xFF0000))
    if isinstance(error, commands.BadArgument):
        await ctx.send(embed=discord.Embed(title="오류 발생!", description =f"{ctx.author.mention}님 명령어를 확인해주세요! \n 올바른 명령어는 `{pre}밴 (유저멘션)`입니다!", color=0xFF0000))
    elif discord.errors.Forbidden:
        await ctx.send(embed=discord.Embed(title="권한 오류 발생!", description =f"대상자보다 권한이 낮습니다", color=0xFF0000))

@kick.error
async def kick_error(ctx, error):
    with open("prefix.json", "r") as f:
        prefixes = json.load(f)
        pre = prefixes[str(ctx.guild.id)] 
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=discord.Embed(title="오류 발생!", description =f"{ctx.author.mention}님은 이 명령어를 사용할 권한이 없습니다!", color=0xFF0000))
        return
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(title="오류 발생!", description =f"{ctx.author.mention}님 명령어를 확인해주세요! \n 올바른 명령어는 `{pre}킥 (유저멘션)`입니다!", color=0xFF0000))
    if isinstance(error, commands.BadArgument):
        await ctx.send(embed=discord.Embed(title="오류 발생!", description =f"{ctx.author.mention}님 명령어를 확인해주세요! \n 올바른 명령어는 `{pre}킥 (유저멘션)`입니다!", color=0xFF0000))
    if discord.errors.Forbidden:
        await ctx.send(embed=discord.Embed(title="권한 오류 발생!", description =f"대상자보다 봇의 권한이 낮습니다", color=0xFF0000))
        return


client.run(토큰)
