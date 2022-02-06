# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 10:29:50 2022

@author: ramak
"""

import random
from tkinter import *
root= Tk()
root.title("Random Countries And Capitals")
root.geometry("400x400")
root.configure(bg="light blue")

enter_country= Entry(root)
enter_capital= Entry(root)
enter_country.place(relx=0.5, rely=0.1, anchor=CENTER)
enter_capital.place(relx=0.5, rely=0.2, anchor=CENTER)

country_list= Label(root)
capital_list= Label(root)
random_number_label= Label(root)
rand_country= Label(root)
rand_capital= Label(root)

country =[]
capital =[]


def addplace():
    country_name=enter_country.get()
    country.append(country_name)
    country_list["text"]= "Your Countries Are : "+str(country)
    capital_name=enter_capital.get()
    capital.append(capital_name)
    capital_list["text"]= "Your Capitals Are : "+str(capital)
    
def randomnumber():
    length= len(country)
    random_no= random.randint(0, length-1)
    random_number_label["text"]= str(random_no)
    generated_random_no = country[random_no]
    rand_country["text"]= "Your Country: "+ str(generated_random_no)
    
    length= len(capital)
    random_no= random.randint(0, length-1)
    random_number_label["text"]= str(random_no)
    generated_random_no = capital[random_no]
    rand_capital["text"]= "Your Capital: "+ str(generated_random_no)
    
btn= Button(root, text="Add to List", command=addplace, bg="blue", fg="white")
btn.place(relx=0.5, rely=0.3, anchor=CENTER)

country_list.place(relx=0.5, rely=0.4, anchor=CENTER)
capital_list.place(relx=0.5, rely=0.5, anchor=CENTER)

btn1= Button(root, text="What is Your Place?  ", command=randomnumber, bg="blue", fg="white")
btn1.place(relx=0.5, rely=0.6, anchor=CENTER)

random_number_label.place(relx=0.5, rely=0.7, anchor=CENTER)
rand_country.place(relx=0.5, rely=0.8, anchor=CENTER)
rand_capital.place(relx=0.5, rely=0.9, anchor=CENTER)



root.mainloop()