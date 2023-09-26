import customtkinter as ctk
import tkinter as tk

from PIL import Image, ImageTk

# Pages
class main(ctk.CTkFrame):
+ 
+     def __init__(self, parent, controller):
+         ctk.CTkFrame.__init__(self, parent)
+         self.controller = controller
+         self.new_frame_status = False
+ 
+ 
+ 
+         # Full Screen Code
+         pad=3
+         self._geom='500x600+0+0'
         controller.geometry("{0}x{1}+0+0".format(
            controller.winfo_screenwidth()-pad, controller.winfo_screenheight()-pad))
        controller.bind('<F11>',self.togg)
class main(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.new_frame_status = False



        # Full Screen Code
        pad=3
        self._geom='500x600+0+0'
        controller.geometry("{0}x{1}+0+0".format(
            controller.winfo_screenwidth()-pad, controller.winfo_screenheight()-pad))
        controller.bind('<F11>',self.toggle_geom)

class WelcomePage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Welcome')
        self.geometry('400x300')

        p1 = tk.PhotoImage(file="./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.iconphoto(False, p1)

        self.image = Image.open("./assets/logo/favicon/opengmaezone-website-favicon-color.png")

        new_width = 200
        new_height = 150
        self.image = self.image.resize((new_width, new_height), Image.ANTIALIAS)

        self.photo = ImageTk.PhotoImage(self.image)

        self.label = ctk.CTkLabel(self, image=self.photo, text='')
        self.label.pack(pady=20)

        self.welcome_label = ctk.CTkLabel(self, text='Welcome to the app!', font=('roboto', 25))
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

        for F in (main, shop, library, profile):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(main)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    welcome_page = WelcomePage()
    welcome_page.mainloop()
