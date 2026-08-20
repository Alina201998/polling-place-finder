import os        # read the loaded environment variables
import sys       # for sys.exit(1) to shut down the program if the DB connection fails
import pyodbc
import tkinter as tk
from tkinter import ttk, messagebox # popup window
from dotenv import load_dotenv   #imports the function to read .env file

load_dotenv()  # load DB

#GUI colors
COLOR_BG = "#F4F6F8"        
COLOR_CARD = "#FFFFFF"      
COLOR_PRIMARY = "#2F6FED"   
COLOR_PRIMARY_HOVER = "#255ACC"
COLOR_TEXT = "#1F2937"     
COLOR_SUBTEXT = "#6B7280"   


# Connect to database
try:
    conn = pyodbc.connect(
        f"Driver={{{os.getenv('DB_DRIVER')}}};"
        f"Server={os.getenv('DB_SERVER')};"
        f"Database={os.getenv('DB_DATABASE')};"
        f"Uid={os.getenv('DB_USERNAME')};"
        f"Pwd={os.getenv('DB_PASSWORD')};"
        r"Encrypt=yes;"
        r"TrustServerCertificate=no;"
        r"Connection Timeout=30;"
    )
    crs = conn.cursor()
except pyodbc.Error as e:
    messagebox.showerror(
        "Database Connection Failed",
        f"Could not connect to the database.\n\nDetails: {e}"
    )
    sys.exit(1) #stop the program
    
    
    
def get_polling_place(zip_code: str, precinct: int):
    query = (
        "SELECT Polling_place_name, P.address "
        "FROM Polling_place P "
        "JOIN Voters V ON P.polling_place_id = V.polling_place_id "
        "WHERE V.zip_code = ? AND precinct_number = ?;"
    )
    crs.execute(query, (zip_code, precinct))
    return crs.fetchone()  

def polling_place():  #GUI handler to read input fields
    try:
        input_zip = int(txt_zip.get())
        input_precinct = int(txt_precinct.get())
    except ValueError:
        result_label.config(text="Please enter valid ZIP and Precinct numbers.")
        return

    
    try:
        row = get_polling_place(input_zip,input_precinct)
    except pyodbc.Error as e:
        result_label.config(text=f"Database error occurred. Please try again.")
        print(f"Database error during query: {e}")  
        return

    if row:
        result_label.config(text=f"Polling place: {row[0]}\nAddress: {row[1]}")
    else:
        result_label.config(text="No results found.")




# GUI
def launch_gui():
    global txt_zip, txt_precinct, result_label
    
    root = tk.Tk()
    root.title("Choose or Lose")
    root.geometry("500x500")
    root.configure(bg=COLOR_BG)
    root.resizable(False, False) 


    style = ttk.Style()
    style.theme_use("clam") 
    style.configure("TEntry", padding=8, relief="flat")  
    style.configure(  
        "Primary.TButton",
        font=("Segoe UI", 12, "bold"),
        foreground="white",
        background=COLOR_PRIMARY,
        borderwidth=0,
        padding=10,
    )
    style.map( 
        "Primary.TButton",
        background=[("active", COLOR_PRIMARY_HOVER), ("pressed", COLOR_PRIMARY_HOVER)],
    )


    outer = tk.Frame(root, bg=COLOR_BG)
    outer.pack(fill="both", expand=True, padx=20, pady=20)

    title_label = tk.Label(
        outer,
        text="🗳️ Where Do I Vote?",
        font=("Segoe UI", 22, "bold"), 
        bg=COLOR_BG,
        fg=COLOR_TEXT,
    )
    title_label.pack(pady=(0, 4))

    subtitle_label = tk.Label(
        outer,
        text="Find your polling place in seconds",
        font=("Segoe UI", 11),
        bg=COLOR_BG,
        fg=COLOR_SUBTEXT,
    )
    subtitle_label.pack(pady=(0, 20))

    card = tk.Frame(outer, bg=COLOR_CARD, highlightbackground="#E5E7EB", highlightthickness=1)
    card.pack(fill="x", pady=(0, 16))

    card_inner = tk.Frame(card, bg=COLOR_CARD)  
    card_inner.pack(fill="x", padx=20, pady=20)

    # ZIP input
    lbl_zip = tk.Label(card_inner, text="ZIP Code", font=("Segoe UI", 10, "bold"), bg=COLOR_CARD, fg=COLOR_SUBTEXT)
    lbl_zip.pack(anchor="w")
    txt_zip = ttk.Entry(card_inner, font=("Segoe UI", 12)) 
    txt_zip.pack(fill="x", pady=(4, 14)) 

    # Precinct number input
    lbl_precinct = tk.Label(card_inner, text="Precinct Number", font=("Segoe UI", 10, "bold"), bg=COLOR_CARD, fg=COLOR_SUBTEXT)
    lbl_precinct.pack(anchor="w")
    txt_precinct = ttk.Entry(card_inner, font=("Segoe UI", 12))
    txt_precinct.pack(fill="x", pady=(4, 18))

    # Button
    button = ttk.Button(card_inner, text="Search", style="Primary.TButton", command=polling_place)
    button.pack(fill="x")  # NEW: full-width button instead of a small centered one

    # Output
    result_label = tk.Label(
        outer,  
        text="",
        font=("Segoe UI", 12),
        bg=COLOR_BG,
        fg=COLOR_TEXT,
        wraplength=400,
        justify="left",
    )
    result_label.pack(pady=(4, 0))

    root.mainloop()

if __name__ == "__main__":     
    launch_gui()  