'''
Author       : DiheChen
Date         : 2021-01-05 01:32:37
LastEditors  : DiheChen
LastEditTime : 2021-01-05 02:34:48
Description  : None
GitHub       : https://github.com/Chendihe4975
'''
# 部分内容是从 [Ice-Cirno / HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot) 上抄来的
import time
from collections import defaultdict
from datetime import datetime, timedelta
from nonebot import require
import pytz
import collections
from matplotlib import pyplot as plt


class FreqLimiter:
    def __init__(self, default_cd_seconds):
        self.next_time = defaultdict(float)
        self.default_cd = default_cd_seconds

    def check(self, key) -> bool:
        return bool(time.time() >= self.next_time[key])

    def start_cd(self, key, cd_time=0):
        self.next_time[key] = time.time() + (cd_time if cd_time > 0 else self.default_cd)

    def left_time(self, key) -> float:
        return self.next_time[key] - time.time()
                                            

class DailyNumberLimiter:
    tz = pytz.timezone('Asia/Shanghai')
    
    def __init__(self, max_num):
        self.today = -1
        self.count = defaultdict(int)
        self.max = max_num

    def check(self, key) -> bool:
        now = datetime.now(self.tz)
        day = (now - timedelta(hours=5)).day
        if day != self.today:
            self.today = day
            self.count.clear()
        return bool(self.count[key] < self.max)

    def get_num(self, key):
        return self.count[key]

    def increase(self, key, num=1):
        self.count[key] += num

    def reset(self, key):
        self.count[key] = 0