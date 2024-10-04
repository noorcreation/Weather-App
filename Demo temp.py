from tkinter import *
from tkinter import ttk
import requests

def data_get():
 city= city_name.get()
 response = requests.get("http://api.weatherapi.com/v1/current.json?key=786c8d485ed644b88f5110504241609&q=+city+&aqi=no")
 data=response.json()
 w_label1.config(text=data["current"]["condition"]["text"])
 wS_label1.config(text=data["current"]["wind_kph"])
 temp_label1.config(text=data["current"]["temp_c"])
 per_label1.config(text=data["current"]["pressure_mb"])

win = Tk()
win.title("Noor Tech")
win.config(bg = "blue")
win.geometry("500x570")

name_label = Label(win,text="Weather App",
                   font=("Times New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry","West Bengal"]
com=ttk.Combobox(win,text="Noor Weather App",values=list_name,
                   font=("Times New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

done_button = Button(win, text="Done",
                     font=("Times New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)



w_label = Label(win,text=" Weather Climate",
                   font=("Times New Roman",20,))
w_label.place(x=25,y=260,height=50,width=210)

w_label1 = Label(win,text="",
                   font=("Times New Roman",20,))
w_label1.place(x=250,y=260,height=50,width=210)



wS_label = Label(win,text=" Wind Speed",
                   font=("Times New Roman",17,))
wS_label.place(x=25,y=330,height=50,width=210)

wS_label1 = Label(win,text="",
                   font=("Times New Roman",17,))
wS_label1.place(x=250,y=330,height=50,width=210)


temp_label = Label(win,text="Temperature",
                   font=("Times New Roman",20,))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1 = Label(win,text="",
                   font=("Times New Roman",20,))
temp_label1.place(x=250,y=400,height=50,width=210)

per_label = Label(win,text=" Pressure",
                   font=("Times New Roman",20,))
per_label.place(x=25,y=470,height=50,width=210)

per_label1 = Label(win,text="",
                   font=("Times New Roman",20,))
per_label1.place(x=250,y=470,height=50,width=210)

win.mainloop()