import queue
import random
import time
import threading

request_queue = queue.Queue()
stop_event = threading.Event()


def generate_request():
    while not stop_event.is_set():
        request_id = random.randint(1000, 9999)
        request_data = f"Request ID: {request_id}"
        request_queue.put(request_data)
        print(f"Added to the queue: {request_data}. Queue length: {request_queue.qsize()}")
        time.sleep(1)


def process_request():
    while not stop_event.is_set() or not request_queue.empty():
        if not request_queue.empty():
            request_data = request_queue.get()
            print(f"Processing: {request_data}. Queue length: {request_queue.qsize()}")
            processing_time = random.uniform(0.9, 2)
            time.sleep(processing_time)
        else:
            print("The queue is empty.")
            time.sleep(1)


def main():
    generator_thread = threading.Thread(target=generate_request)
    processor_thread = threading.Thread(target=process_request)

    generator_thread.start()
    processor_thread.start()

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nGraceful shutdown started...")
        print("\nProcessing remaining tasks...")
        stop_event.set()

    generator_thread.join()
    processor_thread.join()


if __name__ == "__main__":
    main()
