import tkinter as tk
light_grey = "#f5f5f5"


class calcelator:
    def _init_(self):
        self.window = tk.tk()
        self.window.geometry("357x667")
        self.window.resizable(00)
        self.window.title("calculater")
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_exprertion = "0"
        self.curunt_exprertion = "0"

        def create_displyay_frame(self):
            frame = tk.Frame(self.window, height=221, bg=light_grey)
            frame.pack(expand=True, fill="both")
            return frame

            def create_buttons_frame(self):
                frame = tk.Frame(self.window)
            frame.pack(expand=True, fill="both")
            return frame

    def run(self):
        self.window.mainloop()

        if __name__ == "_main_":
            calc = calcelator
            calc.run()
