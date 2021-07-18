#!/bin/python

# module
import os,sys,time,requests
from time import sleep

# untuk mengclear
def bersih():
    os.system("clear")
# mengetik otomatis
def mengetik(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)



# mengetik_cepat
def speed(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#nanya1
def nanya1():
    time.sleep(0.01)
    bersih()
    f = raw_input("[+] Tekan ENTER Untuk Masuk Ke Tools Nya")
    if f =="" or f ==" " or f  ==" " or f ==" ":
	menu()
    else:
	mengetik("[!] Salah, Tekan ENTER untuk masuk ke toolsnya stah")
	time.sleep(1)
	nanya1()


# nanya
def nanya():
    a = raw_input("Apakah Anda Ingin Install Tools Lainya? [Y/T] ~~> ")
    if a =="Y" or a =="y":
	menu()
    elif a =="T" or a =="t":
        time.sleep(0.5)
	mengetik("Terima kasih sudah menggunakan tools ini :)")
	time.sleep(1)
	mengetik("Code by AmmarBN")
	time.sleep(1)
	os.system("xdg-open https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ")
	time.sleep(3)
	sys.exit()
    elif a =="" or a ==" " or a =="  " or a =="   ":
	mengetik("Jangan kosong stah")
	time.sleep(1)
	nanya()
    else:
	mengetik("Salah, masukin inputnya dengan benar ya stah!")
	time.sleep(1)
	nanya()

# menu_pertama
def menu1():
    bersih()
    mengetik("\033[1;96m+\033[1;93m-----------------------------------------------\033[1;96m+")
    mengetik("\033[1;90m[\033[1;96m+\033[1;90m] \033[1;91mAuthor   \033[1;92m: \033[1;96mAmmarBN")
    mengetik("\033[1;90m[\033[1;96m+\033[1;90m] \033[1;91mYoutube  \033[1;92m: \033[1;96mAmmarSP")
    mengetik("\033[1;90m[\033[1;96m+\033[1;90m] \033[1;91mGithub  \033[1;92m: \033[1;96mhttps://github.com/AmmarBN")
    mengetik("\033[1;90m[\033[1;96m+\033[1;90m] \033[1;91mWhatsApp \033[1;92m: +\033[1;96m62 877-0877-3367")
    mengetik("\033[1;96m+\033[1;93m-----------------------------------------------\033[1;96m+")
    mengetik("\033[1;90m[\033[1;91mA\033[1;90m] \033[1;92mSubrek Channel Admin")
    mengetik("\033[1;90m[\033[1;93m1\033[1;90m] \033[1;95mInstall Bahan Rempahnya dulu ges")
    mengetik("\033[1;90m[\033[1;93m2\033[1;90m] \033[1;95mMasuk Tools")
    mengetik("\033[1;90m[\033[1;93m0\033[1;90m] \033[1;95mKeluar/Exit")
          																					

    pilih = raw_input("\033[96mPilih Menu \033[1;90m~~\033[191m> \033[1;95m")
    if pilih =="a" or pilih =="A":
	os.system("xdg-open https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ")
	time.sleep(5)
	print "[+] Terima kasih sudah subrek channel saya :)"
	nanya()
    elif pilih =="01" or pilih =="1":
	time.sleep(2)
	bersih()
        print "[+] Tunggu Ges Proses Akan Di Mulai"
	time.sleep(2)
	os.system("cd /data/data/com.termux/files/home")
	os.system("pkg update && pkg upgrade -y")
	os.system("pkg install bash php python python2 fish clang jq figlet ruby git nano -y")
	os.system("pip install --upgrade pip && pip install requests && pip install mechanize && pip2 install requests && pip2 install mechanize")
	os.system("pkg install wget -y")
        time.sleep(1)
	nanya1()
    elif pilih =="02" or pilih =="2":
	menu()
    elif pilih =="" or pilih ==" " or pilih =="  ":
	mengetik("Jangan Kosong Stah ^_^")
	time.sleep(1)
	menu1()
    elif pilih =="00" or pilih =="0":
	sleep(1)
	mengetik("\033[1;93mTerimak kasih sudah menggunakan tools ini :)")
	time.sleep(1)
	mengetik("\033[1;96mCode by AmmarBN")
	time.sleep(1)
	sys.exit()
    else:
	mengetik("Salah stah, masukan input dengan benar :)")
	time.sleep(1.5)
	menu1()

# menu inti
def menu():
    bersih()
    speed('\033[1;96m+\033[1;93m------------------------------------------------\033[1;96m+')
    speed("\033[1;90m[\033[1;95m+\033[1;90m] \033[1;91mAuthor      \033[1;92m: \033[1;96mAmmarBN")
    speed("\033[1;90m[\033[1;95m+\033[1;90m] \033[1;91mYoutube     \033[1;92m: \033[1;96mAmmarSP")
    speed("\033[1;90m[\033[1;95m+\033[1;90m] \033[1;91mGithub      \033[1;92m: \033[1;96mhttps://github.com/AmmarBN")
    speed("\033[1;90m[\033[1;95m+\033[1;90m] \033[1;91mAlamat      \033[1;92m: \033[1;96mJawa Tengah ||Semarang")
    speed("\033[1;90m[\033[1;95m+\033[1;90m] \033[1;91mJenis Tools \033[1;92m: \033[1;96mInstaller Tools")
    speed('\033[1;96m+\033[1;93m------------------------------------------------\033[1;96m+')
    speed("\033[1;90m[\033[1;91mAB\033[1;90m] \033[1;95mSubscribe Channel Saya\033[1;96m")
    speed("[\033[1;93m01\033[1;96m] Dark Fb") # 1
    speed("[\033[1;93m02\033[1;96m] Munculkan Tombol kiri kanan") # 2
    speed("[\033[1;93m03\033[1;96m] Fake User") #3
    speed("[\033[1;93m04\033[1;96m] Spam Call") #4
    speed("[\033[1;93m05\033[1;96m] DdoS Lucita") #5
    speed("[\033[1;93m06\033[1;96m] DdoS Trojan \033[1;90m(\033[1;91mupdate\033[1;90m)\033[1;96m") #6
    speed("[\033[1;93m07\033[1;96m] LiteDdos")
    speed("[\033[1;93m08\033[1;96m] Virus Perusak Hp")
    speed("[\033[1;93m09\033[1;96m] Virtex Untuk WhatsApp")
    speed("[\033[1;93m10\033[1;96m] Hack Fb Teman")
    speed("[\033[1;93m11\033[1;96m] Cek Ip Saya")
    speed("[\033[1;93m12\033[1;96m] Hack Fb Premium")
    speed("[\033[1;93m13\033[1;96m] Lacak Ip")
    speed("[\033[1;93m14\033[1;96m] Spam Sms 6 jenis")
    speed("[\033[1;93m15\033[1;96m] Bot Chat")
    speed("[\033[1;93m16\033[1;96m] Auto bot facebook")
    speed("[\033[1;93m17\033[1;96m] Osif")
    speed("[\033[1;93m18\033[1;96m] Crack Akun Fb")
    speed("[\033[1;93m19\033[1;96m] Bajingan Versi 6")
    speed("[\033[1;93m20\033[1;96m] Hack Fb Target")
    speed("[\033[1;93m21\033[1;96m] Install Cmatrix")
    speed("[\033[1;93m22\033[1;96m] Archilnu")
    speed("[\033[1;93m23\033[1;96m] Ubuntu-Linux")
    speed("[\033[1;93m24\033[1;96m] Kali-Linux")
    speed("[\033[1;93m25\033[1;96m] Debian Linux")
    speed("[\033[1;93m26\033[1;96m] Kali Net Hunter")
    speed("[\033[1;93m28\033[1;96m] Metasploit-Framework")
    speed("[\033[1;93m29\033[1;96m] Routersploit-Framework")
    speed("[\033[1;93m30\033[1;96m] Spam Sms Mapclub")
    speed("\033[1;90m[\033[1;91m00\033[1;90m] \033[1;95mKeluar/Exit")
    pil = raw_input("\033[1;93mPilih Sesuai Nomor Input \033[1;90m~~\033[1;91m> \033[1;95m")
    # out put
    if pil =="ab" or pil =="Ab" or pil =="AB" or pil =="aB":
	os.system("xdg-open https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ")
	time.sleep(5)
	mengetik("Terima Kasih Sudah Ada Niat Untuk Subrek Channel Akuh :)")
	nanya()
    elif pil =="1" or pil =="01": # dark fb
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/Rendi-ID/DarkFb")
	os.system("cd DarkFb && python2 darkfb.py")
    elif pil =="2" or pil =="02": # terkey
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/karjok/terkey")
	os.system("cd terkey && python2 terkey.py")
    elif pil =="3" or pil =="03": # fake user
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/Rendi-ID/FakeUser")
	os.system("cd FakeUser")
    elif pil =="4" or pil =='04': # spam call 
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/Rendi-ID/SpamCall")
	os.system("cd SpamCall")
    elif pil =="05" or pil =="5": # ddos lucita
	os.system("git clone https://github.com/zlucifer/lucita_ddos")
	sleep(1)
	mengetik("[+] Tools sudah terinstall silahkan coba")
	sleep(1)
	nanya()
    elif pil =="06" or pil =="6": # ddos trojan (update)
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/BPCATTACKER/DOS-TOOKITS")
	os.system("cd DOS-TOOKITS && bash DOS-TOOKITS.sh")
    elif pil =="07" or pil =="7": # lite ddos
	os.system("git clone https://github.com/4L13199/LITEDDOS")
	sleep(1)
	mengetik("[+] Tools sudah terinstall silahkan coba")
	sleep(1)
	nanya()
    elif pil =="08" or pil =="8": # virus perusak hp
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/justahackers/perusak")
	os.system("cd perusak")
	os.system("python2 perusak.py")
    elif pil =="09" or pil =="9": # virtex untuk whatsApp
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/muhammadfathul/VIRTEX")
	os.system("cd VIRTEX && bash virtex.sh")
    elif pil =="100" or pil =="10": # hack efbeh teman
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/blackcodercrush/hack-facebook-teman")
	os.system("cd hack-fb-teman && python2 hack-fb.py")
    elif pil =="111" or pil =="11": # cek ip saya
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/Bl4ckDr460n/My-Ip")
	os.system("cd My-Ip && python2 My-Ip.py")
    elif pil =="12": # hack efbi premium
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/Bl4ckDr460n/Black-Fb-Premium")
	os.system("cd Black-Fb-Premium && python2 Black-Fb.py")
    elif pil =="13": # lacak ip
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/Bl4ckDr460n/IP-Location")
	os.system("cd Ip-Location && python2 lacak.py")
    elif pil =="14": # spam sms 6 jenis
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/hekelpro/spammer")
	os.system("cd spammer && python2 spammer.py")
    elif pil =="15": # bot chat
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/Bl4ckDr460n/BotChat")
	os.system("cd BotChat && python2 BotChat.py")
    elif pil =="16": # auto bot facebook
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/Senitopeng/BotFbBangDjon.git")
	os.system("cd BotFbBangDjon && python2 bangdjon.py")
    elif pil =='17': # osif
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/ciku370/OSIF")
	os.system("cd OSIF && python2 osif.py")
    elif pil =='18': # crack akun fb
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/Makky2693/Hack-FB")
	os.system("cd Hack-FB && python2 Hack-FB.py")
    elif pil =="19": # bajingan versi 6
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/DarknessCyberTeam/BAJINGANv6")
	os.system("cd BAJINGANv6 && python2 bajingan.py")
    elif pil =='20': # hack fb target
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/FR13ND8/BRUTEFORCEnew")
	os.system("cd BRUTEFORCEnew")
    elif pil =='21': # cmatrix
        os.system("cd /data/data/com.termux/files/home")
	os.system("apt install cmatrix")
	mengetik("Packages sudah terinstall \n Ketik cmatric lalu enter untuk melihat hasilnya")
	nanya()
    elif pil =="22": # archilnu
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/zlucifer/light_bringer")
	os.system("cd Light_bringer && bash light.sh")
    elif pil =="23": # ubuntu-linux
	os.system("cd /data/data/com.termux/files/home")
	os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")
	os.system("bash start-ubuntu.sh")
    elif pil =='24': # kali-linux
	os.system("cd /data/daya/com.termux/files/home")
	os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
	os.system("bash start-kali.sh")
    elif pil =="25": # debian-linux
	os.system("cd /data/data/com.termux/files/home")
	os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh")
	os.system("bash start-debian.sh")
    elif pil =="26": # kali net hunter
	os.system("cd /data/data/com.termux/files/home")
	os.system("curl -LO https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/kalinethunter")
	mengetik("Terinstall")
	sleep(1)
	nanya()
    elif pil =="27": # metasploit
	os.system("cd /data/data/com.termux/files/home")
	os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
	mengetik("Proses installasi memakan data  600 MB")
	sleep(2)
	mengetik("Waktu proses installasi tergantung kecepatan internet")
	sleep(2)
	hayyu()
    elif pil =='28': # routersploit
 	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/threat04/routersploit")
	os.system("cd routersploit && pip install -r requirements-dev.txt && pip install -r requirements.txt && python3 rsf.py")
    elif pil =="29": # spam sms mcp
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/Rendi-ID/SpamMCP")
	os.system("cd SpamMCP && python spam.py")
    elif pil =="00": #keluar/exit
	mengetik("Terima kasih sudah menggunakan tools ini")
	sleep(1)
	mengetik("Code by AmmarBN")
	sleep(1)
	sys.exit()
    elif pil =="" or pil ==" " or pil =="  " or pil =="   ": #kosong
	mengetik("Jangan Sampe Kosong Stah :)")
	sleep(1)
	menu()
    else: #salah pilih
	mengetik("Salah, masukan input dengan benar!")
	sleep(2)
	menu()
menu1()
																																				

