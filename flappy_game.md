## Flappy Game with tkinter 

```python

import tkinter as tk
import random as r

in_game = True 

win_height = 500
root = tk.Tk()
root.title('Flappy Game')
xwin = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2.5 #параметры появления окна на экране
ywin = (root.winfo_screenheight() - root.winfo_reqheight()) / 2.5 #параметры появления окна на экране
root.wm_geometry("+%d+%d" % (xwin, ywin)) #параметры появления окна на экране
canv = tk.Canvas(root, width = 500, height = win_height, bg = '#cde2f8')
canv.grid()


class rect(object): #летящий объект
    y = 20
    x = 30
    vy = 10
    id = canv.create_rectangle(80,80,40,40, fill = '#d02222')
    
    def move(self): 
        self.vy += 1.3 # свою скорость увеличить на 1,3
        self.y += self.vy # к своей координате y прибавить свою скорость
        canv.coords(self.id, self.x, self.y, self.x+40, self.y+40)
        
re = rect()        

def rect_fly(event):
    global re
    re.vy = (15 - re.y)/14 #отскок вверх при нажатии 

canv.bind('<1>', rect_fly)    


class pipe(): #трубы
    def __init__(self):
        self.x = 510
        self.y = r.randint(150, 300) #произвольная высота трубы
        self.id = canv.create_rectangle(self.x, self.y, 590, 690, fill = '#60e540') #описание трубы 
        
    def move(self):
        self.x -= 10
        canv.coords(self.id, self.x, self.y, self.x+80, self.y+400)

pipes = []

def new_pipe():
    global in_game
    if in_game:
        p = pipe()
        pipes.append(p)
        root.after(1500, new_pipe) #через 1.5 секунды появляется новая труба
    
       
def main():
    global in_game
    btn.destroy()
    if in_game:
        for ps in pipes:
            ps.move()
        re.move()   
        canv.after(30, main)
    
        if re.y >= 457 or ((re.x+40) >= ps.x and (re.y+40) >= ps.y):
            canv.create_text(250, 250, text="GAME OVER!", font="Arial 20",  fill="#ff0000")
            in_game = False #игровой процесс останавливается
                  

new_pipe()


btn = tk.Button(root, text = 'Start', bg = '#cde2f8', command = main) 
btn.place(x = 225, y = 250)


root.mainloop()



```

