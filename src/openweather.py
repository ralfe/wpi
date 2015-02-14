__author__ = 'renderle'

import restcall

def getData():
    restcall.doReq("openwaetherData.com")
    return 5
