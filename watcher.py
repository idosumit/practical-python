import os
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from threading import Timer


class Watcher:
    DIRECTORY_TO_WATCH = "."  # Base directory to watch

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)  # Prevent excessive CPU usage
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


class Handler(FileSystemEventHandler):
    def __init__(self):
        self.running_processes = {}
        self.debounce_timers = {}  # To handle rapid successive events

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            if event.src_path in self.debounce_timers:
                self.debounce_timers[
                    event.src_path
                ].cancel()  # Cancel any existing timer

            # Set a debounce timer of 1 second
            self.debounce_timers[event.src_path] = Timer(
                1, self.restart_script, [event.src_path]
            )
            self.debounce_timers[event.src_path].start()

    def restart_script(self, script_path):
        # Stop the previous process if it's running
        if script_path in self.running_processes:
            process = self.running_processes[script_path]
            process.terminate()
            print(f"\nStopped process for {script_path}\n")

        # Start a new process for the updated script
        print(f"Starting new process for {script_path}")
        script_dir = os.path.dirname(script_path)
        new_process = subprocess.Popen(
            ["python", script_path],
            cwd=script_dir,  # Set the working directory to the script's directory
        )
        self.running_processes[script_path] = new_process


if __name__ == "__main__":
    watcher = Watcher()
    watcher.run()
