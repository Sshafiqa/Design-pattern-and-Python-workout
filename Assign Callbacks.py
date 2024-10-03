from multiprocessing import Process, Queue


def worker(queue):
    """Worker function to be executed in a separate process."""
    result = "Hello from the worker process!"
    queue.put(result)  # Use queue to send result back to main process


def callback(result):
    """Callback function to handle results."""
    print(f"Callback received result: {result}")


if __name__ == '__main__':
    # Create a queue for inter-process communication
    queue = Queue()

    # Create and start a new process
    process = Process(target=worker, args=(queue,))
    process.start()

    # Wait for the process to complete
    process.join()

    # Retrieve result from the queue
    result = queue.get()

    # Call the callback function
    callback(result)
