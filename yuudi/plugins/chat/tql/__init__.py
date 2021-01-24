'''
Author: DiheChen
Date: 2021-01-01 16:03:36
LastEditors  : DiheChen
LastEditTime : 2021-01-04 20:48:49
Description: None
GitHub: https://github.com/Chendihe4975
'''
import os
import random
from loguru import logger
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.plugin import on_command
from nonebot.typing import T_State
from nonebot.exception import ActionFailed

tql = on_command("tql", aliases={"太强了"})

file = os.path.join(os.path.dirname(__file__), 'tql.txt')
with open(file, encoding='utf8') as txt:
    data = txt.read().split('\n')


@tql.handle()
async def say_tql(bot: Bot, event: Event, state: T_State):
    name = event.message.extract_plain_text()
    if name == '':
        return
    s = random.choice(data)
    result = s.replace('%name%', name)
    try:
        await tql.finish(result)
    except ActionFailed as e:
        logger.error(
            f'ActionFailed | {e.info["msg"].lower()} | retcode = {e.info["retcode"]} | {e.info["wording"]}'
        )
        return
