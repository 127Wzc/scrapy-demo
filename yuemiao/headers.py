
def get_user_heaer(session):
    headers = {
        # 'charset': 'utf-8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://servicewechat.com/wx2c7f0f3c30d99445/92/page-frame.html',
        'Cookie': "ASP.NET_SessionId="+session,
        'Content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'Host': 'cloud.cn2030.com',
        'Connection': 'Keep-Alive',
        'zftsl': '1568b8c75390a68b84ba46413e58f56f'
    }
    return headers;



