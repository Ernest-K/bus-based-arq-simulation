import random


class Channel:
    def __init__(self, bandwidth):
        self.bandwidth = bandwidth # bps (bit per second)
        self.busy = False
        self.current_transmitter_id = None
        self.current_packet = None
        self.packets_left = None
        self.ACK = True
        self.is_current_packet_broken = False # prevent breaking the same packet multiple times, reset this flag in send response event

    def damage_current_packet(self):
        packet_data_len = len(self.current_packet.data)

        if not self.is_current_packet_broken:
            random_index = random.randint(0, packet_data_len - 1)
            if self.current_packet.data[random_index] == 1:
                self.current_packet.data[random_index] = 0
            else:
                self.current_packet.data[random_index] = 1

            self.is_current_packet_broken = True

