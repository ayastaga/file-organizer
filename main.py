import tkinter as tk
from file_organizer import FileOrganizer

def main():
    root = tk.Tk()
    app = FileOrganizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()