import customtkinter
import tkinter
import random
#customtkinter.set_appearance_mode('dark') # Modes: system (default), light, dark
#customtkinter.set_default_color_theme('blue')

chars = 'qwertyuiopasdfghjklzxcvbnm'
symbols = '@#$%^&_'
chars = list(chars+chars.upper()+symbols)

def generate():
    count_password = int(entry_count.get())
    len_password = int(entry_len.get())
    for i in range(count_password):
        password =''
        for j in range(len_password):
            password += random.choice(chars)
        text_field.insert(tkinter.END, password+'\n')

def clear():
    text_field.delete(0.0, tkinter.END)


window = customtkinter.CTk()
window.title('Generate')
window.geometry('600x600')
window.resizable(False, False)

customtkinter.CTkLabel(window, text='count password: ').place(x=170, y=30)
entry_count = customtkinter.CTkEntry(window, width=50)
entry_count.place(x=290, y=30)

customtkinter.CTkLabel(window, text='len password: ').place(x=170, y=60)
entry_len = customtkinter.CTkEntry(window, width=50)
entry_len.place(x=290, y=60)

btn_clear = customtkinter.CTkButton(window, text='Clear', command=clear)
btn_clear.place(x=350, y=100)

btn_generate = customtkinter.CTkButton(window, text='Generate', command=generate)
btn_generate.place(x=150, y=100)

text_field = customtkinter.CTkTextbox(window, width=560, height=420)
text_field.place(x=20, y=150)


window.mainloop()