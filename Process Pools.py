from multiprocessing import Pool


def worker(num):
    """Worker function that squares a number."""
    return num * num


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    # Create a Pool of 3 worker processes
    with Pool(3) as pool:
        results = pool.map(worker, numbers)

    print(f"Results: {results}")
