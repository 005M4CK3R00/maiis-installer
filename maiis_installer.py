import os
import time
os.system('clear')
try:
	ver = input("are you suru want to install maiis in your system y/n :")
	if ver == "y" or ver == "Y":
		back_restore = input("do you want to backup maiis y/n : ")
		if back_restore == "y" or back_restore == "Y" :
			print("ok pleas enter a path of the maiis database ")
			path_maiis_backup = input('input path : ')
			print("pleas wait.....")
			os.chdir('/sdcard/111...Maiis/')
			os.system('mkdir main')
			os.chdir(path_maiis_backup)
			os.system('cp alarm.txt /sdcard/111...Maiis/main/')
			os.system('cp datab.txt /sdcard/111...Maiis/main/')
			os.system('cp pc.txt /sdcard/111...Maiis/main/')
			os.system('cp wp.txt /sdcard/111...Maiis/main/')
			# os.system('cp rec.txt /sdcard/111...Maiis/main/')
			os.system('cp usp.txt /sdcard/111...Maiis/main/')
			os.system('cp database.txt /sdcard/111...Maiis/main/')
			os.system('cp find.txt /sdcard/111...Maiis/main/')
			maiis_install_agan = input('do you want to install maiis y/n : ')
			if maiis_install_agan == 'n':
				print('ok sir pleas wait removing maiis installer file ....')
				time.sleep(2)
				os.chdir('/data/data/com.termux/files/home/maiis-installer/')
				
				os.system('cp kill.py /sdcard/111...Maiis/main')
				os.system('cp alarm.mp3 /sdcard/111...Maiis/main')
				
				os.system('cp pac.py /sdcard/111...Maiis/main')
				os.chdir('/data/data/com.termux/files/home')
				os.system('rm -rf maiis-installer')
				print('ok its done now restart your terminal')
				input('press any key to continue')
				exit()
			elif maiis_install_agan == 'y':
				os.chdir('/data/data/com.termux/files/home/')
				os.system('git clone https://github.com/005M4CK3R00/maiis.git')
				os.chdir('/data/data/com.termux/files/home/maiis/')
				os.system('cp maiis /data/data/com.termux/files/usr/bin/')
				os.chdir('/data/data/com.termux/files/home/')
				os.system('clear')
				os.chdir('/data/data/com.termux/files/home/maiis-installer/')
				
				os.system('cp kill.py /sdcard/111...Maiis/main')
				os.system('cp alarm.mp3 /sdcard/111...Maiis/main')
				
				os.system('cp pac.py /sdcard/111...Maiis/main')
				os.chdir('/data/data/com.termux/files/home')
				os.system('rm -rf maiis-installer')
				print("every this is done ")
				redif = input("do you want to start maiis : ")
				if redif == "y" or redif == "Y" :
					print("ok pleas wait....")
					time.sleep(2)
					print("its done maiis are working properly you will a maiis folder in your home directory where you can start maiis by typing python maiis1.py ......")
					print("starting maiis .............. ")
					time.sleep(2)
					# os.chdir('maiis')
					os.system('maiis')
				else:
					print("ok as your wish ....")
					time.sleep(2)
					print("now type maiis and hit enter to start maiis")
					time.sleep(2)
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
			os.system('apt install mpv -y')
			os.system('apt install nano -y')
			os.system('apt install fortune -y')
			os.system('apt install toilet -y')
			os.system('apt install git -y')

			os.system('git clone https://github.com/005M4CK3R00/maiis.git')
			os.chdir('/data/data/com.termux/files/home/maiis/')
			os.system('cp maiis /data/data/com.termux/files/usr/bin/')
			# os.system('chmod +x *')
			os.chdir('/data/data/com.termux/files/home/')
			os.system('rm -rf maiis')
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
			
			print('you need to install the termux api please wait while installing termux-api ........ ')
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
			with open("pass.txt" , 'w+') as iopt: pass
			iopt.close()
			with open('wp.txt' , 'w') as wxz:
				wxz.writelines('0')
			wxz.close()
			user_nmr = input('Pleas chuse the username for maiis : ')
			print('pleas do not include @ and = in password and username')
			pass_wr = input('pleas chuse the password : ')
			# setting uer name and password from here
			with open('usp.txt' , 'w') as opw:
				opw.writelines('username = '+user_nmr)
				opw.writelines('password @ '+pass_wr)
				print('password and username set...')
			opw.close()
			print('please chuse a password which you can remember')
			set_rp = input('please enter a recovery password : ')
			set_rps = str(set_rp)
			with open('pc.txt' , 'w') as srp:
				srp.writelines(set_rp)
				print('Done password set ')
				time.sleep(1)
			srp.close()
			os.system('cp kill.py /sdcard/111...Maiis/main')
			os.system('cp alarm.mp3 /sdcard/111...Maiis/main')
			os.system('cp pass.txt /sdcard/111...Maiis/main')
			os.system('cp wp.txt /sdcard/111...Maiis/main/')
			os.system('cp pc.txt /sdcard/111...Maiis/main/')
			os.system('cp usp.txt /sdcard/111...Maiis/main/')
			# os.system('cp rec.txt /sdcard/111...Maiis/main/')
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
				time.sleep(4)
				os.chdir('/data/data/com.termux/files/home')
				os.system('maiis')
				print("pleas restart your termux .......")
				time.sleep(2)
				print('Now can also start maiis from any where from typing maiis')
				time.sleep(3)
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
	print("now restart your maiis_installer")
	exit()