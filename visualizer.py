# coding:utf-8
from pprint import pprint

import matplotlib.patches as mpatches
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.collections import PatchCollection
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.patheffects as path_effects

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    # 'axes.labelsize': 7,
    # 'font.size': 7,
    # 'legend.fontsize': 7,
    # 'xtick.labelsize': 7,
    # 'ytick.labelsize': 7,
})

from config import COPY_TO_CLIPBOARD


def copy_to_clipboard(content):
    if COPY_TO_CLIPBOARD:
        import clipboard
        clipboard.copy(content)


def main():
    pass


if __name__ == '__main__':
    main()
