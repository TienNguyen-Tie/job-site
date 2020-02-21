import threading
import time
import glob
import subprocess


class SingleThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        # subprocess.run(["ls", "-l"])
        print("Exiting " + self.name)


scripts = glob.glob("./outputs/*.py")

threads = []
count = 1
for script in scripts:
    init_thread = SingleThread(count, f'Running {script}', count)
    count = count+1
    init_thread.start()
    threads.append(init_thread)

for t in threads:
    t.join()

print("Exiting Main Thread")
