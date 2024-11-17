#using tkinter to create simple GUI
from tkinter import *
from tkinter import ttk

#import request from api
import requests

def get_weather():
    city = city_name.get()
    data_url = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c9305b16a699ed26bd90565bdac03121").json()
    w_label1.config(text= data_url["weather"][0]["main"])
    wb_label1.config(text= data_url["weather"][0]["description"])
    temp_label1.config(text= str(data_url["main"]["temp"] -273.15))
    per_label1.config(text= data_url["main"]["pressure"])

#window title and bgcolor
win = Tk()
win.title("my first")
win.config(bg = "aqua")
win.geometry("500x500")


#main label of the window
name_label = Label(win,text="my_weather_app", font=("arial",30,"bold"))
name_label.place(x=25, y=50, height=50, width=450)


#list box contain all the states
city_name = StringVar()
list_names = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="my_weather_app", values=list_names, font=("arial",20,"bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)


##label to display the selected state
#weather
w_label = Label(win,text="weather", font=("arial",10,"bold"))
w_label.place(x=25, y=260, height=50, width=210)

w_label1 = Label(win,text="", font=("arial",10,"bold"))
w_label1.place(x=250, y=260, height=50, width=210)


#weather decription
wb_label = Label(win,text="weather description", font=("arial",10,"bold"))
wb_label.place(x=25, y=330, height=50, width=210)

wb_label1 = Label(win,text="", font=("arial",10,"bold"))
wb_label1.place(x=250, y=330, height=50, width=210)


#temperture
temp_label = Label(win,text="temperture", font=("arial",10,"bold"))
temp_label.place(x=25, y=400, height=50, width=210)

temp_label1 = Label(win,text="", font=("arial",10,"bold"))
temp_label1.place(x=250, y=400, height=50, width=210)


#pressure
per_label = Label(win,text="presure", font=("arial",10,"bold"))
per_label.place(x=25, y=470, height=50, width=210)

per_label1 = Label(win,text="", font=("arial",10,"bold"))
per_label1.place(x=250, y=470, height=50, width=210)


# button tag
done_button = Button(win,text="done", font=("arial",10,"bold"), command=get_weather)
done_button.place(x=200, y=190, height=50, width=100)

#to run the window
win.mainloop()