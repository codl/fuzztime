# -*- coding: utf-8 -*-

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
    "eleven",
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

hoursplural = (1, 2, 3, "COMPLETELY", "USELESS", "HERE")

minutes = { # % will be replaced by the current hour, ! will be replaced by the next hour
            # = will be "s" if hours are plural, see hoursplural variable
    0: "% o'clock",
    0.5: "past %",
    10: "ten past %",
    15: "quarter past %",
    20: "twenty past %",
    30: "half past %",
    40: "twenty to !",
    45: "quarter to !",
    50: "ten to !",
    60: "!"
    }

soon = "%"
almost = "almost %"
exactly = "exactly %"
