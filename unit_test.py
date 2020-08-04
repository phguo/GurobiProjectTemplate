# coding:utf-8

import pytest

from solution import GurobiSolution


def construct_test_instances():
    instance_name_li = [None, None, None]
    test_instance = [a for a in instance_name_li]

    return test_instance


instances = construct_test_instances()


class Test(object):

    @pytest.mark.parametrize('instance_name', instances)
    def test_solution_feasibility(self, instance_name):
        test_instance = GurobiSolution(instance_name)
        assert test_instance.instance_name == instance_name


def main():
    pytest.main()


if __name__ == '__main__':
    main()
