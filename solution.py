# coding:utf-8

from instance import Instance


class GurobiSolution(Instance):

    def __init__(self, instance_name):
        Instance.__init__(self, instance_name)
        self.instance_name = instance_name

    def make_solution(self):
        pass

    def read_solution(self):
        pass


def main():
    G = GurobiSolution(None)


if __name__ == "__main__":
    main()
