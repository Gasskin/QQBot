from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message

help_log = """帮助文档：
【本分值】
计算：/bfz dps tps hps
【肉猪笑话】
上传：/up pig 图片
获取：/肉猪笑话
"""

help = on_command("help",aliases={"帮助文档"})
@help.handle()
async def help_handle(bot: Bot, event: Event):
    await help.finish(help_log)