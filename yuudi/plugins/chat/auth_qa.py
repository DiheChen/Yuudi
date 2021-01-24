'''
Author: DiheChen
Date: 2020-12-31 12:37:25
LastEditors  : DiheChen
LastEditTime : 2021-01-04 21:47:41
Description: None
GitHub: https://github.com/Chendihe4975
'''
import aiohttp
import nonebot
import re
import random
import time
import string
from hashlib import md5
from urllib.parse import quote_plus
from nonebot.plugin import on_message
try:
    import ujson as json
except ImportError:
    import json
from loguru import logger
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.typing import T_State
from nonebot.exception import ActionFailed

config = nonebot.get_driver().config
app_id = str(config.tencent_app_id)
app_key = config.tencent_app_key

cq_code_pattern = re.compile(r'\[CQ:\w+,.+\]')
salt = None

chat = on_message(priority=5, block=True)


def getReqSign(params: dict) -> str:
    hashed_str = ''
    for key in sorted(params):
        hashed_str += key + '=' + quote_plus(params[key]) + '&'
    hashed_str += 'app_key='+app_key
    sign = md5(hashed_str.encode())
    return sign.hexdigest().upper()


def rand_string(n=8):
    return ''.join(
        random.choice(string.ascii_uppercase + string.digits)
        for _ in range(n))


@chat.got('msg')
async def _(bot: Bot, event: Event, state: T_State):
    if not random.randint(1, 100) <= 1:
        return
    msg = event.get_plaintext()
    if msg.startswith(f'[CQ:at,qq={bot.self_id}]'):
        return
    text = re.sub(cq_code_pattern, '', msg).strip()
    global salt
    if salt is None:
        salt = rand_string()
    session_id = md5((str(event.user_id)+salt).encode()).hexdigest()
    param = {
        'app_id': app_id,
        'session': session_id,
        'question': text,
        'time_stamp': str(int(time.time())),
        'nonce_str': rand_string(),
    }
    sign = getReqSign(param)
    param['sign'] = sign
    async with aiohttp.request(
        'POST',
        'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat',
        params=param,
    ) as response:
        code = response.status
        if code != 200:
            raise ValueError(f'bad server http code: {code}')
        res = await response.read()
    param = json.loads(res)
    if param['ret'] != 0:
        raise ValueError(param['msg'])
    reply = param['data']['answer']
    try:
        await chat.send(Message(reply))
    except ValueError as e:
        logger.info(f'api call failed : {e}')
    except ActionFailed as e:
        logger.error(
            f'ActionFailed | {e.info["msg"].lower()} | retcode = {e.info["retcode"]} | {e.info["wording"]}'
        )
        return
