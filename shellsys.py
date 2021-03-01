
from configparser import ConfigParser
import os, time

class Shellsys:
    """ """

    def __init__(self):
        self.__config = ConfigParser()
        self.__config.read('config.ini')
        self.__shell = self.__config.get('history', 'shell')
        self.__historyDir = self.__config.get('history', 'history_dir')
        self.__historyFile = self.__config.get('history', 'history_file')
        self.__last_line

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
        
        
        #if last_line in file then we read from that point on else return file not modified
            history_handle = open(history, 'r')
            return history_handle.read()
        else:
            return "File not modified"

    def __isFileChanged(self, file, modified_time):
        new_time = time.ctime(os.path.getmtime(file))
        print(new_time)
        if new_time != self.__modified_time:
            return True
        else:
            return False


s = Shellsys()

shell = s.getShell()
dir = s.getHistoryDir()
file = s.getHistoryFile()

history = s.readHistory(dir, file)
print(history)

