import customtkinter as ctk
import tkinter as tk

from PIL import Image, ImageTk

# Pages

## profile
class profile_p(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.new_frame_status = False

        # Full Screen Code
        pad=3
        self._geom='500x600+0+0'
        controller.geometry("{0}x{1}+0+0".format(
            controller.winfo_screenwidth()-pad, controller.winfo_screenheight()-pad))
        controller.bind('<F11>', self.toggle_geom)

        menu_top_frame = ctk.CTkFrame(self)
        menu_top_frame.pack(side='top', fill='x', expand=False)

    def toggle_geom(self, event):
        if self.new_frame_status:
            self.controller.geometry(self._geom)
        else:
            self._geom = self.controller.geometry()
            self.controller.geometry("{0}x{1}+0+0".format(
                self.controller.winfo_screenwidth() - 3, self.controller.winfo_screenheight() - 3))
        self.new_frame_status = not self.new_frame_status

## library
class library_p(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.new_frame_status = False

        # Full Screen Code
        pad=3
        self._geom='500x600+0+0'
        controller.geometry("{0}x{1}+0+0".format(
            controller.winfo_screenwidth()-pad, controller.winfo_screenheight()-pad))
        controller.bind('<F11>', self.toggle_geom)

        menu_top_frame = ctk.CTkFrame(self)
        menu_top_frame.pack(side='top', fill='x', expand=False)

    def toggle_geom(self, event):
        if self.new_frame_status:
            self.controller.geometry(self._geom)
        else:
            self._geom = self.controller.geometry()
            self.controller.geometry("{0}x{1}+0+0".format(
                self.controller.winfo_screenwidth() - 3, self.controller.winfo_screenheight() - 3))
        self.new_frame_status = not self.new_frame_status

## shop
class shop_p(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.new_frame_status = False

        # Full Screen Code
        pad=3
        self._geom='500x600+0+0'
        controller.geometry("{0}x{1}+0+0".format(
            controller.winfo_screenwidth()-pad, controller.winfo_screenheight()-pad))
        controller.bind('<F11>', self.toggle_geom)

        menu_top_frame = ctk.CTkFrame(self)
        menu_top_frame.pack(side='top', fill='x', expand=False)

    def toggle_geom(self, event):
        if self.new_frame_status:
            self.controller.geometry(self._geom)
        else:
            self._geom = self.controller.geometry()
            self.controller.geometry("{0}x{1}+0+0".format(
                self.controller.winfo_screenwidth() - 3, self.controller.winfo_screenheight() - 3))
        self.new_frame_status = not self.new_frame_status

## main
class main_p(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.new_frame_status = False

        # Full Screen
        pad=3
        self._geom='500x600+0+0'
        controller.geometry("{0}x{1}+0+0".format(
            controller.winfo_screenwidth()-pad, controller.winfo_screenheight()-pad))
        controller.bind('<F11>', self.toggle_geom)

        # OBJ

        # Menu Top Frame
        menu_top_frame = ctk.CTkFrame(self)
        menu_top_frame.pack(side='top', fill='x', expand=False)

        # Menu Top Frame OBJs

        main_p_btn = ctk.CTkButton(menu_top_frame, text='main')
        main_p_btn.pack(side='left', fill='x', expand=False)

        library_p_btn = ctk.CTkButton(menu_top_frame, text='library')
        library_p_btn.pack(side='left', fill='x', expand=False)

        shop_p_btn = ctk.CTkButton(menu_top_frame, text='shop')
        shop_p_btn.pack(side='left', fill='x', expand=False)

        profile_p_btn = ctk.CTkButton(menu_top_frame, text='profile')
        profile_p_btn.pack(side='left', fill='x', expand=False)

    # Func Full Screen
    def toggle_geom(self, event):
        if self.new_frame_status:
            self.controller.geometry(self._geom)
        else:
            self._geom = self.controller.geometry()
            self.controller.geometry("{0}x{1}+0+0".format(
                self.controller.winfo_screenwidth() - 3, self.controller.winfo_screenheight() - 3))
        self.new_frame_status = not self.new_frame_status

## WelcomePage
class WelcomePage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Welcome')
        self.geometry('400x300')

        p1 = tk.PhotoImage(file="./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.iconphoto(False, p1)

        self.image = Image.open("./assets/logo/favicon/opengmaezone-website-favicon-color.png")

        self.image = self.image.resize((128, 128), Image.ANTIALIAS)

        self.photo = ImageTk.PhotoImage(self.image)

        self.label = ctk.CTkLabel(self, image=self.photo, text='')
        self.label.pack(pady=20)

        self.welcome_label = ctk.CTkLabel(self, text='Welcome\nOpenGameZone', font=('roboto', 25))
        self.welcome_label.pack()

        self.after(5000, self.close_welcome)

    def close_welcome(self):
        self.destroy()
        self.open_main_app()

    def open_main_app(self):
        app = Frame_ch()
        app.mainloop()

# Frame Changer
class Frame_ch(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title('OpenGameZone')

        scrollbar = ctk.CTkScrollbar(self)
        value_1, value_2 = scrollbar.get()
        scrollbar.set(value_1, value_2)

        # icon
        p1 = tk.PhotoImage(file="./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.iconphoto(False, p1)

        self.frames = {}

        for F in (main_p, shop_p, library_p, profile_p):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(main_p)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    # welcome_page = WelcomePage()
    # welcome_page.mainloop()
    app = Frame_ch()
    app.mainloop()