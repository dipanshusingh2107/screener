import logging
logger = logging.getLogger('django')

def getStocks(code):
    
    loc={}
    exec(code,globals(),loc)    #error handling required  
    check = loc['check']
    return check()  

