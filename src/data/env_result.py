class EnvResult:
    done: list
    state: list
    reward: list

    def __init__(self):
        self.done = []
        self.state = []
        self.reward = []
        pass

    def reset(self):
        self.done = []
        self.state = []
        self.reward = []
