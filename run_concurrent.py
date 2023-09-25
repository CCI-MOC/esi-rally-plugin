import subprocess
import threading

# List of task files to execute concurrently
task_files = ["esi_node_network_attach_task_2.yaml", "esi_node_network_attach_task_1.yaml", "esi_node_network_attach_task_3.yaml", "esi_node_network_attach_task_4.yaml", "esi_node_network_attach_task_5.yaml"]

def execute_rally_task(task_file):
    command = f"rally --plugin-paths esi_node_network_attach_plugin.py task start {task_file}"
    subprocess.call(command, shell=True)

# Create threads for each task file
threads = []
for task_file in task_files:
    thread = threading.Thread(target=execute_rally_task, args=(task_file,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All tasks completed.")

