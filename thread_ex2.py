import threading
import time
class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        for i in range(5):
            print(f"{self.name}: {i}")
            time.sleep(2)
            print(f"After sleep{i}=> {self.name}: {i}")
# Create and start threads
thread1 = MyThread("Thread1")
thread2 = MyThread("Thread2")
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("All threads completed.")