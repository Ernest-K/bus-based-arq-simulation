import math


class StatsController:
    num_of_retransmission = None
    num_of_collision = None
    time = None
    total_time_wasted_on_retransmission = None
    transmitter_collision_count_arr = []

    def __init__(self, num_of_transmitters, message_size, packet_size, bandwidth):
        self.num_of_transmitters = num_of_transmitters
        self.message_size = message_size
        self.packet_size = packet_size
        self.bandwidth = bandwidth

    def print_stats(self):
        print(f"Number of transmitters: {self.num_of_transmitters}")
        print(f"Message size: {self.message_size} [b]")
        print(f"Packet size: {self.packet_size} [b]")
        print(f"Channel bandwidth: {self.bandwidth} [bps]")
        print(f"Total time: {int((self.time / (1000 * 60)) % 60)} minutes {int((self.time / 1000) % 60)} seconds {int((self.time) % 1000)} milliseconds")
        print(f"Total number of retransmissions: {self.num_of_retransmission}")
        print(f"Total number of collision: {self.num_of_collision}")
        self.total_time_wasted_on_retransmission = self.__get_total_time_wasted_on_retransmission()
        print(f"Total time wasted on retransmission: {int((self.total_time_wasted_on_retransmission / (1000 * 60)) % 60)} minutes {int((self.total_time_wasted_on_retransmission / 1000) % 60)} seconds {int((self.total_time_wasted_on_retransmission) % 1000)} milliseconds")

    def set_num_of_retransmission(self, num_of_retransmission):
        self.num_of_retransmission = num_of_retransmission

    def set_num_of_collision(self, num_of_collision):
        self.num_of_collision = num_of_collision

    def set_total_time(self, total_time):
        self.time = total_time

    def __get_total_time_wasted_on_retransmission(self):
        return self.num_of_retransmission * math.ceil((self.packet_size / self.bandwidth) * 1000)
