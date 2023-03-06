# Assignment 02 - Barbershop
## About assignment
The barbershop problem is a classic synchronization problem in parallel programming
that involves managing a set of resources that are shared among multiple threads 
or processes. The problem is based on a hypothetical scenario in which a barber 
operates a barbershop with a limited number of chairs for waiting customers.

## How to run
All you need to successfully run this implementation is to install fei.ppds package for python like so:  
Windows: `py -3 -m pip install --upgrade fei.ppds`  
Linux:`pip3 install --upgrade fei.ppds`.

## Implementation
This implementation of the solution to the sleeping barber problem uses the fei.ppds package.
Defined class `Shared` contains several semaphores and a mutex lock. The semaphores are used 
to signal events between the barber and customers, while the mutex lock is used to protect 
the shared variable called `waiting_room`.  
The main() function creates a shared object and a list of customer threads. 
Each customer thread calls the `customer()` function, which represents the behavior of a customer 
entering the barbershop, waiting for an available seat, getting a haircut, and leaving / growing hair
and balk when waiting room is full.  
The barber thread calls the `barber()` function, which represents the behavior of the barber 
waiting for customers to arrive, cutting their hair, and signaling them.  
The implementation uses a signaling mechanism (rendezvous) where customers signal the barber when 
they are ready to get a haircut, and the barber signals the customer when they are finished with 
their haircut. These signals are implemented using `semaphores`.  
The `mutex lock` is used to ensure that only one customer at a time can modify the waiting_room variable.

