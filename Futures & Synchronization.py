# Example 1
import asyncio


async def produce(future):
    print("Producing result...")
    await asyncio.sleep(1)
    future.set_result("Result produced")


async def consume(future):
    print("Waiting for result...")
    result = await future
    print(f"Received: {result}")


async def main():
    future = asyncio.Future()

    producer = asyncio.create_task(produce(future))
    consumer = asyncio.create_task(consume(future))

    await producer
    await consumer


# Run the event loop
if __name__ == '__main__':
    asyncio.run(main())

# Example 2
import asyncio


async def critical_section(lock, name):
    async with lock:
        print(f"{name} entered critical section")
        await asyncio.sleep(1)
        print(f"{name} leaving critical section")


async def main():
    lock = asyncio.Lock()

    # Create multiple tasks that use the lock
    tasks = [
        asyncio.create_task(critical_section(lock, "Task 1")),
        asyncio.create_task(critical_section(lock, "Task 2")),
        asyncio.create_task(critical_section(lock, "Task 3")),
    ]

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)


# Run the event loop
if __name__ == '__main__':
    asyncio.run(main())
