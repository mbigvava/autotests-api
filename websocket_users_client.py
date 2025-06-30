import asyncio
import websockets

async def run_client():
    uri = "ws://localhost:8766"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Привет, сервер!")

        for _ in range(5):
            message = await websocket.recv()
            print(message)

if __name__ == "__main__":
    asyncio.run(run_client())