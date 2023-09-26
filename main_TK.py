import tkinter as tk


class Window:
    def __init__(self, root):
        self.root = root
        self.root.title('Tournament maker')

        # Create a label to display messages
        self.label = tk.Label(root, text="Hello, Tkinter!")
        self.label.pack(pady=10)

        # Create a button to change the message
        self.button = tk.Button(
            root, text="Change Message", command=self.change_message)
        self.button.pack()

    def change_message(self):
        self.label.config(text="Button Clicked!")


def main():
    # Create the main Tkinter window
    root = tk.Tk()

    # Create an instance of our application class
    app = Window(root)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
