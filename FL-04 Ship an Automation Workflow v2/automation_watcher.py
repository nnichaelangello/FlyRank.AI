import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define paths
base_dir = os.path.dirname(os.path.abspath(__file__))
target_project_dir = os.path.abspath(os.path.join(base_dir, "..", "FL-17-CUSTOM-MQX0Q5QE-6FE1938E The Plan to Keep Building Details"))
watch_folder = os.path.join(target_project_dir, "resumes")
screener_script = os.path.join(target_project_dir, "resume_screener.py")

class ResumeHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.pdf'):
            print(f"\n[AUTOMATION] New resume detected: {event.src_path}")
            print("[AUTOMATION] Triggering AI Resume Screener pipeline...\n")
            
            # Run the resume screener script
            try:
                subprocess.run(["python", screener_script], cwd=target_project_dir, check=True)
                print("\n[AUTOMATION] Pipeline execution finished.")
                print(f"[AUTOMATION] Waiting for new resumes in {watch_folder}...")
            except Exception as e:
                print(f"[ERROR] Failed to run screener: {e}")

if __name__ == "__main__":
    if not os.path.exists(watch_folder):
        print(f"[ERROR] Watch folder does not exist: {watch_folder}")
        print("Please ensure you have run the screener setup first.")
        exit(1)

    print(f"[*] [SYSTEM] Automation Workflow Watcher Started")
    print(f"[*] Monitoring directory: {watch_folder}")
    print("[*] Drop a new .pdf file into this folder to automatically trigger the ML pipeline. Press Ctrl+C to stop.\n")

    event_handler = ResumeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=watch_folder, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n[SYSTEM] Automation Watcher stopped.")
    
    observer.join()
