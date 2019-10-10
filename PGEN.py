import discord
import math
import random
from discord.ext import commands
from discord import Embed
import webbrowser
import json
import random




client = commands.Bot(command_prefix='!')

accounts = []

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
    await client.change_presence(status=discord.Status.online,
                activity=discord.Game("!help for helping commands"))
    


@client.command()
async def helper(ctx):
    Disembed = discord.Embed(
        title = 'Bot Information',
        description = 'This Displays Information About Bot',
        colour = discord.Colour.blue()
        
    )
    Disembed.add_field(name="!stock <add/remove> <type> <file path>", value="stocks it to the server")
    Disembed.add_field(name="!clearStock <type>", value="clears values from the server")
    Disembed.add_field(name="!getAccount <type>", value="Get Your Account")
    
   
    Disembed.add_field(name="Youtube Channel: ", value="https://www.youtube.com/channel/UCLtcXpEuZo-Px7Hzm_tflGQ?view_as=subscriber")
    
    

@client.command()
async def BotsInfo(ctx):
    # Learn RichEmbed
    Disembed = discord.Embed(
        title = 'Bot Information',
        description = 'This Displays Information About Bot',
        colour = discord.Colour.blue()
        
    )
    Disembed.add_field(name="Join If You Want To Create Your Bot", value="https://discord.gg/TEe4kYX")
    Disembed.add_field(name="Programmer", value="Saugat Siddiky Jarif")
    Disembed.add_field(name="Bot Name: ", value=client.user.name)
    
   
    Disembed.add_field(name="Youtube Channel: ", value="https://www.youtube.com/channel/UCLtcXpEuZo-Px7Hzm_tflGQ?view_as=subscriber")
    Disembed.set_thumbnail(url="https://yt3.ggpht.com/-M8WKk6aG50Q/AAAAAAAAAAI/AAAAAAAAATU/dMuWHFK4VOo/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg")
    
    

    await ctx.send(embed=Disembed)
    


@client.command()
@commads.has_any_role("Admin", "administrator", "admin", "Moderator", "moderator", "Owner", "owner", "Dropper/Restocker", "dropper/restocker")        
async def stock(ctx, Type:str, typeOfAccount:str, typeOfFile:str):
    if Type == 'add':
        if typeOfAccount == 'fortnite':
            
            account_array = []

            # Read To JSON
            with open(typeOfFile, 'r') as fileReader:
                for row in fileReader:
                        account_array.append(row)
            # Write To JSON
            with open('fortnite.json', 'w') as json_file:
                json.dump(account_array, json_file)
            
            await ctx.send("Stock Completed! Yay")

        elif typeOfAccount == 'nordvpn':
            
            account_array = []

            # Read To JSON
            with open(typeOfFile, 'r') as fileReader:
                for row in fileReader:
                        account_array.append(row)
    
            # Write To JSON
            with open('nordvpn.json', 'w') as json_file:
                json.dump(account_array, json_file)

            await ctx.send("Stock Completed! Yay")

        elif typeOfAccount == 'hulu':
            
            account_array = []

            # Read To JSON
            with open(typeOfFile, 'r') as fileReader:
                for row in fileReader:
                        account_array.append(row)
    
            # Write To JSON
            with open('hulu.json', 'w') as json_file:
                json.dump(account_array, json_file)
            await ctx.send("Stock Completed! Yay")
        elif typeOfAccount == 'crunchyroll':
            
            account_array = []

            # Read To JSON
            with open(typeOfFile, 'r') as fileReader:
                for row in fileReader:
                    account_array.append(row)

            # Write To JSON
            with open('crunchyroll.json', 'w') as json_file:
                json.dump(account_array, json_file)
        
            await ctx.send("Stock Completed! Yay")  
    
