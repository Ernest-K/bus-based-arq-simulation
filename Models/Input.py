from Models.Message import Message
import random


class Input:
    def generate_message(self, message_length):
        return Message([random.randint(0, 1) for i in range(message_length)], message_length)
