'''
Author: DiheChen
Date: 2020-12-31 20:53:33
LastEditors  : DiheChen
LastEditTime : 2021-01-04 21:52:22
Description: None
GitHub: https://github.com/Chendihe4975
'''
from nonebot import on_notice
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.event import MessageEvent
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.plugin import on_command
from nonebot.typing import T_State
from loguru import logger
from nonebot.exception import ActionFailed
from nonebot.adapters.cqhttp import PokeNotifyEvent

pokecmd = on_command('戳我', aliases={'戳一戳我'}, block=True)


@pokecmd.handle()
async def poke_me(bot: Bot, event: Event, state: dict):
    user_id = event.user_id
    try:
        await pokecmd.finish(Message(f"[CQ:poke,qq={user_id}]"))
    except ActionFailed as e:
        logger.error(
            f'ActionFailed | {e.info["msg"].lower()} | retcode = {e.info["retcode"]} | {e.info["wording"]}'
        )
        return


async def group_poke(bot: Bot, event: Event, state: T_State) -> bool:
    if event.target_id == event.self_id and event.user_id != event.self_id:
        return isinstance(event, PokeNotifyEvent)

poke = on_notice(group_poke, priority=10, block=True)
poke.handle()(poke_me)
