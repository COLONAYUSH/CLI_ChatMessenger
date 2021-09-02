# This program is demonstrating the role of locks
# in multithreading to emit the race condition

import threading


def counter(n, lock):
    for i in range(n, -1, -1):
        # Acquire the lock
        # This will force it to run by acquiring the lock
        lock.acquire()
        print(i, end=" ")
        # Release the lock
        # This will release the thread for another use
        lock.release()


def counter_inverse(n, lock):
    for i in range(n + 1):
        lock.acquire()
        print(i, end=" ")
        lock.release()


# creation of a lock
lock = threading.Lock()

# Assigning of thread for individual function
t1 = threading.Thread(target=counter, args=(10, lock,))
t2 = threading.Thread(target=counter_inverse, args=(10, lock))

# Starting of thread
t1.start()
t2.start()

# Waiting for thread to finish
t1.join()
t2.join()

print("Done!")
