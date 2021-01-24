'''
Author: DiheChen
Date: 2020-12-31 01:08:54
LastEditors  : DiheChen
LastEditTime : 2021-01-04 20:46:18
Description: None
GitHub: https://github.com/Chendihe4975
'''
from loguru import logger
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.plugin import on_command
from nonebot.typing import T_State
from nonebot.exception import ActionFailed
from nonebot.permission import SUPERUSER

say = on_command("say", aliases={"echo"}, permission=SUPERUSER)


@say.handle()
async def say_unescape(bot: Bot, event: Event, state: T_State):
    try:
        await bot.send(message=Message(event.get_plaintext()), event=event)
    except ActionFailed as e:
        logger.error(
            f'ActionFailed | {e.info["msg"].lower()} | retcode = {e.info["retcode"]} | {e.info["wording"]}'
        )
        return
