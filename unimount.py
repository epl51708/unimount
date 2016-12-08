#!/usr/bin/python

#---------------------------------------#
# Lukas Epple							#
# Q4 2016								#
#										#
# lukas.epple@physik.uni-regensburg.de	#
#---------------------------------------#

import os, re, subprocess, getpass, time
	

#variables
user	= getpass.getuser()
mph		= "/home/"+user+"/Desktop/uni_home"		#mount point for uni /home directory

#Getting NDS name
nds = input("Please enter your NDS user name: ")

#RegEx check
nds_regex = re.compile("[a-z]{3}[0-9]{5}", 0)
while 1:
	if(nds_regex.match(nds)):
		break
	else:
		nds = input("\nPlease enter a valid NDS user name: (e.g. vip12345)")
		
pw		= getpass.getpass("Please enter your NDS Password: ")

#creating mointing point on local Desktop
subprocess.call("mkdir "+mph, shell=True)

#mounting uni /home in the directory mph -> mount point for home
mnt_home  = "echo "+pw+" | "
mnt_home += "sshfs "+nds+"@rex2.uni-regensburg.de:"
mnt_home += "/home/"+nds+" "+mph
mnt_home +=" -o  reconnect -o follow_symlinks -o password_stdin"

subprocess.call(mnt_home, shell=True)


#unmounting and removing locally created folder (mountpoint)
time.sleep(10)
subprocess.call("fusermount -u "+mph, shell=True)
subprocess.call("rmdir "+mph, shell=True)
