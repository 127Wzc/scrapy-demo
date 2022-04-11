import requests
import urllib3

urllib3.disable_warnings()

def function(url,headers,params):
    print(123)
    result=requests.get(url, headers,verify=False)
    print(result)