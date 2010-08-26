#!/usr/bin/python

import time

# Words
hours = ( 
    "twelve",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven"
    )

minutes = { # % will be replaced by the current hour, ! will be replaced by the next hour
    0: "% o'clock",
    1: "past %",
    10: "ten past %",
    15: "quarter past %",
    20: "twenty past %",
    30: "half past %",
    40: "twenty to !",
    45: "quarter to !",
    50: "ten to !",
    60: "!"
    }

almost = "almost %"
exactly = "exactly %"


def fuzzy(h,m):
    diff = 60
    for i in minutes.iterkeys():
        tmpdiff=m-i
        if abs(tmpdiff) < abs(diff):
            diff=tmpdiff
            ret=minutes[i].replace("%", hours[h]).replace("!", hours[h+1])
    if diff == 0:
        ret=exactly.replace("%", ret)
    elif diff >= -2:
        ret=almost.replace("%", ret)
    if partypartyparty and h == 0 and m == 0:
        ret="PARTYPARTYPARTY"
    return ret

if __name__ == "__main__":
    t=time.localtime(time.time())
    # SUPER SECRET EASTER EGG
    partypartyparty=True
    # I WONDER WHAT IT DOES
    print fuzzy(t[3]%12,t[4])
