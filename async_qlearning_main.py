#!/usr/bin/env python
import scripts

from scripts import plot
from scripts import constants

if __name__ == "__main__":

    print "Running Asynchronous Q-Learning"
    first = scripts.run_async_qlearning(constants.FIRST_ASYNC_NUM_PROCESSES)
    second = scripts.run_async_qlearning(constants.SECOND_ASYNC_NUM_PROCESSES)
    third = scripts.run_async_qlearning(constants.THIRD_ASYNC_NUM_PROCESSES)
    print "Asynchronous Q-Learning Finished"

    print "Generating Plot:"
    plot.async_plot(first, second, third)
    print "End of program"

