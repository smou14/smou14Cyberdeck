from customtkinter import *
import sys
UI = CTk()
UI.geometry("800x480")
#UI.attributes("-fullscreen", True)   # fullscreen
#UI.overrideredirect(True)
UI._set_appearance_mode("dark")
btnW = 188
btnH = 100

menuHeader = CTkLabel(master=UI, text="CYBERDECK", text_color="#ff00ff",
fg_color="transparent",font=("aerial",100))
menuHeader.place(relx=0.5,rely=0.125,anchor="center")

# START btn funcs
def goodbye():
    print("Bye")
    UI.quit()
    UI.destroy()
    sys.exit()

def infrared():
    print("IR")
def nfc():
    print("NFC")
def rfid():
    print("RFID")
def sdr():
    print("SDR")

#END btn funcs
# START Define main menu btns
IR_btn = CTkButton(master=UI,  text="IR",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ff2775",
font=("aerial",25), width=btnW, height=btnH,
border_color="#008cff", border_width=7,command=infrared)

NFC_btn = CTkButton(master=UI,  text="NFC",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#5200ff",
font=("aerial",25), width=btnW, height=btnH,
border_color="#008cff", border_width=7,command=nfc)

RFID_btn = CTkButton(master=UI,  text="RFID",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#27ff84",
font=("aerial",25), width=btnW, height=btnH,
border_color="#008cff", border_width=7,command=rfid)

SDR_btn = CTkButton(master=UI,  text="SDR",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ffffff",
font=("aerial",25), width=btnW, height=btnH,
border_color="#008cff", border_width=7,command=sdr)

EXIT_btn = CTkButton(master=UI,  text="X",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ff0000",
font=("aerial",25), width=50, height=50,
border_color="#008cff", border_width=7,command=goodbye)

# END Define main menu btns

# START btn places
IR_btn.place(relx=(5/16),rely=0.5,anchor="center")
NFC_btn.place(relx=(9/16),rely=0.5,anchor="center")
RFID_btn.place(relx=(7/16),rely=0.75,anchor="center")
SDR_btn.place(relx=(11/16),rely=0.75,anchor="center")
EXIT_btn.place(relx=(15/16),rely=0.125,anchor="center")
# END btn places
UI.mainloop()
