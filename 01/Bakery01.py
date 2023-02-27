"""This module contains an implementation of Bakery Algorithm.

This implementation is based on pseudocode we had on the ppds seminar.
"""

__author__ = "Matej Bredik, Tomáš Vavro"
__email__ = "xbredik@stuba.sk"
__license__ = "MIT"

from fei.ppds import Thread
from time import sleep

num = [0, 0, 0, 0, 0]
intr = [0, 0, 0, 0, 0]


def bakery_process(i: int):
    """Simulates a process.

    Arguments:
        i -- identification number of thread
    """
    intr[i] = 1
    num[i] = max(num) + 1
    intr[i] = 0
    for j in range(i):
        # process wants to enter critical section
        while intr[j] == 1:
            continue
        # process has to wait for its turn
        while (num[j] != 0) and (num[j] < num[i] or (num[j] == num[i] and j < i)):
            continue

    # execute critical section
    print(f"Process {i} runs a computation!")
    sleep(1)

    # exit critical section
    num[i] = 0


if __name__ == '__main__':
    threads = [Thread(bakery_process, i) for i in range(5)]
    [t.join() for t in threads]
