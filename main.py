import os
import threading
import time

from opcua import client
from client import OPCClient
from datetime import datetime



def main():
    finishFlag = False
    file = open("config.txt")

    timeInterval = float(file.read())
    url = "opc.tcp://localhost:4841/freeopcua/server/"

    opcClient = OPCClient()

    while not finishFlag:
        opcClient.ReceiveDataFromServer()
        time.sleep(timeInterval)
        print(opcClient.dataReceived)
        finishFlag = opcClient.CheckConnection()

    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")
    filename = current_time + ".csv"
    f = open(str(filename), "w")
    f.write(opcClient.dataReceived)









if __name__ == "__main__":
    main()