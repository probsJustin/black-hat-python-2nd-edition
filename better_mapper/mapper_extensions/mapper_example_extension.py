import re
from urllib.parse import urlparse

class Extension:
    #FILTERS = [".jpg", ".gif", ".png", ".css"]
    FILTERS = []
    NAME = ""
    STORAGE_FILE_DIR = ""
    TARGET = ""
    THREADS = 1
    URL_PARSED_OBJECT = ""
    PRIORITY_LEVEL = 0

    def __init__(self, targetUrl, filters, priorityLevel):
        print(f'init new target extension')
        self.setTarget(targetUrl)
        self.setName(targetUrl)
        self.createStorageFileDir()
        self.setFilters(filters)
        self.createCurrentUrl()
        self.setPriorityLevel(priorityLevel)

# BELOW THIS ARE JUST SETTERS, GETTERS AND CREATES FOR DATA FOR THE EXTENSION IT SELF

    def setPriorityLevel(self, priorityLevel):
        self.PRIORITY_LEVEL = priorityLevel

    def getPriorityLevel(self):
        return self.PRIORITY_LEVEL

    def setFilters(self, filters):
        self.FILTERS = filters

    def setTarget(self, targetURL):
        self.TARGET = targetURL

    def getTarget(self):
        return self.TARGET

    def createStorageFileDir(self):
        self.STORAGE_FILE_DIR = f'./stored_trees/{self.NAME}'

    def setStorageFileDir(self, fileDirectory):
        self.STORAGE_FILE_DIR = fileDirectory

    def getStorageFileDir(self):
        return self.STORAGE_FILE_DIR

    def setName(self, targetUrl):
        self.NAME = re.search("^(?:http.?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n?]+)", self.TARGET)

    def getName(self):
        return self.NAME

    def createCurrentUrl(self):
        self.URL_PARSED_OBJECT = urlparse(self.TARGET)

    def setCurrentUrl(self):
        self.URL_PARSED_OBJECT = urlparse(self.TARGET)

    def getCurrentUrl(self):
        return self.URL_PARSED_OBJECT

    def setThreads(self, threads):
        self.THREADS = threads

    def getThreads(self):
        return self.THREADS