import discord
from discord import app_commands
import requests
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
     

@tree.command(name = "weather", description = "Gives you current weather")
async def weather_command(interaction,*, place: str):
    response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={key}&q={place}&days=1&aqi=no&alerts=no').json()
    temp = response['current']['temp_c']
    await interaction.response.send_message(f"{place}'s tempreature: {temp}°C")   
                             
    
@client.event
async def on_ready():
    await tree.sync()
    c.start()
    print("Ready!")   
  client.run(TOKEN)
