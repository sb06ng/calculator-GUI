import tkinter as tk

import logic

FONT = "Arial"
BACKGROUND_COLOR = "white"
CALCULATOR_COLOR = "blue"
BUTTON_COLOR = "YELLOW"
CALCULATOR_WIDTH = 700
CALCULATOR_HEIGHT = 700
EQUATION_FONT_SIZE = int(CALCULATOR_HEIGHT / 10)
PADDING = 2
BUTTONS_LAYOUT = [
    ['pow', '<-', '(', ')', '/', ','],
    ['tan', '7', '8', '9', '*'],
    ['sin', '4', '5', '6', '-'],
    ['fac', '1', '2', '3', '+'],
    ['sqrt', '.', '0', 'C', '='],
]
BUTTON_HEIGHT = lambda canvas_h: canvas_h / len(BUTTONS_LAYOUT)
BUTTON_WIDTH = lambda canvas_w: canvas_w / len(BUTTONS_LAYOUT[0])


class Calculator:
    def __init__(self, master):
        self.button_canvas = None
        self.root = master
        self.root.title("Calculator-GUI")
        self.root.geometry(f"{CALCULATOR_WIDTH}x{CALCULATOR_HEIGHT}")
        self.root.configure(background=BACKGROUND_COLOR)
        self.root.resizable(False, False)

        # create the area where the equation exist
        self.equation = tk.StringVar()
        self.entry = tk.Entry(
            master,
            width=CALCULATOR_WIDTH,
            font=(FONT, EQUATION_FONT_SIZE),
            textvariable=self.equation
        )
        self.entry.pack(side="top", fill="x")

        self.root.update()
        canvas_h = CALCULATOR_HEIGHT - self.entry.winfo_height()

        self.create_button_grid(CALCULATOR_WIDTH, canvas_h)

    def create_button_grid(self, w, h):
        self.button_canvas = tk.Canvas(
            self.root,
            width=w,
            height=h,
            background=CALCULATOR_COLOR,
            highlightthickness=0,
            borderwidth=0
        )
        self.button_canvas.pack(side="top", fill="both")

        for row, buttons_list in enumerate(BUTTONS_LAYOUT):
            for column, label in enumerate(buttons_list):
                self.create_button(label, row, column)

    def create_button(self, text, row, column):
        btn = tk.Button(
            self.button_canvas,
            text=text,
            bg=BUTTON_COLOR,
            font=(FONT, 14),
            padx=PADDING,
            pady=PADDING,
            command=lambda: self.on_button_click(text)

        )
        btn.grid(row=row, column=column)

    def on_button_click(self, value):
        if value == "C":
            self.equation.set("")
        elif value == "=":
            self.equation.set(logic.calculate(self.equation.get()))
        elif value == "<-":
            self.equation.set(self.equation.get()[:-1])
        else:
            self.equation.set(self.equation.get() + value)


if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
