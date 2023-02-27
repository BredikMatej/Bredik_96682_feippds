# Assignment 01 - Bakery Algorithm
## About assignment
The goal of this assignment is to implement Bakery Algorithm using fei.ppds package for python. 
The Bakery Algorithm is a computer science technique that was created by Leslie Lamport. 
It aims to enhance the safety of shared resources across multiple threads by utilizing mutual exclusion.
If multiple threads try to write to the same memory region simultaneously or if one thread accesses 
a memory location before another thread has finished writing to it, data corruption may occur. Bakery Algorithm 
takes care of this problem.

## How to run
All you need to successfully run this implementation is to install fei.ppds package for python like so: \
Windows:
    `py -3 -m pip install --upgrade fei.ppds` \
Linux:
    `pip3 install --upgrade fei.ppds`

## Conclusion
1. No more than one process may be performed in a critical area at any time:\
Every process has to wait for its number to be "called" and each process has been assigned different number.
2. A process that is carried out outside the critical area must not obstruct others to enter:\
Processes with lower ticket numbers have higher priority and will enter the critical section first, therefore 
there is no possibility for process with higher number to obstruct process with lower number.
3. The decision to enter must come at a finite time:\
Once a process has been assigned a ticket number, it will repeatedly check whether it is its turn to 
enter the critical section. If a process is not able to enter the critical section immediately, 
it will wait until it is its turn to enter.
4. Processes cannot assume anything about each other's timing when entering a critical region:\
Bakery Algorithm uses a lock-free approach, which means that there are no blocking or 
waiting operations that could result in processes depending on the timing of other processes.