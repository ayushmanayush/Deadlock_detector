import networkx as nx
import matplotlib.pyplot as plt
from tkinter import messagebox

def visualize_graph(graph):
    """Draws the process wait-for graph"""
    if not graph:
        messagebox.showinfo("Graph Empty", "No dependencies to visualize.")
        return
    
    G = nx.DiGraph(graph)
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='red', arrows=True)
    plt.title("Wait-For Graph")
    plt.show()
