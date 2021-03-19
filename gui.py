import tkinter as tk
from tkinter import messagebox

import anim

window = tk.Tk()
window.title('Движение трехатомной молекулы')
window.geometry("500x500")
frmMain = tk.Frame(window)

entries = {}
def_conds = {}
start_conds = {}

class ErrorWindow:
    def __init__(self,error_message):
        self.error_window = tk.Tk()
        self.error_window.withdraw()
        messagebox.showerror("ERROR",error_message, parent=window)


    def __del__(self):
      self.error_window.destroy()

def entry_create(name, default=0):
  ## Greeting string
  greeting = tk.Label(window, text=f'{name} = ', font=("Consolas", 20))
  entries[name] = tk.Entry(window)
  def_conds[name] = str(default)
  entries[name].insert(tk.END, str(default)) 

  greeting.grid(column=0, row=len(entries) - 1)
  entries[name].grid(column=1, row=len(entries) - 1)


def get_data():
  #if len(start_conds) != 0:
    #return
  is_raised = False
  err_w = None

  for key in entries.keys():
    string = entries[key].get()
    if len(string) == 0 or not string.lstrip('-').replace('.','',1).isdigit():
    #e('Все поля должны быть заполнены')
      is_raised = True
      break

    val = float(string)
    start_conds[key] = val

    
  if is_raised:
    start_conds.clear()
    return

  anim.draw(start_conds)



##field for input
