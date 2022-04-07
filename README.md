# websocket_benchmark
python websocket rx benchmark.
- check only RX performance.

## target
- QWebSocket
- websockets (https://pypi.org/project/websockets/)
- websocket-client (https://pypi.org/project/websocket-client/)

# result 
- QWebSocket > websockets >= websocket-client
- QWebSocket is best.

```             
(4096/ws)       elapsed(sec) msg-size(bytes) cnt  
QWebSocket        2.766004      4096        50000  * BEST
websockets        3.124001      4096        50000 
websocket-client 70.143076      4096        50000  (skip_utf8_validation=False) default
websocket-client  3.076994      4096        50000  (skip_utf8_validation=True)

(512/ws)        elapsed(sec) msg-size(bytes) cnt  
QWebSocket        2.458998       512        50000  * BEST
websockets        3.066020       512        50000 
websocket-client 10.640008       512        50000  (skip_utf8_validation=False) default
websocket-client  2.745998       512        50000  (skip_utf8_validation=True)

(512/wss)       elapsed(sec) msg-size(bytes) cnt  
QWebSocket        2.983025       512        50000  * BEST
websockets        3.504999       512        50000 
websocket-client 11.673517       512        50000  (skip_utf8_validation=False) default
websocket-client  3.658998       512        50000  (skip_utf8_validation=True)

```
