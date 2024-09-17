from tkinter import Tk, PhotoImage, Label, Entry, Button, StringVar, ttk, font, OptionMenu
from collections import Counter

algorithms = ("ASCII", "HUFFMAN", "BINARY")

class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def __str__(self):
        return self.left, self.right


def huffman_code_tree(node, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, binString + '0'))
    d.update(huffman_code_tree(r, binString + '1'))
    return d


def make_tree(nodes):
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    return nodes[0][0]


def ascii_convert():
    nums = [ord(c) for c in my_text.get()]
    final = sum(nums) % 1000
    my_str = str(final)
    label_var.set(my_str)


def binary_convert():
    nums = [format(ord(c), 'b') for c in my_text.get()]
    ints = [int(c) for c in nums]
    final = sum(ints) % 1000
    my_str = str(final)
    label_var.set(my_str)


def huffman_convert():
    if not my_text.get().isalpha():
        error_str.set("ERROR: THIS ALGORITHM ONLY SUPPORTS ALPHABETICAL CHARACTERS")
        return
    else:
        string = my_text.get()
        freq = dict(Counter(string))
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        node = make_tree(freq)
        encoding = huffman_code_tree(node)
        final = 0
        for i in encoding:
            final += ord(i)
        final = final % 1000
        my_str = str(final)
        label_var.set(my_str)


def handle_button_press(event=None):
    error_str.set("")
    if current_algorithm.get() == "ASCII":
        ascii_convert()
    elif current_algorithm.get() == "HUFFMAN":
        huffman_convert()
    elif current_algorithm.get() == "BINARY":
        binary_convert()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    window = Tk()
    window.title("Baseball Encoder")
    # window.geometry('400x150')
    window.call("wm", "iconphoto", window._w, PhotoImage(file="icon.png"))
    window.resizable(0, 0)

    title_label = Label(window, text="Enter A Word")
    title_label.grid(row=0, column=0, pady=10)

    my_text = Entry(window, width=50)
    my_text.grid(row=1, column=0, padx=10 , pady=5)

    button = Button(text="Get Value", command=handle_button_press)

    button.grid(row=2, column=0, pady=15)

    label_var = StringVar()
    label_var.set("")
    my_label = Label(window,
                     textvariable=label_var,
                     )
    my_label.grid(row=3, column=0, pady=10)

    window.bind('<Return>', handle_button_press)

    algos_label = Label(window, text="Algorithms:", font=('Arial', 9))
    algos_label.grid(row=0, column=1, padx=10)

    algos = algorithms
    current_algorithm = StringVar(value="ASCII")
    algos_options = OptionMenu(window, current_algorithm, *algos)
    algos_options.grid(row=1, column=1, padx=10)

    error_str = StringVar()
    error_label = Label(window, textvariable=error_str, fg='red')
    error_label.grid(row=4, column=0)

    # Start the event loop.
    window.mainloop()

