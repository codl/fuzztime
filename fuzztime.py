#!/usr/bin/python

import time

# SUPER SECRET EASTER EGG
partypartyparty=True

t=time.localtime(time.time())
h=t[4]
m=t[5]

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

minutes = (
    0 : "% o'clock"
    1 : "past %"
    10 : "ten past %"
    15 : "quarter past %"
    20 : "twenty past %"
    30 : "half past %"
    40 : "twenty to !"
    45 : "quarter to !"
    50 : "ten to !"
    60 : "!"
    )

exactly = "exactly %"

def fuzzy(h,m):
    for i in minutes.iterkeys():
      #Do stuff

if __name__ == "__main__":
    print fuzzy(h,m)
