class Packet:
    def __init__(self, data, checksum):
        self.data = data
        self.checksum = checksum
        self.size = len(data)
