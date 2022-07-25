# coding:utf-8

from instance import Instance
from dataclasses import dataclass, field


class GurobiSolution(Instance):

    def __init__(self, instance_name):
        Instance.__init__(self, instance_name)
        self.instance_name = instance_name

    def make_solution(self):
        pass

    def read_solution(self):
        pass


@dataclass
class SolutionStat(object):
    instance_name: str = ""

    upper_bound_dic: dict = field(default_factory=lambda: dict())
    best_upper_bound_dic: dict = field(default_factory=lambda: dict())
    # NOTICE: the LB for calculating LBBD gap and Gurobi gap are different
    gap_dic: dict = field(default_factory=lambda: dict())
    runtime_dic: dict = field(default_factory=lambda: dict())

    optimized: bool = None
    total_iteration_time: int = -1
    total_runtime: float = -1
    opt_sol_time: float = -1

    SolutionInfo: dict = field(
        default_factory=lambda: {
            "Status": None,
            "Runtime": None,
            "ObjVal": None,
            "ObjBound": None,
            "MIPGap": None,
            "SolCount": None,
        })

    # LBBD specific
    warm_start_runtime: float = -1
    lbbd_lower_bound_dict: dict = field(default_factory=lambda: dict())
    cut_count: dict = field(default_factory=lambda: dict())
    master_recourse_cost: dict = field(default_factory=lambda: dict())
    sub_recourse_cost: dict = field(default_factory=lambda: dict())

    # Gurobi specific
    lp_lower_bound_dict: dict = field(default_factory=lambda: dict())

    def __post_init__(self):
        pass


def main():
    G = GurobiSolution(None)


if __name__ == "__main__":
    main()
