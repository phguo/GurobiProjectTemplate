# Gurobi Project Template
This is a template for implementing project based on Gurobi and Python.

The purpose of files and folders are as follows.

- `config.py` saves global variables.
- `run.py` arranges `.py` files such that the project can be implemented on a remote machine.
- `instance.py` generates experimental instances with `RandomDataGenerator` and saves a instance in class `Instance`. All the instances can be saved in the `instances` folder.
- `solver.py` solves instances with Gurobi solver, and there may be a counterpart `.py` file which including your specialized algorithm.
- `solution.py` saves Gurobi solutions with class `GurobiSolution`. All the solutions can be saved in the `solutions` folder.
- `io_operator.py` processing either file writing or reading works.
- `unit_test.py` test validity of `GurobiSolution` .  Since `GurobiSolution` is  an inheritance from `Instance`, `GurobiSolution` contains all the information for validity checking.
- `visualizer.py` visualizes the solutions.
- `notify.py` provides notification pushing services, e.g., bark and pushover, such that your are notified once all the works in `run.py` are finished.