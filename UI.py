from customtkinter import *
import sys
set_appearance_mode("dark")
UI = CTk()
UI.geometry("800x480")
#UI.attributes("-fullscreen", True)   # fullscreen
#UI.overrideredirect(True)
current_frame = None

def show_frame(frame):
    global current_frame

    if current_frame is not None:
        current_frame.pack_forget()

    current_frame = frame
    current_frame.pack(fill="both", expand=True)

#MAIN FRAME
mainMenu = CTkFrame(
    master=UI,
    fg_color="#000000",
    corner_radius=0
)
show_frame(mainMenu)
#END MAIN FRAME

#IR FRAME
IRMenu = CTkFrame(
    master=UI,
    fg_color="#330000",
    corner_radius=0
)
irHeader = CTkLabel(master=IRMenu, text="IR", text_color="#dd0000",
fg_color="transparent",font=("aerial",100))
irHeader.place(relx=0.5,rely=0.125,anchor="center")

EXIT_IR_btn = CTkButton(master=IRMenu,  text="X",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ff0000",
font=("aerial",25), width=50, height=50,
border_color="#008cff", border_width=7,command=lambda: show_frame(mainMenu))

EXIT_IR_btn.place(relx=(15/16),rely=0.125,anchor="center")


# END IR FRAME
# NFC FRAME
NFCMenu = CTkFrame(
    master=UI,
    fg_color="#050025",
    corner_radius=0
)
nfcHeader = CTkLabel(master=NFCMenu, text="NFC", text_color="#aa00dd",
fg_color="transparent",font=("aerial",100))
nfcHeader.place(relx=0.5,rely=0.125,anchor="center")

EXIT_NFC_btn = CTkButton(master=NFCMenu,  text="X",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ff0000",
font=("aerial",25), width=50, height=50,
border_color="#008cff", border_width=7,command=lambda: show_frame(mainMenu))

EXIT_NFC_btn.place(relx=(15/16),rely=0.125,anchor="center")

# END NFC FRAME
# RFID FRAME
RFIDMenu = CTkFrame(
    master=UI,
    fg_color="#002500",
    corner_radius=0
)
rfidHeader = CTkLabel(master=RFIDMenu, text="RFID", text_color="#00aa00",
fg_color="transparent",font=("aerial",100))
rfidHeader.place(relx=0.5,rely=0.125,anchor="center")

EXIT_RFID_btn = CTkButton(master=RFIDMenu,  text="X",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ff0000",
font=("aerial",25), width=50, height=50,
border_color="#008cff", border_width=7,command=lambda: show_frame(mainMenu))

EXIT_RFID_btn.place(relx=(15/16),rely=0.125,anchor="center")

#END RFID FRAME
# SDR FRAME
SDRMenu = CTkFrame(
    master=UI,
    fg_color="#252525",
    corner_radius=0
)
sdrHeader = CTkLabel(master=SDRMenu, text="SDR", text_color="#ffffff",
fg_color="transparent",font=("aerial",100))
sdrHeader.place(relx=0.5,rely=0.125,anchor="center")

EXIT_SDR_btn = CTkButton(master=SDRMenu,  text="X",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ff0000",
font=("aerial",25), width=50, height=50,
border_color="#008cff", border_width=7,command=lambda: show_frame(mainMenu))

EXIT_SDR_btn.place(relx=(15/16),rely=0.125,anchor="center")

# END SDR FRAME
btnW = 188
btnH = 100
menuHeader = CTkLabel(master=mainMenu, text="CYBERDECK", text_color="#ff00ff",
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
IR_btn = CTkButton(master=mainMenu,  text="IR",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ff2775",
font=("aerial",25), width=btnW, height=btnH,
border_color="#008cff", border_width=7,command=lambda: show_frame(IRMenu))

NFC_btn = CTkButton(master=mainMenu,  text="NFC",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#5200ff",
font=("aerial",25), width=btnW, height=btnH,
border_color="#008cff", border_width=7,command=lambda: show_frame(NFCMenu))

RFID_btn = CTkButton(master=mainMenu,  text="RFID",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#27ff84",
font=("aerial",25), width=btnW, height=btnH,
border_color="#008cff", border_width=7,command=lambda: show_frame(RFIDMenu))

SDR_btn = CTkButton(master=mainMenu,  text="SDR",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ffffff",
font=("aerial",25), width=btnW, height=btnH,
border_color="#008cff", border_width=7,command=lambda: show_frame(SDRMenu))

EXIT_btn = CTkButton(master=mainMenu,  text="X",fg_color="#000000",bg_color="#000000",
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
