import os
import time
try:
	ver = input("are you suru want to install maiis in your system y/n :")
	if ver == "y" or ver == "Y":
		back_restore = input("do you want to backup maiis y/n : ")
		if back_restore == "y" or back_restore == "Y" :
			print("ok pleas enter a path of the maiis database ")
			path_maiis_backup = input('input path : ')
			print("pleas wait.....")
			os.chdir(path_maiis_restore)
			os.system('cp alarm.txt /sdcard/111...Maiis/main/')
			os.system('cp datab.txt /sdcard/111...Maiis/main/')
			os.system('cp database.txt /sdcard/111...Maiis/main/')
			os.system('cp find.txt /sdcard/111...Maiis/main/')
			maiis_install_agan = ('do you want to install maiis y/n : ')
			if maii_install_agan == 'n':
				print('ok sir pleas wait removing maiis installer file ....')
				time.sleep(2)
				os.chdir('/data/data/com.termux/files/home/maiis-installer/')
				with open("alarm.txt", "w+"): pass
				with open("datab.txt", "w+"): pass
				with open("database.txt", "w+"): pass
				with open("find.txt", "w+"): pass
				os.system('cp kill.py /sdcard/111...Maiis/main')
				os.system('cp alarm.mp3 /sdcard/111...Maiis/main')
				os.system('cp alarm.txt /sdcard/111...Maiis/main')
				os.system('cp datab.txt /sdcard/111...Maiis/main')
				os.system('cp database.txt /sdcard/111...Maiis/main')
				os.system('cp find.txt /sdcard/111...Maiis/main')
				os.system('cp pac.py /sdcard/111...Maiis/main')
				os.chdir('/data/data/com.termux/files/home')
				os.system('rm -rf maiis-installer')
				print('ok its don now re start your terminal')
				input('press enter to continue')
				exit()
			elif maiis_install_agan == 'y':
				os.chdir('/data/data/com.termux/files/home/')
				os.system('git clone https://github.com/005M4CK3R00/maiis.git')
				os.system('clear')
				os.chdir('/data/data/com.termux/files/home/maiis-installer/')
				with open("alarm.txt", "w+") as op: pass
				op.close()
				with open("datab.txt", "w+") as oi: pass
				io.close()
				with open("database.txt", "w+") as di: pass
				di.close()
				with open("find.txt", "w+") as di: pass
				di.close()
				os.system('cp kill.py /sdcard/111...Maiis/main')
				os.system('cp alarm.mp3 /sdcard/111...Maiis/main')
				os.system('cp alarm.txt /sdcard/111...Maiis/main')
				os.system('cp datab.txt /sdcard/111...Maiis/main')
				os.system('cp database.txt /sdcard/111...Maiis/main')
				os.system('cp find.txt /sdcard/111...Maiis/main')
				os.system('cp pac.py /sdcard/111...Maiis/main')
				os.chdir('/data/data/com.termux/files/home')
				os.system('rm -rf maiis-installer')
		elif back_restore == "n" or back_restore == "N":
			print('make sure that internet is connected ')
			print("ok pleas wait while installing maiis in your system .....")
			time.sleep(3)
			os.chdir('/data/data/com.termux/files/home/')
			os.system('clear')
			os.system('apt update -y')
			os.system('apt upgrade -y')
			os.system('apt install python -y')
			os.system('apt install python2  -y')
			os.system('apt install figlet -y')
			os.system('apt install nano -y')
			os.system('apt install fortune -y')
			os.system('apt install toilet -y')
			os.system('apt install git -y')
			# os.system('apt install pip -y')
			os.system('git clone https://github.com/005M4CK3R00/maiis.git')
			os.system('clear')
			os.system('apt install mpv -y')
			os.system('pip install tts')
			os.system('pip2 install cookiejar')
			os.system('pip2 install requests')
			os.system('pip2 install bs4')
			os.system('clear')
			print("setting storage permition pleas wait")
			time.sleep(1)
			print("press allow to continue")
			os.system('termux-setup-storage')
			# os.system('pip2 install getpass')
			print('you need to install the termux api pleas wait while installing termux-api ........ ')
			time.sleep(5)
			os.chdir('/data/data/com.termux/files/home/maiis-installer/') # non
			os.system('xdg-open termux-api.apk')
			os.system('apt install termux-api')
			print("Worning be cairefull donot try to rename any file")
			print("or donot try to edit maiis")
			time.sleep(4)
			print('pleas wait setting up maiis for you')
			os.chdir('/sdcard/')
			if not os.path.exists('111...Maiis'):
				os.makedirs('111...Maiis')
			os.chdir('/sdcard/111...Maiis/')
			if not os.path.exists('3dsong'):
				os.makedirs('3dsong')
			if not os.path.exists('sadsongs'):
				os.makedirs('sadsongs')
			if not os.path.exists('popsongs'):
				os.makedirs('popsongs')
			if not os.path.exists('bhajan'):
				os.makedirs('bhajan')
			if not os.path.exists('panjabi'):
				os.makedirs('panjabi')
			if not os.path.exists('othersongs'):
				os.makedirs('othersongs')
			if not os.path.exists('main'):
				os.makedirs('main')
			os.chdir('/data/data/com.termux/files/home/maiis-installer/')
			with open("alarm.txt", "w+") as fu: pass
			fu.close()
			with open("datab.txt", "w+") as cu: pass
			cu.close()
			with open("database.txt", "w+") as fdi: pass
			fdi.close()
			with open("find.txt", "w+") as fgi: pass
			fgi.close()
			os.system('cp kill.py /sdcard/111...Maiis/main')
			os.system('cp alarm.mp3 /sdcard/111...Maiis/main')
			os.system('cp alarm.txt /sdcard/111...Maiis/main')
			os.system('cp datab.txt /sdcard/111...Maiis/main')
			os.system('cp database.txt /sdcard/111...Maiis/main')
			os.system('cp find.txt /sdcard/111...Maiis/main')
			os.system('cp pac.py /sdcard/111...Maiis/main')
			os.chdir('/data/data/com.termux/files/home')
			os.system('rm -rf maiis-installer')
			print("pleas wait .......")
			os.system('termux-tts-speak please now go to your home directory and stsrt maiis and you can type help to see command list please now go to your home directory and stsrt maiis and you can type help to see command list please now go to your home directory and stsrt maiis and you can type help to see command list ')
			print("please now go to your home directory and start maiis by typing cd maiis python maiis.py and you can type help to see command list")
			insrt = input("do you want to start maiis y/n ")
			if insrt=="y" or "Y" :
				print("ok pleas wait ..... ")
				print("in first time maiis can take more time to start")
				print("if you got any issu you can talk to admin which is 5M4CK3R .....")
				time.sleep(5)
				os.chdir('/data/data/com.termux/files/home/maiis')
				os.system('python maiis1.py')
				print("pleas restart your termux .......")
				exit()
			elif insrt =="n" or insrt =="N" :
				print("ok sir pleas restart your termux :-) ")
				exit()
			else:
				print("ok sir ......")
				print("pleas restart your termux ...... ")
				exit()
		else:
			print("enter a valid command")
	else:
		print("ok sir as your wish ...... :-) ")
		time.sleep(4)
		
except KeyboardInterrupt:
	print("pleas enter a valid entry donot use ctrl kry")
			
		
		
		
		
		
		
		
