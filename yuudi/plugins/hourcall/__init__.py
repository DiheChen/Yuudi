'''
Author: DiheChen
Date: 2020-12-17 22:17:35
LastEditors  : DiheChen
LastEditTime : 2021-01-05 02:11:23
Description: None
GitHub: https://github.com/Chendihe4975
'''
import aiohttp
try: 
    import ujson as json
except ImportError:
    import json
import nonebot
import pytz
import datetime
import asyncio
from nonebot import require
from nonebot.log import logger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from yuudi import getBot

scheduler = require('nonebot_plugin_apscheduler').scheduler

@scheduler.scheduled_job('cron', hour='*')
async def _():
    tz = pytz.timezone('Asia/Shanghai')
    nowtime = datetime.datetime.now(tz).strftime("%H:%M")
    bot = getBot()
    async with aiohttp.request(
        'POST',
        'https://v1.jinrishici.com/all.json'
    ) as resp:
        res = await resp.json()
        poem = res["content"]
    msg = f"现在时间: {nowtime}" + "\n" + poem
    gl = await bot.call_api('get_group_list')
    gl = [ g['group_id'] for g in gl ]
    for g in gl:
        await asyncio.sleep(0.5)
        try:
            await bot.send_msg(message_type='group', group_id=g, message=msg)
        except Exception as e:
            logger.error(f'Error: {type(e)}')
