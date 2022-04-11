import asyncio
import time

import requests

import test

list = [
    # "006$wxv_1600147358070161411$wx",
    # "007$wxv_1600147572331986945$wx",
    # "008$wxv_1600148810809294851$wx",
    # "009$wxv_1600148907815157761$wx",
    # "010$wxv_1600169298474385408$wx",
    # "011$wxv_1600169373552427013$wx",
    # "012$wxv_1600169454485716996$wx",
    # "013$wxv_1600169589391310851$wx",
    # "014$wxv_1600169743322267649$wx",
    # "015$wxv_1600169882338279424$wx",
    # "016$wxv_1600170088446377986$wx",
    # "017$wxv_1600170196189659136$wx",
    "018$wxv_1600213531470151682$wx",
    "019$wxv_1600213835808849929$wx",
    "020$wxv_1600214014972739585$wx",
    "021$wxv_1600214307919708163$wx",
    "022$wxv_1600238354703400970$wx",
    "023$wxv_1600238442381131781$wx",
    "024$wxv_1600238492846997504$wx",
    "025$wxv_1610434557504208899$wx",
    "026$wxv_1610434997906128902$wx",
    "027$wxv_1610435381030633472$wx",
    "028$wxv_1610435529358000131$wx",
    "029$wxv_1610435560513290247$wx",
    "030$wxv_1610436141709606919$wx",
    "031$wxv_1610457667179724800$wx",
    "032$wxv_1610458165463040006$wx",
    "033$wxv_1610458273592197125$wx",
    "034$wxv_1610458514278137856$wx",
    "035$wxv_1610458515083444229$wx",
    "036$wxv_1610458515771310084$wx",
    "037$wxv_1610458818147074057$wx",
    "038$wxv_1610460308685275137$wx",
    "039$wxv_1610460317006774275$wx",
    "040$wxv_1610460462163247106$wx",
    "041$wxv_1619532034958245891$wx",
    "042$wxv_1619594966882664449$wx",
    "043$wxv_1619595105881899013$wx",
    "044$wxv_1619595236207312899$wx",
    "045$wxv_1801699149013139458$wx",
    "046$wxv_1801699295646007308$wx",
    "047$wxv_1801700037819711488$wx",
    "048$wxv_1801700231093239816$wx",
    "049$wxv_1801703114006151171$wx",
    "050$wxv_1801803476268564483$wx",
    "051$wxv_1797832806467715072$wx",
    "052$wxv_1797833272404557828$wx",
    "053$wxv_1797833603704242178$wx",
    "054$wxv_1797834102373433345$wx"
]
headers={
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Connection":"keep-alive",
        "Host":"www.dxzy163.com",
        "Cookie":"UM_distinctid=17f698337e016a3-05433a2d64bef1-37677109-16a7f0-17f698337e1186b; CNZZDATA1396347=cnzz_eid%3D918984535-1646738369-%26ntime%3D1646738369",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }

def down(i):
    url = "http://www.dxzy163.com/js/player/wx.php?url=" + i.split("$")[1]
    print("下载地址：" + url)
    res = requests.get(url=url, headers=headers, allow_redirects=False)  # 注 allow_redirects=False是必须的

    real_address = res.headers['location'];
    print("当前下载集：" + i.split("$")[0])
    video = requests.get(real_address)
    test.down_from_url(real_address, "/Users/wangzc/video/" + i.split("$")[0] + ".mp4")


async def func1():
    for i in range(1,10,1):
        down(list[i])

async def func2():
    for i in range(11,20,1):
        down(list[i])

async def func3():
    for i in range(21,30,1):
        down(list[i])

async def func4():
    for i in range(31,37,1):
        down(list[i])

async def main():
    # 第一种写法
    # f1 = func1()
    # await f1  # 一般await挂起操作放在协程对象前面
    # 第二种写法(推荐)
    # tasks = [
    #     func1(),
    #     func2(),
    #     func3()
    # ]
    tasks = [
        asyncio.create_task(func1()),  # py3.8以后加上asyncio.create_task()
        asyncio.create_task(func2()),
        asyncio.create_task(func3()),
        asyncio.create_task(func4())
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    t1 = time.time()
    # 一次性启动多个任务(协程)
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)