# Producer - comsumer queue lock
import concurrent.futures
import logging
import queue
import random
import threading
import time


def producer(queue, event):
    """
    Pretend we're getting a number from the network.
    """
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        queue.put(message)

    logging.info("Producer received event. Exiting")


def consumer(queue, event):
    """
    Pretend we're saving a number in the database
    """
    while not queue.is_set() or not pipeline.empty():
        message = queue.get()
        logging.info(
            "Consumer storing message: %s (queue size=%d)", message, queue.qsize()
        )

    logging.info("Consumer received event. Exiting")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)

    pipeline = queue.Queue(maxsize=10)
    # threading.Event object allows one thread to signal an event while many other threads can be waiting for that event to happen.
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()
