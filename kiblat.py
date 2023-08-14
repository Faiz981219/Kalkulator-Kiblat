import customtkinter as CKr
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

    if LonK<-140.1736278:
        C_Sudut=360-abs(LonT)-LonK
    else:
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

CKr.set_appearance_mode("dark")  # Modes: system (default), light, dark
CKr.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
app=CKr.CTk()
app.geometry("720x480")
app.title("Kalkulator Arah Kiblat")


title_label = CKr.CTkLabel(app, text="Kalkulator Arah Kiblat", font=CKr.CTkFont(size=20, weight="bold"))
title_label.pack(pady=10)

instruction_label = CKr.CTkLabel(app, text="Sila masukkan koordinat lokasi kawasan (Nilai (+) merujuk Utara dan Timur \ndan nilai (-) merujuk Selatan dan Barat):")
instruction_label.pack(pady=5)

latitude_frame = CKr.CTkFrame(app)
latitude_frame.pack(pady=5)

latitude_label = CKr.CTkLabel(latitude_frame, text="Latitud:",)
latitude_label.pack(side="left")

latitude_var = CKr.DoubleVar()
latitude_entry = CKr.CTkEntry(latitude_frame, textvariable=latitude_var)
latitude_entry.pack(side="left")

longitude_frame = CKr.CTkFrame(app)
longitude_frame.pack(pady=7)

longitude_label = CKr.CTkLabel(longitude_frame, text="Longitud:")
longitude_label.pack(side="left")

longitude_var = CKr.DoubleVar()  # Variable to store longitude
longitude_entry = CKr.CTkEntry(longitude_frame, textvariable=longitude_var)
longitude_entry.pack(side="left")

lokasi_label = CKr.CTkLabel(app, text="Lokasi kawasan: ")
lokasi_label.pack(padx=5,pady=5)

calculate_button = CKr.CTkButton(app, text="Kira", command=azimuth)
calculate_button.pack(pady=10)

direction_result_label = CKr.CTkLabel(app, text="Azimut kiblat:")
direction_result_label.pack(pady=5)

result_label = CKr.CTkLabel(app, text="")
result_label.pack()

app.mainloop()
