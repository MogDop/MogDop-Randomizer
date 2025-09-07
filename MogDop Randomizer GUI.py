import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class MogDopRandomizerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MogDop Randomizer")
        self.geometry("350x320")
        self.resizable(False, False)

        tk.Label(self, text="MogDop Randomizer", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Button(self, text="Number Randomizer", width=25, command=self.num_randomizer).pack(pady=5)
        tk.Button(self, text="Word Randomizer", width=25, command=self.word_randomizer).pack(pady=5)
        tk.Button(self, text="Dice Roller", width=25, command=self.dice_roller).pack(pady=5)
        tk.Button(self, text="Exit", width=25, command=self.destroy).pack(pady=20)
        self.result_label = tk.Label(self, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=5)

    def num_randomizer(self):
        try:
            lower = simpledialog.askinteger("Number Randomizer", "Enter the lower bound:")
            if lower is None:
                return
            upper = simpledialog.askinteger("Number Randomizer", "Enter the upper bound:")
            if upper is None:
                return
            if upper < lower:
                messagebox.showerror("Error", "Upper bound must be >= lower bound!")
                return
            result = random.randint(lower, upper)
            self.result_label.config(text=f"Random number: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def word_randomizer(self):
        words_input = simpledialog.askstring("Word Randomizer", "Enter words separated by commas:")
        if words_input is None:
            return
        words = [w.strip() for w in words_input.split(",") if w.strip()]
        if not words:
            messagebox.showerror("Error", "Please enter at least one word!")
            return
        result = random.choice(words)
        self.result_label.config(text=f"Random word: {result}")

    def dice_roller(self):
        try:
            num_dice = simpledialog.askinteger("Dice Roller", "Number of dice (1-100):", minvalue=1, maxvalue=100)
            if num_dice is None:
                return
            num_sides = simpledialog.askinteger("Dice Roller", "Sides per die (2-1000):", minvalue=2, maxvalue=1000)
            if num_sides is None:
                return
            rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
            result = ", ".join(map(str, rolls))
            self.result_label.config(text=f"Rolls: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = MogDopRandomizerGUI()
    app.mainloop()