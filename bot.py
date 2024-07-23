import disnake
from disnake.ext import commands
from threading import Thread
import datetime

PREFIX = '!'
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)
bot.remove_command("help")
##########################################################
#Тут был спамер не надо таким заниматься)
##########################################################

@bot.event
async def on_ready():
    print('Bot_connected')
    await bot.change_presence(status=disnake.Status.streaming, activity=disnake.Game('Minecraft'))

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1198174185751593002)
    role = disnake.utils.get(member.guild.roles, name='Minecraft')
    await member.add_roles(role)
    await channel.send(embed = disnake.Embed(description=f'Пользователь {member.name}, присоединился к нам'))


@bot.command()
async def q(ctx, member: disnake.Member):
    await ctx.channel.purge(limit=1)
    emd = disnake.Embed(title='Q COMMAND', color=0x00ff00)
    emd.add_field(name=f'{ctx.author.name}, передает привет {member.name}', value='')
    emd.set_footer(text=f'{ctx.author.name} 🤘 {member.name}', icon_url='')    #gif
    await ctx.send(embed=emd)


@bot.slash_command(description='Передает пользователю привет.')
async def q(interaction, member: disnake.Member):
    emd = disnake.Embed(title='Q COMMAND', color=0x00ff00)
    emd.add_field(name=f'{interaction.author.name}, передает привет {member.name}', value='')
    emd.set_footer(text=f'{interaction.author.name} 🤘 {member.name}', icon_url='')
    await interaction.response.send_message(embed=emd)


@bot.command()
async def hello(ctx, member: disnake.Member):
    await ctx.channel.purge(limit=1)
    users = member or ctx.author or bot.user
    emd = disnake.Embed(title='HELLO COMMAND', color=0x00ff00)
    emd.add_field(name=f'Пользователь {ctx.author.name} передает привет {users.name}', value='')
    emd.set_footer(text=f'{ctx.author.name} 👋 {users.name}', icon_url='')
    await ctx.send(embed=emd)


@bot.slash_command(description='Передает любому привет.')
async def hello(interaction, member: disnake.Member):
    users = member or interaction.author or bot.user
    emd = disnake.Embed(title='HELLO COMMAND', color=0x00ff00)
    emd.add_field(name=f'Пользователь {interaction.author.name} передает привет {users.name}', value='')
    emd.set_footer(text=f'{interaction.author.name} 👋 {users.name}', icon_url='')
    await interaction.send(embed=emd)


