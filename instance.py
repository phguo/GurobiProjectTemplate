# coding:utf-8

# making random instances
# making case study instances

import random

from dataclasses import dataclass, asdict

from io_operator import write_instance

from config import RANDOM_SEED, CASE_STUDY_META_DATA, RANDOM_META_DATA

random.seed(RANDOM_SEED)


@dataclass
class RandomDataGenerator(object):
    some_meta_data: int

    def __post_init__(self):
        self.some_meta_data = some_meta_data

    def __str__(self):
        return "instance name"

    def make_random_instance(self):
        pass


@dataclass(init=False)
class Instance(object):
    some_data: int

    def __init__(self, instance_name):
        self.instance_name = instance_name
        self.meta_data = CASE_STUDY_META_DATA

    def make_instance(self):
        a = self.meta_data

    def save_instance(self):
        write_instance(instance_file_path, asdict(self))

    def read_instance(self):
        a = self.instance_name


def main():
    R = RandomDataGenerator(**RANDOM_META_DATA)
    I = Instance(**R.data)


if __name__ == '__main__':
    main()
