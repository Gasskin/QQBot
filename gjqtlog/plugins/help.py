from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message

help = on_command("help",aliases={"帮助文档"})
@help.handle()
async def help_handle(bot: Bot, event: Event):
    await help.finish("计算本分值：/本分值 dps tps hps 或者 /bfz dps tps hps\n" +
                      "上传肉猪笑话：/up pig 一张图片\n"+
                      "获取肉猪笑话：/肉猪笑话 或者 /pig joke")