@bot.command()
async def cls(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    emd = disnake.Embed(title='', color=0x00ff00)
    emd.add_field(name=f'Очищено {amount + 1} сообщений', value='')
    emd.set_footer(text=f'Очищено {ctx.author.name}', icon_url=ctx.author.display_avatar)
    emd.set_thumbnail(url='https://velikayaevraziya.ru/wp-content/uploads/2023/04/6-2.png')
    await ctx.send(embed=emd)


@bot.slash_command(description='Вы можете очищать чат')
async def cls(interaction, amount: int):
    await interaction.channel.purge(limit=amount + 1)
    emd = disnake.Embed(title='', color=0x00ff00)
    emd.add_field(name=f'Очищено {amount + 1} сообщений', value='')
    emd.set_footer(text=f'Очищено {interaction.author.name}', icon_url=interaction.author.display_avatar)
    emd.set_thumbnail(url='https://velikayaevraziya.ru/wp-content/uploads/2023/04/6-2.png')
    await interaction.response.send_message(embed=emd)

@bot.command()
async def timeout(ctx, user: disnake.Member, time: str, *, reason: str = 'Нарушение правил чата или сервера'):
    await ctx.channel.purge(limit=1)
    time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
    cool_time = disnake.utils.format_dt(time, style='R')
    await user.timeout(reason=reason, until=time)
    emd = disnake.Embed(title='', color=0x00ff00)
    emd.add_field(name=f'Пользователь {user.name}, замьючен по причине {reason} и будет размьючен {cool_time}', value='')
    emd.set_footer(text=f'Пользователь замьючен администрацией {ctx.author.name}', icon_url=ctx.author.display_avatar)
    emd.set_thumbnail(url='https://cdn1.vectorstock.com/i/1000x1000/72/90/no-time-hourglass-sign-icon-sand-timer-symbol-vector-1907290.jpg')
    await ctx.send(embed=emd)


@bot.slash_command(description='МЬютит пользователя на время')
async def timeout(interaction, user: disnake.Member, time: str, *, reason: str = 'Нарушение правил чата или сервера'):
    time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
    cool_time = disnake.utils.format_dt(time, style='R')
    await user.timeout(reason=reason, until=time)
    emd = disnake.Embed(title='TIMEOUT COMMAND', color=0x00ff00)
    emd.add_field(name=f'Пользователь {user.name}, замьючен по причине {reason} и будет размьючен {cool_time}', value='')
    emd.set_footer(text='', icon_url=interaction.author.display_avatar)
    emd.set_thumbnail(url='https://cdn1.vectorstock.com/i/1000x1000/72/90/no-time-hourglass-sign-icon-sand-timer-symbol-vector-1907290.jpg')
    await interaction.channel.send(embed=emd)



@bot.command()
async def untimeout(ctx, user: disnake.Member, reason: str = 'Исправление прошло успешно'):
    await ctx.channel.purge(limit=1)
    await user.timeout(reason=None, until=None)
    emd = disnake.Embed(title='UNTIMEOUT COMMAND', color=0x00ff00)
    emd.add_field(name=f'Пользователь {user.name} размьючен', value='')
    emd.set_footer(text=f'Пользователь размьючен администрацией {ctx.author.name}', icon_url=ctx.author.display_avatar)
    emd.set_thumbnail(url='https://webpulse.imgsmail.ru/imgpreview?mb=webpulse&key=pulse_cabinet-file-3324bb9e-ded4-401e-847f-a86fe5b6dc1d')
    await ctx.send(embed=emd)


@bot.slash_command(description='Вы можете размьютить пользователя.')
async def untimeout(interaction, user: disnake.Member):
    await user.timeout(reason=None, until=None)
    emd = disnake.Embed(title='UNTIMEOUT COMMAND', color=0x00ff00)
    emd.add_field(name=f'Пользователь {user.name} размьючен', value='')
    emd.set_footer(text=f'Пользователь размьючен администрацией {interaction.author.name}', icon_url=interaction.author.display_avatar)
    emd.set_thumbnail(url='https://webpulse.imgsmail.ru/imgpreview?mb=webpulse&key=pulse_cabinet-file-3324bb9e-ded4-401e-847f-a86fe5b6dc1d')
    await interaction.channel.send(embed=emd)


@bot.command()
async def mute(ctx, user: disnake.Member, *, reason: str = 'Нарушение правил сервера'):
    if ctx.author.guild_permissions.mute_members:
        await ctx.channel.purge(limit=1)
        mute_role = disnake.utils.get(ctx.guild.roles, name='mute')
        await user.add_roles(mute_role, reason=reason)
        emd = disnake.Embed(title='MUTE COMMAND', color=0x00ff00)
        emd.add_field(name=f'Пользователь {user.name} замьючен по причине {reason} ', value='')
        emd.set_footer(text=f'Пользователь замьючен администрацией {ctx.author.name}', icon_url=ctx.author.display_avatar)
        emd.set_thumbnail(url='https://www.psicologos.com.co/site/articles/cf/cd/0/49286/shutterstock-646645432.jpg')
        await ctx.send(embed=emd)
    else:
        await ctx.send(f'{ctx.author.name}, у вас недостаточно прав')


@bot.slash_command(description='Вы можете замутить пользователя.')
async def mute(interaction, user: disnake.Member, *, reason: str = 'Нарушение правил сервера'):
        mute_role = disnake.utils.get(interaction.guild.roles, name='mute')
        await user.add_roles(mute_role, reason=reason)
        emd = disnake.Embed(title='MUTE COMMAND', color=0x00ff00)
        emd.add_field(name=f'Пользователь {user.name} замьючен по причине {reason}', value='')
        emd.set_footer(text=f'Пользователь замьючен администрацией {interaction.author.name}', icon_url=interaction.author.display_avatar)
        emd.set_thumbnail(url='https://www.psicologos.com.co/site/articles/cf/cd/0/49286/shutterstock-646645432.jpg')
        await interaction.channel.send(embed=emd)

#inreaction.edit_original_message
@bot.command()
async def unmute(ctx, member: disnake.Member):
        await ctx.channel.purge(limit=1)
        mute_role = disnake.utils.get(ctx.guild.roles, name='mute')
        await member.remove_roles(mute_role)
        emd = disnake.Embed(title='UNMUTE COMMAND', color=0x00ff00)
        emd.add_field(name=f'Пользователь {member.name} был размьючен', value='')
        emd.set_footer(text=f'Пользователь размьючен администранией {ctx.author.name}', icon_url=ctx.author.display_avatar)
        emd.set_thumbnail(url='https://papik.pro/uploads/posts/2023-03/1678835764_papik-pro-p-bolshoi-rot-na-risunke-12.jpg')
        await ctx.send(embed=emd)


@bot.slash_command(description='Вы можете размьютить пользователя.')
async def unmute(interaction, user: disnake.Member):
        mute_role = disnake.utils.get(interaction.guild.roles, name='mute')
        await user.remove_roles(mute_role)
        emd = disnake.Embed(title='UNMUTE COMMAND', color=0x00ff00)
        emd.add_field(name=f'Пользователь {user.name} был размьючен', value='')
        emd.set_footer(text=f'Пользователь размьючен администранией {interaction.author.name}', icon_url=interaction.author.display_avatar)
        emd.set_thumbnail(url='https://papik.pro/uploads/posts/2023-03/1678835764_papik-pro-p-bolshoi-rot-na-risunke-12.jpg')
        await interaction.channel.send(embed=emd)



@bot.command()
async def kick(ctx, user: disnake.Member, *, reason: str = 'Нарушение правил сервера.'):
    if ctx.author.guild_permissions.kick_members:
        await ctx.channel.purge(limit=1)
        await user.kick(reason=reason)
        emd = disnake.Embed(title='KICK COMMAND', color=0x00ff00)
        emd.add_field(name=f'Пользователь {user.name} кикнут', value='')
        emd.set_footer(text=f'Кикнут администрацией {ctx.author.name}', icon_url=ctx.author.display_avatar)
        emd.set_thumbnail(url='https://i.ytimg.com/vi/UnPGk-RjMKc/maxresdefault.jpg')
        await ctx.send(embed=emd)
    else:
        await ctx.send(f'{ctx.author.name}, у вас недостаточно прав')


@bot.slash_command(description='Вы можете кикать пользователей')
async def kick(interaction, user: disnake.Member, *, reason: str = 'Нарушение правил сервера'):
    if interaction.author.guild_permissions.kick_members:
        await user.kick(reason=reason)
        emd = disnake.Embed(title='KICK COMMAND', color=0x00ff00)
        emd.add_field(name=f'Пользователь {user.name} кикнут', value='')
        emd.set_footer(text=f'Кикнут администрацией {interaction.author.name}', icon_url=interaction.author.display_avatar)
        emd.set_thumbnail(url='https://i.ytimg.com/vi/UnPGk-RjMKc/maxresdefault.jpg')
        await interaction.channel.send(embed=emd)
    else:
        await interaction.response.send_message(f'{interaction.author.name}, у вас недостаточно прав')


@bot.command()
async def ban(ctx, user: disnake.Member, *, reason: str = 'Грубое нарушение правил сервера'):
    if ctx.author.guild_permissions.ban_members:
        await ctx.channel.purge(limit=1)
        await user.ban(reason=reason)
        emd = disnake.Embed(title='BAN COMMAND', color=0x00ff00)
        emd.add_field(name=f'Пользователь {user.name} забанен по причине {reason}', value='')
        emd.set_footer(text=f'Забанен администрацией {ctx.author.name}', icon_url=ctx.author.display_avatar)
        emd.set_thumbnail(url='https://a.d-cd.net/c6D_yqaqVvg1ovYmlSm8sc8WBYs-960.jpg')
        await ctx.send(embed=emd)
    else:
        await ctx.send(f'{ctx.author.name}, у вас недостаточно прав')


@bot.slash_command(description='Вы можете банить участников')
async def ban(interaction, user: disnake.Member, *, reason: str = 'Грубое нарушение правил сервера'):
    if interaction.author.guild_permissions.ban_members:
        await user.ban(reason=reason)
        emd = disnake.Embed(title='BAN COMMAND', color=0x00ff00)
        emd.add_field(name=f'Пользователь {user.name} забанен по причине {reason}', value='')
        emd.set_footer(text=f'Заб анен администрацией {interaction.author.name}', icon_url=interaction.author.display_avatar)
        emd.set_thumbnail(url='https://a.d-cd.net/c6D_yqaqVvg1ovYmlSm8sc8WBYs-960.jpg')
        await interaction.channel.send(embed=emd)
    else:
        await interaction.channel.send(f'{interaction.author.name}, у вас недостаточно прав')


@bot.command()
async def unban(ctx, user_id: int):
    await ctx.channel.purge(limit=1)
    emd = disnake.Embed(title='UNBAN COMMAND', color=0x00ff00)
    user = await bot.fetch_user(user_id)
    try:
        await ctx.guild.unban(user)
        emd.add_field(name=f'Пользователь {user.name}, разбанен', value='')
        emd.set_footer(text=f'Разбанен администрацией {ctx.author.name}', icon_url=ctx.author.display_avatar)
        return await ctx.send(embed=emd)
    except disnake.NotFound:
        emd.add_field(name=f'Пользователь не найден | Введите корректный id пользователя', value='')
        return await ctx.send(embed=emd)
    except disnake.Forbidden:
        emd.add_field(name=f'{ctx.author.name}, у вас недостаточно прав', value='')
        return await ctx.send(embed=emd)


@bot.slash_command()
async def unban(interaction, user_id: int):
    emd = disnake.Embed(title='UNABN COMMAND', color=0x00ff00)
    user = await bot.fetch_user(user_id)
    try:
        await interaction.guild.unban(user)
        emd.add_field(name=f'Пользователь {user.name}, был разбанен администарией {interaction.author.name}', value='')
        return await interaction.response.send_message(embed=emd)
    except disnake.NotFound:

        return await interaction.response.send_message(f'Пользователь {user.name}, не найден')
    except disnake.Forbidden:
        emd.add_field(name=f'{interaction.author.name}, у вас недостаточно прав', value='')
        return await interaction.response.send_message(embed=emd)


@bot.command()
async def pay(ctx):
    view = disnake.ui.View()
    cardButton = disnake.ui.Button(label='Картой', style=disnake.ButtonStyle.blurple, emoji='💳')
    cashButton = disnake.ui.Button(label='Наличными', style=disnake.ButtonStyle.green, emoji='💰')
    criptoButton = disnake.ui.Button(label='Криптовалютой', style=disnake.ButtonStyle.danger, emoji='💹')
    otherButton = disnake.ui.Button(label='Другое', style=disnake.ButtonStyle.url, url='https://YouTube.com')

    async def cardcallback(interaction: disnake.Interaction):
        await interaction.response.send_message(f'{interaction.author.name}, вы выбрали оплату картой.')
    cardButton.callback = cardcallback

    async def cashcallback(interaction: disnake.Interaction):
        await interaction.response.send_message(f'{interaction.author.name}, вы выбрали оплату наличными.')
    cashButton.callback = cashcallback

    async def criptocallback(interaction: disnake.Interaction):
        await interaction.response.send_message(f'{interaction.author.name}, вы выбрали оплату криптовалютой.')
    criptoButton.callback = criptocallback

    async def othercallback(interaction: disnake.Interaction):
        await interaction.response.send_message(f'{interaction.author.name}, вы вырбрали оплату другим способом.')
    otherButton.callback = othercallback

    view.add_item(cardButton)
    view.add_item(cashButton)
    view.add_item(criptoButton)
    view.add_item(otherButton)
    await ctx.send(f'Выберите способ оплаты:', view=view)


@bot.command()
async def help(ctx):
    await ctx.channel.purge(limit=1)
    emd = disnake.Embed(title='HELP COMMAND', description=f'{ctx.author.name}, вы сможете узнать команды бота.',  color=0x00ff00)
    emd.add_field(name=f'{PREFIX}q', value='Пишет привет другому пользователю')
    emd.add_field(name=f'{PREFIX}hello', value='Пишет привет боту, а бот вам')
    emd.add_field(name=f'{PREFIX}cls', value='Очищает чат')
    emd.add_field(name=f'{PREFIX}timeout', value='МЬют на время')
    emd.add_field(name=f'{PREFIX}untimeout', value='Снимает ограничения мьюта по времени')
    emd.add_field(name=f'{PREFIX}mute', value='Мьютит пользователя пока не снимут ограничения')
    emd.add_field(name=f'{PREFIX}unmute', value='Размьючивает пользователя')
    emd.add_field(name=f'{PREFIX}kick', value='Удаляет пользователя из сервера')
    emd.add_field(name=f'{PREFIX}ban', value='Ограничивает доступ пользователя к серверу')
    emd.add_field(name=f'{PREFIX}unban', value='Снимает ограничение доступа пользователя к серверу')
    await ctx.send(embed=emd)


bot.run('token_bot')




