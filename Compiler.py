# Importing tkinter module for GUI
from tkinter import *
# Importing filedialog submodule to use its file opening and saving prompts
from tkinter.filedialog import asksaveasfilename, askopenfilename
# importing subprocess module for creating a process which is then used for executing code via shell
import subprocess
# importing messagebox submodule
from tkinter import messagebox

# Creating main window object
ide = Tk()
# Set dimensions of main window
ide.geometry("800x600")
# Set title of main window
ide.title("Vcode Compiler")

# Saving recently saved / opened files path
save_path = ''
# Saving input status of inputs given to code being executed
inputs = False


# Saves file path of most recently opened / saved files in save_path global variable
def save_file_path(path):
    global save_path
    save_path = path


# Updates input status of inputs given to code being executed on radiobutton yes input or no input click
def get_inputs():
    global inputs
    if var.get() == 1:
        inputs = True
    else:
        inputs = False


# Executes for on-click event for labels having command as run
# Accepts language to whose code to execute as parameter
# messagebox is prompted if input to code option is not selected
# Subprocess is created by creating Popen class constructor and run command depending on language
# is sent as command parameter stdin,stdout and stderror are pipelined to process created
# then shell is made active to execute this process having stdin,stdout and stderror
# then if input to code exists then data is read from input terminal and saved in a file
# then given as parameter to communicate method if no input then no parameter given to communicate
# communicate method interacts with process for inputs and also fetches output and error from the process
# then output and if any error are displayed on output terminal.
def run(language):
    if var.get() == 0:
        messagebox.showwarning('INPUTS', 'Please select one input option')
        return

    if language == "Run Java":
        run("Run Python")
    elif language == "Run C":
        run("Run Python")
    elif language == "Run CPP":
        run("Run Python")
    else:
        command = f'python {save_path}'

    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    test_string = str(input_terminal.get('1.0', END))
    if inputs and test_string != '':
        input_file = open('VcodeInput.txt', 'w')
        inputs_given = input_terminal.get('1.0', END)
        input_file.write(inputs_given)
        input_file = open('VcodeInput.txt', 'r')
        byte_input_file = ''.join(input_file.readlines())
        output, error = process.communicate(byte_input_file.encode())
    else:
        output, error = process.communicate()
    out_put_terminal.insert('1.0', "\nVcode IDE:\n\n")
    out_put_terminal.insert('1.0', output)
    out_put_terminal.insert('1.0', error)


# Opens a file using askopenfilename function which returns file path of selected file
# Then the file is opened by open file function by giving path of file to it also open function is
# in read mode as code from file needs to be read and displayed on editor (text area)
# delete method erases previous data on the editor and insert method adds new code on editor (text area)
# Save file path saves recently opened file's path
# If askopenfile function was used then there wasn't any need of open function it returns open file
def open_file():
    filetype = [('Python Files', '*.py'), ('All Files', '*'), ('Text Files', '*.txt')]
    path = askopenfilename(filetypes=filetype, defaultextension=filetype)
    file = open(path, 'r')
    editor.delete('1.0', END)
    editor.insert('1.0', file.read())
    save_file_path(path)


# Saves file if not previously saved , if save_path is null means file is not saved so if save
# command is used dialog box will be prompted to save as , also if file is previously saved
# then save_path wont be empty and changes will be made in the same file
# asksaveasfilename returns path and name where to save file then open function checks on this
# path if file present if yes then open's the file else creates file with name given by user
# mode of open function is write because new changes needs to be written on file
# get method fetches data from editor(text area) and writes on file
# save file path saves recently saved file's path
# If askopenfile function was used then there wasn't any need of open function it returns open file
def save_file():
    if save_path == '':
        filetype = [('Python Files', '*.py'), ('All Files', '*'), ('Text Files', '*.txt')]
        path = asksaveasfilename(filetypes=filetype, defaultextension=filetype)
    else:
        path = save_path
    file = open(path, 'w')
    program = editor.get('1.0', END)
    file.write(program)
    save_file_path(path)


