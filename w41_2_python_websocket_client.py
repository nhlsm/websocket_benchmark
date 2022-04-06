import asyncio
import logging
import time

import websockets

async def WebSocketClient_websockets(size=4096, cnt=50_000):
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as websocket:
        t0 = time.time()
        await websocket.send(f'start_bm {size} {cnt}')
        while True:
            rx_msg = await websocket.recv()
            if rx_msg == 'end_bm':
                break
        t1 = time.time()
        logging.info(f'elapsed: {t1 - t0:.06f}, size:{size:,}, cnt:{cnt:,}')


if __name__ == '__main__':
    # debug
    LOG_FORMAT = '%(pathname)s:%(lineno)03d | %(asctime)s | %(levelname)s | %(message)s'
    # LOG_LEVEL = logging.DEBUG  # DEBUG(10), INFO(20), (0~50)
    LOG_LEVEL = logging.INFO  # DEBUG(10), INFO(20), (0~50)

    logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)

    # elapsed: 3.124001, size:4,096, cnt:50,000
    # elapsed: 3.283999, size:4,096, cnt:50,000

    # elapsed: 2.353029, size:10, cnt:50,000
    # elapsed: 2.407032, size:10, cnt:50,000
    asyncio.get_event_loop().run_until_complete(WebSocketClient_websockets())
