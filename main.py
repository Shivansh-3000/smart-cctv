import tkinter as tk
import tkinter.font as font
from motion import motion
from motiononvideo import motiononvideo
from record import record
from in_out import in_out

window = tk.Tk()
window.title = "CCTV"
window.geometry('860x500')

label = tk.Label(window, text="Smart-CCTV", fg='blue')
label.grid(row=0, column=10, pady=(10, 10))
label['font'] = font.Font(size=35, weight='bold', family='Helvetica')

button1 = tk.Button(window, text="Visitors in room", fg="black", height=2, width=20, command=in_out)
button1['font'] = font.Font(size=15, weight='bold', family='Helvetica')
button1.grid(row=1, pady=(50, 10), padx=(40, 0), column=2)

button3 = tk.Button(window, text="Motion detect", fg="black", height=2, width=20, command=motion)
button3['font'] = font.Font(size=15, weight='bold', family='Helvetica')
button3.grid(row=1, pady=(50, 10), column=14)

button4 = tk.Button(window, text="Record", fg="black", height=2, width=20, command=record)
button4['font'] = font.Font(size=15, weight='bold', family='Helvetica')
button4.grid(row=2, pady=(50, 10), column=10)

button2 = tk.Button(window, text="exit", fg="red", height=2, width=20, command=window.quit)
button2['font'] = font.Font(size=15, weight='bold', family='Helvetica')
button2.grid(row=3, pady=(50, 10), column=10)

window.mainloop()