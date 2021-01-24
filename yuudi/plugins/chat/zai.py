'''
Author: DiheChen
Date: 2021-01-01 20:18:29
LastEditors  : DiheChen
LastEditTime : 2021-01-04 21:51:03
Description: None
GitHub: https://github.com/Chendihe4975
'''
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from loguru import logger
from nonebot.exception import ActionFailed
from nonebot.adapters import Bot, Event

zai = on_command("在", aliases = {'在?', 'zai?', '在？', '在吗', '在么？', '在嘛', '在嘛？'}, rule=to_me())
 
@zai.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    try:
        await zai.finish("在的哦~")
    except ActionFailed as e:
        logger.error(
            f'ActionFailed | {e.info["msg"].lower()} | retcode = {e.info["retcode"]} | {e.info["wording"]}'
        )
        return