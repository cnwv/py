import itertools
import time
from time import sleep
from itertools import cycle


class Trafficlight:
    __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [5, 32]], ["yellow", [2, 33]]]

    def change(self):
        for i in itertools.cycle(self.__color):
            print(f"\r\033[{i[1][1]}m\033[1m{i[0]}\033[0m", end="")
            time.sleep(i[1][0])


light = Trafficlight()
light.change()



