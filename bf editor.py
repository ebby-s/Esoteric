from tkinter import *
import tkinter.filedialog
import bf_interpreter

def make_file():
    global text
    program = text.get("1.0", "end-1c")
    filename = tkinter.filedialog.asksaveasfilename()
    f = open(filename+".bf", "w")
    f.write(program)
    f.close()

def run():
    global text
    program = text.get("1.0", "end-1c")
    bf_interpreter.in_memory = str(input("Enter inputs: ")).split()
    bf_interpreter.execute(program)

root = Tk()

root.title("Brainf@$! Editor")
text = Text(root)
text.grid()
save_button = Button(root, text="Save", command=make_file) 
save_button.grid()
run_button = Button(root, text="Run", command=run) 
run_button.grid()

root.mainloop()
