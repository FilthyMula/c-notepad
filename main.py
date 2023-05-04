import httpx, sys, os
from discord_webhook import DiscordWebhook
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import font
from tkinter import *
import requests
import win32api


build = 'C-NotePad 1.0.2023'

#updater
def updater():
    global update_win, current_version, new_version
    
    current_version = httpx.get('https://raw.githubusercontent.com/FilthyMula/c-notepad/main/version.txt').text.splitlines()
    new_version = httpx.get('https://raw.githubusercontent.com/FilthyMula/c-notepad/main/updater/version.txt').text.splitlines()
    
    if new_version > current_version:
        update_win = Tk()
        update_win.title("Update found")
        update_win.resizable(False, False)
        w = 300  
        h = 100
        screen_width = update_win.winfo_screenwidth()
        screen_height = update_win.winfo_screenheight()
        x = (screen_width/2) - (w/2)
        y = (screen_height/2) - (h/2)
        update_win.geometry('%dx%d+%d+%d' % (w, h, x, y))

        Label(update_win, text='Update found\nWould you like to update?', font=main_font).place(x=55, y=10)
        
        update_yes = Button(update_win, text='Yes', width=10, command=update)
        update_yes.place(x=63, y=55)
        
        update_no = Button(update_win, text='No', width=10, command=update_win.destroy)
        update_no.place(x=150, y=55)
    else:
        no_update_win = Tk()
        no_update_win.title("No update found")
        no_update_win.resizable(False, False)
        w = 300  
        h = 70
        screen_width = no_update_win.winfo_screenwidth()
        screen_height = no_update_win.winfo_screenheight()
        x = (screen_width/2) - (w/2)
        y = (screen_height/2) - (h/2)
        no_update_win.geometry('%dx%d+%d+%d' % (w, h, x, y))

        Label(no_update_win, text='No updates found', font=main_font).place(x=85, y=20)
        
def update():
    root.destroy()
    update_win.destroy()
    updating_win = Tk()
    updating_win.title(f"Updating")
    updating_win.resizable(False, False)
    w = 300  
    h = 100
    screen_width = updating_win.winfo_screenwidth()
    screen_height = updating_win.winfo_screenheight()
    x = (screen_width/2) - (w/2)
    y = (screen_height/2) - (h/2)
    updating_win.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    url = "https://github.com/FilthyMula/c-notepad/blob/main/main.py"
    resp = requests.get(url)
    os.remove('main.py')
    with open('main.py', 'a+') as f:
        f.write(resp)
        f.close()
        
    #Label(updating_win, text='Updating..', font=main_font).place(x=5, y=10)
    #for i in range(5):
        #progress = Progressbar(updating_win, orient=HORIZONTAL, length=100, mode='indeterminate')
        #progress.place(x=7, y=35, width=200)
        #updating_win.update_idletasks()
        #progress['value'] += 5

    
#color configs
def dark():
    events.config(text='Dark mode set')
    root.config(bg="black")
    events.config(bg="black", fg='white')
    pad.config(bg='gray18', fg='gray80')
    file_menu.config(bg="black", fg="white")
    edit_menu.config(bg="black", fg="white")
    settings_menu.config(bg="black", fg="white")
    helper_menu.config(bg="black", fg="white")
    txt_sub_menu.config(bg='black', fg="white")
    notepad_sub_menu.config(bg='black', fg="white")
    cmd_entry.config(bg='gray18', fg="yellow")

def light():
    events.config(text='Light mode set')
    root.config(bg="white")
    events.config(bg="white", fg='black')
    pad.config(bg='grey', fg='black')
    file_menu.config(bg="white", fg="black")
    edit_menu.config(bg="white", fg="black")
    settings_menu.config(bg="white", fg="black")
    helper_menu.config(bg="white", fg="black")
    txt_sub_menu.config(bg='white', fg="black")
    notepad_sub_menu.config(bg='white', fg="black")
    cmd_entry.config(bg='grey', fg="black")
    
def underline():
    try:
        if pad.tag_nextrange('underline_selection', 'sel.first', 'sel.last') != ():
            pad.tag_remove('underline_selection', 'sel.first', 'sel.last')
        else:
            pad.tag_add('underline_selection', 'sel.first', 'sel.last')
            pad.tag_configure('underline_selection', underline=True)
    except TclError:
        pass

def size_8():
    pad.config(font=font.Font(size = 8))
    
def size_10():
    pad.config(font=font.Font(size = 10))
    
