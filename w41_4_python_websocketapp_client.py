import logging
import time

import websocket

# skip_utf8_validation=False (default)
# elapsed: 70.143076, size:4,096, cnt:50,000
#
# skip_utf8_validation=True
# elapsed:  3.225032, size:4,096, cnt:50,000
# elapsed:  2.591002, size:4,096, cnt:50,000
# elapsed:  3.076994, size:4,096, cnt:50,000

# skip_utf8_validation=False (default)
# elapsed: 1.976994, size:10, cnt:50,000
# elapsed: 1.648000, size:10, cnt:50,000
# elapsed: 1.601053, size:10, cnt:50,000

# skip_utf8_validation=True
# elapsed: 2.373036, size:10, cnt:50,000
# elapsed: 1.563003, size:10, cnt:50,000
# elapsed: 1.722402, size:10, cnt:50,000

# skip_utf8_validation=True
# elapsed: 14.123049, size:4,096, cnt:10,000
# elapsed: 19.235037, size:1,024, cnt:50,000
# elapsed: 4.029000, size:1,024, cnt:10,000

# size = 10
size = 4096
# size = 1024
cnt = 50_000
# cnt = 10_000
t0 = 0
t1 = 0

def on_open(ws):
    global t0
    logging.info(f'### on_open ###')
    t0 = time.time()
    ws.send(f'start_bm {size} {cnt}')

def on_message(ws, message):
    # print(message)
    if message == 'end_bm':
        t1 = time.time()
        logging.info(f'elapsed: {t1 - t0:.06f}, size:{size:,}, cnt:{cnt:,}')

def on_error(ws, error):
    logging.info(f'### on_error ###, err:{error}')

def on_close(ws, close_status_code, close_msg):
    logging.info(f'### closed ###')

if __name__ == "__main__":
    # debug
    LOG_FORMAT = '%(pathname)s:%(lineno)03d | %(asctime)s | %(levelname)s | %(message)s'
    # LOG_LEVEL = logging.DEBUG  # DEBUG(10), INFO(20), (0~50)
    LOG_LEVEL = logging.INFO  # DEBUG(10), INFO(20), (0~50)

    logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)

    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://localhost:8080",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    # ws.run_forever(skip_utf8_validation=False) # Set dispatcher to automatic reconnection(default)
    ws.run_forever(skip_utf8_validation=True)  #

    # ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    # rel.signal(2, rel.abort)  # Keyboard Interrupt
    # rel.dispatch()


