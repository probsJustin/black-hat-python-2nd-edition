import logging

def configFile(configFileLocation, logLevel):
    if(logLevel == "debug"):
        logLevel = logging.DEBUG
    if(logLevel == "info"):
        logLevel = logging.INFO
    logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename=configFileLocation, level=logLevel)

def debug(msg):
    print(f'[DEBUG] {msg}')
    logging.debug(msg)

def info(msg):
    print(f'[INFO] {msg}')
    logging.info(msg)


