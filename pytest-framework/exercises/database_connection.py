class DatabaseConnection:
    def __init__(self,ip,connected):
        self.ip = ip
        self.connected = False
    def connect(self):
        print("connecting")
        self.connected=True
    def disconnect(self):
        print("Disconnected")
        self.connected = False
    def get_records(self):
        return self.ip
    