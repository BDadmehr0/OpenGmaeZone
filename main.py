import customtkinter as ctk
import tkinter as tk
import os
import random
import logging

from PIL import Image, ImageTk

# Polet Color

class color:
    yellow = '#FFBB5C'
    dark_yellow = '#FF9B50'
    red = '#E25E3E'
    dark_red = '#C63D2F'

# Pages

## profile
class profile_p_friends(ctk.CTkFrame):

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
        self.menu_top_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_top_frame.pack(side='top', fill='x', expand=False)

        # Menu Top Frame OBJs

        # APP Logo
        self.image = Image.open("./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.image = self.image.resize((64, 64), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.logo = ctk.CTkLabel(self.menu_top_frame, image=self.photo, text='', corner_radius=0)
        self.logo.pack(side='left', fill='x', expand=False, padx=5)

        # Menu Top Buttons

        self.main_p_btn = ctk.CTkButton(self.menu_top_frame, text='Main', font=('Times New Roman', 35), command=lambda: controller.show_frame(main_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.main_p_btn.pack(side='left', fill='y', expand=False)

        self.library_p_btn = ctk.CTkButton(self.menu_top_frame, text='Library', font=('Times New Roman', 35), command=lambda: controller.show_frame(library_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.library_p_btn.pack(side='left', fill='y', expand=False)

        self.shop_p_btn = ctk.CTkButton(self.menu_top_frame, text='Shop', font=('Times New Roman', 35), command=lambda: controller.show_frame(shop_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.shop_p_btn.pack(side='left', fill='y', expand=False)

        self.profile_p_btn = ctk.CTkButton(self.menu_top_frame, text='Profile', font=('Times New Roman', 35), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.profile_p_btn.pack(side='left', fill='y', expand=False)

        self.exit_btn = ctk.CTkButton(self.menu_top_frame, text='Exit', font=('Times New Roman', 35), command=self.exitf, corner_radius=0, fg_color=color.yellow, hover_color=color.dark_yellow)
        self.exit_btn.pack(side='right', fill='y', expand=False)

        # Profile setting menu
        self.menu_left_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_left_frame.pack(padx=12, pady=10, side='left', fill='y', expand=False)

        # Profile setting menu OBJs       
        self.button_setting_profile = ctk.CTkButton(self.menu_left_frame, text='Profile', font=('Times New Roman',20), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_profile.pack(fill='x')

        self.button_setting_passowrd = ctk.CTkButton(self.menu_left_frame, text='Password', font=('Times New Roman',20), command=lambda: controller.show_frame(profile_p_password), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_passowrd.pack(fill='x')

        self.button_setting_email = ctk.CTkButton(self.menu_left_frame, text='Email', font=('Times New Roman',20), corner_radius=0, command=lambda: controller.show_frame(profile_p_email), fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_email.pack(fill='x')

        self.button_setting_firends = ctk.CTkButton(self.menu_left_frame, text='Friends', font=('Times New Roman',20), corner_radius=0, command=lambda: controller.show_frame(profile_p_friends), fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_firends.pack(fill='x')



    def exitf(self):
        exit()

    def toggle_geom(self, event):
        if self.new_frame_status:
            self.controller.geometry(self._geom)
        else:
            self._geom = self.controller.geometry()
            self.controller.geometry("{0}x{1}+0+0".format(
                self.controller.winfo_screenwidth() - 3, self.controller.winfo_screenheight() - 3))
        self.new_frame_status = not self.new_frame_status

# email
class profile_p_email(ctk.CTkFrame):

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
        self.menu_top_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_top_frame.pack(side='top', fill='x', expand=False)

        # Menu Top Frame OBJs

        # APP Logo
        self.image = Image.open("./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.image = self.image.resize((64, 64), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.logo = ctk.CTkLabel(self.menu_top_frame, image=self.photo, text='', corner_radius=0)
        self.logo.pack(side='left', fill='x', expand=False, padx=5)

        # Menu Top Buttons

        self.main_p_btn = ctk.CTkButton(self.menu_top_frame, text='Main', font=('Times New Roman', 35), command=lambda: controller.show_frame(main_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.main_p_btn.pack(side='left', fill='y', expand=False)

        self.library_p_btn = ctk.CTkButton(self.menu_top_frame, text='Library', font=('Times New Roman', 35), command=lambda: controller.show_frame(library_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.library_p_btn.pack(side='left', fill='y', expand=False)

        self.shop_p_btn = ctk.CTkButton(self.menu_top_frame, text='Shop', font=('Times New Roman', 35), command=lambda: controller.show_frame(shop_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.shop_p_btn.pack(side='left', fill='y', expand=False)

        self.profile_p_btn = ctk.CTkButton(self.menu_top_frame, text='Profile', font=('Times New Roman', 35), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.profile_p_btn.pack(side='left', fill='y', expand=False)

        self.exit_btn = ctk.CTkButton(self.menu_top_frame, text='Exit', font=('Times New Roman', 35), command=self.exitf, corner_radius=0, fg_color=color.yellow, hover_color=color.dark_yellow)
        self.exit_btn.pack(side='right', fill='y', expand=False)

        # Profile setting menu
        self.menu_left_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_left_frame.pack(padx=12, pady=10, side='left', fill='y', expand=False)

        # Profile setting menu OBJs
        
        self.button_setting_profile = ctk.CTkButton(self.menu_left_frame, text='Profile', font=('Times New Roman',20), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_profile.pack(fill='x')

        self.button_setting_passowrd = ctk.CTkButton(self.menu_left_frame, text='Password', font=('Times New Roman',20), command=lambda: controller.show_frame(profile_p_password), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_passowrd.pack(fill='x')

        self.button_setting_email = ctk.CTkButton(self.menu_left_frame, text='Email', font=('Times New Roman',20), corner_radius=0, command=lambda: controller.show_frame(profile_p_email), fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_email.pack(fill='x')

        self.button_setting_firends = ctk.CTkButton(self.menu_left_frame, text='Friends', font=('Times New Roman',20), corner_radius=0, command=lambda: controller.show_frame(profile_p_friends), fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_firends.pack(fill='x')


        # Profile Menu Detials
        self.menu_left_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_left_frame.pack(padx=12, pady=10, side='bottom', fill='both', expand=True)

    def exitf(self):
        exit()

    def toggle_geom(self, event):
        if self.new_frame_status:
            self.controller.geometry(self._geom)
        else:
            self._geom = self.controller.geometry()
            self.controller.geometry("{0}x{1}+0+0".format(
                self.controller.winfo_screenwidth() - 3, self.controller.winfo_screenheight() - 3))
        self.new_frame_status = not self.new_frame_status

## password
class profile_p_password(ctk.CTkFrame):

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
        self.menu_top_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_top_frame.pack(side='top', fill='x', expand=False)

        # Menu Top Frame OBJs

        # APP Logo
        self.image = Image.open("./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.image = self.image.resize((64, 64), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.logo = ctk.CTkLabel(self.menu_top_frame, image=self.photo, text='', corner_radius=0)
        self.logo.pack(side='left', fill='x', expand=False, padx=5)

        # Menu Top Buttons

        self.main_p_btn = ctk.CTkButton(self.menu_top_frame, text='Main', font=('Times New Roman', 35), command=lambda: controller.show_frame(main_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.main_p_btn.pack(side='left', fill='y', expand=False)

        self.library_p_btn = ctk.CTkButton(self.menu_top_frame, text='Library', font=('Times New Roman', 35), command=lambda: controller.show_frame(library_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.library_p_btn.pack(side='left', fill='y', expand=False)

        self.shop_p_btn = ctk.CTkButton(self.menu_top_frame, text='Shop', font=('Times New Roman', 35), command=lambda: controller.show_frame(shop_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.shop_p_btn.pack(side='left', fill='y', expand=False)

        self.profile_p_btn = ctk.CTkButton(self.menu_top_frame, text='Profile', font=('Times New Roman', 35), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.profile_p_btn.pack(side='left', fill='y', expand=False)

        self.exit_btn = ctk.CTkButton(self.menu_top_frame, text='Exit', font=('Times New Roman', 35), command=self.exitf, corner_radius=0, fg_color=color.yellow, hover_color=color.dark_yellow)
        self.exit_btn.pack(side='right', fill='y', expand=False)

        # Profile setting menu
        self.menu_left_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_left_frame.pack(padx=12, pady=10, side='left', fill='y', expand=False)

        # Profile setting menu OBJs
        
        self.button_setting_profile = ctk.CTkButton(self.menu_left_frame, text='Profile', font=('Times New Roman',20), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_profile.pack(fill='x')

        self.button_setting_passowrd = ctk.CTkButton(self.menu_left_frame, text='Password', font=('Times New Roman',20), command=lambda: controller.show_frame(profile_p_password), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_passowrd.pack(fill='x')

        self.button_setting_email = ctk.CTkButton(self.menu_left_frame, text='Email', font=('Times New Roman',20), corner_radius=0, command=lambda: controller.show_frame(profile_p_email), fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_email.pack(fill='x')

        self.button_setting_firends = ctk.CTkButton(self.menu_left_frame, text='Friends', font=('Times New Roman',20), corner_radius=0, command=lambda: controller.show_frame(profile_p_friends), fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_firends.pack(fill='x')


        # Profile Menu Detials
        self.menu_left_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_left_frame.pack(padx=12, pady=10, side='bottom', fill='both', expand=True)
    
    def exitf(self):
        exit()

    def toggle_geom(self, event):
        if self.new_frame_status:
            self.controller.geometry(self._geom)
        else:
            self._geom = self.controller.geometry()
            self.controller.geometry("{0}x{1}+0+0".format(
                self.controller.winfo_screenwidth() - 3, self.controller.winfo_screenheight() - 3))
        self.new_frame_status = not self.new_frame_status

class profile_p(ctk.CTkFrame):

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
        self.menu_top_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_top_frame.pack(side='top', fill='x', expand=False)

        # Menu Top Frame OBJs

        # APP Logo
        self.image = Image.open("./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.image = self.image.resize((64, 64), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.logo = ctk.CTkLabel(self.menu_top_frame, image=self.photo, text='', corner_radius=0)
        self.logo.pack(side='left', fill='x', expand=False, padx=5)

        # Menu Top Buttons

        self.main_p_btn = ctk.CTkButton(self.menu_top_frame, text='Main', font=('Times New Roman', 35), command=lambda: controller.show_frame(main_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.main_p_btn.pack(side='left', fill='y', expand=False)

        self.library_p_btn = ctk.CTkButton(self.menu_top_frame, text='Library', font=('Times New Roman', 35), command=lambda: controller.show_frame(library_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.library_p_btn.pack(side='left', fill='y', expand=False)

        self.shop_p_btn = ctk.CTkButton(self.menu_top_frame, text='Shop', font=('Times New Roman', 35), command=lambda: controller.show_frame(shop_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.shop_p_btn.pack(side='left', fill='y', expand=False)

        self.profile_p_btn = ctk.CTkButton(self.menu_top_frame, text='Profile', font=('Times New Roman', 35), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.profile_p_btn.pack(side='left', fill='y', expand=False)

        self.exit_btn = ctk.CTkButton(self.menu_top_frame, text='Exit', font=('Times New Roman', 35), command=self.exitf, corner_radius=0, fg_color=color.yellow, hover_color=color.dark_yellow)
        self.exit_btn.pack(side='right', fill='y', expand=False)

        # Profile setting menu
        self.menu_left_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_left_frame.pack(padx=12, pady=10, side='left', fill='y', expand=False)

        # Profile setting menu OBJs
        
        self.button_setting_profile = ctk.CTkButton(self.menu_left_frame, text='Profile', font=('Times New Roman',20), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_profile.pack(fill='x')

        self.button_setting_passowrd = ctk.CTkButton(self.menu_left_frame, text='Password', font=('Times New Roman',20), command=lambda: controller.show_frame(profile_p_password), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_passowrd.pack(fill='x')

        self.button_setting_email = ctk.CTkButton(self.menu_left_frame, text='Email', font=('Times New Roman',20), corner_radius=0, command=lambda: controller.show_frame(profile_p_email), fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_email.pack(fill='x')

        self.button_setting_firends = ctk.CTkButton(self.menu_left_frame, text='Friends', font=('Times New Roman',20), corner_radius=0, command=lambda: controller.show_frame(profile_p_friends), fg_color=color.red, hover_color=color.dark_red)
        self.button_setting_firends.pack(fill='x')


        # Profile Menu Detials

        self.menu_detials_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_detials_frame.pack(padx=12, pady=10, side='bottom', fill='both', expand=True)

        # Profile Menu Detials OBJs
        self.menu_detials_frame = ctk.CTkFrame(self.menu_detials_frame, corner_radius=0)
        self.menu_detials_frame.pack(pady=30, padx=20, side='left', fill='both', expand=False)

        # Profile image
        self.image = Image.open("./assets/profile/user.png")
        self.image = self.image.resize((256, 256 ), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)

        self.label = ctk.CTkLabel(self.menu_detials_frame, image=self.photo, text='')
        self.label.pack()

        # Profile Detail lb
        self.username_lb = ctk.CTkLabel(self.menu_detials_frame, text='\nUsername', font=('Times New Roman', 35))
        self.username_lb.pack(side='left', fill='both', expand=False)

        self.username_lb = ctk.CTkLabel(self.menu_detials_frame, text='Mail\n', font=('Times New Roman', 35))
        self.username_lb.pack(side='left', fill='both', expand=False)

        self.username_lb = ctk.CTkLabel(self.menu_detials_frame, text='Regoin', font=('Times New Roman', 35))
        self.username_lb.pack(side='left', fill='both', expand=False)
        

    def exitf(self):
        exit()

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

        # Full Screen
        pad=3
        self._geom='500x600+0+0'
        controller.geometry("{0}x{1}+0+0".format(
            controller.winfo_screenwidth()-pad, controller.winfo_screenheight()-pad))
        controller.bind('<F11>', self.toggle_geom)

        # OBJ

        # Menu Top Frame
        self.menu_top_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_top_frame.pack(side='top', fill='x', expand=False)

        # Menu Top Frame OBJs

        # APP Logo
        self.image = Image.open("./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.image = self.image.resize((64, 64), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.logo = ctk.CTkLabel(self.menu_top_frame, image=self.photo, text='', corner_radius=0)
        self.logo.pack(side='left', fill='x', expand=False, padx=5)

        # Menu Top Buttons

        self.main_p_btn = ctk.CTkButton(self.menu_top_frame, text='Main', font=('Times New Roman', 35), command=lambda: controller.show_frame(main_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.main_p_btn.pack(side='left', fill='y', expand=False)

        self.library_p_btn = ctk.CTkButton(self.menu_top_frame, text='Library', font=('Times New Roman', 35), command=lambda: controller.show_frame(library_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.library_p_btn.pack(side='left', fill='y', expand=False)

        self.shop_p_btn = ctk.CTkButton(self.menu_top_frame, text='Shop', font=('Times New Roman', 35), command=lambda: controller.show_frame(shop_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.shop_p_btn.pack(side='left', fill='y', expand=False)

        self.profile_p_btn = ctk.CTkButton(self.menu_top_frame, text='Profile', font=('Times New Roman', 35), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.profile_p_btn.pack(side='left', fill='y', expand=False)

        self.exit_btn = ctk.CTkButton(self.menu_top_frame, text='Exit', font=('Times New Roman', 35), command=self.exitf, corner_radius=0, fg_color=color.yellow, hover_color=color.dark_yellow)
        self.exit_btn.pack(side='right', fill='y', expand=False)

    def exitf(self):
        exit()

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

        # Full Screen
        pad=3
        self._geom='500x600+0+0'
        controller.geometry("{0}x{1}+0+0".format(
            controller.winfo_screenwidth()-pad, controller.winfo_screenheight()-pad))
        controller.bind('<F11>', self.toggle_geom)

        # OBJ

        # Menu Top Frame
        self.menu_top_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_top_frame.pack(side='top', fill='x', expand=False)

        # Menu Top Frame OBJs

        # APP Logo
        self.image = Image.open("./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.image = self.image.resize((64, 64), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.logo = ctk.CTkLabel(self.menu_top_frame, image=self.photo, text='', corner_radius=0)
        self.logo.pack(side='left', fill='x', expand=False, padx=5)

        # Menu Top Buttons

        self.main_p_btn = ctk.CTkButton(self.menu_top_frame, text='Main', font=('Times New Roman', 35), command=lambda: controller.show_frame(main_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.main_p_btn.pack(side='left', fill='y', expand=False)

        self.library_p_btn = ctk.CTkButton(self.menu_top_frame, text='Library', font=('Times New Roman', 35), command=lambda: controller.show_frame(library_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.library_p_btn.pack(side='left', fill='y', expand=False)

        self.shop_p_btn = ctk.CTkButton(self.menu_top_frame, text='Shop', font=('Times New Roman', 35), command=lambda: controller.show_frame(shop_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.shop_p_btn.pack(side='left', fill='y', expand=False)

        self.profile_p_btn = ctk.CTkButton(self.menu_top_frame, text='Profile', font=('Times New Roman', 35), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.profile_p_btn.pack(side='left', fill='y', expand=False)

        self.exit_btn = ctk.CTkButton(self.menu_top_frame, text='Exit', font=('Times New Roman', 35), command=self.exitf, corner_radius=0, fg_color=color.yellow, hover_color=color.dark_yellow)
        self.exit_btn.pack(side='right', fill='y', expand=False)

    def exitf(self):
        exit()

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
        self.menu_top_frame = ctk.CTkFrame(self, corner_radius=0)
        self.menu_top_frame.pack(side='top', fill='x', expand=False)

        # Menu Top Frame OBJs

        # APP Logo
        self.image = Image.open("./assets/logo/favicon/opengmaezone-website-favicon-color.png")
        self.image = self.image.resize((64, 64), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.logo = ctk.CTkLabel(self.menu_top_frame, image=self.photo, text='', corner_radius=0)
        self.logo.pack(side='left', fill='x', expand=False, padx=5)

        # Menu Top Buttons

        self.main_p_btn = ctk.CTkButton(self.menu_top_frame, text='Main', font=('Times New Roman', 35), command=lambda: controller.show_frame(main_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.main_p_btn.pack(side='left', fill='y', expand=False)

        self.library_p_btn = ctk.CTkButton(self.menu_top_frame, text='Library', font=('Times New Roman', 35), command=lambda: controller.show_frame(library_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.library_p_btn.pack(side='left', fill='y', expand=False)

        self.shop_p_btn = ctk.CTkButton(self.menu_top_frame, text='Shop', font=('Times New Roman', 35), command=lambda: controller.show_frame(shop_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.shop_p_btn.pack(side='left', fill='y', expand=False)

        self.profile_p_btn = ctk.CTkButton(self.menu_top_frame, text='Profile', font=('Times New Roman', 35), command=lambda: controller.show_frame(profile_p), corner_radius=0, fg_color=color.red, hover_color=color.dark_red)
        self.profile_p_btn.pack(side='left', fill='y', expand=False)

        self.exit_btn = ctk.CTkButton(self.menu_top_frame, text='Exit', font=('Times New Roman', 35), command=self.exitf, corner_radius=0, fg_color=color.yellow, hover_color=color.dark_yellow)
        self.exit_btn.pack(side='right', fill='y', expand=False)

    def exitf(self):
        exit()

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

        for F in (main_p, shop_p, library_p, profile_p,
                                             profile_p_friends,
                                             profile_p_email,
                                             profile_p_password):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(main_p)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    # # LOG
    # logging.basicConfig(filename='log.log', filemode='w', level=logging.INFO)

    # logger = logging.getLogger()
    # # logger.info('This is error')
    # logger.debug('This is Debug')
    # # logger.warning('This is error')
    # logger.error('This is Error')
    # logger.critical('This is Critical')


    # welcome_page = WelcomePage()
    # welcome_page.mainloop()
    app = Frame_ch()
    os.system('clear')
    app.mainloop()