#coding: utf-8

import settings.py
import discord

YOUR_TOKEN = settings.AP
client = discord.Client()

@client.event
async def on_ready():
    print('Bot Name:' , client.user.name)
    print('Client ID：' , client.user.id)
    print('------')

@client.event
async def on_message(message):
    # BOTとメッセージの送り主が同じ人なら処理しない
    if client.user == message.author:
        return

    if message.content.startswith('!help'):
        await message.channel.send('現在使用できるコマンドは次の通りです。ただし、コマンドの前には __::__ を付けてください。\n')
        await message.channel.send('``` hello\n system call generate aerial element burst element\n kyomu\n hey siri```')

    elif message.content.startswith('::hello'):
        # await client.send_message(message.channel, 'こんにちは') #これ使えん
        await message.channel.send('おはよおぉぉ！！！\nこんちはぁぁぁぁ！！！\nこんばんはぁぁぁあ！！！\nおやすみぃぃぃぃ！！！\nおぎてぇエェエェえええええ！！！！')

    elif message.content.startswith('::system call generate aerial element burst element'):
        await message.channel.send('**ﾋﾞｭｰｰｰｰｰｰｰｰｰｰｰｰｰｰﾝ**\n上に行きます！上に行きます！\n')

    elif message.content.startswith('::kyomu'):
        await message.channel.send('__#ツイッターせずに飯食え教務\n#後輩に意地悪するな教務\n#教務を許すな__')

    elif message.content.startswith('::hey siri'):
        await message.channel.send('私はクローバです。')

    elif message.content.startswith('::vote'):
        await message.channel.send('以下に半角空白で区切りながら任意の日付けを羅列させてください。\n')

        user_input = input()

        if user_input is not None:
            # letters = user_input.split()
            await message.channel.send('テストー\n')
            # print('テストー\n')


client.run(TOKEN)
