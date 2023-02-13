import requests
import tkinter


root = tkinter.Tk()
 
# root window title and dimension
root.title("air quality")
# Set geometry(widthxheight)
root.geometry('1000x200')

# create a StringVar class
out_string_var = tkinter.StringVar()

#set label
lbl = tkinter.Label(root, text = "Enter the city to find air quality for.")
lbl.grid(column =0, row =5)


# adding Entry Field
txt = tkinter.Entry(root, width=30)
txt.grid(column =0, row =15)

# Create text widget and specify size.
out = tkinter.Label(root, height = 5, width = 100, textvariable = out_string_var)
out.grid(column =0, row =35)


#api call to get aqi
def get_aq():
    city = txt.get().strip().title()
    city_url=f'https://api.waqi.info/feed/{city}/?token=1daf67993aba4537581e07b803bdc7ea71ccac64'
    city_response=requests.get(city_url).json()
    aqi=city_response['data']['aqi']
    city_name=city_response['data']['city']['name']
    dominent_pollutant=city_response['data']['dominentpol']
    air_quality = f'The current AQI for {city_name} is {aqi}, and the primary pollutant is {dominent_pollutant}'
    out_string_var.set(air_quality)
 
#button widget with blue color text inside
btn = tkinter.Button(root, text = "Find", 
            fg='#03045e', command=get_aq,
                        relief=tkinter.RIDGE, bg='#caf0f8', activebackground='#ef233c',
                        activeforeground='white')
btn.grid(column=0, row=25)
btn.bind("<Enter>", lambda e: btn.config(fg='#caf0f8', bg='#03045e'))
btn.bind("<Leave>", lambda e: btn.config(fg='#03045e', bg='#caf0f8'))
 
root.mainloop()