def size_12():
    pad.config(font=font.Font(size = 12))
    
def size_14():
    pad.config(font=font.Font(size = 14))
    
def size_16():
    pad.config(font=font.Font(size = 16))
    
def size_18():
    pad.config(font=font.Font(size = 18))
    
def size_20():
    pad.config(font=font.Font(size = 20))
    
def size_22():
    pad.config(font=font.Font(size = 22))
    
def size_24():
    pad.config(font=font.Font(size = 24))
    
def size_26():
    pad.config(font=font.Font(size = 26))
    
def size_28():
    pad.config(font=font.Font(size = 28))
    
def size_30():
    pad.config(font=font.Font(size = 30))

def black_pad():
    pad.config(bg='black')
    events.config(text='NotePad - Black back-ground selected')

def white_txt():
    pad.config(fg='white')
    events.config(text='NotePad - White text selected')

def black_txt():
    pad.config(fg='black')
    events.config(text='NotePad - Black text selected')
    
def yellow_txt():
    pad.config(fg='yellow')
    events.config(text='NotePad - Yellow text selected')

def blue_txt():
    pad.config(fg='blue')
    events.config(text='NotePad - Blue text selected')

def green_txt():
    pad.config(fg='green')
    events.config(text='NotePad - Green text selected')
    
def new_file():
    pad.delete('1.0', END)
    root.title("New File - NotePad")
    events.config(text='New File')
    
def open_file():
    pad.delete('1.0', END)    
    text_file = filedialog.askopenfilename(title='Open File', filetypes=(('Text Files', '*.txt'), ('HTML Files', '*.html'), ('Python Files', '*.py'), ('All Files', '*.*')))
    if text_file:
        name = text_file
        events.config(text=f'Opened: {name}')
        name = name.replace('C:/notepad/', "")
        root.title(f"{name}")
        text_file = open(text_file, 'r')
        stuff = text_file.read()
        pad.insert(END, stuff)
        text_file.close()

def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", title='Save File', filetypes=(('Text Files', '*.txt'), ('HTML Files', '*.html'), ('Python Files', '*.py'), ('All Files', '*.*')))
    if text_file:
        name = text_file
        events.config(text=f'Saved: {name}')
        name = name.replace('C:/notepad/', "")
        root.title(f"{name}")
        text_file = open(text_file, 'w')
        text_file.write(pad.get(1.0, END))
        text_file.close()
    
def select_all():
    pad.tag_add('sel', '1.0', 'end')
    
def bold_func():
    bold_font = font.Font(pad, pad.cget('font'))
    bold_font.configure(weight='bold')
    pad.tag_configure('bold', font=bold_font)
    current_tags = pad.tag_names('sel.first')
    if 'bold' in current_tags:
        pad.tag_remove('bold', 'sel.first', 'sel.last')
    else:
        pad.tag_add('bold', 'sel.first', 'sel.last')

def italic_func():
    italic_font = font.Font(pad, pad.cget('font'))
    italic_font.configure(slant='italic')
    pad.tag_configure('italic', font=italic_font)
    current_tags = pad.tag_names('sel.first')
    if 'italic' in current_tags:
        pad.tag_remove('italic', 'sel.first', 'sel.last')
    else:
        pad.tag_add('italic', 'sel.first', 'sel.last')

def cut_text(e):
    global selected
    if pad.selection_get():
        selected = pad.selection_get()
        pad.delete('sel.first', 'sel.last')
        
def copy_text(e):
    global selected
    if pad.selection_get():
        selected = pad.selection_get()
        events.config(text='NotePad - Copied to clipboard')
        
def paste_text(e):
    if selected:
        position = pad.index(INSERT)
        pad.insert(position, selected)
        events.config(text='NotePad - Pasted to NotePad')

