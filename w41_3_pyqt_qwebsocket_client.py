import logging
import time

from PyQt5.QtCore import *
from PyQt5.QtWebSockets import *
from PyQt5.QtWidgets import *


class WebSocketClient_qwebsocket(QObject):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.m_ws =QWebSocket()
        self.m_ws.connected.connect(self.on_connected)
        self.m_ws.disconnected.connect(self.on_disconnected)
        self.m_ws.textMessageReceived.connect(self.on_textMessageReceived)

        self.m_t0 = 0
        self.m_size = 0
        self.m_cnt = 0

    def start(self, size = 4096, cnt=50_000):
        self.m_t0 = 0
        self.m_size = size
        self.m_cnt = cnt
        self.m_ws.open(QUrl('ws://localhost:8080'))

    def on_connected(self):
        logging.info(f'on_connected')
        self.m_t0 = time.time()
        self.m_ws.sendTextMessage(f'start_bm {self.m_size} {self.m_cnt}')

    def on_disconnected(self):
        logging.info(f'on_disconnected')

    def on_textMessageReceived(self, msg):
        # logging.info(f'on_textMessageReceived: {msg}')
        if msg ==  'end_bm':
            t1 = time.time()
            logging.info(f'elapsed: {t1-self.m_t0:.06f}, size:{self.m_size:,}, cnt:{self.m_cnt:,}')


if __name__ == '__main__':
    # debug
    LOG_FORMAT = '%(pathname)s:%(lineno)03d | %(asctime)s | %(levelname)s | %(message)s'
    # LOG_LEVEL = logging.DEBUG  # DEBUG(10), INFO(20), (0~50)
    LOG_LEVEL = logging.INFO  # DEBUG(10), INFO(20), (0~50)

    logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)

    ##################################################
    app = QApplication([])

    # elapsed: 2.766004, size:4,096, cnt:50,000
    # elapsed: 2.811036, size:4,096, cnt:50,000
    # elapsed: 2.811036, size:4,096, cnt:50,000

    # elapsed: 1.743027, size:10, cnt:50,000
    # elapsed: 1.585999, size:10, cnt:50,000
    wsc = WebSocketClient_qwebsocket()
    # wsc.start(size = 4096, cnt = 50_000)
    wsc.start(size = 10, cnt = 50_000)

    app.exec_()

