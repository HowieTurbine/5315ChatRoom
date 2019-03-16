import tkinter as tk
from tkinter import ttk
from bin.Client.util.GUI_util import center_window


def GUI_main():
    def cleanText():
        input_text.delete(1.0, tk.END)

    root = tk.Tk()
    root.title('Chat Room')
    center_window(root, 550, 260)
    root.maxsize(900, 900)
    root.minsize(300, 240)
    root.configure(background='grey')
    # text, bottons and label

    # input_text = tk.Text(root, height=4, width=50, background='grey')
    input_text = tk.Text(root, height=4, width=50)

    name_label = tk.Label(root, text='Your name')

    name_label.grid(row=0, column=2)

    send_botton = tk.Button(root, text='send', width=5, height=1, activebackground='blue')

    txt = '12345678909876543212345678987654321'
    # message_text = tk.Text(root, height=10, width=50, state='normal', background='grey')
    message_text = tk.Text(root, height=10, width=50, state='normal')
    message_text.insert(tk.INSERT, txt)
    message_text.grid(row=0, column=0, rowspan=2, columnspan=1)
    # message_text.pack()
    # friends that you can @
    number = tk.StringVar()
    friend_list = ttk.Combobox(root, width=12, textvariable=number)
    friend_list['values'] = ('friendname', 'python', 'tkinter', 'widget')
    friend_list.current(0)
    # friend_list.pack()
    friend_list.grid(row=1, column=2)

    # scroller
    message_scroller = tk.Scrollbar()
    message_scroller.grid(row=0, column=1, rowspan=4)
    # set scroller and message box
    message_scroller.config(command=message_text.yview)
    message_text.config(yscrollcommand=message_scroller.set)
    # set clean botton
    clean_data = tk.Button(root, text='clean', width=5, height=1, command=cleanText, activebackground='blue')
    input_text.grid(row=2, column=0, rowspan=2, columnspan=1,)
    send_botton.grid(row=2, column=2)
    clean_data.grid(row=3, column=2)
    # input_text.pack()
    # send_botton.pack()
    # clean_data.pack()
    # root.mainloop()

#
# GUI_main()
