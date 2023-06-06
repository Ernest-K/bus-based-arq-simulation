import logging as log
from Models.Message import Message
from Models.Output import Output

output_model = Output()


class Receiver:
    def __init__(self, channel):
        self.packets = []
        self.channel = channel
        self.packet_counter = 0
        self.message = None

    def receive_packet(self):
        self.packets.append(self.channel.current_packet)

    def send_response(self):
        if self.__is_valid_last_packet():
            self.channel.ACK = True
            if self.channel.packets_left == 0:
                message_data = self.__flatten([packet.data for packet in self.packets])
                self.message = Message(message_data, len(message_data))
                output_model.set_message(self.message)
                log.info(f"\tReceiver: All message received")
                # log.info(f"\tMessage data: {output_model.get_message().data}")
                self.packets = []
        else:
            self.packets.pop()
            self.channel.ACK = False

    def __is_valid_last_packet(self):
        if self.__calc_checksum(self.packets[-1].data) == self.packets[-1].checksum:
            return True
        else:
            self.packets[-1] = None
        return False

    def __calc_checksum(self, data):
        return sum(int(bit) for bit in data) % 2 ** 8

    def __flatten(self, array):
        result = []
        for el in array:
            result += el
        return result