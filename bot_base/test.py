from threading import Timer
from time import sleep

def test():
    pass
def bye():
    print("Bye...bye...")

while 1:
    timer = Timer(interval=1,function=bye)
    sleep(5400)
    timer.start()

