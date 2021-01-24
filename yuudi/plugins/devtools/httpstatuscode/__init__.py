'''
Author: DiheChen
Date: 2020-12-31 18:46:49
LastEditors  : DiheChen
LastEditTime : 2021-01-04 20:42:33
Description: None
GitHub: https://github.com/Chendihe4975
'''
import os
try:
	import ujson as json
except:
	import json
from loguru import logger
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.event import MessageEvent
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.exception import ActionFailed
from nonebot.permission import SUPERUSER
from nonebot.plugin import on_command
from nonebot.typing import T_State

try:
    file = os.path.join(os.path.dirname(__file__), 'httpstatuscode.json')
    with open(file, encoding='utf8') as f:
        httpstatuscode = json.load(f)
except FileNotFoundError:
    logger.error(f'file not found...')

statuscode = on_command("http", aliases = {"HTTP"})

@statuscode.handle()
async def http_status(bot: Bot, event: Event, state: dict):
    code = event.message.extract_plain_text()
    res = Message(f'[CQ:image,file=https://http.cat/{str(code)}.jpg]')
    if not code.isdigit():
        return
    msg = httpstatuscode[code] + res
    await statuscode.send(msg)
