# Assignment 04 - Dining savages
## About assignment
The dining savages problem involves a group of savages who share a single pot of food. The savages can take 
a serving from the pot as long as it is not empty. If the pot is empty, a savage must wake up the cook to 
refill the pot before continuing the feast. Therefore, the primary abstractions are the savages, the cook, 
and the pot containing a fixed number of servings of food. The savages can only eat when the pot is not empty, 
while the cook can only fill the pot when it is empty.  
The problem arises when multiple savages attempt to access the pot simultaneously, as well as when the pot 
becomes empty or full. The goal is to synchronize the savages and the cook so that they don't interfere with 
each other and the pot doesn't overflow or become empty.[1,2]

## How to run
All you need to successfully run this implementation is to install fei.ppds package for python like so:  
Windows: `py -3 -m pip install --upgrade fei.ppds`  
Linux:`pip3 install --upgrade fei.ppds`.

## Implementation
This implementation of a solution to the dining savages with one cook problem uses the fei.ppds package.
The `SimpleBarrier` class implements a simple barrier that is used to ensure that all the savages are ready 
to eat before any of them can start eating.  
The `Shared` class represents shared data between threads like mutex or semaphores.   
The `savage` function represents a savage thread, which waits for other savages to be ready to eat using the 
`SimpleBarrier`. Once all savages are ready, the thread tries to access the shared data using the mutex. 
If the pot is empty, the savage that came to the empty pot signals the cook to prepare a new meal for the pot 
and waits for it to be filled with food. When the pot is full, the savage takes a serving and eats.
The `cook` function represents the cook thread, which waits for the signal that the pot is empty, then prepares 
a new pot and fills it with `H` servings of food before signaling the savages that the pot is full again.
The `main` function is where a number of savage threads and one cook thread are created and started. The number 
of threads is determined by the `D` constant, and the number of servings in each pot is determined by the `H` 
constant.[2]

We've set the default values of `D` to 10 and `H` to 5.  
As for time it takes to cook the food or eat serving we chose `sleep(randint(50, 200) / 100)` because sometimes 
cook can prepare food faster because the fire under the pot was bigger, on the other hand savage can eat faster 
or slower depending on how hungry he was (these were just potential real-life examples ofcourse).


## Synchronization patterns
### 1. Mutex

![alt text](https://i.imgur.com/zlGLrdo.png)


We've used mutex to protect the critical section which includes servings counter. 

### 2. Barrier

![alt text](https://i.imgur.com/mZJdkFn.png)

Thanks to the simple barrier all savage threads wait for each other before accessing the pot with food.

### 3. Semaphore
1. in savage method:
![alt text](https://i.imgur.com/dbTZTLU.png)
2. in cook method:
![alt text](https://i.imgur.com/1MB5wxc.png)

We use semaphores for signaling when it's cooks turn to cook and fill the pot with servings and when the 
pot is full and savages can take servings from it and proceed to eat. 


## Sources
[1] https://www.eiffel.org/doc/solutions/Dining_savages  
[2] https://chat.openai.com/chat/

