# coding:utf-8

from notify import bark, pushover
from config import CASE_STUDY_META_DATA, CASE_STUDY_PARAMETERS
from solver import Solver


def shutdown():
    from keys import sudo_password
    cmd = "shutdown -h now"
    os.system("echo {}|sudo -S {}".format(sudo_password, cmd))


def send(make_and_solve):
    def wrapper(instance_name, parameters, instance_type, solution_method, **exp_set):
        try:
            t = time.perf_counter()
            title = "✅ {} | {} | {} Solved in (s) ".format(instance_name, instance_type, exp_set)
            make_and_solve(instance_name, parameters, instance_type, solution_method, **exp_set)
            content = str(time.perf_counter() - t)
            pushover(title, content)
        except Exception as content:
            title = "❌ {} | {} | {} Error".format(instance_name, instance_type, exp_set)
            pushover(title, content)

    return wrapper


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
