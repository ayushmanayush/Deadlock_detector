import tkinter as tk
from tkinter import messagebox
from deadlock_detector import DeadlockDetector
from graph_visuals import visualize_graph

class DeadlockGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Deadlock Detection Tool")

        # User enters the number of processes
        self.process_label = tk.Label(root, text="Enter Number of Processes:")
        self.process_label.pack()
        
        self.process_entry = tk.Entry(root)
        self.process_entry.pack()
        
        self.set_process_button = tk.Button(root, text="Set Processes", command=self.set_processes)
        self.set_process_button.pack()

        # Dependency input field (Hidden initially)
        self.dep_label = tk.Label(root, text="Enter Process Dependencies (P1 P2):")
        self.dep_entry = tk.Entry(root)
        self.add_button = tk.Button(root, text="Add Dependency", command=self.add_dependency)
        
        self.detect_button = tk.Button(root, text="Detect Deadlock", command=self.detect_deadlock)
        self.visual_button = tk.Button(root, text="Visualize Graph", command=self.visualize_graph)

        self.detector = None  # Detector is created after setting processes

    def set_processes(self):
        """Sets the number of processes based on user input"""
        try:
            num_processes = int(self.process_entry.get())
            if num_processes <= 0:
                raise ValueError("Number of processes must be greater than 0.")
            
            self.detector = DeadlockDetector(num_processes)
            messagebox.showinfo("Success", f"Number of processes set to {num_processes}")

            # Show dependency input fields
            self.dep_label.pack()
            self.dep_entry.pack()
            self.add_button.pack()
            self.detect_button.pack()
            self.visual_button.pack()

        except ValueError:
            messagebox.showerror("Error", "Enter a valid positive integer for processes.")

    def add_dependency(self):
        """Handles user input to add dependencies"""
        if not self.detector:
            messagebox.showerror("Error", "Set the number of processes first!")
            return

        try:
            p1, p2 = map(int, self.dep_entry.get().split())
            self.detector.add_edge(p1, p2)
            messagebox.showinfo("Success", f"Dependency Added: {p1} -> {p2}")
        except ValueError:
            messagebox.showerror("Error", "Invalid Input! Enter two space-separated integers.")

    def detect_deadlock(self):
        """Calls deadlock detection if processes are set"""
        if not self.detector:
            messagebox.showerror("Error", "Set the number of processes first!")
            return
        self.detector.detect_deadlock()

    def visualize_graph(self):
        """Calls visualization if processes are set"""
        if not self.detector:
            messagebox.showerror("Error", "Set the number of processes first!")
            return
        visualize_graph(self.detector.get_graph())
