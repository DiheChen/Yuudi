'''
Author       : DiheChen
Date         : 2021-01-04 17:03:33
LastEditors  : DiheChen
LastEditTime : 2021-01-04 17:32:11
Description  : None
GitHub       : https://github.com/Chendihe4975
'''
import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot

nonebot.init()
driver = nonebot.get_driver()
app = nonebot.get_asgi()
driver.register_adapter("cqhttp", CQHTTPBot)
# nonebot.load_builtin_plugins()
nonebot.load_plugins("yuudi/plugins")

if __name__ == "__main__":
    nonebot.run()