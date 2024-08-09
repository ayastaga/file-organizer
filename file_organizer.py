from tkinter import *
from tkinter import ttk, scrolledtext, filedialog, PhotoImage, messagebox
from config import *
import utils
import os
import shutil

class FileOrganizer:
    def __init__(self, master):
        self.master = master
        self.master.title(WINDOW_TITLE)
        self.master.geometry(WINDOW_SIZE)
        self.master.resizable(False, False)
        self.master.configure(background=WINDOW_BG)

        self.path = ""
        self.folder_selected = False
        self.log_dict = {1: [], 2: [], 3: [], 4: [], 5: []}
        self.counting = 0

        self.create_frames()
        self.create_widgets()
        self.setup_main_screen()

    def create_frames(self):
        self.main_loading_screen = Frame(self.master, bg=WINDOW_BG)
        self.options_frame = Frame(self.master, bg=WINDOW_BG)
        self.type_frame = Frame(self.master, bg=WINDOW_BG)
        self.loading_frame = Frame(self.master, bg=WINDOW_BG)
        self.customize_frame_a = Frame(self.master, bg=WINDOW_BG)
        self.customize_frame_b = Frame(self.master, bg=WINDOW_BG)

    def create_widgets(self):
        self.create_options_widgets()
        self.create_type_widgets()
        self.create_custom_widgets()
        self.create_loading_widgets()

    def setup_main_screen(self):
        self.main_loading_screen.pack()
        self.home_frame_photo = PhotoImage(file="home_frame.png")
        self.home_frame = Label(self.main_loading_screen, image=self.home_frame_photo, bg=WINDOW_BG)
        self.home_frame.pack()
        self.master.after(1500, self.load_main)

    def create_options_widgets(self):
        self.options_title = Label(self.options_frame, text="1. choose\nyour files", font=TITLE_FONT, bg=WINDOW_BG, justify="left")
        self.open_btn = Button(self.options_frame, text="select folder", command=self.open_file_dialog, font=BUTTON_FONT, width=20, height=1, bg="black", fg="white")
        self.selected_file_lbl = Label(self.options_frame, text="Selected File: ")
        self.file_text = scrolledtext.ScrolledText(self.options_frame, wrap="none", height=11, width=30, undo=True, font=TEXT_FONT)
        self.next_btn = Button(self.options_frame, text="next", command=self.submitted, font=BUTTON_FONT, width=20, height=1, bg="black", fg="white")

    def create_type_widgets(self):
        self.type_title = Label(self.type_frame, text="2. choose how\nto organize", font=TITLE_FONT, bg=WINDOW_BG)
        self.file_type_btn = Button(self.master, text="by file type", font=BUTTON_FONT_2, width=17, bg="#D9D9D9", command=self.org_by_type)
        self.ext_type_btn = Button(self.master, text="by ext type", font=BUTTON_FONT_2, width=17, bg="#E7E7E7", command=self.org_by_ext)
        self.customize_btn = Button(self.master, text="customize", font=BUTTON_FONT_2, width=17, bg="#F8F8F8", command=self.custom_type)
        self.folder_img = PhotoImage(file="folder.png").zoom(1, 1)
        self.folder_lbl = Label(self.type_frame, image=self.folder_img, bg=WINDOW_BG)
        
    def create_custom_widgets(self):
        self.custom_title = Label(self.customize_frame_a, text="let's customize", font=TITLE_FONT, bg=WINDOW_BG, justify="left")
        self.subheading = Label(self.customize_frame_a, text="> add upto 5 groups", font=BUTTON_FONT, width=20, height=1, bg=WINDOW_BG, fg="black")
        self.btn_2_frame = Frame(self.customize_frame_a, bg=WINDOW_BG)
        self.whitespace_1 = Label(self.btn_2_frame, text=" ", bg=WINDOW_BG)
        self.btn_frame = Frame(self.btn_2_frame, bg=WINDOW_BG)
        self.button_1 = Button(self.btn_frame, text="N/A", command=lambda: self.frame_b(1), font=("Algol", 12), width=22, height=2)
        self.button_2 = Button(self.btn_frame, text="N/A", command=lambda: self.frame_b(2), font=("Algol", 12), width=22, height=2)
        self.button_3 = Button(self.btn_frame, text="N/A", command=lambda: self.frame_b(3), font=("Algol", 12), width=22, height=2)
        self.button_4 = Button(self.btn_2_frame, text="N/A", command=lambda: self.frame_b(4), font=("Algol", 12), width=22, height=2)
        self.button_5 = Button(self.btn_2_frame, text="N/A", command=lambda: self.frame_b(5), font=("Algol", 12), width=22, height=2)
        self.details = Label(self.btn_2_frame, text="all your files will be organized into these groups. you decide how files will be seperated.", font=BUTTON_FONT, width=9, wraplength=100, bg=WINDOW_BG, fg="black", justify="left")
        self.custom_done_btn = Button(self.btn_2_frame, text="done", command=self.done_task, font=BUTTON_FONT, width=9, height=1, bg="black", fg="white")
        self.custom_cancel_btn = Button(self.btn_2_frame, text="cancel", command=self.cancel_task, font=BUTTON_FONT, width=9, height=1, bg="black", fg="white")

        self.button_menu_title = Label(self.customize_frame_b, text="folder type", font=TITLE_FONT, bg=WINDOW_BG, justify="left")
        self.white_space = Label(self.customize_frame_b, text="   ", bg=WINDOW_BG)
        self.entry_frame = Frame(self.customize_frame_b, bg=WINDOW_BG)
        self.name_var = StringVar()
        self.folder_name_lbl = Label(self.entry_frame, text="folder name:", font=BUTTON_FONT, height=2, bg=WINDOW_BG, fg="black")
        self.folder_entry = Entry(self.entry_frame, textvariable=self.name_var, width=27)
        self.key_var = StringVar()
        self.keyword_lbl = Label(self.entry_frame, text="keywords:", font=BUTTON_FONT, height=2, bg=WINDOW_BG, fg="black")
        self.keyword_entry = Entry(self.entry_frame, textvariable=self.key_var, width=27)
        self.ext_var = StringVar()
        self.ext_lbl = Label(self.entry_frame, text="ext type:", font=BUTTON_FONT, height=2, bg=WINDOW_BG, fg="black")
        self.ext_entry = Entry(self.entry_frame, textvariable=self.ext_var, width=27)
        self.custom_done_btn_b = Button(self.customize_frame_b, text="done", command=self.save_b, font=BUTTON_FONT, width=9, height=1, bg="black", fg="white")
        self.custom_close_btn_b = Button(self.customize_frame_b, text="close", command=self.close_b, font=BUTTON_FONT, width=9, height=1, bg="black", fg="white")

    def create_loading_widgets(self):
        self.text_1 = Label(self.loading_frame, text="organizing your files...", font=LOADING_FONT, bg=WINDOW_BG, justify="left")
        self.text_2 = Label(self.loading_frame, text="almost there...", font=LOADING_FONT, bg=WINDOW_BG, justify="left")
        self.text_3 = Label(self.loading_frame, text="we're done",  font=LOADING_FONT, bg=WINDOW_BG, justify="left")
        self.home_btn = Button(self.loading_frame, text="Return home", command=self.go_home, font=BUTTON_FONT, bg="black", fg="white", justify="left")

    def open_file_dialog(self):
        file_path = filedialog.askdirectory(title="Select a File")
        if file_path:
            self.selected_file_lbl.config(text=f"Selected File: {file_path}")
            self.process_file(file_path)

    def process_file(self, file_path):
        self.path = file_path
        original_path = file_path
        
        if not os.path.exists(f"{original_path}_copy"):
            self.path = utils.copy_folder(original_path)
        else:
            self.path = f"{original_path}_copy"
            utils.delete_files(self.path)
            utils.copy_folder_contents(original_path, self.path)
    
        try:
            self.file_text.configure(state=NORMAL)
            self.file_text.delete('1.0', END)
            self.file_text.insert(END, "\n  Preview of files within this directory:\n\n")
            for filename in os.listdir(file_path):
                self.file_text.insert(END, f"  > {filename}\n")
            self.file_text.configure(state=DISABLED)
        
            self.folder_selected = True
        except Exception as e:
            self.selected_file_lbl.config(text=f"Error: {str(e)}")

    def submitted(self):
        if self.folder_selected:
            self.type_title.pack()
            self.folder_lbl.pack()
            self.options_frame.pack_forget()
            self.type_frame.pack(fill="both", expand=1)
            self.file_type_btn.place(x=20, y=214)
            self.ext_type_btn.place(x=51, y=289)
            self.customize_btn.place(x=92, y=373)

    def forget_type(self):
        self.type_frame.pack_forget()
        self.file_type_btn.place_forget()
        self.ext_type_btn.place_forget()
        self.customize_btn.place_forget()

    def load_first_txt(self):
        self.loading_frame.pack()
        self.text_1.config(fg="black")
        self.text_2.config(fg="#B3B3B3")
        self.text_3.config(fg="#E9E9E9")
        self.text_1.pack(pady=20, padx=20, anchor="w")
        self.text_2.pack(pady=20, padx=20, anchor="w")
        self.text_3.pack(pady=20, padx=20, anchor="w")

    def load_second_txt(self):
        self.text_2.config(fg="black")
        self.text_3.config(fg="#B3B3B3")

    def load_third_txt(self):
        self.text_3.config(fg="black")
        self.home_btn.pack(pady=20, padx=20, anchor="w")

    def org_by_ext(self):
        utils.organize_by_extension(self.path)
        self.forget_type()
        self.load_first_txt()
        self.master.after(2000, self.load_second_txt)
        self.master.after(4900, self.load_third_txt)

    def org_by_type(self):
        utils.organize_by_type(self.path, FILE_TYPE_LIST)
        self.forget_type()
        self.load_first_txt()
        self.master.after(2000, self.load_second_txt)
        self.master.after(4900, self.load_third_txt)

    def go_home(self):
        self.loading_frame.pack_forget()
        self.options_frame.pack()
        self.file_text.delete('1.0', END)

    def custom_type(self):
        self.forget_type()
        self.customize_frame_a.pack()
        self.custom_title.pack()
        self.subheading.pack()
        self.btn_2_frame.pack()
        self.whitespace_1.grid(row=0, column=0, columnspan=2)
        self.button_1.pack()
        self.button_2.pack()
        self.button_3.pack()
        self.btn_frame.grid(row=1, column=1, padx=20, sticky=NW)
        self.button_4.grid(row=2, column=1)
        self.button_5.grid(row=3, column=1)
        self.details.grid(row=1, column=2, sticky=W)
        self.custom_done_btn.grid(row=2, column=2, sticky=W)
        self.custom_cancel_btn.grid(row=3, column=2, sticky=W)

    def frame_b(self, val):
        self.counting = val
        self.customize_frame_a.pack_forget()
        self.customize_frame_b.pack()
        
        self.button_menu_title.pack(fill="both", expand=1)
        self.white_space.pack(fill="both", expand=1)
        
        self.entry_frame.config(highlightbackground="black", highlightthickness=1)
        self.entry_frame.pack(fill="both", expand=1, pady=10)
        
        self.folder_name_lbl.grid(row=0, column=0, sticky=E, padx=10, pady=10)
        self.folder_entry.grid(row=0, column=1, sticky=W)

        self.keyword_lbl.grid(row=1, column=0, sticky=E, padx=10, pady=10)
        self.keyword_entry.grid(row=1, column=1, sticky=W)
        
        self.ext_lbl.grid(row=2, column=0, sticky=E, padx=10, pady=10)
        self.ext_entry.grid(row=2, column=1, sticky=W)
        
        self.customize_frame_b.config(bg="red")
        self.custom_done_btn_b.pack(fill="y", expand=1, pady=30, padx=0, side=LEFT)
        self.custom_done_btn_b.config(bg=WINDOW_BG, fg="black")
        self.custom_close_btn_b.pack(fill="y", expand=1, pady=30, padx=0, side=RIGHT)
        self.custom_close_btn_b.config(bg=WINDOW_BG, fg="black")

    def close_b(self):
        self.name_var.set("")
        self.ext_var.set("")
        self.key_var.set("")
        self.customize_frame_b.pack_forget()
        self.customize_frame_a.pack()

    def save_b(self):
        folder_name = self.name_var.get()
        ext_type = self.ext_var.get().replace(' ', '').split(',')
        keyword_include = self.key_var.get().replace(' ', '').split(',')

        if folder_name.replace(' ', '') == '':
            messagebox.showwarning(title="Invalid input", message="Enter a valid group name or else it won't be saved")
            return
        
        if ext_type != ['']:
            for elem in ext_type:
                if elem not in EXTENSION_LIST:
                    messagebox.showerror(title="Invalid input", message=f"Error: {elem} is not a valid extension")
                    self.ext_var.set("")
                    return
            
        button = getattr(self, f"button_{self.counting}")
        button.config(text=folder_name)

        self.log_dict[self.counting] = [folder_name, ext_type, keyword_include]
        
        self.name_var.set("")
        self.ext_var.set("")
        self.key_var.set("")
            
        self.customize_frame_b.pack_forget()
        self.customize_frame_a.pack()
        self.btn_2_frame.pack()

    def org_by_custom(self):
        utils.organize_by_custom(self.path, self.log_dict)

    def done_task(self):
        messagebox.showinfo("Ordering", message="Note that the files will be sorted based on chronological order")
        self.org_by_custom()

        self.customize_frame_a.pack_forget()    
        self.load_first_txt()
        self.master.after(2000, self.load_second_txt)
        self.master.after(4900, self.load_third_txt)

    def cancel_task(self):
        if self.counting > 1:
            button = getattr(self, f"button_{self.counting}")
            button.config(text="N/A")
            if self.counting <= 3:
                button.pack_forget()
            else:
                button.grid_forget()
        self.customize_frame_a.pack_forget()
        self.submitted()

    def load_main(self):
        self.main_loading_screen.pack_forget()
        self.home_frame.pack_forget()
        self.options_frame.pack()
        self.options_title.pack()
        Label(self.options_frame, bg=WINDOW_BG).pack()
        self.open_btn.pack(expand=1)
        self.file_text.pack(padx=10, pady=10)
        Label(self.options_frame, bg=WINDOW_BG).pack()
        self.next_btn.pack()