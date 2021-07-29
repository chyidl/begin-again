# racecond.py
"""
Race conditions can occur when two or more threads access a shared piece of data or resource.

Similar race conditions can arise when one thread frees memory or closes a file handle before the other thread is finished accessing it.
"""
import concurrent.futures
import threading
import logging
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0
        # This ._lock is initialized in the unlocked state and locked and released by the with statement.
        self._lock = threading.Lock()

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update, Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)
