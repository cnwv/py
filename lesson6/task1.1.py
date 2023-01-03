from time import sleep
from itertools import cycle


class TrafficLight:
    __colors = [("red", 3), ("yellow", 5), ("green", 2)]

    def running(self):
        for i in cycle(self.__colors):
            print(i[0])
            sleep(i[1])


light = TrafficLight()
light.running()

