'''
Author       : DiheChen
Date         : 2021-01-05 01:35:52
LastEditors  : DiheChen
LastEditTime : 2021-01-05 02:42:20
Description  : None
GitHub       : https://github.com/Chendihe4975
'''
from nonebot.plugin import on_command
from nonebot.typing import T_State
from loguru import logger
from nonebot.adapters.cqhttp.message import Message
from nonebot.exception import ActionFailed
from nonebot.adapters import Bot, Event
from yuudi.util import FreqLimiter, DailyNumberLimiter

setu = on_command(
    "setu", aliases={"色图", "涩图", "来点色图", "来点涩图", "看过了", "不够色", "就这", "铜"})

setudlmt = DailyNumberLimiter(30)
setuflmt = FreqLimiter(15)


def get_setu():
    return f"[CQ:image,cache=0,file=https://michikawachin.art/]"


@setu.handle()
async def push_setu(bot: Bot, event: Event, state: T_State):
    user_id = event.user_id
    if not setudlmt.check(user_id):
        await setu.send("您今天已经冲了10次了, 雨滴很担心你, 还是明天再冲吧。")
    if not setuflmt.check(user_id):
        await setu.send("您冲得太快了，小心人没了！")
    try:
        pic = get_setu()
        setudlmt.increase(user_id)
        setuflmt.start_cd(user_id)
        await setu.send(Message(pic))
    except ActionFailed as e:
        logger.error(
            f'ActionFailed | {e.info["msg"].lower()} | retcode = {e.info["retcode"]} | {e.info["wording"]}'
        )
