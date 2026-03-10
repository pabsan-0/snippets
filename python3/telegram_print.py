import queue
import threading
import time

import requests

# Config
BOT_TOKEN = ""
CHAT_ID = ""  # Broadcast group ID
RETRY_DELAY = 3  # Seconds between retries

# Internal Queue and Worker Thread
message_queue = queue.Queue()


def _telegram_worker():
    while True:
        text = message_queue.get()
        while True:
            try:
                url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                payload = {"chat_id": CHAT_ID, "text": text}
                response = requests.post(url, data=payload, timeout=5)
                response.raise_for_status()
                break  # success
            except requests.exceptions.RequestException:
                time.sleep(RETRY_DELAY)
        message_queue.task_done()


# Queue consumer daemonizer
threading.Thread(target=_telegram_worker, daemon=True).start()


# Public API
def tprint(*args, sep=" ", end="", flush=False):
    """
    Mimics the built-in print(), but sends the output to Telegram.
    Non-blocking. Will retry on failure in background.
    """
    text = sep.join(str(arg) for arg in args) + end
    message_queue.put(text)


def tprint_flush(timeout=10):
    """
    Blocks until all messages in the tprint queue are sent or until timeout is reached.
    """
    start_time = time.time()
    while not message_queue.empty():
        elapsed = time.time() - start_time
        if elapsed >= timeout:
            break
        # Wait briefly to yield control and avoid busy-waiting
        time.sleep(0.1)
