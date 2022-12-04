import discord
from discord import channel
import config

from contract_interaction import send_token
from config import  RITU, CHANNEL_NAME,TOKEN, WALLET,HELPFUL_ANSWER,AWESOME_ANSWER,SUPER_USEFUL_ANSWER

client = discord.Client()


#Getting a channel id and sending message on it
@client.event
async def on_ready():
    all_channels = client.get_channel(1048490199405047868) #channel name
    await all_channels.send('Hello, the bot is woken up just now.. zzzhh ')

#https://discord.com/channels/980471733695950908/983722858909945916
#Replying based on user's message

#every 5th time they would be rewarded.


@client.event
async def on_message(message):
    attention_list = ['blockchain','private keys','sha 256','solidity','web3']
    for i in message.content.split():
         if i in attention_list and str(message.channel) == CHANNEL_NAME:   #all_channels = client.get_channel(980471734182498335) #general channel 
            await message.channel.send('Appreciate your time spent!!') 
            #await message.channel.send(f'Hey {message.author.username} thanks for answering')
                   
           # await message.add_reaction('\U0001F525')
            
@client.event
async def on_reaction_add(reaction,user):
    scholar = str(user).split('#')[0]
    if reaction.emoji == '\U0001F525':
        await reaction.message.channel.send(f'{scholar} has given a {reaction}')
        for username in WALLET:
            if username == scholar:        
                txn = await send_token(WALLET[username],AWESOME_ANSWER)
                await reaction.message.channel.send(f'**Proof of reward** -  https://goerli.etherscan.io/tx/{txn.hex()}',mention_author = True) 
        
    if reaction.emoji == '\U0001F44D':
        await reaction.message.channel.send(f'{scholar} has given a {reaction}')
        for username in WALLET:
            if username == scholar:  
                txn = await send_token(WALLET[username],HELPFUL_ANSWER)
                await reaction.message.channel.send(f'**Proof of reward** -  https://goerli.etherscan.io/tx/{txn.hex()}',mention_author = True) 
    
    # if reaction.count == 2:
    #     await reaction.message.channel.send(f'{scholar} has given a {reaction}')
    #     for username in WALLET:
    #         if username == scholar:  
    #             txn = await send_token(WALLET[username],SUPER_USEFUL_ANSWER)
    #             await reaction.message.channel.send(f'**Token of gratitude** -  https://rinkeby.etherscan.io/tx/{txn.hex()}',mention_author = True) 
    # if reaction.count == 1:
    #     await reaction.message.channel.send(f'Hey there {type(str(user))} {str(user)}')
    
client.run(TOKEN)