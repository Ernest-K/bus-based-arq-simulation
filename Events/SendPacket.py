import random
import math
import logging as log

from Events.Event import Event
from Events.ReceivePacket import ReceivePacket
from Events.WaitForChannel import WaitForChannel


class SendPacket(Event):

    def __init__(self, exec_time, model_set):
        super().__init__(exec_time, model_set)
        self.description = "Sending packet"

    def execute(self, queue):
        if self.model_set.channel.current_transmitter_id is None or self.model_set.channel.current_transmitter_id == self.model_set.transmitter.id:
            self.model_set.transmitter.send_packet()
            self.model_set.channel.current_transmitter_id = self.model_set.transmitter.id
            self.model_set.channel.busy = True
            log.info(f"\tTransmitter id = {self.model_set.transmitter.id}: Sending packet {self.model_set.transmitter.packet_index + 1} / {len(self.model_set.transmitter.packets)}")
            queue.put(ReceivePacket(self.exec_time + math.ceil((self.model_set.channel.current_packet.size / self.model_set.channel.bandwidth) * 1000), self.model_set))
        else:
            log.info(f"\tTransmitter id = {self.model_set.transmitter.id}: Collision")
            self.model_set.channel.damage_current_packet()
            self.model_set.transmitter.collision_counter += 1
            queue.put(WaitForChannel(self.exec_time + 1, self.model_set))

