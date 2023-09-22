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

    def __init__(self):
        self.__path     = './cfg/uav_config.cfg'
        self.__config   = configparser.ConfigParser()

    def load_config(self):
        self.__config.read(self.__path)

        self.__mode             = int(self.__config.get('COMMON', 'MODE'))
        self.__num_of_uav       = int(self.__config.get('COMMON', 'NUM_OF_UAV'))
        self.__grid_size        = int(self.__config.get('COMMON', 'GRID_SIZE'))
        self.__maximum_step     = int(self.__config.get('COMMON', 'MAXIMUM_STEP'))
        self.__maximum_scenario = int(self.__config.get('COMMON', 'MAXIMUM_SCENARIO'))
        self.__model            =     self.__config.get('COMMON', 'MODEL')

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
