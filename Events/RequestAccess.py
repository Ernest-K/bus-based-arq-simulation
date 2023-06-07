import random
import logging as log
from Events.Event import Event
from Events.SendPacket import SendPacket


class RequestAccess(Event):

    def __init__(self, exec_time, model_set):
        super().__init__(exec_time, model_set)
        self.description = "Channel access request"

    def execute(self, queue):
        from Events.WaitForChannel import WaitForChannel

        channel_busy = self.model_set.transmitter.check_channel_availability()
        if channel_busy:
            log.info(f"\tTransmitter id = {self.model_set.transmitter.id}: Channel is occupied")
            queue.put(WaitForChannel(self.exec_time + 1, self.model_set))

        else:
            log.info(f"\tTransmitter id = {self.model_set.transmitter.id}: Channel is free")
            queue.put(SendPacket(self.exec_time + random.randint(5, 50), self.model_set))


