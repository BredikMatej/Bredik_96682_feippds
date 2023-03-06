"""
This is implementation of solution to barbershop (sleeping barber) problem using fei.ppds package


University: STU Slovak Technical University in Bratislava
Faculty: FEI Faculty of Electrical Engineering and Information Technology
Year: 2023
"""

__authors__ = "Matej Bredik, Marián Šebeňa"
__email__ = "xbredik@stuba.sk, mariansebena@stuba.sk, xvavro@stuba.sk"
__license__ = "MIT"

from fei.ppds import Mutex, Thread, Semaphore, print
from time import sleep
from random import randint


class Shared(object):

    def __init__(self):
        self.mutex = Mutex()
        self.waiting_room = 0
        self.customer = Semaphore(0)
        self.barber = Semaphore(0)
        self.customer_done = Semaphore(0)
        self.barber_done = Semaphore(0)


def get_haircut(i):
    """Simulates customer getting their hair cut by barber"""
    print(f'CUSTOMER {i}: gets haircut')
    sleep(1/10)


def cut_hair():
    """Simulates time when barber cuts customer's hair"""
    print('BARBER: cuts hair')
    sleep(1/20)


def balk(i):
    """Simulates situation when waiting room is full."""
    print(f'CUSTOMER {i}: Waits for an empty seat')
    sleep(1 / 5)


def growing_hair(i):
    """Represents situation when customer wait after getting haircut."""
    print(f'CUSTOMER {i}: Leaves and waits for hair to grow')
    sleep(1 / 5)


def customer(i, shared):
    while True:
        if shared.waiting_room < N:
            shared.mutex.lock()
            shared.waiting_room += 1
            print(f'CUSTOMER {i}: Sitting in waiting room')
            shared.mutex.unlock()

            # Customer signals barber that he is ready for haircut and waits
            shared.customer.signal()
            shared.barber.wait()

            # Customer gets his hair cut by barber
            get_haircut(i)

            # Customer is done, signals barber and waits
            shared.customer_done.signal()
            shared.barber_done.wait()

            # Customer is leaving the waiting room
            shared.mutex.lock()
            shared.waiting_room -= 1
            shared.mutex.unlock()

            # Customer waits for his hair to grow
            growing_hair(i)
        else:
            # Waiting room is full customer leaves
            balk(i)
            continue


def barber(shared):

    while True:
        # Barber waits for customer to arrive
        shared.customer.wait()

        # Barber waits for customer to come in
        shared.barber.signal()

        # Barber cuts customers hair
        cut_hair()

        # Barber is done signals customer and waits for customer to leave
        shared.barber_done.signal()
        shared.customer_done.wait()


def main():
    shared = Shared()
    customers = []

    for i in range(C):
        customers.append(Thread(customer, i, shared))
    hair_stylist = Thread(barber, shared)

    for t in customers + [hair_stylist]:
        t.join()


C = 5
N = 3

if __name__ == "__main__":
    main()
