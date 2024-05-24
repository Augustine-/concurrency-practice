"""
Implement two methods in a class, schedule() and waitUntilComplete().
schedule() should enqueue work to be performed and should be non-blocking.
waitUntilComplete() should block the call untill all scheduled work is completed.

Builtin thread safe constructs like Deque, BlockingQueue, etc. can't be used. Implement it using locks, etc ensuring thread safety.
"""
import threading
from concurrent.futures import ThreadPoolExecutor

class Scheduler:
    def __init__(self, max_workers):
        self.futures = []
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.exec = ThreadPoolExecutor(max_workers=max_workers)

    def schedule(self, task, *args, **kwargs):
        with self.lock:
            future = self.exec.submit(task, *args, **kwargs)
            self.futures.append(future)
            future.add_done_callback(self._task_done)

    def _task_done(self, future):
        with self.lock:
            if all(f.done() for f in self.futures):
                self.condition.notify_all()

    def waitUntilComplete(self):
        with self.lock:
            while not all(f.done() for f in self.futures):
                self.condition.wait()
            self.condition.notify_all()
        self.exec.shutdown(wait=True)





if __name__ == '__main__':
    import time

    def example_task(seconds):
        print(f"sleeping for {seconds} seconds...")
        time.sleep(seconds)
        print("...task complete!")

    s = Scheduler(max_workers=3)
    s.schedule(example_task, 3)
    s.schedule(example_task, 1)
    s.schedule(example_task, 2)
    s.waitUntilComplete()
    print("All tasks completed!")