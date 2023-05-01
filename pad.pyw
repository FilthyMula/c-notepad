from discord_webhook import DiscordWebhook
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import font
from tkinter import *
import win32api
import sys, os


version = '1.0'
build = 'C-NotePad 1.0.2023'


#color configs
def dark():
    events.config(text='Dark mode set')
    root.config(bg="black")
    events.config(bg="black", fg='white')
    pad.config(bg='gray18', fg='gray80')
    file_menu.config(bg="black", fg="white")
    edit_menu.config(bg="black", fg="white")
    webhook_menu.config(bg="black", fg="white")
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
    webhook_menu.config(bg="white", fg="black")
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
    help.geometry("300x500")
    help.resizable(False, False)
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
    w_hooks.title("Webhooks")
    w_hooks.config(bg="grey")
    w_hooks.geometry("800x400")
    w_hooks.resizable(False, False)
    
    Label(w_hooks, text='Webhooks', font=('Halvetica', 25), bg='grey').place(y=5)
    discord_hook = Label(w_hooks, text='Discord', bg='grey', font=('Halvetica', 15))
    discord_hook.place(x=3, y=55)
    
    enter_w_hook = Entry(w_hooks, width=130)
    enter_w_hook.place(x=5, y=85)
    
    save_w_hook = Button(w_hooks, text='Set webhook', width=15, bg='black', fg='white', command=get_discord_webhook)
    save_w_hook.place(x=5, y=105)
    
    clear_w_hook = Button(w_hooks, text='Clear webhook', width=15, bg='black', fg='white', command=clear_d_hook)
    clear_w_hook.place(x=125, y=105)

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
    

#MAIN
def main():
    global root, pad, events, cmd_entry, file_menu, edit_menu, webhook_menu, settings_menu, helper_menu, txt_sub_menu, notepad_sub_menu, main_font
    root = Tk()
    root.title("Complex NotePad")
    root.geometry("960x510")
    root.resizable(False, False)
    
    my_menu = Menu(root)
    root.config(menu=my_menu)
    
    main_font = font.Font(family='Helvetica', size='15')
    
    #notepad
    pad = scrolledtext.ScrolledText(root, wrap=WORD, undo=True, bg='grey', font=main_font)
    pad.pack(expand=True, fill=BOTH, pady=25)
    
    #cmd line
    cmd_entry = Entry(root, text='test', bg='grey')
    cmd_entry.place(x=0, y=485, height=24.5, width=220)
    root.bind('<Return>', cmds)

    #EVENTS
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
    #style edit sub
    style_sub_menu = Menu(edit_menu, tearoff=0)
    style_sub_menu.add_command(label='Bold', command=bold_func)
    style_sub_menu.add_command(label='Italic', command=italic_func)
    style_sub_menu.add_command(label='Underline', command=underline)
    edit_menu.add_cascade(
    label="Style",
    menu=style_sub_menu
    )

    #webhooks
    webhook_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Webhook", menu=webhook_menu)
    webhook_menu.add_command(label="Discord", command=send_discord_hook)

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
    # discord hook settings sub
    settings_menu.add_separator()
    sub_menu = Menu(settings_menu, tearoff=0)
    sub_menu.add_command(label='Discord', command=webhooks)
    settings_menu.add_cascade(
    label="Set webhooks",
    menu=sub_menu
    )
    # settings
    settings_menu.add_separator()
    settings_menu.add_command(label="Refresh", command=restart)
    settings_menu.add_command(label="Exit", command=root.quit)

    #help menu
    helper_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Help", menu=helper_menu)
    helper_menu.add_command(label="Commands", command=help_menu)

    #build menu
    build_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Build", menu=build_menu)
    build_menu.add_command(label=f"{build}")

    root.mainloop()

#APP
if __name__ == '__main__':
    main()