def help_menu():
    help = Tk()
    events.config(text='Help - Commands')
    help.title("Console commands")
    help.resizable(False, False)
    w = 300  
    h = 550
    screen_width = help.winfo_screenwidth()
    screen_height = help.winfo_screenheight()
    x = (screen_width/2) - (w/2)
    y = (screen_height/2) - (h/2)
    help.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    help.config(bg="grey")
    Label(help, text='close', font=('Halvetica', 15), bg='grey').place(x=5, y=10)
    Label(help, text='Close NotePad', font=('Halvetica', 10), bg='grey').place(x=5, y=35)
    
    Label(help, text='discord', font=('Halvetica', 15), bg='grey').place(x=5, y=60)
    Label(help, text='Send note as discord webhook', font=('Halvetica', 10), bg='grey').place(x=5, y=85)
    
    Label(help, text='dark', font=('Halvetica', 15), bg='grey').place(x=5, y=110)
    Label(help, text='Set dark mode', font=('Halvetica', 10), bg='grey').place(x=5, y=135)
    
    Label(help, text='light', font=('Halvetica', 15), bg='grey').place(x=5, y=160)
    Label(help, text='Set light mode', font=('Halvetica', 10), bg='grey').place(x=5, y=185)
    
    Label(help, text='open', font=('Halvetica', 15), bg='grey').place(x=5, y=210)
    Label(help, text='Open file', font=('Halvetica', 10), bg='grey').place(x=5, y=235)
    
    Label(help, text='(path)', font=('Halvetica', 15), bg='grey').place(x=5, y=260)
    Label(help, text='Open path', font=('Halvetica', 10), bg='grey').place(x=5, y=285)
    
    Label(help, text='restart', font=('Halvetica', 15), bg='grey').place(x=5, y=310)
    Label(help, text='Restart app', font=('Halvetica', 10), bg='grey').place(x=5, y=335)
    
    Label(help, text='save', font=('Halvetica', 15), bg='grey').place(x=5, y=360)
    Label(help, text='Save file', font=('Halvetica', 10), bg='grey').place(x=5, y=385)
    
    Label(help, text='sethook', font=('Halvetica', 15), bg='grey').place(x=5, y=410)
    Label(help, text='Set webhooks', font=('Halvetica', 10), bg='grey').place(x=5, y=435)

def cmds(event):
    cmd = cmd_entry.get()
    if cmd_entry.get() == 'help':
        events.config(text='Help menu')
        help_menu()
    elif cmd == 'save':
        save_as_file()
    elif cmd == 'open':
        open_file()
    elif cmd == 'close':
        sys.exit()
    elif cmd == 'discord':
        send_discord_hook()
    elif cmd == 'dark':
        dark()
    elif cmd == 'light':
        light()
    elif cmd == 'restart':
        restart()
    elif cmd == 'sethook':
        webhooks()
    elif os.path.exists(cmd):
        try:
            pad.delete('1.0', END)    
            with open(cmd, 'r', encoding='utf-8-sig') as f:
                lines = f.readlines()
                pad.insert(END, lines)
                name = cmd
                events.config(text=f'Opened: {name}')
                name = name.replace('C:/notepad/', "")
        except:
            pass
    else:
        pass
    
def restart():
    os.execv(sys.executable, ['python'] + sys.argv)
    
def print_file():
    file_to_print = filedialog.askopenfilename(title='Open File', filetypes=(("Text Files", "*.txt"), ('All Files', "*.*")))
    if file_to_print:
        win32api.ShellExecute(0, 'print', file_to_print, None, '.', 0)

def webhooks():
    global enter_w_hook
    w_hooks = Tk()
    w_hooks.title("Discord webhook")
    w_hooks.config(bg="grey")
    w_hooks.resizable(False, False)
    w = 800  
    h = 120
    screen_width = w_hooks.winfo_screenwidth()
    screen_height = w_hooks.winfo_screenheight()
    x = (screen_width/2) - (w/2)
    y = (screen_height/2) - (h/2)
    w_hooks.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    discord_hook = Label(w_hooks, text='Discord webhook', bg='grey', font=('Halvetica', 25))
    discord_hook.place(x=3, y=15)
    
    enter_w_hook = Entry(w_hooks, width=130)
    enter_w_hook.place(x=5, y=55)
    
    save_w_hook = Button(w_hooks, text='Set webhook', width=15, bg='black', fg='white', command=get_discord_webhook)
    save_w_hook.place(x=5, y=75)
    
    clear_w_hook = Button(w_hooks, text='Clear webhook', width=15, bg='black', fg='white', command=clear_d_hook)
    clear_w_hook.place(x=125, y=75)

def d_hook_success():
    events.config(text='Webhook - Saved')

def d_hook_error():
    events.config(text='Webhook - Invalid')

def get_discord_webhook():
    webhook = enter_w_hook.get()
    if webhook.startswith('https://discord.com/api/webhooks/'):
        os.remove('Webhooks/discord.txt')
        f = open('Webhooks/discord.txt', 'a+')
        f.write(webhook)
        f.close()
        d_hook_success()
    else:
        d_hook_error()

