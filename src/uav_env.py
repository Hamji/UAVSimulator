from src.uav import Uav
from src.uav_config import UavConfig


class UavEnvironment:
    current_action = None
    __grid_size: int
    __num_of_uav: int
    __uav_arr: list
    __maximum_step: int

    def __init__(self, config: UavConfig):
        self.__grid_size = config.grid_size
        self.__num_of_uav = config.num_of_uav
        self.__uav_arr = config.maximum_step
        self.__uav_arr = [Uav(i) for i in range(0, self.__num_of_uav)]


    def reset_env(self):
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
        self.decision_cycle()
        self.empty_cycle()
        self.capture_cycle()
        self.transmission_cycle()

        result = [
            self.is_scenario_end(),
            self.calculate_rewards(),
            self.calculate_state()
        ]

        return result

    # check, Is scenario end
    def is_scenario_end(self):
        pass

    # Calculate rewards of this step
    def calculate_rewards(self):
        pass

    # Calculate state of this step
    def calculate_state(self):
        pass
