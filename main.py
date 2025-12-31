import tkinter as tk

CALCULATOR_WIDTH = 400
CALCULATOR_HEIGHT = 700
EQUATION_FONT_SIZE = int(CALCULATOR_HEIGHT / 10)
PADDING = 2
BUTTONS_LAYOUT = [
            '(',')','tan(','sin(',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
COLUMNS_NUMBER = 4
ROWS_NUMBER = len(BUTTONS_LAYOUT) // COLUMNS_NUMBER


class Calculator:
    def __init__(self, master):
        self.root = master
        self.root.title("Calculator-GUI")
        self.root.geometry(f"{CALCULATOR_WIDTH}x{CALCULATOR_HEIGHT}")
        self.root.configure(background="gray")
        self.root.resizable(False, False)

        # create the area where the equation exist
        self.equation = tk.StringVar()
        self.entry = tk.Entry(
            master,
            width=CALCULATOR_WIDTH,
            font=('Arial', EQUATION_FONT_SIZE),
            textvariable=self.equation
        )
        self.entry.pack(side="top", fill="x")

        self.root.update()
        print(self.entry.winfo_height().real)
        canvas_h = CALCULATOR_HEIGHT - self.entry.winfo_height()

        self.button_canvas = tk.Canvas(
            master,
            width=CALCULATOR_WIDTH,
            height=canvas_h,
            background="pink",
            highlightthickness=0,
            borderwidth=0
        )
        self.button_canvas.pack(side="top", fill="both")

        self.create_button_grid(CALCULATOR_WIDTH,canvas_h)


    def create_button_grid(self,w,h):
        btn_w = w // COLUMNS_NUMBER
        btn_h = h //ROWS_NUMBER

        for i, label in enumerate(BUTTONS_LAYOUT):
            col = i % COLUMNS_NUMBER
            row = i // COLUMNS_NUMBER

            x_pos = col * btn_w
            y_pos = row * btn_h

            btn = tk.Button(
                self.button_canvas,
                text=label,
                bg="white",
                font=("Ariel", 14, "bold"),
                command=lambda l=label: self.on_button_click(l)
            )

            self.button_canvas.create_window(
                x_pos + PADDING,
                y_pos + PADDING,
                window=btn,
                anchor="nw",
                width=btn_w - (PADDING * 2),
                height=btn_h - (PADDING * 2)
            )


    def on_button_click(self, value):
        if value == "C":
            self.equation.set("")
        else:
            self.equation.set(self.equation.get() + value)



if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()