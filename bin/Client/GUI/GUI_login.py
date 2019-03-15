import tkinter as tk

from bin.Client.util.GUI_util import center_window
from GUI_main import GUI_main



def GUI_login():
    def OpenMain_CloseLogin():
        root.destroy()
        GUI_main()
    root = tk.Tk()
    root.title('login')
    center_window(root, 300, 240)
    root.maxsize(600, 400)
    root.minsize(300, 240)

    label_name = tk.Label(root, text='Your Nickname')
    label_name.pack(pady=20)

    input_text = tk.Entry(root)
    input_text.pack()

    login_button = tk.Button(root, text='login', activebackground='blue', command=OpenMain_CloseLogin, relief='ridge',
                             width=5, height=1)
    login_button.pack()

    tk.mainloop()


GUI_login()
