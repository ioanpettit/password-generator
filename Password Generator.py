#!/usr/bin/env python
# coding: utf-8

# In[9]:


from random import random
import string
import tkinter as tk
import random
from sklearn.utils import shuffle
import customtkinter as ctk
from tkinter import *
from tkinter import ttk


# In[10]:


def generate_password():
    '''A function to generate a random password'''
    l = generate_letters()
    n = generate_numbers()
    n = [str(i) for i in n]
    s = generate_symbols()
    
    return ''.join(shuffle(l+n+s))


# In[11]:


def generate_numbers():
    '''A function to generate list of random integers between 0 and 9'''
    numbers = []
    length = random.randint(5,8)
    for i in range(length):
        numbers.append(random.randint(0,9))
    return numbers


# In[12]:


def generate_symbols():
    '''function to generate list of random symbols'''
    symbols = []
    symbol_options = ['%','&','/','@','!','?']
    length = random.randint(3,6)
    for i in range(length):
        symbols.append(random.choice(symbol_options))
    return symbols


# In[13]:


def generate_letters():
    '''function to generate a list of random letters'''
    letters = []
    length = random.randint(5,8)
    for i in range(length):
        letters.append(random.choice(string.ascii_letters))
    return letters


# In[15]:


def clear_widgets(frame):
    # select all frame widgets and delete them
    for widget in frame.winfo_children():
        widget.destroy()


# In[32]:


background='#323050'
ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('dark-blue')


def load_frame1():
    clear_widgets(frame2)
    # stack frame 1 on top
    frame1.tkraise()
    # prevent widgets from modifying the frame
    frame1.pack_propagate(False)


    # create label with the title of the app
    tk.Label(frame1, text="Random Password Generator",bg=background,
        fg="white",
        font=("Rockwell", 50)
        ).place(rely=0.4,relx=0.5,anchor=CENTER)

    # create button for generating password
    ctk.CTkButton(
    frame1,
    text="GENERATE",
        
        bg="#28393a",
        text_font=("Rockwell",40),
        command=lambda:load_frame2()
        ).place(rely=0.5,relx=0.5, anchor=CENTER)

def load_frame2():
    clear_widgets(frame1)
    # stack frame 2 
    frame2.tkraise()


    # random password  widget
    tk.Label(
        frame2, 
        text=f'Your Random Password: {generate_password()}',
        bg=background,
        fg='white',
        font=("Rockwell", 30)
        ).pack(pady=25, padx=25)

    # back button
    ctk.CTkButton(frame2, text="BACK", text_font=("Rockwell", 40),command=lambda:load_frame1()
                 ).pack(pady=25, padx=25)


# generate tkinter window
window = ctk.CTk()
window.title("Password Generator")
window.geometry("1200x500+10+10")

 
# create frames
frame1 = tk.Frame(window, width=2000, height=1500, bg=background)
frame2 = tk.Frame(window, bg=background)

# place frame widgets in window
for frame in (frame1, frame2):
    frame.place(rely=0.5,relx=0.5, anchor = CENTER)

# load the first frame
load_frame1()

# run app
window.mainloop()


# In[ ]:




