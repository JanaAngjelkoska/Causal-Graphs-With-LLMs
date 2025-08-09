from enum import Enum


class Stage(str, Enum):
    initialization = "initialization"
    expansion = "expansion"
    insertion = "insertion"
