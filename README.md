# Assignment 03 - Dining Philosophers
## About assignment 
The dining philosopher's problem is a well-known synchronization problem in computer science. The problem
scenario involves five philosophers seated around a circular table, whose task is to alternate between 
thinking and eating. In the center of the table is a bowl of some food and five forks, one for each 
philosopher. To eat, a philosopher needs to use both their right and left forks. However, a philosopher
can only eat if they have both their immediate left and right forks available. The dining philosopher's 
problem represents a large class of concurrency control problems.[1]

## How to run
All you need to successfully run this implementation is to install fei.ppds package for python like so:  
Windows: `py -3 -m pip install --upgrade fei.ppds`  
Linux:`pip3 install --upgrade fei.ppds`.

## Implementation
The Shared class contains the shared data for all threads, which in this case is a list of `NUM_PHILOSOPHERS` 
forks represented by `Mutex` objects.  
The `philosopher` class represents a philosopher thread. Each philosopher has a unique id, which is used to 
determine whether they take the left or right fork first. When a philosopher wants to eat, they first check 
if the fork in the appropriate order (left fork for philosopher 0, right fork for all other philosophers) 
is available. If the fork is available, the philosopher waits for a short time and then tries to grab the 
other fork. If both forks are successfully grabbed, the philosopher eats and then releases both forks. 
If either fork is unavailable, the philosopher releases any forks they are holding and tries again after a 
short delay.  
The `main` function creates NUM_PHILOSOPHERS(default is 5) philosopher threads, each with a unique id and 
a reference to the shared forks list. It then starts each philosopher thread and waits for all threads to finish.

## Comparison with waiter(footman) solution
In implementation with waiter(footman) solution a waiter was used to ensure that no more than four(NUM_PHILOSOPHERS - 1) 
philosophers were eating at the same time, in order to prevent deadlock. If four philosophers were eating at the same
time the fifth one had to wait.

In the waiter-based solution, a philosopher needs to acquire a semaphore before they can start eating. If all the 
other philosophers are currently eating, the philosopher will have to wait until at least one of them finishes and 
releases the semaphore before they can start eating. This can lead to some philosophers waiting for a long time 
before being able to eat, which can result in potential starvation. The solution where one philosopher takes the 
left fork first ensures that all philosophers can grab at least one fork. This reduces the potential for starvation,
as it ensures that every philosopher can make progress towards getting both forks.

Overall, while neither solution can completely eliminate the potential for starvation, the solution where one 
philosopher takes the left fork first has a lower potential for starvation compared to the waiter-based solution.

## Sources
[1] https://www.javatpoint.com/os-dining-philosophers-problem