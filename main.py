import sys, os
sys.path.insert(0, 'evoman_framework/evoman')
from environment import Environment


def init():
    """
    Initialise game environment
    """
    # create map for outputs
    experiment_name = 'testrun'
    if not os.path.exists(experiment_name):
        os.makedirs(experiment_name)

    # init environment class
    env = Environment(experiment_name=experiment_name)

    return env


if __name__ == '__main__':

    env = init()

    # use first EA
    # TODO:

    # use second EA
    # TODO:

    env.play()