def send_discord_hook():
    try:
        my_hook = open('Webhooks/discord.txt').read()
        hook_content = pad.get(1.0, END)
        hook = DiscordWebhook(url=my_hook, content=hook_content)
        hook.execute()
        events.config(text=f'Webhook - Sent [Discord]')
    except:
        events.config(text='Webhook - Error')
        
def clear_d_hook():
    enter_w_hook.delete(0, END)
    events.config(text='Webhook - Cleared')

#unfinished
def create_form():
    global create_form_window, how_many
    create_form_window = Tk()
    create_form_window.title("Create form")
    create_form_window.resizable(False, False)
    create_form_window.config(bg='grey')
    w = 150  
    h = 100
    screen_width = create_form_window.winfo_screenwidth()
    screen_height = create_form_window.winfo_screenheight()
    x = (screen_width/2) - (w/2)
    y = (screen_height/2) - (h/2)
    create_form_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    Label(create_form_window, text='Label/Input amount', bg='grey').place(x=18, y=10)
    how_many = Entry(create_form_window, width=17)
    how_many.place(x=20, y=30)
    
    select_many = Button(create_form_window, text='Create', command=form_window, bg='grey', fg='white', width=14)
    select_many.place(x=20, y=50)

def form_window():
    global display_output, form_title, amount, form_label, form_input, i, form_title, form_label, form_input
    form_window = Tk()
    form_window.title("Form")
    form_window.config(bg='grey')
    w = 300  
    h = 500
    screen_width = form_window.winfo_screenwidth()
    screen_height = form_window.winfo_screenheight()
    x = (screen_width/2) - (w/2)
    y = (screen_height/2) - (h/2)
    form_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    form_menu = Menu(form_window)
    form_window.config(menu=form_menu)
    
    form_file_menu = Menu(form_menu, tearoff=False)
    form_menu.add_cascade(label="File", menu=form_file_menu)
    form_file_menu.add_command(label="Save to text file", command=form_to_txt)
    form_file_menu.add_command(label="Print form", command=print_form)
    
    try:
        amount = int(how_many.get())
    except:
        pass
    
    text = StringVar()
    form_title = Entry(form_window, width=35, textvariable=text)
    form_title.pack(pady=10)
    form_title.insert(0, "Title")
    try:
        for i in range(amount):
            text = StringVar()
            form_label = Entry(form_window, width=10, textvariable=text)
            form_label.pack(pady=3)
            form_label.insert(0, "Label")
            
            text = StringVar()
            form_input = Entry(form_window)
            form_input.pack()
            form_input.insert(0, "Input")
    except:
        text = StringVar()
        form_label = Entry(form_window, width=10, textvariable=text)
        form_label.pack(pady=3)
        form_label.insert(0, "Label")
            
        text = StringVar()
        form_input = Entry(form_window)
        form_input.pack()
        form_input.insert(0, "Input")
        
        
    display_output = Label(form_window, text='', bg='grey')
    display_output.pack()
    create_form_window.destroy()

#unfinished
def form_to_txt():
    title = form_title.get()
    label = form_label.get()
    f_input = form_input.get()
    if os.path.exists(f'{title}.txt'):
        display_output.config(text='Form title already exists')
    
    else:
        f = open(f'{title}.txt', 'a+')
        f.write(f'[ {title} ]\n{label}\n{f_input}')
        f.close()
        display_output.config(text='Saved to txt file')

def print_form():
    #unfinished
    display_output.config(text='Printing form\n(default printer must be set in Windows Settings)')
    


