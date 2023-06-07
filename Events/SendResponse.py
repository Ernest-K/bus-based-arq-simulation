import random
import logging as log
from Events.Event import Event
from Events.ReceiveResponse import ReceiveResponse


class SendResponse(Event):
    def __init__(self, exec_time, model_set):
        super().__init__(exec_time, model_set)
        self.description = "Send response"

    def execute(self, queue):
        self.model_set.receiver.send_response()
        self.model_set.channel.is_current_packet_broken = False
        response = "ACK" if self.model_set.channel.ACK else "NACK"
        log.info(f"\tReceiver: Sent {response} response")
        queue.put(ReceiveResponse(self.exec_time + random.randint(50, 150), self.model_set))
