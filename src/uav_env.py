class UavEnvironment:
    current_action = None

    def __init__(self):
        pass

    def decision_cycle(self):
        pass

    def empty_cycle(self):
        pass

    def capture_cycle(self):
        pass

    def transmission_cycle(self):
        pass

    def step(self, action):
        pass

    # check, Is scenario end
    def is_scenario_end(self):
        pass

    # Calculate rewards of this step
    def calculate_rewards(self):
        pass

    # Calculate state of this step
    def calculate_state(self):
        pass