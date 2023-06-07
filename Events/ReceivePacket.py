import random
import logging as log
from Events.Event import Event
from Events.SendResponse import SendResponse


class ReceivePacket(Event):

    def __init__(self, exec_time, model_set):
        super().__init__(exec_time, model_set)
        self.description = "Packet receive"

    def execute(self, queue):
        self.model_set.receiver.receive_packet()
        log.info(f"\tReceiver: Receive packet from transmitter id = {self.model_set.transmitter.id}")
        queue.put(SendResponse(self.exec_time + random.randint(50, 100), self.model_set))
