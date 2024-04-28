import tkinter as tk
import webbrowser

window = tk.Tk()
window.title('Minecraft OGName Sniper GUI')
window_width = int(window.winfo_screenwidth()/4)
window_height = int(window.winfo_screenheight()/3)
window.geometry(f'{window_width}x{window_height}+{int((window.winfo_screenwidth() - window_height)/2)}+{int((window.winfo_screenheight() - window_height)/2)}')
window.resizable(False, False)
window.iconbitmap('banner.ico')

def start():
    pass

window_title = tk.Label(window, text='Minecraft OG Name Sniper', font=('Arial','20', 'bold'))
window_title_author = tk.Label(window, text='by senina4', font=('Arial', '10', 'bold'))
window_bearer_token_input = tk.Entry(window)
window_bearer_token_input.grid(row=0,column=0)
window_bearer_token_clear = tk.Button(window, text='Clear', command=window_bearer_token_input.delete(0, 'end'))
window_bearer_token_clear.grid(row=0,column=0)
window_description = tk.Label(window, text='How to get bearer token?',font=('Arial','8'), cursor='hand2')
window_description.bind("<Button-1>", lambda e: webbrowser.open("https://kqzz.github.io/mc-bearer-token/"))
window_start = tk.Button(window, text='Start', command=start())

window_title.pack()
window_title_author.pack()
window_bearer_token_input.pack()
window_bearer_token_clear.pack()
window_description.pack()
window_start.pack()

window.mainloop()