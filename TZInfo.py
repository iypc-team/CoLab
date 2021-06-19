# 09/07/2020

import os
import datetime, dateutil
from datetime import *
from dateutil import *
from dateutil.tz import *
from time import ctime
import BashColors
from BashColors import *

class TZI:
    __all__ = sorted(['workingDir', 'tzi','alutianTZone' ,'getCurrentTimeIn', 
                      'getFileStats', 'alaskanTZone', 'hawaiianTZone'
                      'gmtTZone','easternTZone', 'centralTZone', 
                      'mountainTZone', 'pacificTZone'])

    def __init__(self):
        self.tzi = None
        self.workingDir = None
        self.gmtTZone = dateutil.tz.gettz('Etc/Gmt')
        self.easternTZone = dateutil.tz.gettz('America/New York')
        self.centralTZone = dateutil.tz.gettz('America/Chicago')
        self.mountainTZone = dateutil.tz.gettz('America/Denver')
        self.pacificTZone = dateutil.tz.gettz('America/Los_Angeles')
        self.alaskanTZone = dateutil.tz.gettz('America/Anchorage')
        self. alutianTZone = dateutil.tz.gettz('America/Adak')
        self.hawaiianTZone = dateutil.tz.gettz('Pacific/Honolulu')
        
    def getWorkingDirectory(self):
        workingDirPath = '/gdrive/My Drive'
        return workingDirPath

    def getCurrentTimeIn(self, newTZone, silent=True):
        '''returns tuple (rawDatetimeString, today, formatToday)'''
        dateutil.tz.gettz.cache_clear()
        rawDatetimeString = datetime.now()
        today = datetime.now(tz=newTZone)
        formatToday = today.strftime('%h/%d/%Y   %-I:%M%p')
        if not silent:
            print(f'{C.White}{today}\n{C.Green}{formatToday}')
        elif silent:
            return (rawDatetimeString, today, formatToday)
        
    def getFileStats(self, newPath):
        mTime = os.path.getmtime(filename=newPath)

        modTime = datetime.fromtimestamp(mTime)
        formatDate = str(modTime.strftime('%h/%d/%Y   %-I:%M%p'))
        size = str(os.path.getsize(newPath))
        formatStats = formatDate + '    size: ' + size + ' bytes'
        return formatStats

tzi = TZI()