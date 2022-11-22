from flask import Flask, request, jsonify
from flask_cors import CORS

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


@app.route('/net/linkStatues', methods=['POST'])
def get_linkStatus():
    data = {
        "linkStatus":0,
        "ploss": 'ploss',
        "bandwidth": 'wwww',
        "RTT":5
    }
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)