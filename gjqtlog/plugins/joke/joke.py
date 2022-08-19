import pathlib
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import MessageSegment
import requests
from PIL import Image
from io import BytesIO
from PIL import Image
import os
import random

path = "plugins/joke/img"

joke = on_command("pig joke",aliases={"肉猪笑话"})
@joke.handle()
async def joke_handle(bot: Bot, event: Event):
    name = get_random_img_name()
    if name == " ":
        await joke.finish()
    img = f"{path}/{name}"
    abs = os.path.abspath(img)
    await joke.finish(MessageSegment.image(f"file:///{abs}"))

def get_random_img_name()->str:
    files = os.listdir(path)
    length = len(files)
    if length <= 0:
        return " "
    rd = random.randint(0,length-1)
    img = files[rd]
    return img