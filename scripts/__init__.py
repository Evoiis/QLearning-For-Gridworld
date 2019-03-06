import gridworld
import plot

from qlearning import qlearn
from async_qlearning import async_qlearn


def run_qlearning():
    gw = gridworld.GridWorld()
    plt = plot.Plot()

    qlearn.q_learning(gw, plt)


def run_async_qlearning(num_processes):
    return async_qlearn.init_async_q_learning(num_processes)
