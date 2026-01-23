"""
    Given a time in -hour AM/PM format, convert it to military (24-hour) time.

    - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
    - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""
import re

def timeConversion(s):
    pattern = re.compile(r'([0-9]+):([0-9]+):([0-9]+)(AM|PM)')  
    result = pattern.search(s)
    h, m, s, t = result.groups()
    
    h = int(h)

    if t == 'PM':
        return f"{h+12}:{m}:{s}" if h < 12 else f"{h}:{m}:{s}"

    if t == 'AM':
        return f"0{h-12}:{m}:{s}" if h >= 12 else f"0{h}:{m}:{s}"


#print(timeConversion('12:00:00AM'))

assert timeConversion('12:00:00AM') == '00:00:00'
assert timeConversion('12:00:00PM') == '12:00:00'
assert timeConversion('07:05:45PM') == '19:05:45'

assert timeConversion('23:59:59PM') == '23:59:59'
assert timeConversion('01:00:00AM') == '01:00:00'