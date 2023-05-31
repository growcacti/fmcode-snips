import os
import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()

path = "/home/jh/Desktop"


nodes = dict()
frame = tk.Frame(root)
tree = ttk.Treeview(frame)
ysb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
xsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
tree.configure(yscroll=ysb.set, xscroll=xsb.set)
tree.heading("#0", text="Project tree", anchor="w")

tree.grid()
ysb.grid(row=0, column=1, sticky="ns")
xsb.grid(row=1, column=0, sticky="ew")
frame.grid()

abspath = os.path.abspath(path)
insert_node("", abspath, abspath)
tree.bind("<<TreeviewOpen>>", open_node)


def insert_node(parent, text, abspath):
    node = tree.insert(parent, "end", text=text, open=False)
    if os.path.isdir(abspath):
        nodes[node] = abspath
        tree.insert(node, "end")


def open_node(event):
    node = tree.focus()
    abspath = nodes.pop(node, None)
    if abspath:
        tree.delete(tree.get_children(node))
        for p in os.listdir(abspath):
            insert_node(node, p, os.path.join(abspath, p))


if __name__ == "__main__":

    insert_node()
    open_node()

    root.mainloop()
