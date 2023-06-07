import random
import math
import logging as log
from Events.Event import Event
from Events.ReceivePacket import ReceivePacket


class PacketRetransmission(Event):

    def __init__(self, exec_time, model_set):
        super().__init__(exec_time, model_set)
        self.description = "Packet retransmission"


    def execute(self, queue):
        self.model_set.transmitter.send_packet()
        log.info(f"\tTransmitter id = {self.model_set.transmitter.id}: Retransmitting packet No. {self.model_set.transmitter.packet_index + 1}")
        queue.put(ReceivePacket(self.exec_time + math.ceil((self.model_set.channel.current_packet.size / self.model_set.channel.bandwidth) * 1000), self.model_set))
