from discord.ext import commands
import httpx 

from cogs.weather import command
class Weathe (commands.cogs):
@bot.slash_command(name = "Weather", name_localization = "Погода", discription = "Get weather information for a city", description_localization = "Информация о погоде в городе")
async def weather(ctx, city_name: str, country_code: str, limit: str):
    api_key = "a1303766d15807177046fa911a6acbb2"
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit={limit}&appid={api_key}"

    async with httpx.AsyncClient() as Client:
        response = await client.get()


