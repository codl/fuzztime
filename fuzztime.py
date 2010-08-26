#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Outputs current time as an approximation"""

import sys
import time

# Locale
sys.path=["locale", "/home/codl/dev/fuzztime/locale"]+sys.path
# from en import *
from en import *

def fuzz(h,m):
    """Outputs given time as an approximation"""
    diff = 60
    for i in minutes.iterkeys():
        tmpdiff=m-i
        if abs(tmpdiff) < abs(diff):
            diff=tmpdiff
            ret=minutes[i].replace("%", hours[h]).replace("!", hours[(h+1)%24])
    if h in hoursplural:
        ret=ret.replace("$", plural)
    else:
        ret=ret.replace("$", "")
    if h in hoursfem:
        ret=ret.replace("3", f)
    else:
        ret=ret.replace("3", m)

    if diff == 0:
        ret=exactly.replace("%", ret)
    elif diff >= -3 and diff < 0 and almost != "%":
        ret=almost.replace("%", ret)
    elif diff < 0:
        ret=soon.replace("%", ret)
    if partypartyparty and h == 0 and m == 0:
        ret="PARTYPARTYPARTY"
    return ret

# SUPER SECRET EASTER EGG
partypartyparty=True
# OH GOD I CAN'T WAIT TO SEE WHAT IT DOES

if __name__ == "__main__":
    t=time.localtime(time.time())
    print(unicode(fuzz(t[3],t[4])))
