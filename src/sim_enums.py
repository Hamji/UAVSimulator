from enum import Enum

class MODE(Enum):
    TRAINING = 0
    TEST = 1

class SCENARIO(Enum):
    OUT_OF_RANGE = 0
    DONE = 1
    NOT_YET = 2
