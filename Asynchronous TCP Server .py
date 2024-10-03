# Example 1
import asyncio

async def handle_client(reader, writer):
    data = await reader.read(100)
    print(f"Received: {data.decode()}")
    writer.write(b"Hello, Async Client!")
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 12345)
    async with server:
        await server.serve_forever()

asyncio.run(main())

# Example 2
import asyncio

async def tcp_client():
    reader, writer = await asyncio.open_connection('localhost', 12345)
    writer.write(b"Hello, Async Server!")
    data = await reader.read(100)
    print(f"Received: {data.decode()}")
    writer.close()

asyncio.run(tcp_client())
