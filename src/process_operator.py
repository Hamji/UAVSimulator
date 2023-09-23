from src.sim_enums import MODE
from src.uav_config import UavConfig
from src.uav_env import UavEnvironment
from src.uav_model_manager import UavModelManager


class ProcessOperator:
    # class object
    uav_model_manager = None
    uav_env = None
    uav_config = None

    # etc
    maximum_step: int
    maximum_scenario: int
    model_type: str
    mode: MODE
    batch_size: int
    num_of_uav: int

    episode_reward: list

    # initialize
    def __init__(self):
        self.uav_config = UavConfig()
        self.uav_config.load_config()

        self.uav_model_manager = UavModelManager()

        self.uav_env = UavEnvironment(self.uav_config)

        self.maximum_step = self.uav_config.maximum_step
        self.maximum_scenario = self.uav_config.maximum_scenario
        self.model_type = self.uav_config.model
        self.mode = self.uav_config.mode
        self.batch_size = self.uav_config.batch_size
        self.num_of_uav = self.uav_config.num_of_uav

        self.episode_reward = []
        print("Operator Initialization Success")

    # scenario logic start
    def run(self):
        if self.mode == MODE.TEST:
            self.test_run()
        elif self.mode == MODE.TRAINING:
            self.training_run()
        else:
            return

    # test logic
    def test_run(self):
        pass

    # training logic
    def training_run(self):
        print("Model Training Start")
        print("Model : {0}".format(self.uav_config.model))
        scenario_idx = 0
        total_reward = 0
        # loop
        while scenario_idx < self.maximum_scenario:
            # initialize episode
            states = self.uav_env.reset_env()
            dones = self.num_of_uav * [False]
            step_idx = 0
            total_reward = 0

            if states is None:
                print("Env Scenario reset Error!")
                break

            while not all(dones) and step_idx < self.maximum_step:
                actions = self.uav_model_manager.get_action(states)
                dones, next_states, rewards = self.uav_env.step(actions)

                # process batch memory if you want #
                memory_data = (states, actions, rewards, next_states, dones)
                self.uav_model_manager.push(memory_data)
                if self.uav_model_manager.get_memory_size() > self.batch_size:
                    # here!!
                    pass
                ####################################

                total_reward += sum(rewards)
                state = next_states

                step_idx += 1

        # model update
        self.uav_model_manager.update()

        # episode rewards statistics appends
        self.episode_reward.append(total_reward)

        print(
            f"Episode {scenario_idx + 1}/{scenario_idx}, Total Reward: {total_reward}, Epsilon: {self.uav_model_manager.epsilon:.2f}")
        scenario_idx += 1

        return
