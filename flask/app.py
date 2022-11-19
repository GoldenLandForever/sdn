from flask import Flask,request
from flask_cors import CORS
# from mininet.net import Mininet
# from mininet.node import Controller, RemoteController, OVSController
# from mininet.node import CPULimitedHost, Host, Node
# from mininet.node import OVSKernelSwitch, UserSwitch
# from mininet.node import IVSSwitch
# from mininet.cli import CLI
# from mininet.log import setLogLevel, info
# from mininet.link import TCLink, Intf
# from subprocess import call
# import os

app = Flask(__name__)
CORS(app, supports_credentials=True)
@app.route('/test',methods = ['GET','POST'])
def hello():
    msg = request.get_json()
    print(msg)
    return "hello world!"


# 导入默认拓扑
@app.route('/topo/default-topo',methods = ['GET','POST'])
def default_topo():
    # global net
    # c0=net.addController(name='c0',
    #                 controller=RemoteController,
    #                 ip='127.0.0.1',
    #                 protocol='tcp',
    #                 port=6633)
    #
    # s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    # s3 = net.addSwitch('s2', cls=OVSKernelSwitch)
    # s2 = net.addSwitch('s3', cls=OVSKernelSwitch)
    #
    # h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    # h5 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    # h4 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    # h2 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    # h3 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    #
    # net.addLink(s1, s3)
    # net.addLink(s2, s3)
    # net.addLink(s1, h1)
    # net.addLink(s2, h3)
    # net.addLink(s3, h4)
    # net.addLink(s3, h5)
    # net.addLink(s2, h2)
    #
    # net.build()
    #
    # for controller in net.controllers:
    #     controller.start()
    #
    # net.get('s1').start([c0])
    # net.get('s2').start([c0])
    # net.get('s3').start([c0])

    return "the topo has been built."


# 新增host
@app.route('/topo/addhost',methods = ['POST'])
def add_host():
    # global net
    msg = request.get_json()
    hostname = msg['name']
    ip_address = msg['ip_address']
    switch = msg['switch']
    print("name = ",hostname," ip_address = ",ip_address, " switch = ",switch)

    # net.addHost(hostname, ip = ip_address, defaultRoute=None)
    # net.addLink(host, switch)

    return "added the new host"


# 删除host
@app.route('/topo/deletehost/<hostname>',methods = ['GET'])
def delete_host(hostname):
    # global net
    print("GET:name = ",hostname)
    # net.delHost(net.nameToNode[hostname])
    return "deleted the host"


# 新增switch
@app.route('/topo/addswitch/<switchname>',methods = ['GET'])
def add_switch(switchname):
    # global net
    print("GET:name = ",switchname)
    return "added the new switch"

# 删除switch
@app.route('/topo/deleteswitch/<switchname>',methods = ['GET'])
def delete_switch(switchname):
    # global net
    print("GET:name = ",switchname)
    # net.delSwitch(net.nameToNode[switchname])
    return "deleted the switch"


# 新增链路
@app.route('/topo/addlink',methods = ['POST'])
def add_link():
    # global net
    msg = request.get_json()
    node1 = msg['node1']
    node2 = msg['node2']
    print("node1 = ",node1," node2 = ",node2)
    # net.addLink(node1,node2)

    return "added the new link"


# 删除链路
@app.route('/topo/deletelink',methods = ['POST'])
def delete_link():
    # global net
    msg = request.get_json()
    node1 = msg['node1']
    node2 = msg['node2']
    print("node1 = ",node1," node2 = ",node2)
    # deleted_link = net.delLinkBetween(node1,node2)
    # print(deleted_link)
    return "deleted the link"


# pingall
@app.route('/net/pingall',methods = ['GET'])
def ping_all():
    # global net
    # net.pingAll()
    # for host in net.hosts:
    #     print(host)
    return "pinged all"


if __name__ == '__main__':
    # net = Mininet(topo=None,build=False,ipBase='10.0.0.0/8')
    app.run()