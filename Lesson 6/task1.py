# Task 1 Traffic light
from time import sleep
from itertools import cycle

class TrafficLight:
    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2),
                      ('Green', 5), ('Yellow', 2))
    def run(self):
        for color, sec in cycle(self.__color):
            print(color, '{} sec'.format(sec))
            sleep(sec)

traff_light = TrafficLight()
traff_light.run()