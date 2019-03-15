import tkinter as tk
from tkinter import ttk
from bin.Client.util.GUI_util import center_window


def GUI_main():
    def cleanText():
        input_text.delete(1.0, tk.END)

    root = tk.Tk()
    root.title('Chat Room')
    center_window(root, 500, 500)
    root.maxsize(900, 900)
    root.minsize(300, 240)

    # text and bottons
    input_text = tk.Text(root, height=4, width=50, background='grey', pady=20)

    send_botton = tk.Button(root, text='send', width=5, height=1, activebackground='blue')

    txt = '12345678909876543212345678987654321'
    message_text = tk.Text(root, height=10, width=50, state='normal', background='grey', pady=20)
    message_text.insert(tk.INSERT, txt)
    message_text.pack()
    # friends that you can @
    number = tk.StringVar()
    friend_list = ttk.Combobox(root, width=12, textvariable=number)
    friend_list['values'] = ('friendname', 'python', 'tkinter', 'widget')
    friend_list.current(0)
    friend_list.pack()
    # scroller
    message_scroller = tk.Scrollbar()
    message_scroller.pack(side=tk.RIGHT)
    # set scroller and message box
    message_scroller.config(command=message_text.yview)
    message_text.config(yscrollcommand=message_scroller.set)
    # set clean botton
    clean_data = tk.Button(root, text='clean', width=5, height=1, command=cleanText, activebackground='blue')

    input_text.pack()
    send_botton.pack()
    clean_data.pack()
    root.mainloop()

#
# GUI_main()
