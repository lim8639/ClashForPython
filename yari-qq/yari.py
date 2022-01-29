import asyncio
import platform

from fastapi import FastAPI
from mirai import Mirai, HTTPAdapter, FriendMessage, Plain, GroupMessage, Face, At, Startup, Shutdown
from mirai.models import RequestEvent, NewFriendRequestEvent, FriendRecallEvent
from miraicle import GroupRecallEvent
from plugin import AIbot, translate,getNodeInfo,updateNode,getWeather,getNodeInfo2
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

app = FastAPI()

if __name__ == '__main__':
    config = {}
    if platform.system().lower() == 'windows':
        config = {
            'host': 'qqbot.limfly.cn',
            'port': 80,
            'filePath' :'v2.yaml',
            'urlList' : ['https://cdn.ppypro.xyz/link/Az8kiAHDZ029hBfg?clash=1', 'https://ikmom.cc/api/v1/client/subscribe?token=f22056c1a908b711b3521c513ed1eaed']
        }
    elif platform.system().lower() == 'linux':
        config = {
            'host': 'localhost',
            'port': 18080,
            'filePath': '/www/wwwroot/v2.limfly.cn/v2.yaml',
            'urlList': ['https://cdn.ppypro.xyz/link/Az8kiAHDZ029hBfg?clash=1',
                                    'https://ikmom.cc/api/v1/client/subscribe?token=f22056c1a908b711b3521c513ed1eaed']
        }

    bot = Mirai(
        qq=1806624810,  # 改成你的机器人的 QQ 号
        adapter=HTTPAdapter(
            verify_key='asofihOIBOIoiB778HIUVI', host=config.get('host'), port=config.get('port')
        )
    )


    @bot.on(FriendMessage)
    async def on_friend_message(event: FriendMessage):
        msg = str(event.message_chain)

        if event.sender.id == 863978160 and msg == '更新节点':
            await bot.send_friend_message(event.sender.id, [Plain("正在更新节点")])
            if updateNode.updateNodeConfig(config.get('filePath'),config.get('urlList')):
                await bot.send_friend_message(event.sender.id, [Plain("节点更新完成")])
            else:
                await bot.send_friend_message(event.sender.id, [Plain("节点更新失败")])
        rsp = AIbot.get_response(msg)
        await bot.send_friend_message(event.sender.id, [Plain(rsp)])


    @bot.on(GroupMessage)
    async def on_friend_message(event: GroupMessage):
        msg = str(event.message_chain)
        msg_length = len(msg)
        if '天气' in msg:
            city = msg[0:msg_length - 2]
            weather = getWeather.getWeatherInfo(city)
            weatherINfo = city+"天气："\
                           +"\n温度 ："+ weather.get('temp')+"℃ 最高 "+ weather.get('max_temp')+"℃ 最低 "+weather.get('min_temp')+" ℃"\
                           +"\n风力 ："+ weather.get('wind')+" "+ weather.get('wind_speed')+""+weather.get('wind_scale')+""\
                           +"\n天气 ："+ weather.get('weather')\
                           +"\nPM2.5 ："+ weather.get('air_pm25')\
                           +"\n日出 ："+ weather.get('sunrise')\
                           +"\n日落 ："+ weather.get('sunset')\
                           +"\n穿衣指数 ："+ weather.get('index').get('chuangyi').get('content')\
                           +"\n运动指数 ："+ weather.get('index').get('yundong').get('content')\
                           +"\n更新时间 ："+ weather.get('update_time')\




            await bot.send_group_message(event.sender.group.id, [Plain(str(weatherINfo))])

        if At(bot.qq) in event.message_chain:
            if '节点' in msg :
                await bot.send_group_message(event.sender.group.id, [Plain("正在获取节点信息.....")])
                data = getNodeInfo.getInfo()
                if data.get('code') == 0:
                    await bot.send_group_message(event.sender.group.id, [Plain("节点信息获取失败")])
                else:
                    msgInfo = "第一机场"\
                              +"\n剩余流量："+data.get('transfer')\
                              +"\n今日使用："+data.get('today_transfer')\
                              +"\n过期时间："+data.get('time')\
                              +"\n当前在线："+data.get('device')\
                              +"\n账户余额："+data.get('money')+"\n"
                    SecondNode = getNodeInfo2.getInfo()
                    msgInfo = msgInfo+SecondNode
                    await bot.send_group_message(event.sender.group.id, [Plain(msgInfo)])

        if msg[0] == '#':
            rsp = AIbot.get_response(msg[1:])
            msg = msg[1:]
            await bot.send_group_message(event.sender.group.id, [Plain(rsp), At(event.sender.id), Face(face_id=74)])
        if msg[0] in [":", "："]:
            msg = msg[1:]
            autoTanslate = translate.baiduTranslate(msg)
            autoTanslate = 'en: ' + autoTanslate['trans_result'][0]['dst']
            await bot.send_group_message(event.sender.group.id, autoTanslate)

    @bot.on(FriendRecallEvent)
    async def Friend_Recall_Event(Event):
        print(Event)

    @bot.on(GroupRecallEvent)
    async def Group_Recall_Event(Event):
        print(Event)
        print(bot.message_id)
    @bot.on(NewFriendRequestEvent)
    async def on_Request_Event(event: NewFriendRequestEvent):
        await asyncio.sleep(2)
        if event.message == '子叶':
            await bot.allow(event, '你好呀，我是子叶，一个可爱的小机器人~~')
            # await bot.send_friend_message(event.from_id, [Plain('你好呀，我是子叶，一个可爱的小机器人~~'), Face(face_id=74)])
        else:
            await bot.decline(event, '我不喜欢你')


    scheduler = AsyncIOScheduler()


    @bot.on(Startup)
    async def start_scheduler(_):
        scheduler.start()
        await bot.send_friend_message(863978160, "程序启动成功....  定时器已经部署")


    @bot.on(Shutdown)
    async def stop_scheduler(_):
        scheduler.shutdown(True)  # 结束定时器
        await bot.send_friend_message(863978160, "您的程序已经停止运行")


    @scheduler.scheduled_job(CronTrigger(hour=9, minute=10))
    async def timer():
        await bot.send_friend_message(863978160, "早安")


    @scheduler.scheduled_job(CronTrigger(hour=7, minute=10))
    async def timer():
        await bot.send_group_message(726149152, [Plain('早安~千叶'), At(1625303694), Face(face_id=74)])


    @scheduler.scheduled_job(CronTrigger(hour=22, minute=10))
    async def timer():
        await bot.send_group_message(726149152, [Plain('晚安~千叶'), At(1625303694), Face(face_id=75)])


    bot.run()
