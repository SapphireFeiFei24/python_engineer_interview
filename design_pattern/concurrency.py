'''
Multi threading
'''
import random
import threading
import time
def download_page(url):
    print(f"Starting download: {url}")
    time.sleep(random.randint(0,4))  # Simulate network delay
    print(f"Finished download: {url}")

# List of "URLs" to download
urls = ["http://example.com/page1", "http://example.com/page2", "http://example.com/page3"]
global_lock = threading.Lock()
class safeCounter:
    _instance = None
    _init_lock = threading.Lock()
    def __init__(self):
        with self._init_lock:
            print(f"__init={self.__initialized}")
            if not self.__initialized:
                print("initing")
                time.sleep(2)
                self.lock = threading.Lock()
                self.count = 0
                self.__initialized = True

    def __new__(cls):
        with global_lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance.__initialized = False
        return cls._instance

    def increment(self, worker_id):
        with self.lock:
            print(f"worker_{worker_id} adding one to {self.count}")
            self.count += 1
            print(f"worker_{worker_id} finished. count={self.count}")


def worker(worker_id, num_times):

    counter = safeCounter()
    for i in range(num_times):
        counter.increment(worker_id)
        time.sleep(random.randint(0,4))

if __name__ == "__main__":
    # Start a thread for each download
    threads = []
    # Multi thread reading
    # for url in urls:
    #     thread = threading.Thread(target=download_page, args=(url,))
    #     thread.start()
    #     threads.append(thread)

    # Multi thread writing
    for w in range(5):
        thread = threading.Thread(target=worker, args=(w, 2))
        thread.start()
        threads.append(thread)
    print("waiting...")
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All downloads completed.")

