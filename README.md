# Yuudi

a qqbot under development based nonebot2.

## 已经可以做到

| 指令                 | 描述                            |
| -------------------- | ------------------------------- |
| 在?                  | buzai, cnm                      |
| 戳我                 | 雨滴戳了戳你                    |
| tql 雨滴佬           | 讲一个关于雨滴佬的真实故事      |
| testip \<ip> \<port> | 测试服务器 ICMP 延迟和 TCP 延迟 |
| http \<code>         | 雨滴告诉你 http 状态码的含义    |
| 来点色图             | 乖，要懂得节制噢 →_→            |
| 上号                 | 网抑云, 够味 !                  |

另有 txai 问答以及 古诗文报时。

## 部署

clone 项目 :

```shell
git clone https://github.com/Chendihe4975/Yuudi.git

cd Yuudi
```

推荐使用 poetry :

```shell
pip install poetry
```

考虑到境内特殊的网络环境, 不再推荐使用 `poetry add` 安装依赖 :

```shell
poetry run python -m pip install --upgrade pip

poetry run python -m pip install -r requirements.txt
```

Windows 执行安装 ujson 的时候, 可能会出现报错, ~~可以无视~~ , 自行解决。

复制 `.env.dev.example` , 将其重命名为 `.env.dev` , 并根据自己的情况修改 :

```shell
cp .env.dev.example .env.dev
```

启动 :

```shell
poetry run python bot.py
```

go-cqhttp 配置实例 :

```hjson
{
    ws_reverse_servers: [
        {
            enabled: true
            reverse_url: ws://127.0.0.1:8080/cqhttp/ws
            reverse_api_url: ""
            reverse_event_url: ""
            reverse_reconnect_interval: 3000
        }
    ]
}
```

注意事项 :

nonebot2 版本不能低于 `2.0.0a8.post2` 。

## 关于开源

本项目原定使用 MIT 开源协议, 后来因为使用了 GPL 3.0 的项目的代码而改成了 GPL 3.0 协议, 使用需注意遵守 [GPL 3.0 开源协议](https://www.gnu.org/licenses/gpl-3.0.html) 。即 :

- 如果不修改源代码, 则使用的时候无限制。
- 如果修改了源代码, 也不要求你发布你的修改版或者你修改版的一部分, 但如果你以某种方式向公众发布你的修改版, 你就必须向你的用户提供修改版的源代码。

## 特别感谢

[nonebot / nonebot2](https://github.com/nonebot/nonebot2) ,

[Mrs4s / go-cqhttp](https://github.com/Mrs4s/go-cqhttp) ,

[Lancercmd](https://github.com/Lancercmd) 。