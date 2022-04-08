import tkinter as tk

window = tk.Tk()
#window.geometry("500x500")
window.attributes('-fullscreen', True)
window.title("Switch Button")
window.configure(bg="grey")

frame = tk.Frame(master=window, width=500, height=1000)
frame.pack()
frame.configure(bg="grey")

label = tk.Label(master=frame, text="Switch button", fg="red", font = ('Arial', 50), bg="grey")
label.place(x=120, y=20)

label2 = tk.Label(master=frame, text = "Choose which light\n to turn On or Off", fg ="red", font = ('Arial',30), bg = "grey")
label2.place(x=140, y=100)

button1 = tk.Button(master=frame,text = "Choose light", highlightbackground='grey')
button1.place(x=175, y=300)

def changeText() :
    if(button2['text'] == 'On'):
        button2['text'] = 'Off'

    else:
        button2['text'] = 'On'

button2 = tk.Button(bg = "GREY",fg="red",master=frame, text = "On", command = changeText, highlightbackground='grey')
button2.place(x=300, y=300)

window.mainloop()