import os, sys
os.system('git pull')
try:
    __import__("welcome.py").menu()
except Exception as e:
    exit(str(e))
