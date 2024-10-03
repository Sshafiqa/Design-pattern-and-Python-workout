import threading


def compute_square(number, results):
    """Function to compute the square of a number."""
    result = number * number
    results.append(result)
    print(f"Computed square: {result}")


if __name__ == '__main__':
    results = []

    # Create and start threads
    threads = []
    for i in range(5):
        thread = threading.Thread(target=compute_square, args=(i, results))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print(f"Results: {results}")
