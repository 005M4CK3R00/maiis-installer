import os
import sys
import time
os.system('clear')
try:
	def animate(): # animate section start from here
		blink = '\33[6m'
		bold = '\33[1m'
		selected = '\33[7m'
		url = '\33[4m'
		read='\033[31m'
		green='\033[32m'
		yellow='\033[93m'
		blue='\033[34m'
		bold='\033[01m'
		underline='\033[04m'
		voilet = '\33[35m'
		end = '\33[0m'
		i =0
		done = 'false'
		while done == 'false':
			sys.stdout.write(green+'\rloading |'+end)
			time.sleep(0.1)
			sys.stdout.write(read+'\rloading /'+end)
			time.sleep(0.1)
			sys.stdout.write(yellow+'\rloading -'+end)
			time.sleep(0.1)
			sys.stdout.write(voilet+'\rloading \\'+end)
			time.sleep(0.1)
			if i ==3:
				break
			i =i+1
		sys.stdout.write('\r') # animate section end here
		
	blink = '\33[6m'
	bold = '\33[1m'
	selected = '\33[7m'
	url = '\33[4m'
	read='\033[31m'
	green='\033[32m'
	yellow='\033[93m'
	blue='\033[34m'
	bold='\033[01m'
	underline='\033[04m'
	voilet = '\33[35m'
	end = '\33[0m'
	def main():
		print(read+'Worning be cairefull if you uninstall termux the termux will uninstall but not maiis . maiis will still alive ..'+end)
		ver = input(green+"are you surue want to install maiis in your system y/n :"+end+blue)
		if ver == "y" or ver == "Y":
			back_restore = input(blue+"do you want to backup maiis y/n : "+end+green)
			if back_restore == "y" or back_restore == "Y" :
				print(yellow+"ok pleas enter a path of the maiis database "+end+green)
				path_maiis_backup = input(read+'input path : '+end+yellow)
				animate()
				os.chdir('/sdcard/Maiis/')
				os.system('mkdir main')
				os.chdir(path_maiis_backup)
				os.system('cp alarm.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp datab.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp pass.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp pc.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp wp.txt /sdcard/Android/data/com.maiis.main.files/')
				# os.system('cp rec.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp usp.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp database.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp find.txt /sdcard/Android/data/com.maiis.main.files/')
				maiis_install_agan = input('do you want to install maiis y/n : ')
				if maiis_install_agan == 'n':
					print(green+'ok sir pleas wait removing maiis installer file ....'+end)
					animate()
					os.chdir('/data/data/com.termux/files/home/maiis-installer/')
					
					os.system('cp kill.py /sdcard/Android/data/com.maiis.main.files/')
					os.system('cp alarm.mp3 /sdcard/Android/data/com.maiis.main.files/')
					
					os.system('cp pac.py /sdcard/Android/data/com.maiis.main.files/')
					os.chdir('/data/data/com.termux/files/home')
					os.system('rm -rf maiis-installer')
					print(green+'ok its done now restart your terminal'+end)
					input(yellow+'press any key to continue'+end)
					exit()
				elif maiis_install_agan == 'y':
					os.chdir('/data/data/com.termux/files/home/')
					os.system('git clone https:/github.com/005M4CK3R00/maiis.git')
					os.chdir('/data/data/com.termux/files/home/maiis/')
					os.system('cp maiis /data/data/com.termux/files/usr/bin/')
					os.chdir('/data/data/com.termux/files/home/')
					os.system('clear')
					os.chdir('/data/data/com.termux/files/home/maiis-installer/')
					
					os.system('cp kill.py /sdcard/Android/data/com.maiis.main.files/')
					os.system('cp alarm.mp3 /sdcard/Android/data/com.maiis.main.files/')
					
					os.system('cp pac.py /sdcard/Android/data/com.maiis.main.files/')
					os.chdir('/data/data/com.termux/files/home')
					# os.system('rm -rf maiis-installer')
					print(green+"every this is done "+end)
					redif = input(yellow+"do you want to start maiis : "+end+read)
					if redif == "y" or redif == "Y" :
						print("ok pleas wait....")
						time.sleep(2)
						print(bold+blue+"its done maiis are working properly you will a maiis folder in your home directory where you can start maiis by typing python maiis1.py ......"+end)
						animate()
						os.system('maiis')
					else:
						print(read+"ok as your wish ...."+end)
						time.sleep(2)
						print(yellow+"now type maiis and hit enter to start maiis"+end)
						time.sleep(2)
			elif back_restore == "n" or back_restore == "N":
				print(read+'make sure that internet is connected '+end)
				print(green+"ok pleas wait while installing maiis in your system .....")
				animate()
				os.chdir('/data/data/com.termux/files/home/')
				os.system('clear')
				os.system('apt update -y')
				os.system('apt upgrade -y')
				os.system('apt install python -y')
				os.system('apt install python2  -y')
				os.system('apt install figlet -y')
				os.system('apt install p7zip -y')
				os.system('apt install zip -y')
				os.system('apt install unzip -y')
				os.system('apt install mpv -y')
				os.system('apt install nano -y')
				os.system('apt install fortune -y')
				os.system('apt install cowsay -y')
				os.system('apt install toilet -y')
				os.system('apt install git -y')
				os.system('git clone https://github.com/005M4CK3R00/maiis')
				os.chdir('/data/data/com.termux/files/home/maiis/')
				os.system('cp maiis /data/data/com.termux/files/usr/bin/')
				os.chdir('/data/data/com.termux/files/usr/bin')
				os.system('chmod +x *')
				os.chdir('/data/data/com.termux/files/home/')
				os.system('clear')
				os.system('apt install mpv -y')
				os.system('apt install curl -y')
				os.system('pip install tts')
				os.system('pip2 install cookiejar')
				os.system('pip install requests')
				os.system('pip install bs4')
				
				os.system('clear')
				print(read+"setting storage permition pleas wait..."+end)
				animate()
				print(green+"press allow to continue"+end)
				os.system('termux-setup-storage')
				animate()
				print(yellow+'you need to install the termux api please wait while installing termux-api ........ '+end)
				time.sleep(3)
				os.chdir('/data/data/com.termux/files/home/maiis-installer/') # non
				os.system('xdg-open termux-api.apk')
				animate()
				input(blue+'press enter to continue'+end)
				if not os.path.exists('/data/app/com.termux.api-1/base.apk'):
					os.chdir('/data/data/com.termux/files/home/maiis-installer/')
					os.system('cp termux-api.apk /sdcard')
					print(read+'Earror............'+end)
					print(read + 'the termux api is not installed '+end)
					print(yellow+'you need to install it manully...'+end)
					while True:
						print('\033[31mpleas go to your internal storage and then you will the termux-api apk install it and then type enter\33[0m')
						input(yellow+'if you have install it  then press enter '+end)
						if not os.path.exists('/data/app/com.termux.api-1/base.apk'):
							print(read+'install it.......'+end)
							time.sleep(2)
							os.system('clear')
						else:
							print(green+'ok its done...'+end)
							os.chdir('/sdcard/')
							os.system('rm -rf termux-api.apk')
							break
					
				os.system('apt install termux-api')
				print(read+"Worning be cairefull donot try to rename any file"+end)
				print(read+"or donot try to edit maiis"+end)
				time.sleep(4)
				print(green+'pleas wait setting up maiis for you'+end)
				animate()
				os.chdir('/sdcard/')
				if not os.path.exists('Maiis'):
					os.makedirs('Maiis')
				os.chdir('/sdcard/Maiis/')
				if not os.path.exists('eng'):
					os.makedirs('eng')
				if not os.path.exists('video'):
					os.makedirs('video')
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
				os.chdir('/sdcard/Android/data/')
				if not os.path.exists('com.maiis.main.files'):
					os.makedirs('com.maiis.main.files')
				os.chdir('/data/data/com.termux/files/home/maiis-installer/')
				with open("alarm.txt", "w+") as fu: pass
				fu.close()
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
				animate()
				user_nmr = input(blue+'Please chuse the username for maiis : '+end+read)
				print(read+'pleas do not include @ and = in password and username'+end)
				pass_wr = input(green+'pleas chuse the password : '+end)
				# setting uer name and password from here
				with open('usp.txt' , 'w') as opw:
					opw.writelines('username = '+user_nmr+'\n')
					opw.writelines('password @ '+pass_wr)
					print(green+'password and username set...'+end)
				opw.close()
				print(bold+blue+'please chuse a password which you can remember'+end)
				set_rp = input(blue+'please enter a recovery password : '+end)
				set_rps = str(set_rp)
				with open('pc.txt' , 'w') as srp:
					srp.writelines(set_rp)
					print(green+'Done password set '+end)
					time.sleep(1)
				srp.close()
				with open('weather.txt' , 'w') as wetw:
					wr_nm = input(blue+'please enter your current village name : '+end)
					wetw.writelines(wr_nm)
					print(green+'added ....'+end)
				animate()
				os.system('cp kill.py /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp alarm.mp3 /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp pass.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp wp.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp pc.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp usp.txt /sdcard/Android/data/com.maiis.main.files/')
				# os.system('cp rec.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp alarm.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp datab.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp database.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp find.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp pac.py /sdcard/Android/data/com.maiis.main.files/')
				os.chdir('/data/data/com.termux/files/home')
				# os.system('rm -rf maiis-installer')
				print(yellow+"pleas wait ......."+end)
				animate()
				# os.system('termux-tts-speak please now go to your home directory and stsrt maiis and you can type help to see command list please now go to your home directory and stsrt maiis and you can type help to see command list please now go to your home directory and stsrt maiis and you can type help to see command list ')
				print(read+"now start maiis by typing maiis and you can type help to see command list"+end)
				os.chdir('/data/data/com.termux/files/home/')
				os.system('rm -rf maiis-installer')
				os.system('rm -rf maiis')
				os.chdir('/data/data/com.termux/files/usr/bin/')
				os.system('chmod +x *')
				os.chdir('/data/data/com.termux/files/home/')
				insrt = input(yellow+"do you want to start maiis y/n "+end+blue)
				if insrt=="y" or insrt=="Y" :
					print(green+"ok pleas wait ..... "+end)
					print(read+"in first time maiis can take more time to start"+end)
					print(bold+blink+underline+url+"if you got any issu you can talk to admin which is 5M4CK3R ....."+end)
					time.sleep(3)
					animate()
					os.chdir('/data/data/com.termux/files/home')
					os.system('maiis')
					print(read+"pleas restart your termux ......."+end)
					time.sleep(2)
					print(green+'Now can also start maiis from any where from typing maiis'+end)
					time.sleep(3)
					exit()
				elif insrt =="n" or insrt =="N" :
					print(green+"ok sir pleas restart your termux and you can type maiis to start maiis :-) "+end)
					exit()
				else:
					print(green+"ok sir ......"+end)
					print(read+"pleas restart your termux ...... "+end)
					exit()
			else:
				print(read+"enter a valid command"+end)
		else:
			print(green+"ok sir as your wish ...... :-) "+end)
			time.sleep(4)
		
except KeyboardInterrupt:
	print(read+"pleas enter a valid entry donot use ctrl kry"+end)
	main()
	
main()