# coding:utf-8
import socket


SERVERS = [
    'ali-8c16g',
    'us-compute',
    'VM-12-13-centos',
    'ecs-s2-large-2-linux-20190730174954'
]
SEND_NOTIFICATION = False
SERVER_NAME = socket.gethostname()
if SERVER_NAME in SERVERS:
    SEND_NOTIFICATION = True

COPY_TO_CLIPBOARD = False
if SERVER_NAME in ['guoph-MBP.lan']:
    COPY_TO_CLIPBOARD = True


# saving global variables here

RANDOM_SEED = 1

GUROBI_INFEASIBLE_CODE = (3, 4, 5, 6)

RANDOM_META_DATA = {
    'key': None
}

RANDOM_PARAMETERS = {
    'key': None
}

CASE_STUDY_META_DATA = {
    'key': None
}

CASE_STUDY_PARAMETERS = {
    'key': None
}

GUROBI_PARAMETERS = {
    'Seed': RANDOM_SEED,
    'MIPGap': 0.5 / 100,

    'NodefileStart': 2.5,  # in GB
    # 'Threads': 1,

    # 'TimeLimit': 7200,

    # 'InputFile': './tune/tune0.prm',
    # 'LogToConsole': False,
    # 'LogFile': './gurobi_log/{}.log',

    # 'PreQLinearize': -1,
    # 0 leaves Q matrices unmodified, 1 for a strong LP relaxation, 2 for a compact relaxation.
    # 'MIQCPMethod': -1,
    # 1 uses a linearized, outer-approximation approach, 0 solves continuous QCP relaxations at each node.
}

PARAMETERS = {}

FOLDER = ''
FILE_DIRECTORY = {
    'instances': './instances/',
    'solutions': './solutions/',
}
FILE_DIRECTORY = {key: FOLDER + FILE_DIRECTORY[key] for key in FILE_DIRECTORY}

EXP_PARAMETERS = {}
