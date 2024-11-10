
import time

from FlagThread import FlagThread
from client import OPCClient
from datetime import datetime



def main():
    finishFlag = False
    file = open("config.txt")

    timeInterval = float(file.read())
    url = "opc.tcp://localhost:4841/freeopcua/server/"
    opcclient = OPCClient()
    opcData = ""

    thread = FlagThread()
    thread.start()

    while not finishFlag:
        opcclient.ReceiveDataFromServer()

        print(opcclient.dataReceived)


        finishFlag = thread.value
        print(finishFlag)
        time.sleep(timeInterval)

    opcData += opcclient.dataReceived

    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")
    filename = current_time + ".csv"


    f = open(filename, "w")
    f.write(opcData)
    opcclient.CloseConnection()
    exit(1)









if __name__ == "__main__":
    main()