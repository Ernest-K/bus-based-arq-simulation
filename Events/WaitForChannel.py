import random
import logging as log
from Events.Event import Event


class WaitForChannel(Event):

    def __init__(self, exec_time, model_set):
        super().__init__(exec_time, model_set)
        self.description = "Waiting"

    def execute(self, queue):
        from Events.RequestAccess import RequestAccess

        log.info(f"\tTransmitter id = {self.model_set.transmitter.id}: Waiting")
        queue.put(RequestAccess(self.exec_time + random.randint(100, 500), self.model_set))


