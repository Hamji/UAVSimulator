from src.replay_memory import ReplayMemory


class UavModelManager:
    epsilon: float
    memory: ReplayMemory


    def __init__(self):
        self.memory = ReplayMemory(capacity=1000)
        pass

    def get_action(self, state):
        pass

    def update(self):
        pass

    def batch_memory(self):
        pass

    def push(self, memory_data: tuple):
        pass

    def get_memory_size(self):
        return len(self.memory)