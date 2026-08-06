from customtkinter import *
import sys
import subprocess
set_appearance_mode("dark")
UI = CTk()
UI.geometry("800x480")
UI.attributes("-fullscreen", True)   # fullscreen
UI.overrideredirect(True)
current_frame = None
font="DejaVu Sans Mono"
# START btn funcs
def goodbye():
    print("Bye")
    UI.quit()
    UI.destroy()
    sys.exit()
def infrared():
    print("IR")
def send_ir(code):
    result = subprocess.run(
        [
            "sudo",
            "ir-ctl",
            "-d",
            "/dev/lirc0",
            "-S",
            code
        ],
        capture_output=True,
        text=True
    )

    return result.returncode == 0, result.stdout, result.stderr
def transmit():
    code = IR_code.get("0.0", "end").strip()

    if code == "":
        print("No code entered.")
        return

    result = subprocess.run(
        [
            "sudo",
            "ir-ctl",
            "-d",
            "/dev/lirc0",
            "-S",
            code
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"Transmission successful! {code}")
    else:
        print(result.stderr)
def getWifiData():
    result = subprocess.run(
        ["nmcli", "device", "wifi", "list"],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print("Got Wifi data")
        return result.stdout
    else:
        print(result.stderr)
def nfc():
    print("NFC")
def rfid():
    print("RFID")
def sdr():
    print("SDR")
def wifi():
    print("wifi")


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
fg_color="transparent",font=(font,100))
irHeader.place(relx=0.5,rely=0.125,anchor="center")

EXIT_IR_btn = CTkButton(master=IRMenu,  text="X",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ff0000",
font=(font,25), width=50, height=50,
border_color="#008cff", border_width=7,command=lambda: show_frame(mainMenu))

IR_btn_TX = CTkButton(master=IRMenu,  text="TX",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ff2775",
font=(font,25), width=200, height=200,
border_color="#ff2775", border_width=7,command=transmit)

IR_btn_RX = CTkButton(master=IRMenu,  text="RX",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ff2775",
font=(font,25), width=200, height=200,
border_color="#ff2775", border_width=7,command=infrared)


IR_code = CTkTextbox(master=IRMenu, fg_color="#000000" ,text_color="#ff2775",
border_color="#ff2775", border_width=7, width=225, height=50)

IR_code.place(relx=(5/16),rely=0.75,anchor="center")
IR_btn_RX.place(relx=(11/16),rely=0.45,anchor="center")
IR_btn_TX.place(relx=(5/16),rely=0.45,anchor="center")
EXIT_IR_btn.place(relx=(15/16),rely=0.125,anchor="center")


# END IR FRAME
# NFC FRAME
NFCMenu = CTkFrame(
    master=UI,
    fg_color="#050025",
    corner_radius=0
)
nfcHeader = CTkLabel(master=NFCMenu, text="NFC", text_color="#aa00dd",
fg_color="transparent",font=(font,100))
nfcHeader.place(relx=0.5,rely=0.125,anchor="center")

EXIT_NFC_btn = CTkButton(master=NFCMenu,  text="X",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ff0000",
font=(font,25), width=50, height=50,
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
fg_color="transparent",font=(font,100))
rfidHeader.place(relx=0.5,rely=0.125,anchor="center")

EXIT_RFID_btn = CTkButton(master=RFIDMenu,  text="X",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ff0000",
font=(font,25), width=50, height=50,
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
fg_color="transparent",font=(font,100))
sdrHeader.place(relx=0.5,rely=0.125,anchor="center")

EXIT_SDR_btn = CTkButton(master=SDRMenu,  text="X",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ff0000",
font=(font,25), width=50, height=50,
border_color="#008cff", border_width=7,command=lambda: show_frame(mainMenu))

EXIT_SDR_btn.place(relx=(15/16),rely=0.125,anchor="center")

# END SDR FRAME

# WIFI FRAME
WIFIMenu = CTkFrame(
    master=UI,
    fg_color="#002255",
    corner_radius=0
)
wifiHeader = CTkLabel(master=WIFIMenu, text="WIFI", text_color="#33ddff",
fg_color="transparent",font=(font,100))
wifiHeader.place(relx=0.5,rely=0.125,anchor="center")

EXIT_WIFI_btn = CTkButton(master=WIFIMenu,  text="X",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ff0000",
font=(font,25), width=50, height=50,
border_color="#008cff", border_width=7,command=lambda: show_frame(mainMenu))

EXIT_WIFI_btn.place(relx=(15/16),rely=0.125,anchor="center")

WIFI_box = CTkTextbox(master=WIFIMenu, fg_color="#000000" ,text_color="#33ddff",
border_color="#33ddff", border_width=7, width=550, height=300)
WIFI_box.place(relx=(8/16),rely=0.25,anchor="center")



# END WIFI FRAME


btnW = 188
btnH = 100
menuHeader = CTkLabel(master=mainMenu, text="CYBERDECK", text_color="#ff00ff",
fg_color="transparent",font=(font,100))
menuHeader.place(relx=0.5,rely=0.125,anchor="center")


# START Define main menu btns
IR_btn = CTkButton(master=mainMenu,  text="IR",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ff2775",
font=(font,25), width=btnW, height=btnH,
border_color="#008cff", border_width=7,command=lambda: show_frame(IRMenu))

NFC_btn = CTkButton(master=mainMenu,  text="NFC",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#5200ff",
font=(font,25), width=btnW, height=btnH,
border_color="#008cff", border_width=7,command=lambda: show_frame(NFCMenu))

RFID_btn = CTkButton(master=mainMenu,  text="RFID",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#27ff84",
font=(font,25), width=btnW, height=btnH,
border_color="#008cff", border_width=7,command=lambda: show_frame(RFIDMenu))

SDR_btn = CTkButton(master=mainMenu,  text="SDR",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ffffff",
font=(font,25), width=btnW, height=btnH,
border_color="#008cff", border_width=7,command=lambda: show_frame(SDRMenu))

EXIT_btn = CTkButton(master=mainMenu,  text="X",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#ff0000",
font=(font,25), width=50, height=50,
border_color="#008cff", border_width=7,command=goodbye)

WIFI_btn = CTkButton(master=mainMenu,  text="WIFI",fg_color="#000000",bg_color="#000000",
hover_color="#000000",text_color="#33ddff",
font=(font,25), width=btnW, height=btnH,
border_color="#008cff", border_width=7,command=lambda: show_frame(WIFIMenu))

# END Define main menu btns

# START btn places

WIFI_btn.place(relx=(3/16),rely=0.75,anchor="center")
IR_btn.place(relx=(5/16),rely=0.5,anchor="center")
NFC_btn.place(relx=(9/16),rely=0.5,anchor="center")
RFID_btn.place(relx=(7/16),rely=0.75,anchor="center")
SDR_btn.place(relx=(11/16),rely=0.75,anchor="center")
EXIT_btn.place(relx=(15/16),rely=0.125,anchor="center")
# END btn places

WIFI_box.insert("0.0", getWifiData())

UI.mainloop()
