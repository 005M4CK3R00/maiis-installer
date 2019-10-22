import os
import time
import datetime
def main():
	try:
		while True:
			print('Pleas Chuse the option ...... ')
			print('''
			
1. Recovery

2. Install Maiis Normally

3. Maiis Update

4. Forgot Password And User Name														

5. Earror Fixing

6. About

7. Exit

			''')
			chuse_option=int(input(">> : "))
			if chuse_option==1:
				print('Enter The Recovery path .... ')
				recovery_path=input('>> : ')
				os.system('termux-setup-storage')
				input('Press Enter to continue')
				os.chdir(recovery_path)
				print('Pleas wait while recovring the docunments .... ')
				if not os.path.exists('/sdcard/Android/data/com.maiis.main.files/'):
					os.chdir('/sdcard/Android/data/')
					os.mkdir('com.maiis.main.files')
					time.sleep(0.1)
					os.system('clear')
					print('please wait .')
				os.chdir(recovery_path)
				os.system('mv alarm.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('clear')
				print('please wait ..')
				os.system('mv datab.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('clear')
				print('please wait ...')
				os.system('mv pass.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('clear')
				print('please wait ....')
				os.system('mv pc.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('clear')
				print('please wait .....') 
				os.system('mv wp.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('clear')
				print('please wait .......')
				os.system('mv usp.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('clear')
				print('please wait .......')
				os.system('mv database.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('clear')
				print('please wait ........')
				os.system('mv find.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('clear')
				print('please wait .........')
				print('Ok every this is done .......')
				time.sleep(1)
				maiis_install_agan=input('Do you want to install maiis agan y/n : ')
				if maiis_install_agan=='y':
					print('Ok Pleas wait while checking requirenment .............')
					if not os.path.exists('/data/app/com.termux.api-1/base.apk'):
						os.chdir('/data/data/com.termux/files/home/maiis-installer/')
						os.system('xdg-open termux-api.apk')
						input('Press Enter To Continue ')
						if not os.path.exists('/data/app/com.termux.api-1/base.apk'):
							os.chdir('/data/data/com.termux/files/home/maiis-installer/')
							os.system('cp termux-api.apk /sdcard')
							print('Earror............')
							print('The termux api is not installed ')
							print('you need to install it manully...')
							while True:
								input('If you have installed it then press enter ......')
								if not os.path.exists('/data/app/com.termux.api-1/base.apk'):
									print('Install it from your sdcard....')
								print('Ok apk is installed ......')
					print('Checking pakges please wait...')
					if not os.path.exists('/data/data/com.termux/files/usr/bin/python'):
						os.system('apt install python -y')
					
						
					if not os.path.exists('/data/data/com.termux/files/usr/bin/mpv'):
						os.system('apt install mpv -y')
					
						
					if not os.path.exists('/data/data/com.termux/files/usr/bin/python2'):
						os.system('apt install python')
					
						
					if not os.path.exists('/data/data/com.termux/files/usr/bin/figlet'):
						os.system('apt install figlet -y')
					
					if not os.path.exists('/data/data/com.termux/files/usr/bin/nano'):
						os.system('apt install nano -')
					
						
					if not os.path.exists('/data/data/com.termux/files/usr/bin/fortune'):
						os.system('apt install fortune -')
					
						
					if not os.path.exists('/data/data/com.termux/files/usr/bin/python'):
						os.system('apt install python -y')
					
						
					if not os.path.exists('/data/data/com.termux/files/usr/bin/pip'):
						os.system('apt install pip -y ')
					
						
					if not os.path.exists('/data/data/com.termux/files/usr/lib/python3.7/random.py'):
						os.system('pip install rando')
					
						
					if not os.path.exists('/data/data/com.termux/files/usr/lib/python3.7/webbrowser.py'):
						os.system('pip install webbrowser')
						
					if not os.path.exists('/data/data/com.termux/files/usr/lib/python3.7/http/cookiejar.py'):
						os.system('pip install cookiejar')
						os.system('pip install http.cookiejar')
						
					if not os.path.exists('/data/data/com.termux/files/usr/lib/python3.7/threading.py'):
						os.system('pip install threading')
						
					if not os.path.exists('/data/data/com.termux/files/usr/bin/cowsay'):
						os.system('apt install cowsay -y')
						
					if not os.path.exists('/data/data/com.termux/files/usr/bin/fortune'):
						os.system('apt install fortune -y ')
					if not os.path.exists('/data/data/com.termux/files/usr/bin/zip'):
						os.system('apt install zip -y')
					if not os.path.exists('/data/data/com.termux/files/usr/bin/mpv'):
						os.system('apt install mpv -y')
					if not os.path.exists('/data/data/com.termux/files/usr/bin/curl'):
						os.system('apt install curl -y')
					if not os.path.exists('/data/data/com.termux/files/usr/bin/termux-tts-engines'):
						os.system('apt install tts -y')
					
					print('Every thing is installed ........')
					time.sleep(1)
					print('please wait installing some pkgs .......')
					os.system('pip install bs4')
					os.system('pip install http.cookiejar')
					os.system('pip install cookiejar')
					os.system('pip install requests')
					os.chdir('/data/data/com.termux/files/home/')
					os.system('git clone https://github.com/005M4CK3R00/maiis')
					os.chdir('/data/data/com.termux/files/home/maiis/')
					os.system('cp maiis /data/data/com.termux/files/usr/bin/')
					os.chdir('/data/data/com.termux/files/usr/bin/')
					os.system('chmod +x *')
					os.chdir('/data/data/com.termux/files/home/')
					os.system('clear')
					print('Ok every thing is done now tou can type maiis to start maiis ....')
					os.chdir('/data/data/com.termux/files/home/')
					os.system('rm -rf maiis-installer')
					os.system('rm -rf maiis')
				elif maiis_install_agan=='n':
					print('Ok sir now restart the termux and enjoy the maiis ......... ')
					os.chdir('/data/data/com.termux/files/home/')
					os.system('rm -rf maiis-installer')
					os.system('rm -rf maiis')
					exit()
				else:
					print('Pleas enter a valid commands type y and n in small letter\n and y means yes and n means no ....')
					time.sleep(1)
					
# earror fixing start from here ..................

			elif chuse_option==5:
				print('Please wait while fixing all the earrors ........   ')
				os.chdir('/sdcard/Android/data/com.maiis.main.files/')
				with open('wp.txt' , 'w') as opn:
					opn.writelines('0')
				opn.close()
				with open('alarm.txt' , 'w') as fi: pass
				fi.close()
				with open('datab.txt' , 'w') as dfg: pass
				dfg.close()
				print('all earrors are fixed .......\nNow you can restart your maiis')
				os.chdir('/data/data/com.termux/files/home/')
				os.system('rm -rf maiis-installer')
				os.system('rm -rf maiis')
				exit()
			elif chuse_option==3:
				print('Please wait while updating maiis .......')
				if not os.path.exists('/data/data/com.termux/files/usr/bin/maiis'):
					print('Sorry Maiis is not installed in your system ......')
					exit()
				os.chdir('/data/data/com.termux/files/usr/bin/')
				os.system('rm -rf maiis')
				os.chdir('/data/data/com.termux/files/home')
				os.system('git clone https://github.com/005M4CK3R00/maiis')
				os.chdir('/data/data/com.termux/files/home/maiis')
				os.system('cp maiis /data/data/com.termux/files/usr/bin/')
				os.chdir('/data/data/com.termux/files/usr/bin/')
				os.system('chmod +x *')
				os.chdir('/data/data/com.termux/files/home/')
				os.system('rm -rf maiis')
				os.system('clear')
				print('Ok its done maiis is now updated ........')
				exit()
			elif chuse_option==4:
				while True:
					print('Pleas enter your recovery password to confirm that its you ..... ')
					recov_pa_check=input('>> : ')
					if not os.path.exists('/data/data/com.termux/files/usr/bin/maiis'):
						print('Sorry Maiis is not installed in your system ......')
						exit()
					os.chdir('/sdcard/Android/data/com.maiis.main.files/')
					with open('pc.txt' , 'r') as rty:
						real_recov_pa=rty.readline()
						if real_recov_pa==recov_pa_check:
							print('Ok id is confirmed ...')
							with open('usp.txt' , 'r') as dfg:
								print('The username is without = and spaces')
								print(dfg.readline())
								print('password is without @ and spaces')
								print(dfg.readline())
								os.chdir('/data/data/com.termux/files/home/')
								os.system('rm -rf maiis-installer')
								os.system('rm -rf maiis')
								exit()
							dfg.close()
						else:
							print('Sorry id not confirmed please try agan ....')
							time.sleep(1)
					rty.close()
								
			elif chuse_option==2:
				print('Ok Pleas wait while checking requirenment .............')
				time.sleep(1)
				print('If requirenment does not exixt it will install it automatically .....')
				if not os.path.exists('/data/app/com.termux.api-1/base.apk'):
					os.chdir('/data/data/com.termux/files/home/maiis-installer/')
					os.system('xdg-open termux-api.apk')
					input('Press Enter To Continue ')
					if not os.path.exists('/data/app/com.termux.api-1/base.apk'):
						os.chdir('/data/data/com.termux/files/home/maiis-installer/')
						os.system('cp termux-api.apk /sdcard')
						print('Earror............')
						print('The termux api is not installed ')
						print('you need to install it manully...')
						while True:
							input('If you have installed it then press enter ......')
							if not os.path.exists('/data/app/com.termux.api-1/base.apk'):
								print('Install it from your sdcard....')
							print('Ok apk is installed ......')
				print('Checking pakges please wait...')
				if not os.path.exists('/data/data/com.termux/files/usr/bin/python'):
					os.system('apt install python -y')
				
					
				if not os.path.exists('/data/data/com.termux/files/usr/bin/mpv'):
					os.system('apt install mpv -y')
				
					
				if not os.path.exists('/data/data/com.termux/files/usr/bin/python2'):
					os.system('apt install python')
				
					
				if not os.path.exists('/data/data/com.termux/files/usr/bin/figlet'):
					os.system('apt install figlet -y')
				
				if not os.path.exists('/data/data/com.termux/files/usr/bin/nano'):
					os.system('apt install nano -')
				
					
				if not os.path.exists('/data/data/com.termux/files/usr/bin/fortune'):
					os.system('apt install fortune -')
				
					
				if not os.path.exists('/data/data/com.termux/files/usr/bin/python'):
					os.system('apt install python -y')
				
					
				if not os.path.exists('/data/data/com.termux/files/usr/bin/pip'):
					os.system('apt install pip -y ')
				
					
				if not os.path.exists('/data/data/com.termux/files/usr/lib/python3.7/random.py'):
					os.system('pip install rando')
				
					
				if not os.path.exists('/data/data/com.termux/files/usr/lib/python3.7/webbrowser.py'):
					os.system('pip install webbrowser')
					
				if not os.path.exists('/data/data/com.termux/files/usr/lib/python3.7/http/cookiejar.py'):
					os.system('pip install cookiejar')
					os.system('pip install http.cookiejar')
					
				if not os.path.exists('/data/data/com.termux/files/usr/lib/python3.7/threading.py'):
					os.system('pip install threading')
					
				if not os.path.exists('/data/data/com.termux/files/usr/bin/cowsay'):
					os.system('apt install cowsay -y')
					
				if not os.path.exists('/data/data/com.termux/files/usr/bin/fortune'):
					os.system('apt install fortune -y ')
				if not os.path.exists('/data/data/com.termux/files/usr/bin/zip'):
					os.system('apt install zip -y')
				if not os.path.exists('/data/data/com.termux/files/usr/bin/mpv'):
					os.system('apt install mpv -y')
				if not os.path.exists('/data/data/com.termux/files/usr/bin/curl'):
					os.system('apt install curl -y')
				if not os.path.exists('/data/data/com.termux/files/usr/bin/termux-tts-engines'):
					os.system('apt install tts -y')
				
				print('Every thing is installed ........')
				time.sleep(1)
				print('please wait installing some pkgs .......')
				os.system('pip install bs4')
				#  os.system('pip install http.cookiejar')
				os.system('pip install cookiejar')
				os.system('pip install requests')
				os.chdir('/data/data/com.termux/files/home/')
				os.system('git clone https://github.com/005M4CK3R00/maiis')
				os.chdir('/data/data/com.termux/files/home/maiis/')
				os.system('cp maiis /data/data/com.termux/files/usr/bin/')
				os.chdir('/data/data/com.termux/files/usr/bin/')
				os.system('chmod +x *')
				os.chdir('/data/data/com.termux/files/home/')
				os.system('clear')
				# coping databases file from maiis to sdcard
				os.chdir('/data/data/com.termux/files/home/maiis-installer/')
# main process start from here
				os.chdir('/sdcard/')
				if not os.path.exists('Maiis'):
					os.system('mkdir Maiis')
				os.chdir('/sdcard/Maiis')
				if not os.path.exists('eng'):
					os.mkdir('eng')
				if not os.path.exists('video'):
					os.mkdir('video')
				if not os.path.exists('3dsong'):
					os.mkdir('3dsong')
				if not os.path.exists('sadsongs'):
					os.mkdir('sadsongs')
				if not os.path.exists('popsongs'):
					os.mkdir('popsongs')
				if not os.path.exists('bhajan'):
					os.mkdir('bhajan')
				if not os.path.exists('panjabi'):
					os.mkdir('panjabi')
				if not os.path.exists('othersongs'):
					os.mkdir('othersongs')
				os.chdir('/sdcard/Android/data/')
				if not os.path.exists('com.maiis.main.files'):
					os.mkdir('com.maiis.main.files')
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
				user_nmr = input('Please chuse the username for maiis : ')
				print('pleas do not include @ and = in password and username')
				pass_wr = input('pleas chuse the password : ')
# setting uer name and password from here
				with open('usp.txt' , 'w') as opw:
					opw.writelines('username = '+user_nmr+'\n')
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
				with open('weather.txt' , 'w') as wetw:
					wr_nm = input('please enter your current village name : ')
					wetw.writelines(wr_nm)
					print('added ....')
					time.sleep(1)
				os.chdir('/data/data/com.termux/files/home/maiis-installer/')
				os.system('cp kill.py /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp alarm.mp3 /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp pass.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp wp.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp pc.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp usp.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp alarm.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp datab.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp database.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp find.txt /sdcard/Android/data/com.maiis.main.files/')
				os.system('cp pac.py /sdcard/Android/data/com.maiis.main.files/')
				os.chdir('/data/data/com.termux/files/home')
# coping done ..... 
				print('Ok every thing is done now you can type maiis to start maiis ....')
				os.chdir('/data/data/com.termux/files/home/')
				os.system('rm -rf maiis-installer')
				os.system('rm -rf maiis')
			
	
			elif chuse_option==6:
				print('''
				
this is maiis the A.I robotic system and it works only in termux app  by using maiis installer\n
you can easily install the maiis you can type help to see commands list in it or you can do \n
many works in maiis it is the one of the best and easy to use tool it can also hack facebook \n
by bruteforce attack and it can also hack zip files and other and it in in a developnment now \n
this is not a real verson of maiis or final verson it is still in a developnment if you found any \n
earror in maiis you can talk to admin who was creater of the maiis which is 5M4CK3R and \n
you can start maiis from any where it is very cool to talk to maiis and it is very usefull tool \n
and this is very big tool not in size but in coading if you see it is very harder and i means its \n
admin i have maded it in android device which seems like pritty imposible but nothing is \n
impossible in here i hope you like maiis and if you got any earror you can contact me at github \n
i will try to solve your all problum and also for sorry for spelling mistakes i thing you can ignore \n
them so enjoy maiis happy hacking day byy ...........

				''')
				exit()
			elif chuse_option==7:
				print('Ok sir as your wish ......')
				exit()
				
				
	except KeyboardInterrupt:
		print('Pleas donot use ctrl + c like keyword ')
	except EOFError:
		print('Pleas donot use ctrl + d like keyword')
	except NameError:
		print('Pleas enter the right name ')
		
main()