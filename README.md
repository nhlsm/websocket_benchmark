# websocket_benchmark
python websocket rx benchmark.
- check only RX performance.
- use ws, not wss.

## target
- QWebSocket
- websockets (https://pypi.org/project/websockets/)
- websocket-client (https://pypi.org/project/websocket-client/)

# result 
- QWebSocket > websockets >= websocket-client
- QWebSocket is best.

```             
                 elapsed(sec) msg-size(bytes) cnt  
QWebSocket        2.766004      4096        50000  * BEST
websockets        3.124001      4096        50000 
websocket-client 70.143076      4096        50000  (skip_utf8_validation=False) default
websocket-client  3.076994      4096        50000  (skip_utf8_validation=True)

```
