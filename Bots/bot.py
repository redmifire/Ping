import discord

from cogs.calc import Calculator
bot = discord.Bot()

bot.add_cog(Calculator(bot))

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    

@bot.slash_command(name = "hello", name_localization={"ru": "Привет"}, description = "Say hello to the bot", description_localization={"ru": "Напишите привет боту"})
async def huh354(ctx):
    await ctx.respond("Hey!")

    
bot.run("MTEzODc3MDA4OTAwMTM2NTU2NA.GR_4c4.oQ7ac6Kzney3jvP2GOPAQUzfCcmrAJu81xENI0")


