from typing import Optional
from loguru import logger
import logging
import threading
import time
from websocket import (
    ABNF,
    create_connection,
    WebSocketException,
    WebSocketConnectionClosedException,
)
from coins.lib.utils import parse_proxies


class CoinsSocketManager(threading.Thread):
    def __init__(
        self,
        stream_url,
        on_message=None,
        on_open=None,
        on_close=None,
        on_error=None,
        on_ping=None,
        on_pong=None,
        logger=None,
        proxies: Optional[dict] = None,
        max_reconnect_attempts=5,
        reconnect_delay=5,
    ):
        threading.Thread.__init__(self)
        if not logger:
            logger = logging.getLogger(__name__)
        self.logger = logger
        self.stream_url = stream_url
        self.on_message = on_message
        self.on_open = on_open
        self.on_close = on_close
        self.on_ping = on_ping
        self.on_pong = on_pong
        self.on_error = on_error
        self.proxies = proxies
        self.max_reconnect_attempts = max_reconnect_attempts
        self.reconnect_delay = reconnect_delay
        self._reconnect_count = 0
        self._stop_flag = False
        self._subscriptions = []  # Track subscriptions for reconnection

        self._proxy_params = parse_proxies(proxies) if proxies else {}

        self.create_ws_connection()

    def create_ws_connection(self):
        logger.info(
            f"Creating connection with WebSocket Server: {self.stream_url}, proxies: {self.proxies}",
        )
        self.ws = create_connection(self.stream_url, **self._proxy_params)
        logger.info(
            f"WebSocket connection has been established: {self.stream_url}, proxies: {self.proxies}",
        )
        self._reconnect_count = 0  # Reset reconnect count on successful connection
        self._callback(self.on_open)

    def _reconnect(self):
        """Attempt to reconnect to the WebSocket server"""
        if self._stop_flag:
            return False
            
        if self._reconnect_count >= self.max_reconnect_attempts:
            self.logger.error(
                f"Maximum reconnection attempts ({self.max_reconnect_attempts}) reached. Stopping reconnection."
            )
            return False

        self._reconnect_count += 1
        self.logger.info(
            f"Attempting to reconnect... (Attempt {self._reconnect_count}/{self.max_reconnect_attempts})"
        )
        
        try:
            time.sleep(self.reconnect_delay)
            self.create_ws_connection()
            
            # Resubscribe to previous subscriptions
            if self._subscriptions:
                self.logger.info(f"Resubscribing to {len(self._subscriptions)} stream(s)")
                for subscription in self._subscriptions:
                    self.ws.send(subscription)
                    
            return True
        except Exception as e:
            self.logger.error(f"Reconnection attempt {self._reconnect_count} failed: {e}")
            return False

    def run(self):
        self.read_data()

    def send_message(self, message):
        self.logger.debug("Sending message to Binance WebSocket Server: %s", message)
        try:
            self.ws.send(message)
            # Track subscriptions for reconnection (only track SUBSCRIBE messages)
            if '"method": "SUBSCRIBE"' in message and message not in self._subscriptions:
                self._subscriptions.append(message)
        except Exception as e:
            self.logger.error(f"Error sending message: {e}")
            raise e

    def ping(self):
        self.ws.ping()

    def read_data(self):
        data = ""
        while not self._stop_flag:
            try:
                op_code, frame = self.ws.recv_data_frame(True)
            except WebSocketException as e:
                if isinstance(e, WebSocketConnectionClosedException):
                    self.logger.error("Lost websocket connection")
                    self._callback(self.on_error, e)
                    
                    # Attempt to reconnect
                    if self._reconnect():
                        self.logger.info("Reconnection successful, resuming data stream")
                        continue
                    else:
                        self.logger.error("Failed to reconnect, stopping thread")
                        break
                else:
                    self.logger.error("Websocket exception: {}".format(e))
                    self._callback(self.on_error, e)
                    
                    # Attempt to reconnect for other WebSocket exceptions too
                    if self._reconnect():
                        self.logger.info("Reconnection successful, resuming data stream")
                        continue
                    else:
                        self.logger.error("Failed to reconnect, stopping thread")
                        break
            except Exception as e:
                self.logger.error("Exception in read_data: {}".format(e))
                self._callback(self.on_error, e)
                
                # Attempt to reconnect for unexpected exceptions
                if self._reconnect():
                    self.logger.info("Reconnection successful, resuming data stream")
                    continue
                else:
                    self.logger.error("Failed to reconnect, stopping thread")
                    break

            if op_code == ABNF.OPCODE_CLOSE:
                self.logger.warning(
                    "CLOSE frame received, closing websocket connection"
                )
                self._callback(self.on_close)
                break
            elif op_code == ABNF.OPCODE_PING:
                self._callback(self.on_ping, frame.data)
                self.ws.pong("")
                self.logger.debug("Received Ping; PONG frame sent back")
            elif op_code == ABNF.OPCODE_PONG:
                self.logger.debug("Received PONG frame")
                self._callback(self.on_pong)
            else:
                data = frame.data
                if op_code == ABNF.OPCODE_TEXT:
                    data = data.decode("utf-8")
                self._callback(self.on_message, data)

    def close(self):
        self._stop_flag = True  # Signal thread to stop
        if not self.ws.connected:
            self.logger.warn("Websocket already closed")
        else:
            self.ws.send_close()
        return

    def _callback(self, callback, *args):
        if callback:
            try:
                callback(self, *args)
            except Exception as e:
                self.logger.error("Error from callback {}: {}".format(callback, e))
                if self.on_error:
                    self.on_error(self, e)
