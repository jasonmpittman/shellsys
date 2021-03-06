
from configparser import ConfigParser
import os, syslog, datetime, time

class Shellsys:
    """ """

    def __init__(self):
        self.__config = ConfigParser()
        self.__config.read('config.ini')
        self.__shell = self.__config.get('history', 'shell')
        self.__historyDir = self.__config.get('history', 'history_dir')
        self.__historyFile = self.__config.get('history', 'history_file')
        

    def getShell(self):
        """ """
        return self.__shell
    
    def getHistoryDir(self):
        """ """
        return self.__historyDir

    def getHistoryFile(self):
        """ """
        return self.__historyFile

    def readHistory(self, dir, file):
        """ """
        history = dir + '/' + file
        with open(history, "r") as history_handle:
            history_handle.seek(0, 2)
            while True:
                line = history_handle.readline()
                if not line:
                    time.sleep(0.5)
                    continue
                print(line.strip('\n')) # this yields #1615052581\nls\n

    def convertEpochTime(self, timestamp):
        return datetime.datetime.fromtimestamp(timestamp).strftime('%c')


s = Shellsys()

shell = s.getShell()
dir = s.getHistoryDir()
file = s.getHistoryFile()

s.readHistory(dir, file)

