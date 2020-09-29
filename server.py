from flask import Flask, url_for, request
import os
import json
import sys
import client
app = Flask(__name__)


@app.route('/')     #首页
def index():
    return 'Hello World'

## api接口地址
api_recv_msg_uri = '/api/recv_msg'
@app.route(api_recv_msg_uri, methods=['POST']) #api接口

def recv_msg():
    if request.method == 'POST':
        ## post过来的参数和值

        #recv_data=request.get_data().decode('UTF-8')
        #print('接收到的数据：',recv_data)
        #recv_dict=json.loads(recv_data)
        recv_dict = request.get_json()
        ob_wxid=recv_dict['from_wxid']
        #ob_wxid='wxid_tp6waxkizpzq52'
        #client.sendjson('反弹反弹',ob_wxid)
        ##for key in request.form:
        ##    print(key + ' -> ' + request.form.get(key))
        ##return 'OK'
    return 'GET method no support!'


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0' ,port = '8081')

