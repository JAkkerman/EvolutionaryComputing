import sys, os
sys.path.insert(0, 'evoman')
from environment import Environment
# from demo_controller import player_controller
# from controller import Controller
from test_controller import test_controller

import numpy as np


def init():
    """
    Initialise game environment
    """
    # create map for outputs
    experiment_name = 'testrun'
    if not os.path.exists(experiment_name):
        os.makedirs(experiment_name)

    n_hidden_neurons = 0

    # init environment class
    # cont = Controller()

    env = Environment(experiment_name=experiment_name,
                        speed='normal')

    env.player_controller = test_controller

    return env


if __name__ == '__main__':

    env = init()

    # use first EA
    # TODO:

    # use second EA
    # TODO:

    env.play()
    yeet = env.player.sensors.get(env)
    print(yeet)
    print(env.logs)
