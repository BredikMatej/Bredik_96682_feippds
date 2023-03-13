"""This module implements dinning philosophers problem.

This implementation uses solution to the dining philosophers problem where one of
the philosophers takes the left fork first and the rest takes right one first.
"""

__author__ = "Matej Bredik, Tomáš Vavro"
__email__ = "xbredik@stuba.sk, xvavro@stuba.sk"
__license__ = "MIT"

from fei.ppds import Thread, Mutex, print
from time import sleep

NUM_PHILOSOPHERS: int = 5
NUM_RUNS: int = 10  # number of repetitions of think-eat cycle of philosophers


class Shared:
    """Represent shared data for all threads."""
    def __init__(self):
        """Initialize an instance of Shared."""
        self.forks = [Mutex() for _ in range(NUM_PHILOSOPHERS)]


def think(i: int):
    """Simulate thinking.

    Args:
        i -- philosopher's id
    """
    print(f"Philosopher {i} is thinking!")
    sleep(0.1)


def eat(i: int):
    """Simulate eating.

    Args:
        i -- philosopher's id
    """
    print(f"Philosopher {i} is eating!")
    sleep(0.1)


def philosopher(i: int, shared: Shared):
    """Run philosopher's code.

    Args:
        i -- philosopher's id
        shared -- shared data
    """
    for _ in range(NUM_RUNS):
        think(i)
        if i == 0:
            # philosopher 0 takes the left fork first
            shared.forks[i].lock()
            sleep(0.5)
            shared.forks[(i+1) % NUM_PHILOSOPHERS].lock()
        else:
            # other philosophers take the right fork first
            shared.forks[(i+1) % NUM_PHILOSOPHERS].lock()
            sleep(0.5)
            shared.forks[i].lock()

        eat(i)
        # philosophers put down both forks after eating
        shared.forks[i].unlock()
        shared.forks[(i + 1) % NUM_PHILOSOPHERS].unlock()


def main():
    """Run main."""
    shared: Shared = Shared()
    philosophers: list[Thread] = [
        Thread(philosopher, i, shared) for i in range(NUM_PHILOSOPHERS)
    ]
    for p in philosophers:
        p.join()


if __name__ == "__main__":
    main()

