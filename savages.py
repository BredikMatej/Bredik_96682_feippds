"""
This is implementation of solution to dinning savages problem using fei.ppds package

University: STU Slovak Technical University in Bratislava
Faculty: FEI Faculty of Electrical Engineering and Information Technology
Year: 2023
"""

__authors__ = "Matej Bredik, Matúš Jokay"
__email__ = "xbredik@stuba.sk"
__license__ = "MIT"


from time import sleep
from random import randint
from fei.ppds import Thread, Mutex, Semaphore, print


class SimpleBarrier(object):
    """Barrier class."""

    def __init__(self, n):
        """Represents SimpleBarrier.

        Attributes:
        n -- number of threads the barrier blocks
        """
        self.n = n
        self.counter = 0
        self.mutex = Mutex()
        self.barrier = Semaphore(0)

    def wait(self, each=None, last=None):
        """Lock's program until each thread completes turnstile."""
        self.mutex.lock()
        self.counter += 1
        # print message for each savage thread that is waiting
        if each:
            print(each)
        if self.counter == self.n:
            # print message for the last savage thread that comes to barrier
            if last:
                print(last)
            # Reset the counter and signal all threads to proceed
            self.counter = 0
            self.barrier.signal(self.n)
        self.mutex.unlock()
        self.barrier.wait()


class Shared(object):
    """Class representing shared data between threads."""
    def __init__(self):
        self.servings = 0
        self.mutex = Mutex()
        self.emptyPot = Semaphore(0)
        self.fullPot = Semaphore(0)
        self.sb1 = SimpleBarrier(D)
        self.sb2 = SimpleBarrier(D)


def eat(i):
    """Simulates savages eating time"""
    print(f'savage {i}: Eating.')
    sleep(randint(50, 200) / 100)


def savage(i, shared):
    """Function representing the savage thread.

    Arguments:
        i -- thread id
        shared -- shared data between threads
    """
    sleep(randint(1, 100) / 100)
    while True:
        # wait for all savages to be ready to eat
        shared.sb1.wait()
        shared.sb2.wait(each=f'savage {i}: Ready to eat.',
                        last=f'savage {i}: We\'re all here, let\'s eat!')
        shared.mutex.lock()
        # if the pot is empty, signal the cook to prepare a new pot
        if shared.servings == 0:
            print(f'savage {i}: The pot is empty!')
            shared.emptyPot.signal()
            # wait for the cook to fill the pot with food
            shared.fullPot.wait()
        print(f'savage {i}: Taking from the pot. {shared.servings-1}/5 left.')
        shared.servings -= 1
        shared.mutex.unlock()
        eat(i)


def cook(shared):
    """Function representing the cook thread.

    Arguments:
        shared -- shared data between threads
    """
    while True:
        # wait for the signal that the pot is empty
        shared.emptyPot.wait()
        print('cook: Cooking!')
        # simulates cooking time
        sleep(randint(50, 200) / 100)
        print(f'cook: Adding {H} servings to pot')
        shared.servings += H
        # signal the savages that the pot is full
        shared.fullPot.signal()


def main():
    shared = Shared()
    savages = []

    for i in range(D):
        savages.append(Thread(savage, i, shared))
    savages.append(Thread(cook, shared))

    for t in savages:
        t.join()


D = 12
H = 5

if __name__ == "__main__":
    main()
