import math
from geopy.geocoders import Nominatim
import customtkinter as CKr

CKr.set_appearance_mode("dark")  # Modes: system (default), light, dark
CKr.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class QiblaDirectionCalculatorApp:
    def __init__(self):
        self.app = CKr.CTk()
        self.app.geometry("720x480")
        self.app.title("Kalkulator Arah Kiblat")

        self.title_label = CKr.CTkLabel(self.app, text="Kalkulator Arah Kiblat", font=CKr.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=10)

        self.instruction_label = CKr.CTkLabel(self.app, text="Sila masukkan koordinat lokasi kawasan (Nilai (+) merujuk Utara dan Timur \ndan nilai (-) merujuk Selatan dan Barat):", font=CKr.CTkFont(size=14))
        self.instruction_label.pack(pady=5)

        self.latitude_frame = CKr.CTkFrame(self.app)
        self.latitude_frame.pack(pady=5)

        self.latitude_label = CKr.CTkLabel(self.latitude_frame, text="Latitud :", font=CKr.CTkFont(size=14))
        self.latitude_label.pack(side="left")

        self.latitude_var = CKr.DoubleVar()
        self.latitude_entry = CKr.CTkEntry(self.latitude_frame, textvariable=self.latitude_var)
        self.latitude_entry.pack(side="left")

        self.longitude_frame = CKr.CTkFrame(self.app)
        self.longitude_frame.pack(pady=7)

        self.longitude_label = CKr.CTkLabel(self.longitude_frame, text="Longitud :", font=CKr.CTkFont(size=14))
        self.longitude_label.pack(side="left")

        self.longitude_var = CKr.DoubleVar()  # Variable to store longitude
        self.longitude_entry = CKr.CTkEntry(self.longitude_frame, textvariable=self.longitude_var)
        self.longitude_entry.pack(side="left")

        self.lokasi_label = CKr.CTkLabel(self.app, text="Lokasi kawasan: ", font=CKr.CTkFont(size=14))
        self.lokasi_label.pack(padx=5, pady=5)

        self.calculate_button = CKr.CTkButton(self.app, text="Kira", font=CKr.CTkFont(size=14), command=self.calculate_azimuth)
        self.calculate_button.pack(pady=10)

        self.direction_result_label = CKr.CTkLabel(self.app, text="Azimut kiblat:", font=CKr.CTkFont(size=14))
        self.direction_result_label.pack(pady=5)

        self.result_label = CKr.CTkLabel(self.app, text="", font=CKr.CTkFont(size=14, weight="bold"))
        self.result_label.pack()

        self.app.mainloop()

    def calculate_azimuth(self):
        LatK = 21.422503
        LonK = 39.826198

        rad_LatK = math.radians(LatK)

        LatT = self.latitude_var.get()
        LonT = self.longitude_var.get()

        rad_LatT = math.radians(LatT)

        try_bezaLon=LonT-LonK

        if try_bezaLon < -180:
            C_Sudut = 360 - abs(LonT) - LonK
        else:
            C_Sudut = abs(LonT - LonK)

        rad_c = math.radians(C_Sudut)

        tan_sudut_kiblat = math.tan(rad_LatK) * math.cos(rad_LatT) / math.sin(rad_c) - math.sin(rad_LatT) / math.tan(rad_c)
        rad_sudut_kiblat = math.atan(tan_sudut_kiblat)
        sudut_kiblat = math.degrees(rad_sudut_kiblat)

        try_arah = 0

        if LatT == LatK and LonT < LonK:
            try_arah = 90
        elif LatT == LatK and LonT > LonK:
            try_arah = 270
        elif LatT > LatK and LonT == LonK:
            try_arah = 180
        elif LatT < LatK and LonT == LonK:
            try_arah = 0
        elif LonT > LonK or LonT < (LonK - 180):
            try_arah = 270 + sudut_kiblat
        else:
            try_arah = 90 - sudut_kiblat

        def decimal_to_hms(decimal):
            decimal = float(decimal)
            hours = int(decimal)
            minutes = int((decimal - hours) * 60)
            seconds = int((((decimal - hours) * 60) - minutes) * 60)
            return "{}:{}:{}".format(hours, minutes, seconds)

        arah = str(decimal_to_hms(try_arah))

        if try_arah == 90:
            ustb = "T"
        elif try_arah == 180:
            ustb = "S"
        elif try_arah == 270:
            ustb = "B"
        elif try_arah < 90:
            ustb = "UT"
        elif try_arah < 180:
            ustb = "ST"
        elif try_arah < 270:
            ustb = "SB"
        elif try_arah < 360:
            ustb = "UB"
        else:
            ustb = "U"

        geolocator = Nominatim(user_agent="my-application/1.0")
        location = geolocator.reverse(f"{self.latitude_var.get()}, {self.longitude_var.get()}")

        self.result_label.configure(text=arah + " " + ustb)
        self.lokasi_label.configure(text="Lokasi kawasan: " + str(location.address))

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    app = QiblaDirectionCalculatorApp()
    app.run()
