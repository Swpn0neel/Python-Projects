import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("600x400")

        # create a text widget
        self.text = tk.Text(self.root, wrap='word')
        self.text.pack(fill='both', expand=True)

        # create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # create file menu
        self.file_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='New', command=self.new_file)
        self.file_menu.add_command(label='Open', command=self.open_file)
        self.file_menu.add_command(label='Save', command=self.save_file)
        self.file_menu.add_command(label='Save as', command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.root.quit)

    def new_file(self):
        self.text.delete(1.0, 'end')

    def open_file(self):
        file = filedialog.askopenfile(mode='r', defaultextension=".txt")
        if file:
            contents = file.read()
            self.text.delete(1.0, 'end')
            self.text.insert('insert', contents)

    def save_file(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file:
            data = self.text.get(1.0, 'end')
            file.write(data)
            file.close()
            messagebox.showinfo("Notepad", "File saved successfully")

    def save_as_file(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file:
            data = self.text.get(1.0, 'end')
            file.write(data)
            file.close()
            messagebox.showinfo("Notepad", "File saved successfully")

if __name__ == '__main__':
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()