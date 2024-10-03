from multiprocessing import Process, Queue


def compute_square(number, queue):
    """Function to compute the square of a number."""
    result = number * number
    queue.put(result)  # Return result via queue


if __name__ == '__main__':
    number = 5
    queue = Queue()

    # Create and start the process
    process = Process(target=compute_square, args=(number, queue))
    process.start()
    process.join()

    # Retrieve the result from the queue
    result = queue.get()
    print(f"The square of {number} is {result}")
