import tkinter as tk
import math
from geopy.geocoders import Nominatim

#FUNGSI PENGIRAAN AZIMUT
def azimuth():

    LatK = 21.42222222
    LonK = 39.825

    rad_LatK =math.radians(LatK)

    LatT = latitude_var.get()
    LonT = longitude_var.get()

    rad_LatT = math.radians(LatT)

    C_Sudut=abs(LonT-LonK)

    rad_c= math.radians(C_Sudut)

    tan_sudut_kiblat = math.tan(rad_LatK) * math.cos(rad_LatT) / math.sin(rad_c) - math.sin(rad_LatT) / math.tan(rad_c)
    rad_sudut_kiblat=math.atan(tan_sudut_kiblat)
    sudut_kiblat = math.degrees(rad_sudut_kiblat)

    sudut_kiblat==sudut_kiblat
    try_arah=0

    if LatT == LatK and LonT < LonK:
        try_arah=90
    elif LatT == LatK and LonT > LonK:
        try_arah=270
    elif LatT > LatK and LonT == LonK:
        try_arah=180
    elif LatT < LatK and LonT == LonK:
        try_arah=0
    elif LonT > LonK or LonT < (LonK - 180):
        try_arah=270 + sudut_kiblat
    else:
        try_arah=90 - sudut_kiblat
    
    def decimal_to_hms(decimal):
        decimal = float(decimal)
        hours = int(decimal)
        minutes = int((decimal - hours) * 60)
        seconds = int((((decimal - hours) * 60) - minutes) * 60)
        return "{}:{}:{}".format(hours, minutes, seconds) 
    
    arah = str(decimal_to_hms(try_arah))
    
    if try_arah == 90:
        ustb= "T"
    elif try_arah == 180:
        ustb= "S"
    elif try_arah == 270:
        ustb= "W"
    elif try_arah < 90:
        ustb= "TU"
    elif try_arah < 180:
        ustb= "TS"
    elif try_arah < 270:
        ustb= "BS"
    elif try_arah < 360:
        ustb= "BU"
    else:
        ustb= "U"
    
    geolocator = Nominatim(user_agent="my-application/1.0")
    location = geolocator.reverse(f"{latitude_var.get()}, {longitude_var.get()}")

    result_label.configure(text=arah+" "+ustb)
    lokasi_label.configure(text="Lokasi kawasan: "+str(location.address))

# Create the main application window
app = tk.Tk()
app.geometry("720x480")
app.title("Kalkulator Arah Kiblat")
app.configure(bg="#F0F0F0")  # Set background color

# Styling for labels, buttons, and entry fields
font_title = ("Helvetica", 18, "bold")
font_normal = ("Helvetica", 12)

# Title Label
title_label = tk.Label(app, text="Kalkulator Arah Kiblat", font=font_title, bg="#F0F0F0")
title_label.pack(pady=15)

# User Instructions
instruction_label = tk.Label(app, text="Sila masukkan koordinat lokasi kawasan:", font=font_normal, bg="#F0F0F0")
instruction_label.pack(pady=5)

# Latitude Input
latitude_frame = tk.Frame(app, bg="#F0F0F0")
latitude_frame.pack(pady=5)

latitude_label = tk.Label(latitude_frame, text="Latitud:", font=font_normal, bg="#F0F0F0")
latitude_label.pack(side="left")

latitude_var = tk.DoubleVar()  # Variable to store latitude
latitude_entry = tk.Entry(latitude_frame, textvariable=latitude_var, font=font_normal)
latitude_entry.pack(side="left")

# Longitude Input
longitude_frame = tk.Frame(app, bg="#F0F0F0")
longitude_frame.pack(pady=7)

longitude_label = tk.Label(longitude_frame, text="Longitud:", font=font_normal, bg="#F0F0F0")
longitude_label.pack(side="left")

longitude_var = tk.DoubleVar()  # Variable to store longitude
longitude_entry = tk.Entry(longitude_frame, textvariable=longitude_var, font=font_normal)
longitude_entry.pack(side="left")

lokasi_label = tk.Label(app, text="Lokasi kawasan: ", font=font_normal, bg="#F0F0F0")
lokasi_label.pack(pady=5)

# Calculate Button
calculate_button = tk.Button(app, text="Kira", font=font_normal, command=azimuth, bg="#4CAF50", fg="white", activebackground="#45A049")
calculate_button.pack(pady=10)

# Azimuth Result Display
direction_result_label = tk.Label(app, text="Azimut kiblat:", font=font_normal, bg="#F0F0F0")
direction_result_label.pack(pady=5)

result_label = tk.Label(app, text="", font=("Helvetica", 16, "bold"), bg="#F0F0F0")
result_label.pack()

# Start the GUI event loop
app.mainloop()