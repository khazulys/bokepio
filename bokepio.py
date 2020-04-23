import sys, os, time
import wget as bokep
import urllib

def logo():
	os.system('clear')
	print ("""

\t \033[1;36m   ___       __              ________ 
\t \033[1;36m  / _ )___  / /_____ ___    /  _/ __ \\
\t \033[1;97m / _  / _ \/  '_/ -_) _ \  _/ // /_/ /
\t \033[1;97m/____/\___/_/\_\\__/ ._ _/ /___/\____/ 
\t \033[1;91m                  /_/                 

	    \033[1;97mDownload Bokep Videos\n""")
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91m\t> \033[1;97mSedang Download \033[1;96m"+o),;sys.stdout.flush();time.sleep(1)

def menu():

			logo()
			print ("""
		\033[1;96m01]> \033[1;97mHijab sange
		\033[1;96m02]> \033[1;97mVina garut
		\033[1;96m03]> \033[1;97mNikmatnya bercinta
		\033[1;96m04]> \033[1;97mSMA Ngentot
		\033[1;96m05]> \033[1;97mAdik kakak \n""")
			try:
				pol = raw_input("	\033[1;91m> \033[1;97m")
				if pol == "01" or pol == "1":
					tik()
					urllib.urlretrieve("http://download847.mediafire.com/qvgjfsd7xuug/zxfwkkglo1t44kl/HijabNgewe.mp4","HijabNgewe.mp4")
					print "\n\033[1;91m\t> \033[1;97mDownload Done"
				elif pol == "02" or pol == "2":
					tik()
					urllib.urlretrieve("http://download1589.mediafire.com/bzdauuxb524g/hi6yuz6z3v18j04/Vina.mp4","Vina.mp4")
					print "\n\033[1;91m\t> \033[1;97mDownload done"
				elif pol == "03" or pol == "3":
					tik()
					urllib.urlretrieve("http://download1515.mediafire.com/1m49t99i7kog/jbzvzpeu38wtgb7/nikmat.mp4","nikmat.mp4")
					print "\n\033[1;91m\t> \033[1;97mDownload Done"
				elif pol == "04" or pol == "4":
					tik()
					urllib.urlretrieve("http://download1479.mediafire.com/d8az90nvfq0g/fejz9fyxj0wzxbt/sma.mp4","sma.mp4")
					print "\n\033[1;91m\t> \033[1;97mDownload Done"
				elif pol == "05" or pol == "5":
					tik()
					urllib.urlretrieve("http://download1496.mediafire.com/1ev7de6798ag/qcf47caxccp2bed/Adikkakak.mp4","AdikKakak.mp4")
					print "\n\033[1;91m\t> \033[1;97mDownload Done"
				else:
					exit()




			except:
				pass

if __name__=="__main__":
	menu()
