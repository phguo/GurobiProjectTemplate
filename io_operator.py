# coding:utf-8

import json
from os import listdir

from gurobipy import tupledict, read

from config import FILE_DIRECTORY, GUROBI_INFEASIBLE_CODE

# from os.path import getsize
# from shutil import copyfile

instances_dir = FILE_DIRECTORY["instances"]
solutions_dir = FILE_DIRECTORY["solutions"]

'''
# # # # # # # # # # # # # # # # # #
#        Instance (.json)         #
# # # # # # # # # # # # # # # # # #
'''


def write_instance(data, instance_name):
    file = instances_dir + instance_name + ".json"
    json_str = json.dumps(data, sort_keys=True, indent=4)
    with open(file, 'w') as f:
        f.write(json_str)


def read_instance(instance_name):
    file = instances_dir + instance_name + ".json"
    with open(file, 'r') as f:
        lines = f.read()
    dict_obj = json.loads(
        lines,
        object_hook=lambda d: {int(k) if k.lstrip('-').isdigit() else k: v for k, v in d.items()}
    )
    return dict_obj


'''
# # # # # # # # # # # # # # # # # #
#          Model (.mps)           #
# # # # # # # # # # # # # # # # # #
'''


def write_model(model, instance_name):
    file = instances_dir + instance_name + ".mps"
    model.write(file)


def read_model(model, instance_name):
    file = instances_dir + instance_name + ".mps"
    model = read(file)
    return model


'''
# # # # # # # # # # # # # # # # # #
#   Solution (.sol .nonzero)      #
# # # # # # # # # # # # # # # # # #
'''


def solution_file_name_process(instance_name, solution_type, **exp_set):
    if solution_type == 'DE':
        solutions_dir = FILE_DIR['de_solutions']
        file_name = '{}'.format(instance_name)


def write_gurobi_sol(model, instance_name):
    if int(model.getAttr("Status")) not in GUROBI_INFEASIBLE_CODE:
        file = solutions_dir + instance_name + ".sol"
        model.write(file, 'w')


def write_nonzero_gurobi_sol(instance_name):
    # call after "write_gurobi_sol"
    file_name = solutions_dir + instance_name
    with open(file_name + ".sol", 'r') as f:
        f_content = [a for a in f if a.split(' ')[-1] != '0\n']
    with open(file_name + ".nonzero", 'w') as f:
        f.writelines(f_content)


def format_sol_lines(lines):
    lines = [(a.split(' ')[0], round(float(a.split(' ')[1]))) for a in lines]
    # Rounding "vars_value" to avoid numerical issues
    lines = [(a[0].strip(']').split('[')[0], a[0].strip(']').split('[')[1], a[1]) for a in lines]
    lines = [(a[0], tuple(int(b) for b in a[1].split(',')), a[2]) for a in lines]
    return lines


def read_gurobi_sol(instance_name):
    file = solutions_dir + instance_name + ".sol"
    with open(file, 'r') as f:
        f_content = [a.strip('\n') for a in f]
        lines = f_content[1:]
        lines = format_sol_lines(lines)

    solution = dict()
    non_zero_solution = dict()
    for var, vars_key, vars_value in lines:
        if var not in solution:
            solution[var] = tupledict()
        if var not in non_zero_solution:
            non_zero_solution[var] = tupledict()
        solution[var][vars_key] = vars_value
        if vars_value != 0:
            non_zero_solution[var][vars_key] = vars_value

    return solution, non_zero_solution


def read_nonzero_gurobi_sol(instance_name):
    if instance_name + ".nonzero" in listdir(solutions_dir):

        file = solutions_dir + instance_name + ".nonzero"
        with open(file, 'r') as f:
            f_content = [a.strip('\n') for a in f]
            lines = f_content[1:]
            lines = format_sol_lines(lines)

        non_zero_solution = dict()
        for var, vars_key, vars_value in lines:
            if var not in non_zero_solution:
                non_zero_solution[var] = tupledict()
            non_zero_solution[var][vars_key] = vars_value

    else:
        non_zero_solution = read_gurobi_sol(instance_name)[1]

    return non_zero_solution


'''
# # # # # # # # # # # # # # # # # #
#         Stats (.json)           #
# # # # # # # # # # # # # # # # # #
'''


def write_gurobi_stats(model, instance_name):
    file = solutions_dir + instance_name + ".json"
    model.write(file)

    # <<< For fixing "0 Runtime Output Issue" in Gurobi 9.0 <<<
    runtime = model.getAttr("Runtime")
    with open(file, 'r') as f:
        json_content = json.load(f)
        json_content["SolutionInfo"]["Runtime"] = str(runtime)
    # >>> For fixing "0 Runtime Output Issue" in Gurobi 9.0 >>>

    with open(file, 'w') as f:
        f.write(json.dumps(json_content, indent=4))


def read_solution_stats(instance_name):
    file = solutions_dir + instance_name + ".json"
    with open(file, 'r') as f:
        solution_stats = json.load(f)
    return solution_stats


def get_objective_value(instance_name):
    return float(read_solution_stats(instance_name)["SolutionInfo"]["ObjVal"])


def get_gap(instance_name):
    return float(read_solution_stats(instance_name)["SolutionInfo"]["MIPGap"])


def get_runtime(instance_name):
    return float(read_solution_stats(instance_name)["SolutionInfo"]["Runtime"])


def main():
    read_nonzero_gurobi_sol('')


if __name__ == "__main__":
    main()
