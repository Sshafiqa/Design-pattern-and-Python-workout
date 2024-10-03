import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def main():
    await say_hello()

# Run the event loop
if __name__ == '__main__':
    asyncio.run(main())
