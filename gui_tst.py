import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Здесь название')
window.geometry("500x500")
frmMain = tk.Frame(window)

entries = {}
start_conds = {}

class ErrorWindow:
    def __init__(self,error_message):
        self.error_window = tk.Tk()
        self.error_window.withdraw()
        messagebox.showerror("ERROR",error_message, parent=window)


    def __del__(self):
      self.error_window.destroy()

def entry_create(name):
  ## Greeting string
  greeting = tk.Label(window, text=f'{name} = ', font=("Consolas", 20))
  entries[name] = tk.Entry(window)

  greeting.grid(column=0, row=len(entries) - 1)
  entries[name].grid(column=1, row=len(entries) - 1)


def get_data():
  if len(start_conds) != 0:
    return
  is_raised = False
  err_w = None

  for key in entries.keys():
    string = entries[key].get()
    if len(string) == 0 or not string.replace('.','',1).isdigit():
    #e('Все поля должны быть заполнены')
      is_raised = True
      break

    val = float(string)
    start_conds[key] = val

    
  if is_raised:
    start_conds.clear()
    for el in entries:
      el.delete(0, tk.END)
    return

  ## here we call draw(start_cond)


##field for input

def main():
  entry_create('c')
  entry_create('m')
  entry_create('n')
  entry_create('x1_0')
  entry_create('x2_0')
  entry_create('x3_0')
  entry_create('x1_0_dot')
  entry_create('x2_0_dot')
  entry_create('x3_0_dot')

  btn = tk.Button(window, text="Старт", font=('Consolas', 20), command=get_data)
  btn.grid(column=1, row=len(entries))

  window.mainloop()
  print(start_conds)

if __name__ == '__main__':
  main()