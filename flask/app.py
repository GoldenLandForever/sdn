from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)

# 删除链路
'''
    JSON格式:
    node1: 节点1的名字
    node2: 节点2的名字
'''

# 测试主机间的连通性、丢包率、带宽、往返时延
'''
    JSON格式:
    node1: 节点1的名字
    node2: 节点2的名字
    返回值：
        linkStatus:连通状态 (0为未连通，1为已连通)
        ploss:丢包率 (数值)
        bandwidth:带宽 (字符串,未连通时为None)
        RTT:往返时延RTT (数值,未连通时为0)
    返回值类型：json
'''


@app.route('/add/flow', methods=['POST'])
def add_flow():
    # url = " http://localhost:8080/stats/flowentry/add"
    # 获取交换机的名字
    msg = request.get_json()
    if type(msg) == type("str"):
        msg = json.loads(msg)
    switchname = msg["switchname"]
    match = msg["match"]
    print(switchname)
    print(match)
    return "error nametype"


@app.route('/net/linkStatues', methods=['POST'])
def get_linkStatus():
    data = {
        "linkStatus": 0,
        "ploss": 'ploss',
        "bandwidth": 'wwww',
        "RTT": 5
    }
    return jsonify(data)


@app.route('/get/switch/<switchname>', methods=['GET'])
def get_switch_desc(switchname):
    json = {
        "1": {
            "actions": [
                "OUTPUT:2"
            ],
            "byte_count": 238,
            "cookie": 0,
            "duration_nsec": 467000000,
            "duration_sec": 205,
            "flags": 0,
            "hard_timeout": 0,
            "idle_timeout": 0,
            "length": 104,
            "match": {
                "dl_dst": "2a:d5:ac:a4:f9:be",
                "dl_src": "36:d0:35:72:42:fa",
                "in_port": 1
            },
            "packet_count": 3,
            "priority": 1,
            "table_id": 0
        },
        "2": {
            "actions": [
                "OUTPUT:1"
            ],
            "byte_count": 140,
            "cookie": 0,
            "duration_nsec": 462000000,
            "duration_sec": 205,
            "flags": 0,
            "hard_timeout": 0,
            "idle_timeout": 0,
            "length": 104,
            "match": {
                "dl_dst": "36:d0:35:72:42:fa",
                "dl_src": "2a:d5:ac:a4:f9:be",
                "in_port": 2
            },
            "packet_count": 2,
            "priority": 1,
            "table_id": 0
        },
        "3": {
            "actions": [
                "OUTPUT:2"
            ],
            "byte_count": 238,
            "cookie": 0,
            "duration_nsec": 434000000,
            "duration_sec": 205,
            "flags": 0,
            "hard_timeout": 0,
            "idle_timeout": 0,
            "length": 104,
            "match": {
                "dl_dst": "2a:d5:ac:a4:f9:be",
                "dl_src": "82:2e:87:0b:ac:2f",
                "in_port": 1
            },
            "packet_count": 3,
            "priority": 1,
            "table_id": 0
        },
        "4": {
            "actions": [
                "OUTPUT:1"
            ],
            "byte_count": 140,
            "cookie": 0,
            "duration_nsec": 431000000,
            "duration_sec": 205,
            "flags": 0,
            "hard_timeout": 0,
            "idle_timeout": 0,
            "length": 104,
            "match": {
                "dl_dst": "82:2e:87:0b:ac:2f",
                "dl_src": "2a:d5:ac:a4:f9:be",
                "in_port": 2
            },
            "packet_count": 2,
            "priority": 1,
            "table_id": 0
        },
        "5": {
            "actions": [
                "OUTPUT:2"
            ],
            "byte_count": 238,
            "cookie": 0,
            "duration_nsec": 401000000,
            "duration_sec": 205,
            "flags": 0,
            "hard_timeout": 0,
            "idle_timeout": 0,
            "length": 104,
            "match": {
                "dl_dst": "2a:d5:ac:a4:f9:be",
                "dl_src": "fa:f8:61:19:57:91",
                "in_port": 1
            },
            "packet_count": 3,
            "priority": 1,
            "table_id": 0
        },
        "6": {
            "actions": [
                "OUTPUT:1"
            ],
            "byte_count": 140,
            "cookie": 0,
            "duration_nsec": 394000000,
            "duration_sec": 205,
            "flags": 0,
            "hard_timeout": 0,
            "idle_timeout": 0,
            "length": 104,
            "match": {
                "dl_dst": "fa:f8:61:19:57:91",
                "dl_src": "2a:d5:ac:a4:f9:be",
                "in_port": 2
            },
            "packet_count": 2,
            "priority": 1,
            "table_id": 0
        },
        "7": {
            "actions": [
                "OUTPUT:2"
            ],
            "byte_count": 238,
            "cookie": 0,
            "duration_nsec": 351000000,
            "duration_sec": 205,
            "flags": 0,
            "hard_timeout": 0,
            "idle_timeout": 0,
            "length": 104,
            "match": {
                "dl_dst": "2a:d5:ac:a4:f9:be",
                "dl_src": "aa:65:56:d5:94:e8",
                "in_port": 1
            },
            "packet_count": 3,
            "priority": 1,
            "table_id": 0
        },
        "8": {
            "actions": [
                "OUTPUT:1"
            ],
            "byte_count": 140,
            "cookie": 0,
            "duration_nsec": 347000000,
            "duration_sec": 205,
            "flags": 0,
            "hard_timeout": 0,
            "idle_timeout": 0,
            "length": 104,
            "match": {
                "dl_dst": "aa:65:56:d5:94:e8",
                "dl_src": "2a:d5:ac:a4:f9:be",
                "in_port": 2
            },
            "packet_count": 2,
            "priority": 1,
            "table_id": 0
        },
        "9": {
            "actions": [
                "OUTPUT:CONTROLLER"
            ],
            "byte_count": 6418,
            "cookie": 0,
            "duration_nsec": 72000000,
            "duration_sec": 221,
            "flags": 0,
            "hard_timeout": 0,
            "idle_timeout": 0,
            "length": 80,
            "match": {},
            "packet_count": 78,
            "priority": 0,
            "table_id": 0
        }
    }
    return jsonify(json)


if __name__ == '__main__':
    app.run(debug=True)
