# 01/02/2021
from __future__ import absolute_import
import time
from BashColors import C

class FunctionTimer:
    """FunctionTimer class"""
    global ft
    def __init__(self):
        """initialize ft"""
        self.ft=None

    def functionTimer(self, start:float, roundedTo=-1) -> None:
        """prints hours, minutes and seconds"""
        start_time = start
        elapse_time = time.time() - start_time
        # print(f'elapse_time: {elapse_time}')

        if elapse_time >= 3600.0:
            hours = int(elapse_time // 3600)
            minutes = elapse_time - hours * 3600
            minutes = int(minutes // 60)
            seconds = elapse_time % 60
            if roundedTo > -1:
                seconds = round(seconds, roundedTo)
            print(f'functionTimer: {C.IBlue}{hours} hour {minutes} minutes {seconds} seconds{C.ColorOff}')
            
        elif elapse_time >= 60.0:
            minutes = int(elapse_time // 60)
            seconds = elapse_time % 60
            if roundedTo > -1:
                seconds = round(seconds, roundedTo)
            print(f'functionTimer: {C.IBlue}{minutes} minutes {seconds} seconds{C.ColorOff}')

        elif elapse_time < 60.0:
            seconds = elapse_time
            if roundedTo > -1 :
                seconds = round(seconds, roundedTo)
            print(f'functionTimer: {C.IBlue}{seconds} seconds{C.ColorOff}')

ft=FunctionTimer()