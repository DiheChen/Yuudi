'''
Author       : DiheChen
Date         : 2021-01-05 01:31:24
LastEditors  : DiheChen
LastEditTime : 2021-01-05 02:18:40
Description  : None
GitHub       : https://github.com/Chendihe4975
'''
import nonebot
from nonebot.adapters import Bot, Event, Message

def getBot() -> Bot:
    return list(nonebot.get_bots().values())[0]