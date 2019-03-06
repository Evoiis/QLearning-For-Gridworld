# QLearning-For-Gridworld
Two programs to solve Gridworld using Q-learning, a reinforcement learning algorithm.

qlearning_main.py uses one agent to generate a q_table to reach the goal.

async_qlearning_main.py uses multiprocessing to run many agents simultaneously to generate a shared q_table used by each agent to reach the goal.

On completion, graphs are generated to show the rate of learning.

### Installation
* Download the repository.

Install:
* [Python 2.7](https://www.python.org/downloads/)
* Packages: numpy, matplotlib
```
Packages can be installed by using pip:
pip install <package_name>
Example: pip install numpy
```

### Execution
Run programs in the repository folder using:
```
For single agent Q-Learning program:
python qlearning_main.py

For multiple agent Q-Learning program:
python async_qlearning_main.py
```

Unit tests:

Run from the repository folder using:
```
python -m tests.<test_file_name>
Example: python -m tests.test_gridworld
```
