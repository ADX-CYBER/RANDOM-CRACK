import os, sys
try:
    __import__("adxx").adx_()
except Exception as e:
    exit(str(e))
