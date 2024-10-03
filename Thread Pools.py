import threading
from concurrent.futures import ThreadPoolExecutor


def worker(num):
    """Worker function that computes the square of a number."""
    print(f"Worker {num} is computing")
    return num * num


if __name__ == '__main__':
    # Create a ThreadPoolExecutor with 3 threads
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks to the pool
        futures = [executor.submit(worker, i) for i in range(5)]

        # Retrieve and print results
        for future in futures:
            result = future.result()
            print(f"Result: {result}")
