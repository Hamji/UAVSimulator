from src.data.env_result import EnvResult
from src.sim_enums import SCENARIO
from src.uav import Uav
from src.uav_config import UavConfig


class UavEnvironment:
    current_action = None
    __grid_size: int
    __num_of_uav: int
    __uav_arr: list
    __maximum_step: int
    __positions: list
    __goal: list
    __actions: list

    def __init__(self, config: UavConfig):
        self.__grid_size = config.grid_size
        self.__num_of_uav = config.num_of_uav
        self.__maximum_step = config.maximum_step
        self.__uav_arr = [Uav(i) for i in range(0, self.__num_of_uav)]
        self.__goal = [self.__grid_size - 1, self.__grid_size - 1]
        # Hover, North, East, South, West
        self.actions = [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]

    def reset_env(self):
        self.__positions = [[0, 0] for _ in range(self.__num_of_uav)]
        states = []
        for position in self.__positions:
            states.extend(self._get_state_from_position(position))
        return states

    def _get_state_from_position(self, position):
        dx = self.__goal[0] - position[0]
        dy = self.__goal[1] - position[1]
        return [position[0], position[1], dx, dy]

    def decision_cycle(self, actions):
        next_states = []
        rewards = []
        dones = []

        for idx, action in enumerate(actions):
            new_position = [self.__positions[idx][0] + self.__actions[action][0],
                            self.__positions[idx][1] + self.__actions[action][1]
                            ]
            # OUT OF RANGE
            if self.is_out_of_range(new_position):
                next_states.extend(self._get_state_from_position(self.__positions[idx]))
                rewards.append(self.calculate_rewards(SCENARIO.OUT_OF_RANGE))
                dones.append(False)
            else:
                self.__positions[idx] = new_position
                if self.__positions[idx] == self.__goal:
                    next_states.extend(self._get_state_from_position(self.__positions[idx]))
                    rewards.append(self.calculate_rewards(SCENARIO.DONE))
                    dones.append(True)
                else:
                    next_states.extend(self._get_state_from_position(self.__positions[idx]))
                    rewards.append(self.calculate_rewards(SCENARIO.NOT_YET))
                    dones.append(False)

        return next_states, rewards, dones


    def empty_cycle(self):
        pass

    def capture_cycle(self):
        pass

    def transmission_cycle(self):
        pass

    def step(self, actions):
        result = self.decision_cycle(actions)
        # self.empty_cycle()
        # self.capture_cycle()
        # self.transmission_cycle()

        return result

    # check, Is scenario end
    def is_scenario_end(self, scenario: SCENARIO):
        if scenario == SCENARIO.DONE:
            return True
        else:
            return False

    def is_out_of_range(self, pos):
        return pos[0] < 0 or pos[0] >= self.__grid_size or pos[1] < 0 or pos[1] >= self.__grid_size


    # Calculate rewards of this step
    def calculate_rewards(self, scenario: SCENARIO):
        if scenario == SCENARIO.OUT_OF_RANGE:
            return -5
        elif scenario == SCENARIO.DONE:
            return 10
        elif scenario == SCENARIO.NOT_YET:
            return -0.1
        else:
            return 0
