#!/usr/bin/python

#---------------------------------------#
# Lukas Epple							#
# Q4 2016								#
#										#
# lukas.epple@physik.uni-regensburg.de	#
#---------------------------------------#

import os

#get username
user = os.popen('echo $USER').read()
print(user)
