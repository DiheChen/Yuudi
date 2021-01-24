'''
Author       : DiheChen
Date         : 2021-01-08 00:58:29
LastEditors  : DiheChen
LastEditTime : 2021-01-08 02:34:34
Description  : None
GitHub       : https://github.com/Chendihe4975
'''
import asyncio
import aiohttp
import random
import string
try:
    import ujson as json
except ImportError:
    import json
from nonebot.plugin import on_command
from nonebot.typing import T_State
from loguru import logger
from nonebot.adapters.cqhttp.message import Message
from nonebot.exception import ActionFailed
from nonebot.adapters import Bot, Event

shanghao = on_command(
    "上号", aliases={"网抑云", "网易云", "生而为人", "生不出人", "抑郁", "已黑化", "到点了"})

async def getres(rand_string):
    try:
        async with aiohttp.request(
            'GET',
            url=f'http://nd.2890.ltd/api/?format={rand_string}'
        ) as resp:
            pretreatment = await resp.read()
            res = eval(pretreatment)
            return res["data"]["content"]["content"]
    except Exception as e:
        return f"Error : {e}"

@shanghao.handle()
async def pushres(bot: Bot, event: Event, state: T_State):
    rand_string = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    msg = await getres(rand_string)
    try:
        await shanghao.send(msg)
    except ActionFailed as e:
        await shanghao.send("上号失败, 我很抱歉。")
        logger.error(
            f'ActionFailed | {e.info["msg"].lower()} | retcode = {e.info["retcode"]} | {e.info["wording"]}'
        )
