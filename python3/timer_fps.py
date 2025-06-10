import time


class FPSCounter:
    """Simple class to measure call frequency"""

    def __init__(self):
        self.last_time = time.time()
        self.frame_count = 0

    def tick(self):
        self.frame_count += 1
        current_time = time.time()
        elapsed = current_time - self.last_time

        if elapsed >= 1.0:
            print("FPS: %s" % self.frame_count)
            self.frame_count = 0
            self.last_time = time.time()
