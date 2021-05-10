# Tkinter
import tkinter

window = tkinter.Tk()
window.title("These nuts GUI")
window.minsize(width=500, height=300)

# Labels
my_label = tkinter.Label(text="I am a label.", font=("Arial", 24, "bold"))
my_label.pack()







window.mainloop()