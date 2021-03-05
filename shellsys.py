
from configparser import ConfigParser
import os, syslog, time

class Shellsys:
    """ """

    __last_line = None

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

        if self.__last_line is None:
            with open(history, 'r') as history_data:        
                self.__setLastLine(history)
                print(history_data.read())
        else:
            with open(history, 'r') as history_data:
                for line in history_data:
                    if line.strip() == self.__last_line:
                        break
                
                for line in history_data:
                    print(line)



    def getLastLine(self, file):
        """returns the last line of the passed file"""
        pass


    def __setLastLine(self, file):
        """ """
        with open(file, 'r') as file_handle:
            self.__last_line = file_handle.readlines()[-1]
            
    # this is no longer necessary
    def __isFileChanged(self, file, modified_time):
        """utility method to check if modified time of indicated file has changed"""
        
        new_time = time.ctime(os.path.getmtime(file))
        print(new_time + "\t" + modified_time)
        if new_time != modified_time:
            return True
        else:
            return False


s = Shellsys()

shell = s.getShell()
dir = s.getHistoryDir()
file = s.getHistoryFile()

try:
    while True:
        s.readHistory(dir, file)
except KeyboardInterrupt:
    pass
