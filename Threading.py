import threading

def worker():
    """Thread worker function."""
    print("Worker thread is running")

if __name__ == '__main__':
    # Create a thread
    thread = threading.Thread(target=worker)
    # Start the thread
    thread.start()
    # Wait for the thread to complete
    thread.join()
    print("Thread has finished")
