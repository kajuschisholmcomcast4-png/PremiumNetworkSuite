import customtkinter as ctk
import socket
import requests

# --- Functions ---
def get_local_ip():
try:
hostname = socket.gethostname()
return socket.gethostbyname(hostname)
except:
return "Error getting local IP"

def get_public_ip():
try:
return requests.get("https://api.ipify.org").text
except:
return "Error getting public IP"

def refresh_ips():
local_ip_label.configure(text=f"Local IP: {get_local_ip()}")
public_ip_label.configure(text=f"Public IP: {get_public_ip()}")

# --- UI Setup ---
ctk.set_appearance_mode("dark") # dark mode
ctk.set_default_color_theme("blue") # premium blue accents

app = ctk.CTk()
app.title("Premium IP Viewer")
app.geometry("420x260")

frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(padx=20, pady=20, fill="both", expand=True)

title = ctk.CTkLabel(
frame,
text="Network IP Dashboard",
font=("Segoe UI", 22, "bold")
)
title.pack(pady=(10, 15))

local_ip_label = ctk.CTkLabel(
frame,
text="Local IP: ...",
font=("Segoe UI", 16)
)
local_ip_label.pack(pady=5)

public_ip_label = ctk.CTkLabel(
frame,
text="Public IP: ...",
font=("Segoe UI", 16)
)
public_ip_label.pack(pady=5)

refresh_button = ctk.CTkButton(
frame,
text="Refresh",
command=refresh_ips,
height=40,
corner_radius=10
)
refresh_button.pack(pady=20)

# Load initial values
refresh_ips()

app.mainloop()
