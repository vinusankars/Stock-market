from StockValue import Data
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from threading import Thread
import sys
import datetime
import smtplib

data=Data()
data.collect()
now = datetime.datetime.now()

f = open('abcd.txt', 'w')
f.close()
print(list(data.world_market.keys()))
name = input('Enter the world market name : ')
threshhold = float(input('Enter the threshhold value for notification : '))


if name not in list(data.world_market.keys()):
    print('Not Available')
    sys.exit()

def val(s):
    s = float(''.join(s.split(',')))
    return s


def loops():
    start = time.time()
    while True :
        
        f = open('abcd.txt', 'a')
        f.write(str(time.time()-start) + ',' + str(val(data.world_market[name])) + '\n')
        f.close()
        data.collect()
        time.sleep(2)
           
Ltime, Lvalue, flag = 0, 0, 0

def plot() :

    fig = plt.figure()
    fig.suptitle('World Stock Market for ' + name, fontsize = 12, fontweight = 'bold')
    g = fig.add_subplot(1,1,1)
    g.set_xlabel('Time')
    g.set_ylabel('Stock Value')

    def change(i) :

        global Ltime, Lvalue, flag
        file_data = open('abcd.txt', 'r').read()
        points = file_data.split('\n')
        xar = []
        yar = []
        
        for l in points :
            if len(l) > 1 :
                x,y = l.split(',')
                if float(y) < float(threshhold) :
                    Ltime = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
                    Lvalue = y
                    flag += 1
                    s = name + ' went to ' + Lvalue + ' at ' + Ltime
                    if flag > 1 :
                        print(s)
                        
                xar.append(float(x))
                yar.append(float(y))
                
        g.plot(xar, yar)
        
    change_graph = animation.FuncAnimation(fig, change, interval = 3000)
    plt.show()

bg = Thread(target = loops)
bg.start()
plot()
