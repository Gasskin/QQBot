import random
from datetime import date
from nonebot.plugin import on_keyword,on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message

bfz = on_command("bfz",aliases={"本分值"})
@bfz.handle()
async def bfz_handle(bot: Bot, event: Event):
    msg = str(event.get_message())
    arr = msg.split(" ")
    res = float(arr[1])/(float(arr[2])-float(arr[3]))
    rnd = random.Random()
    rnd.seed(int(date.today().strftime("%y%m%d")) + int(event.get_user_id()))
    lucknum = rnd.randint(1,100)
    joy =""
    if lucknum>50:
        joy="，鉴定为肉猪"
    await bfz.finish(Message(f'[CQ:at,qq={event.get_user_id()}]一眼本分:{round(res,2)}{joy}'))