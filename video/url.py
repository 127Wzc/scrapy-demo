import os

import requests

from tqdm import tqdm


def down_from_url(url, dst):
    # 设置stream=True参数读取大文件
    response = requests.get(url, stream=True)
    # 通过header的content-length属性可以获取文件的总容量
    file_size = int(response.headers['content-length'])
    if os.path.exists(dst):
        # 获取本地已经下载的部分文件的容量，方便继续下载，如果不存在就从头开始下载。
        first_byte = os.path.getsize(dst)
    else:
        first_byte = 0
    # 如果大于或者等于则表示已经下载完成，否则继续
    if first_byte >= file_size:
        return file_size
    header = {"Range": f"bytes={first_byte}-{file_size}"}

    pbar = tqdm(total=file_size, initial=first_byte, unit='B', unit_scale=True, desc=dst)
    req = requests.get(url, headers=header, stream=True)
    with open(dst, 'ab') as f:
        # 每次读取一个1024个字节
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                pbar.update(1024)
    pbar.close()


if __name__ == '__main__':
    list = [
        "046$wxv_1801699295646007308$wx",
        "047$wxv_1801700037819711488$wx",
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
    for i in list:

        url = "http://www.dxzy163.com/js/player/wx.php?url="+i.split("$")[1]
        print("下载地址："+url)
        res = requests.get(url=url, headers=headers, allow_redirects=False)  # 注 allow_redirects=False是必须的

        real_address = res.headers['location'];
        print("当前下载集："+i.split("$")[0])
        video = requests.get(real_address)
        down_from_url(real_address, "D:/video/f/"+i.split("$")[0]+".mp4")

