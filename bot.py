import discord

from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("    디스코드 봇이 정상적으로 로그인 되었습니다.    ")
    print("    >> 다음으로 로그인합니다.")
    print("     : BOT NAME | " + client.user.name)
    print("     : BOT CLIENT ID | " + str(client.user.id))
    print(" ")
    print(" ")
    game = discord.Game("오류 발생시 402#9685로 연락")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.command(aliases=['이름변경'])
async def change_nickname(ctx, *, nick):
    back_name = str(ctx.message.author)
    user = ctx.message.author
    await user.edit(nick=nick)
    embed = discord.Embed(title="닉네임 변경", color=0xffdd00)
    embed.add_field(name=f'변경 전 닉네임', value=f'{back_name}\n', inline=False)
    embed.add_field(name=f'변경 후 닉네임', value=f'{user.mention}\n\n', inline=False)
    embed.set_footer(text="제작자 : 402#9685")
    await ctx.send(embed=embed)
    #time = datetime.datetime.now().strftime('%Y년 %m월 %d일 / %H시 %M분 %S초')
    #print(f"[ LOG | {time}] {user} 이가 닉네임을 변경하였습니다. 전: {back_name} / 후: {user}")
    print(f"[ LOG ] {user} 이가 닉네임을 변경하였습니다. 전: {back_name} / 후: {user}")

client=run('token')