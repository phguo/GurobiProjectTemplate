# coding:utf-8

from bark import bark
from config import CASE_STUDY_META_DATA, CASE_STUDY_PARAMETERS
from solver import Solver


def main():
    meta_data = CASE_STUDY_META_DATA
    parameters = CASE_STUDY_PARAMETERS

    optimal_objective_value = None
    try:
        S = Solver(meta_data)
        model = S.make_model(parameters)
        optimal_objective_value = S.solve(model).getObjective().getValue()
    except:
        pass

    bark(optimal_objective_value, optimal_objective_value)


if __name__ == '__main__':
    main()
