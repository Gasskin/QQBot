import random
from datetime import date
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message

bfz = on_command("bfz",aliases={"本分值"})
@bfz.handle()
async def bfz_handle(bot: Bot, event: Event):
    arr = str(event.get_message()).split(" ")
    if len(arr)!=4:
        await bfz.finish(Message(f'[CQ:at,qq={event.get_user_id()}]草拟吗的参数都输不对你算个锤子呢你'))
    dps = float(arr[1])
    tps = float(arr[2])
    hps = float(arr[3])
    if(tps-hps<=0):
        await bfz.finish(Message(f'[CQ:at,qq={event.get_user_id()}]TPS比HPS还高，超人类是吧'))
    res = dps/(tps-hps)

    rnd = random.Random()
    rnd.seed(int(date.today().strftime("%y%m%d")) + int(event.get_user_id()))
    lucknum = rnd.randint(1,100)
    joy =""
    if lucknum>50:
        joy="，鉴定为肉猪"
    await bfz.finish(Message(f'[CQ:at,qq={event.get_user_id()}]一眼本分:{round(res,2)}{joy}'))