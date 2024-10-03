import threading
import queue


def producer(q):
    """Function to produce data and put it in the queue."""
    for i in range(5):
        q.put(i)
        print(f"Produced {i}")


def consumer(q):
    """Function to consume data from the queue."""
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed {item}")


if __name__ == '__main__':
    q = queue.Queue()

    producer_thread = threading.Thread(target=producer, args=(q,))
    consumer_thread = threading.Thread(target=consumer, args=(q,))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    q.put(None)  # Sentinel value to indicate the end of data
    consumer_thread.join()
