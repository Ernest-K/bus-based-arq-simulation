import queue
import logging as log

from Models.ModelSet import ModelSet
from Models.Transmitter import Transmitter
from Models.Channel import Channel
from Models.Receiver import Receiver
from Events.RequestAccess import RequestAccess
from StatsController import StatsController


class Simulator:
    queue = queue.PriorityQueue()
    time = 0 # Milliseconds
    log_level = log.WARNING

    def __init__(self, num_of_transmitters, message_size, packet_size, bandwidth):
        self.num_of_retransmissions = None
        self.__create_models(num_of_transmitters, message_size, packet_size, bandwidth)
        self.stats_controller = StatsController(num_of_transmitters, message_size, packet_size, bandwidth)

        for transmitter in self.transmitters:
            self.queue.put(RequestAccess(1, ModelSet(transmitter, self.channel, self.receiver)))

    def start(self):
        log.basicConfig(level=self.log_level, format='%(message)s')

        while not self.queue.empty():
            current_event = self.queue.get()
            log.info(f"Current time = {current_event.exec_time}, Event description = '{current_event.description}'")
            current_event.execute(self.queue)
            self.time = current_event.exec_time

        for transmitter in self.transmitters:
            self.stats_controller.transmitter_collision_count_arr.append(transmitter.collision_counter)

        self.stats_controller.set_num_of_retransmission(sum([transmitter.retransmission_counter for transmitter in self.transmitters]))
        self.stats_controller.set_num_of_collision(sum([transmitter.collision_counter for transmitter in self.transmitters]))
        self.stats_controller.set_total_time(self.time)
        self.stats_controller.print_stats()

    def __create_models(self, num_of_transmitters, message_size, packet_size, bandwidth):
        self.channel = Channel(bandwidth)
        self.receiver = Receiver(self.channel)

        self.transmitters = []
        for i in range(num_of_transmitters):
            self.transmitters.append(Transmitter(i, self.channel, message_size, packet_size))

    def enable_logger(self):
        self.log_level = log.INFO