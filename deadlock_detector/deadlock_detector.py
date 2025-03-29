from collections import defaultdict
from tkinter import messagebox

class DeadlockDetector:
    def __init__(self, num_processes):
        self.graph = defaultdict(list)
        self.num_processes = num_processes

    def add_edge(self, process1, process2):
        """Adds a dependency edge (process1 -> process2) in the wait-for graph"""
        if process1 >= self.num_processes or process2 >= self.num_processes:
            messagebox.showerror("Error", f"Invalid process! Enter values between 0 and {self.num_processes - 1}.")
            return
        self.graph[process1].append(process2)

    def detect_cycle_util(self, process, visited, rec_stack, path):
        """Helper function for cycle detection using DFS"""
        visited[process] = True
        rec_stack[process] = True
        path.append(process)

        for neighbor in self.graph[process]:
            if not visited.get(neighbor, False):
                if self.detect_cycle_util(neighbor, visited, rec_stack, path):
                    return True
            elif rec_stack.get(neighbor, False):  # Cycle detected
                path.append(neighbor)
                cycle_start = path.index(neighbor)
                messagebox.showerror("Deadlock Detected", f"Deadlock Cycle: {' -> '.join(map(str, path[cycle_start:]))}")
                return True

        rec_stack[process] = False
        path.pop()
        return False

    def detect_deadlock(self):
        """Detects cycles in the wait-for graph"""
        visited = {p: False for p in range(self.num_processes)}
        rec_stack = {p: False for p in range(self.num_processes)}

        for process in range(self.num_processes):
            if not visited[process]:
                if self.detect_cycle_util(process, visited, rec_stack, []):
                    return
        messagebox.showinfo("No Deadlock", "No deadlock detected!")

    def get_graph(self):
        """Returns the graph for visualization"""
        return self.graph
