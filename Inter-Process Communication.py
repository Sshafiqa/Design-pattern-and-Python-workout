# Example 1
from multiprocessing import Process, Queue


def producer(queue):
    """Producer function that puts items into the queue."""
    for i in range(5):
        queue.put(i)
    queue.put(None)  # Sentinel value to indicate the end of data


def consumer(queue):
    """Consumer function that processes items from the queue."""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")


if __name__ == '__main__':
    queue = Queue()

    p1 = Process(target=producer, args=(queue,))
    p2 = Process(target=consumer, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

# Example 2
from multiprocessing import Process, Pipe


def sender(pipe):
    """Function to send data through the pipe."""
    pipe.send("Hello from sender!")
    pipe.close()


def receiver(pipe):
    """Function to receive data from the pipe."""
    message = pipe.recv()
    print(f"Received message: {message}")


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()

    p1 = Process(target=sender, args=(child_conn,))
    p2 = Process(target=receiver, args=(parent_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
