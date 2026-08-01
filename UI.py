from customtkinter import *
UI = CTk()
UI.geometry("800x480")
UI.attributes("-fullscreen", True)   # fullscreen
UI.overrideredirect(True)
UI._set_appearance_mode("dark")
btnW = 300
btnH = 150
# START Define main menu btns
IR_btn = CTkButton(master=UI,  text="IR",fg_color="#000000",
hover_color="#090404",text_color="#ff2775",
font=("aerial",25), width=btnW, height=btnH,
border_color="#008cff", border_width=7)

NFC_btn = CTkButton(master=UI,  text="NFC",fg_color="#000000",
hover_color="#090404",text_color="#5200ff",
font=("aerial",25), width=btnW, height=btnH,
border_color="#008cff", border_width=7)

RFID_btn = CTkButton(master=UI,  text="RFID",fg_color="#000000",
hover_color="#090404",text_color="#27ff84",
font=("aerial",25), width=btnW, height=btnH,
border_color="#008cff", border_width=7)

SDR_btn = CTkButton(master=UI,  text="SDR",fg_color="#000000",
hover_color="#090404",text_color="#ffffff",
font=("aerial",25), width=btnW, height=btnH,
border_color="#008cff", border_width=7)
# END Define main menu btns
# START btn places
IR_btn.place(relx=(5/16),rely=0.5,anchor="center")
NFC_btn.place(relx=(9/16),rely=0.5,anchor="center")
RFID_btn.place(relx=(7/16),rely=0.75,anchor="center")
SDR_btn.place(relx=(11/16),rely=0.75,anchor="center")
# END btn places
UI.mainloop()
