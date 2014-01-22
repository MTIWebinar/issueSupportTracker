# -*- coding:utf-8 -*-

"""
Задачи:
1.
2.
3.

"""

try:
    import Tkinter as tkinter
except ImportError:
    import tkinter

WINDOW_WIDTH = '640'
WINDOW_HEIGHT = '480'
WINDOW_TITLE = 'Пример приложения'


class Window:
  def __init__(self, master):
    self.master = master
    self.master.title(WINDOW_TITLE)
    self.master.geometry(WINDOW_WIDTH + 'x' + WINDOW_HEIGHT)
    self.master.protocol('WM_DELETE_WINDOW', self.exitMethod)
    self.master.mainloop()

  def exitMethod(self):
    print ('exit success & save data')
    self.master.destroy()



root = tkinter.Tk()
# запуск окна
Window(root)