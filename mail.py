import aiohttp
from bs4 import BeautifulSoup
from telethon import TelegramClient, events
import telethon
import os
user_agent = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.465 (Edition Yx GX)',
}
TOKEN = os.environ.get('token_bot')
WORKERS_URL = os.environ.get("workers_url")
api_id = xxxxxxx
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
client = TelegramClient('haxwoibot', api_id, api_hash)
client.start(bot_token=TOKEN)
@client.on(events.NewMessage(pattern=r'/hax'))
async def handler(event: telethon.types.Message):
    await event.reply("hax.co.id:\n" + (await grab(host="hax.co.id")))
@client.on(events.NewMessage(pattern=r'/woiden'))
async def handler(event: telethon.types.Message):
    await event.reply("woiden.id:\n" + (await grab(host="woiden.id")))
@client.on(events.NewMessage(pattern=r'/both'))
async def handler(event: telethon.types.Message):
    await event.reply("hax.co.id:\n" + (await grab(host="hax.co.id")) + "\nwoiden.id:\n"+ (await grab(host="woiden.id")))
@client.on(events.InlineQuery)
async def handler(event):
    if event.text != "": return
    a,b = "hax.co.id:\n"+ (await grab(host="hax.co.id")), "woiden.id:\n"+ (await grab(host="woiden.id"))
    builder = event.builder 
    await event.answer( 
    [builder.article(title="hax.co.id", description=a, text=a), 
    builder.article(title="woiden.id", description=b, text=b),
    builder.article(title="both", description=a+'\n'+b, text=a+'\n'+b)] #trying_to_set_that_user_profile_photo_here 
    )

async def grab(host="hax.co.id"):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://{WORKERS_URL}/https://{host}/create-vps', headers=user_agent) as response:
            if response.status != 200: return f"something went wrong. aiohttp could not connect to woiden server. Error Code: {response.status}"
            a = await response.text()
            soup = BeautifulSoup(a, 'html.parser')
            founds = soup.find(id="datacenter").find_all("option")[1:]
            result = ""
            if len(founds) == 0:
                return "No seats appears now"
            for i in founds:
                result += f"{i.text}\n"
            return result


client.run_until_disconnected()