@client.command()
async def getAccount(ctx, Type : str):
    
    if (Type == 'fortnite'):
        # For Loop To Get The First Index
        
        with open('fortnite.json', 'r') as json_file:
            accounts = json.load(json_file)
            account_lenght = len(accounts)

            if (account_lenght < 1):
                await ctx.send("Out Of Stock! Call Admin/Stocker For Help!")
                return
                                        
            random.shuffle(accounts)
            Disembed = discord.Embed(
                title = 'Bot Information',
                description = 'This Displays Information About Bot',
                colour = discord.Colour.blue()
                
            )
            Disembed.add_field(name="Join If You Want To Create Your Bot", value="https://discord.gg/TEe4kYX")
            Disembed.add_field(name="Programmer", value="Saugat Siddiky Jarif")
            Disembed.add_field(name="Bot Name: ", value=client.user.name)
            
           
            Disembed.add_field(name="Youtube Channel: ", value="https://www.youtube.com/channel/UCLtcXpEuZo-Px7Hzm_tflGQ?view_as=subscriber")
            Disembed.set_thumbnail(url="https://yt3.ggpht.com/-M8WKk6aG50Q/AAAAAAAAAAI/AAAAAAAAATU/dMuWHFK4VOo/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg")
            
            await ctx.send("Please Check Your DM!")
            await ctx.author.send("Here Is Your Account Enjoy! {}".format(accounts[0]))
            await ctx.author.send(embed=Disembed)
            
    elif (Type == 'nordvpn'):
        
        with open('nordvpn.json', 'r') as json_file:
            accounts = json.load(json_file)
            account_lenght = len(accounts)

            if (account_lenght < 1):
                await ctx.send("Out Of Stock! Call Admin/Stocker For Help!")
                return
  
                                        # adjust this boundaries to fit your needs
            random.shuffle(accounts)
            Disembed = discord.Embed(
                title = 'Bot Information',
                description = 'This Displays Information About Bot',
                colour = discord.Colour.blue()
                
            )
            Disembed.add_field(name="Join If You Want To Create Your Bot", value="https://discord.gg/TEe4kYX")
            Disembed.add_field(name="Programmer", value="Saugat Siddiky Jarif")
            Disembed.add_field(name="Bot Name: ", value=client.user.name)
            
           
            Disembed.add_field(name="Youtube Channel: ", value="https://www.youtube.com/channel/UCLtcXpEuZo-Px7Hzm_tflGQ?view_as=subscriber")
            Disembed.set_thumbnail(url="https://yt3.ggpht.com/-M8WKk6aG50Q/AAAAAAAAAAI/AAAAAAAAATU/dMuWHFK4VOo/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg")
            
    
            
            await ctx.send("Please Check Your DM!")
            await ctx.author.send("Here Is Your Account Enjoy! {}".format(accounts[0]))
            await ctx.author.send(embed=Disembed)
            
    elif (Type == 'hulu'):
        # For Loop To Get The First Index
        with open('hulu.json', 'r') as json_file:
            accounts = json.load(json_file)
            account_lenght = len(accounts)
  
            if (account_lenght < 1):
                await ctx.send("Out Of Stock! Call Admin/Stocker For Help!")
                return

            
            random.shuffle(accounts)
            Disembed = discord.Embed(
                title = 'Bot Information',
                description = 'This Displays Information About Bot',
                colour = discord.Colour.blue()
                
            )
            Disembed.add_field(name="Join If You Want To Create Your Bot", value="https://discord.gg/TEe4kYX")
            Disembed.add_field(name="Programmer", value="Saugat Siddiky Jarif")
            Disembed.add_field(name="Bot Name: ", value=client.user.name)
            
           
            Disembed.add_field(name="Youtube Channel: ", value="https://www.youtube.com/channel/UCLtcXpEuZo-Px7Hzm_tflGQ?view_as=subscriber")
            Disembed.set_thumbnail(url="https://yt3.ggpht.com/-M8WKk6aG50Q/AAAAAAAAAAI/AAAAAAAAATU/dMuWHFK4VOo/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg")
            
     
            await ctx.send("Please Check Your DM!")
            await ctx.author.send("Here Is Your Account Enjoy! {}".format(accounts[0]))
            await ctx.author.send(embed=Disembed)

    elif (Type == 'crunchyroll'):
        
        with open('crunchyroll.json', 'r') as json_file:
            accounts = json.load(json_file)
            account_lenght = len(accounts)

            if (account_lenght < 1):
                await ctx.send("Out Of Stock! Call Admin/Stocker For Help!")
                return

            Disembed = discord.Embed(
                title = 'Bot Information',
                description = 'This Displays Information About Bot',
                colour = discord.Colour.blue()
                
            )
            Disembed.add_field(name="Join If You Want To Create Your Bot", value="https://discord.gg/TEe4kYX")
            Disembed.add_field(name="Programmer", value="Saugat Siddiky Jarif")
            Disembed.add_field(name="Bot Name: ", value=client.user.name)
            
           
            Disembed.add_field(name="Youtube Channel: ", value="https://www.youtube.com/channel/UCLtcXpEuZo-Px7Hzm_tflGQ?view_as=subscriber")
            Disembed.set_thumbnail(url="https://yt3.ggpht.com/-M8WKk6aG50Q/AAAAAAAAAAI/AAAAAAAAATU/dMuWHFK4VOo/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg")
            

            random.shuffle(accounts)

            await ctx.send("Please Check Your DM!")
            await ctx.author.send("Here Is Your Account Enjoy! {}".format(accounts[0]))
            await ctx.author.send(embed=Disembed)

               
      
@client.command()
async def clearStock(ctx, Type : str):
    if (Type == 'fortnite'):
        remove_array = []
        with open('fortnite.json', 'w') as json_file:
            json.dump(remove_array, json_file)
        await ctx.send("Cleared Stock By: {}".format(ctx.author.name))

    elif (Type == 'nordvpn'):
        remove_array = []
        with open('nordvpn.json', 'w') as json_file:
            json.dump(remove_array, json_file)
        await ctx.send("Cleared Stock By: {}".format(ctx.author.name))

    elif (Type == 'hulu'):
        remove_array = []
        with open('hulu.json', 'w') as json_file:
            json.dump(remove_array, json_file)
        await ctx.send("Cleared Stock By: {}".format(ctx.author.name))
    elif (Type == 'crunchyroll'):
        remove_array = []
        with open('crunchyroll.json', 'w') as json_file:
            json.dump(remove_array, json_file)
        await ctx.send("Cleared Stock By: {}".format(ctx.author.name))

@client.command()
async def stockInfo(ctx, Type : str):
    if (Type == 'fortnite'):
        
        with open('fortnite.json', 'r') as json_file:
            accounts = json.load(json_file)
            account_lenght = len(accounts)
        await ctx.send("Fortnite Account In Stock: {}".format(len(accounts)))
            
    elif (Type == 'nordvpn'):
        with open('nordvpn.json', 'r') as json_file:
            accounts = json.load(json_file)
            account_lenght = len(accounts)
        await ctx.send("NordVPN Account In Stock: {}".format(len(accounts)))
        
    elif (Type == 'hulu'):
        with open('hulu.json', 'r') as json_file:
            accounts = json.load(json_file)
            account_lenght = len(accounts)
        await ctx.send("hulu Account In Stock: {}".format(len(accounts)))
        
    elif (Type == 'crunchyroll'):
        with open('crunchyroll.json', 'r') as json_file:
            accounts = json.load(json_file)
            account_lenght = len(accounts)
        await ctx.send("crunchyroll Account In Stock: {}".format(len(accounts)))
    


client.run(TOKEN)
