import os, sys
try:
    __import__("adxfree").subscribe()
except Exception as e:
    exit(str(e))
