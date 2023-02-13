import tkinter as tk
import random
import time

class TargetPractice:
    def __init__(self, master):
        self.master = master
        self.master.title("Target Practice")
        self.master.geometry("600x400")

        self.target_x = random.randint(50, 550)
        self.target_y = random.randint(50, 350)
        self.hit = False
        self.score = 0
        self.start_time = time.time()
        self.game_over = False

        self.canvas = tk.Canvas(self.master, width=600, height=400)
        self.canvas.pack()
        self.draw_target()

        self.canvas.bind("<Button-1>", self.check_hit)

    def draw_target(self):
        self.canvas.create_oval(self.target_x - 25, self.target_y - 25, self.target_x + 25, self.target_y + 25, fill="red")
        self.canvas.create_oval(self.target_x - 20, self.target_y - 20, self.target_x + 20, self.target_y + 20, fill="white")
        self.canvas.create_oval(self.target_x - 15, self.target_y - 15, self.target_x + 15, self.target_y + 15, fill="red")
        self.canvas.create_oval(self.target_x - 10, self.target_y - 10, self.target_x + 10, self.target_y + 10, fill="white")
        self.canvas.create_oval(self.target_x - 5, self.target_y - 5, self.target_x + 5, self.target_y + 5, fill="red")

    def check_hit(self, event):
        if not self.hit:
            x_diff = event.x - self.target_x
            y_diff = event.y - self.target_y
            distance = (x_diff ** 2 + y_diff ** 2) ** 0.5
            if distance <= 25:
                self.hit = True
                self.score += 1
                self.canvas.create_text(300, 200, text="Hit!", font=("Helvetica", 24))
                self.master.after(1000, self.new_target)

    def new_target(self):
        self.hit = False
        self.canvas.delete("all")
        self.target_x = random.randint(50, 550)
        self.target_y = random.randint(50, 350)
        self.draw_target()

        current_time = time.time()
        elapsed_time = current_time - self.start_time
        if elapsed_time >= 30:
            self.game_over = True
            self.canvas.create_text(300, 200, text="Game Over\nScore: {}".format(self.score), font=("Helvetica", 24))
        else:
            self.master.after(100, self.check_time)

    def check_time(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        if elapsed_time >= 30 and not self.game_over:
            self.game_over = True
            self.canvas.create_text(300, 200, text="Game Over\nScore: {}".format(self.score), font=("Helvetica", 24))

if __name__ == "__main__":
    root = tk.Tk()
    game = TargetPractice(root)
    root.mainloop()
