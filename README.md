>😀疫情期间学校要求打卡，本来只用签到一个，慢慢的成了两个。为了不浪费时间，于是在小伙伴群里写了个签到脚本并挂在nonbot机器人上，借此分享一下

<!-- more -->
## 软件准备
手机抓包软件：Stream
PC：酷Q机器人
## 开发环境
Python 3.6
## 使用框架
nonbot、requests（具体不在赘述）
## 签到实现思路
1. 第一步
按照我的想法，本质是一个Post提交数据的过程，只需要用requests库中的Post方法提交即可。
2. 第二步
我在电脑登陆打卡的网站，发现不能访问，然后我再用手机访问，发现可以正常访问。于是，我猜测是根据请求头浏览器的不同来限定。
3. 第三步
![](file://C:/Users/liujian/Documents/Gridea/post-images/1585702674282.png)
我使用Stream找到我手机浏览器的User-Agent通过requests的get方法，成功访问。
4. 第四步
使用一个没有签到过的账号，Stream开启抓包，然后进行签到，在数据包中优先查看Post方法。最终找到提交的数据
![](file://C:/Users/liujian/Documents/Gridea/post-images/1585703066515.png)
查看数据格式后提交即可
```python
re = requests.post(submit_url,json=json,headers=my_header)
re.encoding=re.apparent_encoding
print(re.text)
```
登陆查看发现成功签到
## nonebot+酷Q构建机器人
>至此核心功能已经实现，为了方便小伙伴所以使用nonebot框架配合酷Q实现签到指令
1. 简单介绍
NoneBot 是一个基于 酷 Q 的 Python 异步 QQ 机器人框架，它会对 QQ 机器人收到的消息进行解析和处理，并以插件化的形式，分发给消息所对应的命令处理器和自然语言处理器，来完成具体的功能。
除了起到解析消息的作用，NoneBot 还为插件提供了大量实用的预设操作和权限控制机制，尤其对于命令处理器，它更是提供了完善且易用的会话机制和内部调用机制，以分别适应命令的连续交互和插件内部功能复用等需求。
NoneBot 在其底层与酷 Q 交互的部分使用 python-aiocqhttp 库，后者是 CoolQ HTTP API 插件 的一个 Python 异步 SDK，在 Quart 的基础上封装了与 CoolQ HTTP API 插件的网络交互。
2. 具体实现
![酷Q下载地址](https://cqp.cc/t/23253)

![](file://C:/Users/liujian/Documents/Gridea/post-images/1585703768721.png)
打开CQA.exe，登陆之后就可以了。
然后我们开始下载HTTP API 插件
![HTTP API 插件下载地址](https://github.com/richardchien/coolq-http-api/releases
x)
下载完之后我们把文件直接放到酷q的插件目录
![](file://C:/Users/liujian/Documents/Gridea/post-images/1585703931226.png)
r然后右键酷q的图标，选择应用管理，启动CQ HTTP
![](file://C:/Users/liujian/Documents/Gridea/post-images/1585704024966.png)
启动后进入酷Q 的 data/app/io.github.richardchien.coolqhttpapi/config/ 目录，有一个.json 的文件，user-id为刚刚登陆的QQ号。修改这个文件的如下配置
![](file://C:/Users/liujian/Documents/Gridea/post-images/1585704119015.png)
关于如何使用，官方文档已经说的很详细了 ![nonebot说明文档点这里](https://nonebot.cqp.moe/guide/)
代码：https://github.com/Liujian1997/Python-Project/
