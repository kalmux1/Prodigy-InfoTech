#Network Packet Analyzer by Kalmux

from scapy.all import sniff
from scapy.layers.inet import IP
from scapy.packet import Raw
from tkinter import *
from tkinter import scrolledtext
import threading

# Protocol mapping
PROTOCOLS = {6: "TCP", 17: "UDP", 1: "ICMP"}

# Global flag to control sniffing
sniffing = False

def packet_analysis(packet):
    if packet.haslayer(IP):
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = PROTOCOLS.get(packet[IP].proto, str(packet[IP].proto))
        payload = b""

        if packet.haslayer(Raw):
            payload = packet[Raw].load

        # Format the packet information
        packet_info = (f"Source IP: {source_ip}\n"
                       f"Destination IP: {destination_ip}\n"
                       f"Protocol: {protocol}\n"
                       f"Payload: {payload}\n"
                       f"{'-' * 100}\n")

        # Insert the packet information into the text box
        packet_display.insert(END, packet_info)
        packet_display.yview(END)  # Auto-scroll to the end

def start_sniffing():
    global sniffing
    sniffing = True

    def run_sniff():
        sniff(filter="ip", prn=packet_analysis, stop_filter=lambda x: not sniffing)
    
    sniff_thread = threading.Thread(target=run_sniff)
    sniff_thread.daemon = True
    sniff_thread.start()

def stop_sniffing():
    global sniffing
    sniffing = False

base = Tk()
base.geometry("880x590")
base.title("Network Packet Analyzer")

head_frame = Frame(base)
head_frame.pack(side=TOP, anchor="center", pady=10)

head_label = Label(head_frame, text="Network Packet Analyzer", font=("Times New Roman", 20, "bold"))
head_label.grid(row=0, column=0)

author_label = Label(head_frame, text="Author : Kalmux", font=("Times New Roman", 15, "bold"))
author_label.grid(row=1, column=0)

option_frame = Frame(base)
option_frame.pack(side=TOP, anchor="center", pady=10)

start_button = Button(option_frame, text="Start Sniffing", font=("Times New Roman", 11, "bold"), command=start_sniffing, padx=10, bg="#7efc68", fg="#1C1C1C")
start_button.grid(row=0, column=0)

space_label = Label(option_frame, text="", padx=230)
space_label.grid(row=0, column=1)

stop_button = Button(option_frame, text="Stop Sniffing", font=("Times New Roman", 11, "bold"), command=stop_sniffing, padx=10, bg="#fc3e38", fg="#1C1C1C")
stop_button.grid(row=0, column=2)

# Add the ScrolledText widget to display packet data
packet_display = scrolledtext.ScrolledText(base, width=100, height=25, font=("Courier New", 10))
packet_display.pack(pady=20)

base.mainloop()
