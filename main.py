import gui
from gui import tk

import anim

def main():
  gui.entry_create('c', 100)
  gui.entry_create('m', 1)
  gui.entry_create('n', 10)
  gui.entry_create('x1_0')
  gui.entry_create('x2_0')
  gui.entry_create('x3_0')
  gui.entry_create('x1_0_dot', 1)
  gui.entry_create('x2_0_dot')
  gui.entry_create('x3_0_dot', -1)

  btn = tk.Button(gui.window, text="Старт", font=('Consolas', 20), command=gui.get_data)
  btn.grid(column=1, row=len(gui.entries))

  gui.window.mainloop()
  #print(gui.start_conds)

if __name__ == '__main__':
  main()