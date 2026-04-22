import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator App")
        self.root.geometry("360x420")
        self.root.resizable(False, False)

        self.current_expression = ""
        self.result_var = tk.StringVar(value="0")

        self._build_ui()

    def _build_ui(self):
        title = tk.Label(
            self.root,
            text="Python Calculator",
            font=("Segoe UI", 16, "bold"),
            pady=10,
        )
        title.pack()

        display = tk.Entry(
            self.root,
            textvariable=self.result_var,
            font=("Segoe UI", 20),
            justify="right",
            bd=8,
            relief="ridge",
        )
        display.pack(fill="x", padx=12, pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both", padx=12, pady=8)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "%", "+"],
            ["C", "DEL", "^", "="],
        ]

        for r, row in enumerate(buttons):
            button_frame.grid_rowconfigure(r, weight=1)
            for c, value in enumerate(row):
                button_frame.grid_columnconfigure(c, weight=1)
                btn = tk.Button(
                    button_frame,
                    text=value,
                    font=("Segoe UI", 14, "bold"),
                    command=lambda v=value: self.on_button_click(v),
                )
                btn.grid(row=r, column=c, sticky="nsew", padx=4, pady=4)

    def on_button_click(self, value):
        if value == "C":
            self.current_expression = ""
            self.result_var.set("0")
            return

        if value == "DEL":
            self.current_expression = self.current_expression[:-1]
            self.result_var.set(self.current_expression or "0")
            return

        if value == "=":
            self._calculate_result()
            return

        if value == "^":
            value = "**"

        self.current_expression += value
        self.result_var.set(self.current_expression)

    def _calculate_result(self):
        if not self.current_expression.strip():
            return

        try:
            # Evaluate arithmetic input in a restricted environment.
            result = eval(self.current_expression, {"__builtins__": {}}, {})
            self.current_expression = str(result)
            self.result_var.set(self.current_expression)
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Division or modulo by zero is not allowed.")
        except Exception:
            messagebox.showerror("Input Error", "Invalid expression. Please try again.")


def main():
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
