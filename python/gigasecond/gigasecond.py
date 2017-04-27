from datetime import timedelta


def add_gigasecond(date):
    '''
    get a time, add increase 10^9 seconds
    '''
    gigatime = timedelta(seconds=1000000000)
    return date + gigatime
