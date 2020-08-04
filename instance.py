# coding:utf-8

# making random instances
# making case study instances

import random

from config import RANDOM_SEED, CASE_STUDY_META_DATA

random.seed(RANDOM_SEED)


class RandomDataGenerator(object):

    def __init__(self, meta_data):
        self.meta_data = meta_data

    def make_random_instance(self):
        pass


class Instance(object):

    def __init__(self, instance_name):
        self.instance_name = instance_name
        self.meta_data = CASE_STUDY_META_DATA

    def make_instance(self):
        a = self.meta_data

    def read_instance(self):
        a = self.instance_name


def main():
    I = Instance(None)


if __name__ == '__main__':
    main()
