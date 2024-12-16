import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    DIRECTORY_TO_WATCH = "."  # Base directory to watch

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                pass
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    def __init__(self):
        self.running_processes = {}

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            script_name = os.path.basename(event.src_path)
            print(f"\nDetected change in {script_name}. Restarting...")

            # Restart the specific script
            self.restart_script(script_name)

    def restart_script(self, script_path):
        script_name = os.path.basename(script_path)
        if script_name in self.running_processes:
            process = self.running_processes[script_name]
            process.terminate()
        print(f"\nStarting new process for {script_path}")
        new_process = subprocess.Popen(["python", script_path])
        self.running_processes[script_name] = new_process

if __name__ == "__main__":
    watcher = Watcher()
    watcher.run()