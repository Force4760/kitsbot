#Import modules
import time

#covert Unix time to GMT
def tcon(t):
    return time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(t))