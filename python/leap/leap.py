def is_leap_year(year):
    if year % 100:
        if year % 4:
            return False
        else:
            return True
    else:
        if year % 400:
            return False
        else:
            return True
