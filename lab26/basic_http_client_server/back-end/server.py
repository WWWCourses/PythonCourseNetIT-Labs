import asyncio
import websockets

connected = set()

HOST='localhost'
PORT=5123

async def server(websocket, path):
    # Register.
    connected.add(websocket)
    try:
        async for message in websocket:
            for conn in connected:
                if conn != websocket:
                    await conn.send(f'Msg send: {message}')
    finally:
        # Unregister.
        connected.remove(websocket)


start_server = websockets.serve(server, HOST, PORT)
print(f'Server is listening on {HOST}:{PORT}')


asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()