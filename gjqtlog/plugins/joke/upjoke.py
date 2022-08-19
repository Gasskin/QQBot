from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
import requests
from PIL import Image
from io import BytesIO
from PIL import Image
import re
import datetime

path = "./plugins/joke/img"

uppig = on_command("up pig")
@uppig.handle()
async def uppig_handle(bot: Bot, event: Event):
    url = re.search(r"https.*term=3",str(event.get_message()))
    res = str(url.group())
    if res == "None":
        uppig.finish()
    response = requests.get(res)
    image = Image.open(BytesIO(response.content))
    image.save(f"{path}/{datetime.datetime.now().timestamp()}.png")
    await uppig.finish()
 