#MAIN
def main():
    global root, pad, events, cmd_entry, file_menu, edit_menu, settings_menu, helper_menu, txt_sub_menu, notepad_sub_menu, main_font
    root = Tk()
    root.title("NotePad")
    root.resizable(False, False)
    w = 960  
    h = 510
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (w/2)
    y = (screen_height/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    #create menu
    my_menu = Menu(root)
    root.config(menu=my_menu)
    
    #main font
    main_font = font.Font(family='Helvetica', size='15')
    
    #notepad
    pad = scrolledtext.ScrolledText(root, wrap=WORD, undo=True, bg='grey', font=main_font)
    pad.pack(expand=True, fill=BOTH, pady=25)
    
    #cmd line
    cmd_entry = Entry(root, text='test', bg='grey')
    cmd_entry.place(x=0, y=485, height=24.5, width=220)
    root.bind('<Return>', cmds)

    #events
    events = Label(root, text='Complex Console')
    events.place(x=225, y=487)
    
    #file menu
    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save as", command=save_as_file)
    file_menu.add_separator()
    file_menu.add_command(label="Print", command=print_file)

    #edit menu
    edit_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Undo", command=pad.edit_undo, accelerator='(Ctrl+z)')
    edit_menu.add_command(label="Redo", command=pad.edit_redo, accelerator='(Ctrl+y)')
    edit_menu.add_separator()
    edit_menu.add_command(label="Select all", command=select_all, accelerator='(Ctrl+a)')
    edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator='(Ctrl+x)')
    edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator='(Ctrl+c)')
    edit_menu.add_command(label="Paste", command=lambda: paste_text(False), accelerator='(Ctrl+v)')
    edit_menu.add_separator()
    
    
    #size edit sub
    size_sub_menu = Menu(edit_menu, tearoff=0)
    size_sub_menu.add_command(label='8', command=size_8)
    size_sub_menu.add_command(label='10', command=size_10)
    size_sub_menu.add_command(label='12', command=size_12)
    size_sub_menu.add_command(label='14', command=size_14)
    size_sub_menu.add_command(label='16', command=size_16)
    size_sub_menu.add_command(label='18', command=size_18)
    size_sub_menu.add_command(label='20', command=size_20)
    size_sub_menu.add_command(label='22', command=size_22)
    size_sub_menu.add_command(label='24', command=size_24)
    size_sub_menu.add_command(label='26', command=size_26)
    size_sub_menu.add_command(label='28', command=size_28)
    size_sub_menu.add_command(label='30', command=size_30)

    edit_menu.add_cascade(
    label="Size",
    menu=size_sub_menu
    )
    
    #style edit sub
    style_sub_menu = Menu(edit_menu, tearoff=0)
    style_sub_menu.add_command(label='Bold', command=bold_func)
    style_sub_menu.add_command(label='Italic', command=italic_func)
    style_sub_menu.add_command(label='Underline', command=underline)
    edit_menu.add_cascade(
    label="Style",
    menu=style_sub_menu
    )


    #forms
    form_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Forms", menu=form_menu)
    form_menu.add_command(label="Create form", command=create_form)


    #tools
    tools_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="tools", menu=tools_menu)
    webhook_sub_menu = Menu(tools_menu, tearoff=0)
    
    set_webhook_sub_menu = Menu(webhook_sub_menu, tearoff=0)
    set_webhook_sub_menu.add_command(label='Discord', command=send_discord_hook)
    
    webhook_sub_menu.add_cascade(
    label="Use webhook",
    menu=set_webhook_sub_menu
    )
    
    add_webhook_sub_menu = Menu(webhook_sub_menu, tearoff=0)
    add_webhook_sub_menu.add_command(label='Discord', command=webhooks)
    
    webhook_sub_menu.add_cascade(
    label="Set webhook",
    menu=add_webhook_sub_menu
    )
    
    tools_menu.add_cascade(
    label="Webhooks",
    menu=webhook_sub_menu
    )


    #settings
    settings_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Settings", menu=settings_menu)
    settings_menu.add_command(label="Light mode", command=light)
    settings_menu.add_command(label="Dark mode", command=dark)
    
    # text settings sub
    txt_sub_menu = Menu(settings_menu, tearoff=0)
    txt_sub_menu.add_command(label='White', command=white_txt)
    txt_sub_menu.add_command(label='Black', command=black_txt)
    txt_sub_menu.add_command(label='Yellow', command=yellow_txt)
    txt_sub_menu.add_command(label='Blue', command=blue_txt)
    txt_sub_menu.add_command(label='Green', command=green_txt)
    settings_menu.add_cascade(
    label="Text color",
    menu=txt_sub_menu
    )
    
    # notepad settings sub
    notepad_sub_menu = Menu(settings_menu, tearoff=0)
    notepad_sub_menu.add_command(label='black', command=black_pad)
    settings_menu.add_cascade(
    label="Notepad color",
    menu=notepad_sub_menu
    )
    
    # settings
    settings_menu.add_separator()
    settings_menu.add_command(label="Refresh", command=restart)
    settings_menu.add_command(label="Exit", command=root.quit)


    #help menu
    helper_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Help", menu=helper_menu)
    helper_menu.add_command(label="Commands", command=help_menu)
    helper_menu.add_separator()
    helper_menu.add_command(label="Discord")


    #build menu
    build_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Build", menu=build_menu)
    build_menu.add_command(label=f"{build}")
    build_menu.add_separator()
    build_menu.add_command(label="Update", command=updater)


    root.mainloop()

#APP
if __name__ == '__main__':
    main()  
