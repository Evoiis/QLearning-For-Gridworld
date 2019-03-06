import matplotlib.pyplot as plt
import matplotlib.patches as patches
import constants


class Plot:

    def __init__(self):
        self.data = []

    def insert_data(self, number):
        self.data.append(number)
        return

    def generate_plot(self):
        # Plot total reward at each step
        plt.plot(range(1001), self.data[:1001], color='black', linewidth=2)
        plt.plot(range(1001, len(self.data)), self.data[1001:], color='blue', linewidth=2)

        # Plot vertical line at 1000
        plt.axvline(x=1000, color='red', linewidth=1)

        # Set view limits
        plt.ylim(0, max(self.data) + 1)
        plt.xlim(0, len(self.data) + 1)

        # Axis labels:
        plt.ylabel("Total Reward")
        plt.xlabel("Step Number")
        plt.title("Total Reward at Each Step")

        # Plot Legend
        black_patch = patches.Patch(color='black', label='Q_Learning before obstacle shift')
        red_patch = patches.Patch(color='red', label='Obstacle Shift')
        blue_patch = patches.Patch(color='blue', label='Q_Learning after obstacle shift')

        plt.legend(handles=[red_patch, black_patch, blue_patch])

        # Show plot
        plt.show()


def async_plot(first, second, third):
    len_first = len(first)
    len_second = len(second)
    len_third = len(third)
    plt.plot(range(len_first), first, color='black', linewidth=2)
    plt.plot(range(len_second), second, color='blue', linewidth=2)
    plt.plot(range(len_third), third, color='green', linewidth=2)

    # Plot vertical line at 1000
    plt.axvline(x=1000, color='red', linewidth=1)

    # Set view limits
    plt.ylim(0, max(max(first), max(second), max(third)) + 1)
    plt.xlim(0, max(len_first, len_second, len_third) + 1)

    # Axis labels
    plt.ylabel("Average Total Episodic Reward")
    plt.xlabel("Episode Number, Episode = " + str(constants.EPISODE_LENGTH) + " steps.")
    plt.title("Average Total Episodic Reward at Each Step")

    # Plot Legend
    black_patch = patches.Patch(color='black', label=str(constants.FIRST_ASYNC_NUM_PROCESSES) + ' Processes')
    blue_patch = patches.Patch(color='blue', label=str(constants.SECOND_ASYNC_NUM_PROCESSES) + ' Processes')
    green_patch = patches.Patch(color='green', label=str(constants.THIRD_ASYNC_NUM_PROCESSES) + ' Processes')
    red_patch = patches.Patch(color='red', label='Obstacle Shift')

    plt.legend(handles=[red_patch, black_patch, blue_patch, green_patch])

    plt.show()

