__author__ = 'renderle'

import restcall

def getData():
    restcall.doReq("wunderground.com")
    return 5
