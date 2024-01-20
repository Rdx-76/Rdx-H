import os, sys
os.system('git pull')
try:
    os.system("python welcome.py")
except Exception as e:
    exit(str(e))
