import asyncio
import logging

import websockets


async def server_main(websocket, path):
    logging.info(f'server_main, path:{path}')
    while True:
        rx_msg = await websocket.recv()
        logging.info(f'< {rx_msg}')

        if rx_msg.startswith('start_bm'):
            tokens = rx_msg.split()
            assert len(tokens) == 3

            size = int(tokens[1])
            cnt  = int(tokens[2])
            logging.info(f'size:{size}, cnt:{cnt}')
            tx_msg = 'a' * size
            for i in range(cnt):
                await websocket.send(tx_msg)
            await websocket.send(f'end_bm')
        else:
            tx_msg = f'echo {rx_msg!r}'
            await websocket.send(tx_msg)
            logging.info(f'> {tx_msg}')

if __name__ == '__main__':
    # debug
    LOG_FORMAT = '%(pathname)s:%(lineno)03d | %(asctime)s | %(levelname)s | %(message)s'
    # LOG_LEVEL = logging.DEBUG  # DEBUG(10), INFO(20), (0~50)
    LOG_LEVEL = logging.INFO  # DEBUG(10), INFO(20), (0~50)

    logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)

    start_server = websockets.serve(server_main, "localhost", 8080)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

