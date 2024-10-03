from multiprocessing import Process, Lock, Condition, Semaphore


def synchronized_task(lock, condition, semaphore):
    """Task that uses mutex, condition, and semaphore for synchronization."""
    with lock:
        print("Task acquired the lock")
        condition.wait()  # Wait for the condition to be notified
        semaphore.acquire()
        print("Semaphore acquired")
        # Simulate some work
        semaphore.release()
        print("Semaphore released")


def notifier(condition):
    """Notifier function to signal the condition."""
    import time
    time.sleep(2)
    with condition:
        print("Notifying condition")
        condition.notify_all()


if __name__ == '__main__':
    lock = Lock()
    condition = Condition(lock)
    semaphore = Semaphore(1)

    p1 = Process(target=synchronized_task, args=(lock, condition, semaphore))
    p2 = Process(target=notifier, args=(condition,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
