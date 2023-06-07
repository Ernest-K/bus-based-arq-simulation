import random
import logging as log
from Events.Event import Event


class ReceiveResponse(Event):

    def __init__(self, exec_time, model_set):
        super().__init__(exec_time, model_set)
        self.description = "Receive response"

    def execute(self, queue):
        from Events.SendPacket import SendPacket
        from Events.PacketRetransmission import PacketRetransmission

        self.model_set.transmitter.receive_response()
        log.info(f"\tTransmitter id = {self.model_set.transmitter.id}: Receive response")
        if self.model_set.transmitter.packet_index == len(self.model_set.transmitter.packets):
            log.info(f"\tTransmitter id = {self.model_set.transmitter.id}: No packet to send")
            self.model_set.channel.busy = False
            self.model_set.channel.current_transmitter_id = None
        elif not self.model_set.channel.ACK:
            queue.put(PacketRetransmission(self.exec_time + random.randint(50, 200), self.model_set))
        else:
            queue.put(SendPacket(self.exec_time + random.randint(50, 200), self.model_set))

        self.model_set.channel.ACK = True





