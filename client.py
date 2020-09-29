import requests
import json

def sendjson(text,ob_wxid):
    print('suibian')
    payload = json.dumps({
        "api":"SendTextMsg",
        "robot_wxid":"wxid_clto5pmye84r12",
        "to_wxid":ob_wxid,
        "msg":text})
    r = requests.post("http://192.168.124.162:88/httpAPI", data=payload)
    return r.text

def sendurl(str):
    url="http://192.168.124.156:88/httpAPI?api=SendTextMsg&robot_wxid=wxid_clto5pmye84r12&to_wxid=wxid_tp6waxkizpzq52&msg=test2"
    r=requests.get(url)
    print(r.text)
    return r.text