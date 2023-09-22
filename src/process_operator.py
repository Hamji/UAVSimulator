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

        print("Operator Initialization Success")

    # scenario logic start
    def run(self):
        if self.mode == MODE.TEST:
            self.test_run()
            return
        elif self.mode == MODE.TRAINING:
            print("Model Training Start")
            print("Model : {0}".format(self.uav_config.model))
        else:
            return

        # loop
        # initialize episode

        #  # loop : check episode is end
        #  # give state & reward to model
        #  # give action to env

        return

    def test_run(self):
        pass
