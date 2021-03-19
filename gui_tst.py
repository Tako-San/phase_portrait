import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Здесь название')
window.geometry("500x500")
frmMain = tk.Frame(window)

entries = []
start_conds = []

class ErrorWindow:
    def __init__(self,error_message):
        self.error_window = tk.Tk()
        self.error_window.withdraw()
        messagebox.showerror("ERROR",error_message, parent=window)


    def __del__(self):
      self.error_window.destroy()

def entry_create(name, rw):
  ## Greeting string
  greeting = tk.Label(window, text=f'{name} = ', font=("Consolas", 20))
  greeting.grid(column=0, row=rw)

  entries.append(tk.Entry(window))
  entries[len(entries) - 1].grid(column=1, row=rw)


def get_data():
  if len(start_conds) != 0:
    return
  is_raised = False
  err_w = None

  for i in range(6):
    string = entries[i].get()
    if len(string) == 0 or not string.replace('.','',1).isdigit():
    #e('Все поля должны быть заполнены')
      is_raised = True
      break

    val = float(string)
    start_conds.append(val)

    
  if is_raised:
    start_conds.clear()
    for el in entries:
      el.delete(0, tk.END)
    return

  draw()


##field for input

def main():
  entry_create('x0 1', 0)
  entry_create('x0 2', 1)
  entry_create('x0 3', 2)
  entry_create('dot x0 1', 3)
  entry_create('dot x0 2', 4)
  entry_create('dot x0 3', 5)

  entries[0].focus()

  btn = tk.Button(window, text="Старт", font=('Consolas', 20), command=get_data)
  btn.grid(column=1, row=6)

  window.mainloop()
  print(start_conds)

if __name__ == '__main__':
  main()