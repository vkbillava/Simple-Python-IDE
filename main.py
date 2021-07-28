from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfilename
import subprocess as sp

root = Tk()
root.title('Py IDE')
root.height = 400
root.width = 600
file_path = ''

def set_path(path):
    global file_path
    file_path = path

def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_path(path)

def save_as():
    if file_path == '':
        path = asksaveasfile(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path

    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_path(path)

def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text="Not saved yet, Please save your code")
        text.pack()
        return

    command = f'python {file_path}'
    ps = sp.Popen(command, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    output, error = ps.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

def exit_app():
    root.destroy()

menu_bar = Menu(root)

file_menu = Menu(menu_bar)
file_menu.add_command(label = 'Open', command = open_file)
file_menu.add_command(label = 'Save', command = save_as)
file_menu.add_command(label = 'Save As', command = save_as)
file_menu.add_command(label = 'Exit', command = exit_app)
menu_bar.add_cascade(label = 'File', menu = file_menu)

run_bar = Menu(menu_bar)
run_bar.add_command(label = "Run", command = run)
menu_bar.add_cascade(label = "Run", menu = run_bar)

root.config(menu=menu_bar)
editor = Text()
editor.pack()
code_output = Text(height = 10)
code_output.pack()
root.mainloop()