from opcua import Client


class OPCClient:
    def __init__(self):
        self._url = "opc.tcp://localhost:4841/freeopcua/server/"
        self._dataFromServer = 0
        self._nodeId = "ns=2;i="
        self._serverStatus = "i=2259"
        self._updateStep = 0
        self._stepAmount = 5
        self.dataReceived = ""
        self.client = None
        self.ConnectToServer()

    def ConnectToServer(self):
        try:
            self.client = Client(self._url)
            self.client.connect()
            print("Connected to OPC UA server.")
        except Exception as e:
            print("Failed to connect to OPC UA server:", e)

    def StartReception(self,it):
        try:
            self._nodeId += str(it)
            node = self.client.get_node(self._nodeId)
            value = node.get_value()
            self.dataReceived += f" {value}"
        except Exception as e:
            print("Error during StartReception:", e)
            self.ConnectToServer()
        finally:
            self._nodeId = "ns=2;i="

    def CloseConnection(self):
        self.client.disconnect()

    def ReceiveDataFromServer(self):
        if self.client is None:
            self.ConnectToServer()

        if self.client is not None:
            tab = [7, 8, 5, 10, 6]
            it = 0
            if self._updateStep % self._stepAmount == 0:
                try:
                    for i in tab:
                        self.StartReception(i)
                    self._updateStep = 0
                except ConnectionResetError:
                    print("Connection was reset. Attempting to reconnect...")
                    self.ConnectToServer()
            self._updateStep += 1