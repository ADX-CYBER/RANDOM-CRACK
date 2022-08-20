import os, sys
try:
    __import__("adxx").subscribe()
except Exception as e:
    exit(str(e))
