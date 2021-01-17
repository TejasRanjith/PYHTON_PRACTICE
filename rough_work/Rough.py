#import os     #Bank_Management_System.py
#os.system("python grp_app//Bank_Management_System.py")
#os.system("python Rough.py")

#to run another python file in this file ↑↑↑

import re
s = "blahblah@yahoo.com"
domain = re.search("@[\w.]+", s)
print (domain.group())
