from src.uav_config import UavConfig
from src.uav_env import UavEnvironment
from src.uav_model_manager import UavModelManager


class ProcessOperator:
    # class object
    uav_model_manager = None
    uav_env = None
    uav_config = None

    # initialize
    def __init__(self):
        self.uav_config = UavConfig()
        self.uav_config.load_config()

        self.uav_model_manager = UavModelManager()

        self.uav_env = UavEnvironment()

        print("Operator Initialization Success")

    # scenario logic start
    def run(self):
        # loop
        # initialize episode

        #  # loop : check episode is end
        #  # give state & reward to model
        #  # give action to env

        pass
