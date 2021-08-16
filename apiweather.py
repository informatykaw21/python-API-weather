# -*- coding: utf-8 -*-
import requests
import json
import tkinter as tk #gui

API_KEY = open("kluczAPI.txt").read()

def pokazTemp(miasto):
    wynikZapytania = \
        requests.get('http://api.openweathermap.org/data/2.5/weather?q='+miasto+'&appid='+API_KEY)
    #print(wynikZapytania.text)
    ekstrakt = json.loads(wynikZapytania.text)
    #print(ekstrakt['main']['temp']-273.15)
    return round(ekstrakt['main']['temp']-273.15) 

# while True:
#     miasto = input("Podaj miasto: ")
#     print(pokazTemp(miasto))
class aplikacja (tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.przycisk = tk.Button(self)
        self.przycisk['text']='Pokaz temperature'
        self.pack()
        self.przycisk.grid(row=2, column=1)
        self.przycisk['command'] = self.pokazTemp

        self.labelOdp = tk.Label(self)
        self.labelOdp.grid(row=2, column=2)
        self.tuwpisz = tk.Entry(self)
        self.tuwpisz.grid(row=1, column=2)
        self.labelOpis = tk.Label(self)
        self.labelOpis.grid(row=1, column=1)
        self.labelOpis['text']='Wpisz miasto'
        self.labelOpis['font'] = 'Helvetica 14 bold'
        
    
    
    def pokazTemp(self):
        
        miasto = self.tuwpisz.get()
        self.labelOdp['text']= str(pokazTemp(miasto)) + " °C"


root =tk.Tk()
root.minsize(300,100)
root.maxsize(300,100)
win = aplikacja(root)
win.mainloop()


