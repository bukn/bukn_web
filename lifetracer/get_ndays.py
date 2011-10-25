from time import time, mktime
from datetime import datetime

def get_ndays(date):
    date_seconds = mktime((
            date.year,
            date.month,
            date.day,
            date.hour,
            date.minute,
            date.second,
            0, 0, 0))
    return int((time() - date_seconds) / (3600 * 24)) + 1

def get_number_str(n):
    n1 = n % 10
    if n1 == 1:
        appendix = 'st'
    elif n1 == 2:
        appendix = 'nd'
    elif n1 == 3:
        appendix = 'rd'
    else:
        appendix = 'th'
    return str(n) + appendix

if __name__ == '__main__':
    print get_number_str(115), get_number_str(111), get_number_str(222), get_number_str(113), get_number_str(114)
    print get_ndays(datetime(1986,9,21,8,50))
