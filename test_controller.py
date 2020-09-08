import numpy
from controller import Controller

class test_controller(Controller):


    def control(self, params, cont=None):

        print(params)

        # action1 = numpy.random.choice([1,0])
        # action2 = numpy.random.choice([1,0])
        # action3 = numpy.random.choice([1,0])
        # action4 = numpy.random.choice([1,0])
        # action5 = numpy.random.choice([1,0])
        # action6 = numpy.random.choice([1,0])

        # return [action1, action2, action3, action4, action5, action6]
        return [0,1,1,0,0]
