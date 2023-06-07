class Event:
    description = None

    def __init__(self, exec_time, model_set):
        self.exec_time = exec_time
        self.model_set = model_set

    def execute(self, queue):
        pass

    def __lt__(self, other):
        return self.exec_time < other.exec_time