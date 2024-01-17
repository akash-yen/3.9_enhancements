# logging

# depending on the type of logging the data is divided into levels

#Critical 50 --> Reperesents very serious prblm that needs high attenetion

#Error 40 -->  Represnts a serious error

# Warning 30 --> Represents a warning msg some caustion needed,it is a alert to programmer

# Info 20 -->some imp msg

#Debug 10 --> Represnts a msg which can be used for debugging

#NOTSET 0 --> REPRESENTS LOGGING LVL NOT SET

# Deaulft logging lvl is warning so warning and above are displayed


import logging
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# #logging.basicConfig(filename = 'log.txt', level = 30)
# logging.warning('Watch out!')  # will print a message to the console
# logging.info('I told you so')  # will not print anything


logging.basicConfig(filename='log.txt', level=logging.DEBUG , format='%(asctime)s:%(levelname)s:%(message)s')
logging.info('a new request came')
try:
    x = int(input('the number'))
    y = int(input('the number'))
    print('the result',x/y)
except ZeroDivisionError as msg:
    print('canot divide with zero')
    logging.exception(msg)
except ValueError as msg:
    print('please provide int values only')
    logging.exception(msg)
logging.info('request processing compleeted')