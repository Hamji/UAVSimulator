import configparser
class UavConfig:
    __path = None
    __config = None

    # contents of config
    # COMMON
    __mode: int
    __num_of_uav: int
    __grid_size: int
    __maximum_step: int
    __maximum_scenario: int
    __model: str
    __batch_size: int
    __epsilon_start: float
    __epsilon_end: float
    __epsilon_decay: float
    __num_of_actions: int
    __learning_rate: float
    __gamma: float

    def __init__(self):

        self.__path     = './cfg/uav_config.cfg'
        self.__config   = configparser.ConfigParser()

    def load_config(self):
        self.__config.read(self.__path)

        # COMMON
        self.__mode             = int(self.__config.get('COMMON', 'MODE'))
        self.__num_of_uav       = int(self.__config.get('COMMON', 'NUM_OF_UAV'))
        self.__grid_size        = int(self.__config.get('COMMON', 'GRID_SIZE'))
        self.__maximum_step     = int(self.__config.get('COMMON', 'MAXIMUM_STEP'))
        self.__maximum_scenario = int(self.__config.get('COMMON', 'MAXIMUM_SCENARIO'))
        self.__model            =     self.__config.get('COMMON', 'MODEL')
        self.__batch_size       = int(self.__config.get('COMMON', 'BATCH_SIZE'))

        # MODEL
        self.__epsilon_start    = float(self.__config.get('MODEL', 'EPSILON_START'))
        self.__epsilon_end      = float(self.__config.get('MODEL', 'EPSILON_END'))
        self.__epsilon_decay    = float(self.__config.get('MODEL', 'EPSILON_DECAY'))
        self.__num_of_actions   = int(self.__config.get('MODEL', 'NUM_OF_ACTIONS'))
        self.__learning_rate    = float(self.__config.get('MODEL', 'LEARNING_RATE'))
        self.__gamma            = float(self.__config.get('MODEL', 'GAMMA'))

    @property
    def mode(self):
        return self.__mode

    @property
    def num_of_uav(self):
        return self.__num_of_uav

    @property
    def grid_size(self):
        return self.__grid_size

    @property
    def maximum_step(self):
        return self.__maximum_step

    @property
    def maximum_scenario(self):
        return self.__maximum_scenario

    @property
    def model(self):
        return self.__model

    @property
    def batch_size(self):
        return self.__batch_size

    @property
    def epsilon_start(self):
        return self.__epsilon_start

    @property
    def epsilon_end(self):
        return self.__epsilon_end

    @property
    def epsilon_decay(self):
        return self.__epsilon_decay

    @property
    def num_of_actions(self):
        return self.__num_of_actions

    @property
    def learning_rate(self):
        return self.__learning_rate

    @property
    def gamma(self):
        return self.__gamma
