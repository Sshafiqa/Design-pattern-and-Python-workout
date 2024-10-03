import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://echo.websocket.org') as websocket:
        await websocket.send("Hello, WebSocket!")
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.get_event_loop().run_until_complete(hello())
