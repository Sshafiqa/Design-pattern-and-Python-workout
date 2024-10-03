# Example 1
import threading


def safe_increment(counter, lock):
    """Thread-safe increment function."""
    with lock:
        for _ in range(1000):
            counter[0] += 1


if __name__ == '__main__':
    counter = [0]
    lock = threading.Lock()

    # Create and start threads
    threads = [threading.Thread(target=safe_increment, args=(counter, lock)) for _ in range(10)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final counimport threading
import time

condition = threading.Condition()
flag = False

def waiter():
    """Thread that waits for a condition to be met."""
    with condition:
        print("Waiter is waiting")
        while not flag:
            condition.wait()
        print("Waiter is notified")

def notifier():
    """Thread that notifies the condition."""
    time.sleep(2)
    with condition:
        global flag
        flag = True
        condition.notify_all()
        print("Notifier has notified")

if __name__ == '__main__':
    t1 = threading.Thread(target=waiter)
    t2 = threading.Thread(target=notifier)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
ter value: {counter[0]}")

# Example 2
