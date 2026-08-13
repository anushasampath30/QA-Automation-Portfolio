class SystemConnection:
    def __init__(self,version,status):
        self.version = version
        self.status = status
        self.connected = False

    def connect(self):
        print("Connected")
        self.connected = True
    def disconnect(self):
        print("Disconnected")
        self.connected = False
    def get_version(self):
        return self.version
    def get_status(self):
        return self.status
    