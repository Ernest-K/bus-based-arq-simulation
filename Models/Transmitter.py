import logging as log
import copy
from Models.Input import Input
from Models.Packet import Packet

input_model = Input()


class Transmitter:

    def __init__(self, id_, channel, message_size, packet_size):
        self.id = id_
        self.channel = channel
        self.message = input_model.generate_message(message_size)
        self.packets = self.__prepare_packets(self.message, packet_size)
        self.packet_index = 0
        self.retransmission_counter = 0  # for statistics
        self.collision_counter = 0

        # log.info(f"\tTransmitter id = {self.id}: Message to send")
        # log.info(f"\tMessage data: {self.message.data}")

    def check_channel_availability(self):
        return self.channel.busy

    def send_packet(self):
        self.channel.packets_left = len(self.packets) - self.packet_index - 1
        self.channel.current_packet = copy.deepcopy(self.packets[self.packet_index])

    def receive_response(self):
        if self.channel.ACK:
            self.packet_index += 1
        else:
            self.retransmission_counter += 1
            self.collision_counter += 1

    def __prepare_packets(self, message, packet_size):
        packets = []
        for i in range(0, message.length, packet_size):
            data = message.data[i:i + packet_size]
            packets.append(Packet(data, self.__calc_checksum(data)))

        return packets

    def __calc_checksum(self, data):
        return sum(int(bit) for bit in data) % 2 ** 8