# Creates menu named menu_ribbon on main window
menu_ribbon = Menu(ide)

# Creates sub-menu run_ribbon on main menu
run_ribbon = Menu(menu_ribbon, tearoff=0)
# Adds run label/option in sub-menu and give on-click event run to execute code by run function
run_ribbon.add_command(label="Run Python", command=lambda: run("Run Python"))
# Adds run label/option in sub-menu and give on-click event run to execute code by run function
run_ribbon.add_command(label="Run C", command=lambda: run("Run C"))
# Adds run label/option in sub-menu and give on-click event run to execute code by run function
run_ribbon.add_command(label="Run Java", command=lambda: run("Run Java"))
# Adds run label/option in sub-menu and give on-click event run to execute code by run function
run_ribbon.add_command(label="Run CPP", command=lambda: run("Run CPP"))
# Adds sub-menu as execute label/option in main menu in cascade
menu_ribbon.add_cascade(label="Execute", menu=run_ribbon)

# Creates sub-menu file_ribbon on main menu
file_ribbon = Menu(menu_ribbon, tearoff=0)
# Adds Save label/option in sub-menu and give on-click event save_file to execute code by this function
file_ribbon.add_command(label="Save", command=save_file)
# Adds Save As label/option in sub-menu and give on-click event save_file to execute code by this function
file_ribbon.add_command(label="Save As", command=save_file)
# Adds open label/option in sub-menu and give on-click event open_file to execute code by this function
file_ribbon.add_command(label="Open", command=open_file)
# Adds exit label/option in sub-menu and give on-click event exit to execute code by in built exit function
# exit() terminates current executing code
file_ribbon.add_command(label="Exit", command=exit)
# Adds sub-menu as File label/option in main menu in cascade
menu_ribbon.add_cascade(label="File", menu=file_ribbon)

# Overwriting main menu on main window
ide.config(menu=menu_ribbon)

# Creating scroll bar on main window
scroll_ide = Scrollbar(ide)
# Adding scroll bar on main window
scroll_ide.pack(side=RIGHT, fill=Y)

# Creating font object for text style in editor
font = ('Time', 12)

# Creating a text area on main window ;set method sets the slider limit on scroll bar on editor
editor = Text(ide, bg='linen', yscrollcommand=scroll_ide.set)
# Adding font object in editor
editor.config(font=font)
# Filling the text area on entire window
editor.pack(fill=BOTH, expand=True)
# Configuring scroll bar on main window to editor ;parameter sets scroll bar action as vertical movement
scroll_ide.config(command=editor.yview)

# Creating a output text area on main window
out_put_terminal = Text(ide, height=10, width=50, bg='gray1', fg='white', cursor='arrow')
# Adding font object in output terminal
out_put_terminal.config(font=font)
# Filling the text area on entire window
out_put_terminal.pack(side=LEFT, fill=BOTH, expand=True)


# Creating a input text area on main window
input_terminal = Text(ide, height=10, bg='light gray')
# Filling the input text area on entire window
input_terminal.pack(side=LEFT, fill=BOTH, expand=True)
# Adding the font object on input terminal
input_terminal.config(font=font)
# Creating a input label on input terminal
input_menu = Label(input_terminal, height=2, width=5, cursor='arrow', text='Input Area')
# Filling the label on input terminal
input_menu.pack(side=RIGHT, fill=BOTH)

# Intvar class object wraps all radio buttons in same group due to which at a time only one radio button can be selected
var = IntVar()

# Creating a yes input button input label on input terminal
yes_input_button = Radiobutton(input_menu, text='Yes Input', variable=var, value=1, command=get_inputs)
# Filling the button on input label
yes_input_button.grid(row=0, column=1)

# Creating a No input button input label on output terminal
no_input_button = Radiobutton(input_menu, text='No Input', variable=var, value=2, command=get_inputs)
# Filling the button on input label
no_input_button.grid(row=0, column=3)


# Continuously run the main window
ide.mainloop()
