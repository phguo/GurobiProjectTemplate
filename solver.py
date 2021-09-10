# coding:utf-8

import random
import time
from itertools import product

from gurobipy import *

from config import RANDOM_SEED, GUROBI_PARAMETERS, CASE_STUDY_META_DATA, CASE_STUDY_PARAMETERS
from instance import Instance

random.seed(RANDOM_SEED)


class Solver(Instance):

    def __init__(self, meta_data):

        Instance.__init__(self, meta_data)
        self.instance_name = meta_data

    def set_GUROBI_PARAMETERS(self, model, instance_name):
        for key in GUROBI_PARAMETERS:
            value = GUROBI_PARAMETERS[key]
            if key == "LogFile":
                file_name = "{}".format(instance_name)
                file_name = "{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + file_name
                value = value.format(file_name)
            model.setParam(key, value)
        return model

    def make_model(self, parameters):

        model = Model("MIP-Model")

        '''
        # # # # # # # # # # # # # # # # # #
        #     define variable tuples      #
        # # # # # # # # # # # # # # # # # #
        '''
        vars_tup = tupledict([(i, j), -1] for (i, j) in product(range(10), range(10)))

        '''
        # # # # # # # # # # # # # # # # # #
        #     add decision variables      #
        # # # # # # # # # # # # # # # # # #
        '''
        model.addVars(vars_tup, vtype=GRB.BINARY, name='vars')

        '''
        # # # # # # # # # # # # # # # # # #
        #         add constraints         #
        # # # # # # # # # # # # # # # # # #
        '''
        model.addConstrs(vars_tup.sum('*', '*') == 1)

        '''
        # # # # # # # # # # # # # # # # # #
        #      add objective function     #
        # # # # # # # # # # # # # # # # # #
        '''
        model.setObjective('1')

        return model

    def modify_model(self, model):
        # make some modification on mathematical model

        model = model

        return model

    def solve(self, model):
        # optimize mathematical model

        model.optimize()

        return model


def main():
    meta_data = CASE_STUDY_META_DATA
    parameters = CASE_STUDY_PARAMETERS

    S = Solver(meta_data)
    model = S.make_model(parameters)
    optimal_objective_value = S.solve(model).getObjective().getValue()

    print(optimal_objective_value)


if __name__ == '__main__':
    main()
