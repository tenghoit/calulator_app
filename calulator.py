from tkinter import * 
import math

window = Tk()
window.title('Simple Calculator')
window.geometry('315x440')
window.configure(bg="black")

button_size_x = 30
button_size_y = 35
mem = []

screen = Entry(window, width=50,borderwidth=2)
screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5,ipady=15)

def number_click_action(num):
    temp = screen.get()
    clear()
    screen.insert(0, str(temp) + str(num))

def symbol_func(sym):
    global mem
    try:
        mem.append(int(screen.get()))
    except:
        mem.append(float(screen.get()))
    mem.append(sym)
    clear()

def evaluate():
    global mem
    try:
        mem.append(int(screen.get()))
    except:
        mem.append(float(screen.get()))
    clear()
    temp = 0

    while len(mem) > 1:

        if mem[1] == '+':
            temp = mem[0] + mem[2]
        elif mem[1] == '-':
            temp = mem[0] - mem[2]
        elif mem[1] == '*':
            temp = mem[0] * mem[2]
        elif mem[1] == '/':
            temp = mem[0] / mem[2]

        for i in range(3):
            mem.pop(0)
    
    if temp == math.floor(temp):
        temp = math.floor(temp)
        
    screen.insert(0, temp)
    
def clear():
    screen.delete(0, END)

def set_up():

    button_1 = Button(window, text='1', padx=button_size_x, pady=button_size_y, bg='Gray', command=lambda: number_click_action(1))
    button_2 = Button(window, text='2', padx=button_size_x, pady=button_size_y, command=lambda: number_click_action(2))
    button_3 = Button(window, text='3', padx=button_size_x, pady=button_size_y, command=lambda: number_click_action(3))
    button_4 = Button(window, text='4', padx=button_size_x, pady=button_size_y, command=lambda: number_click_action(4))
    button_5 = Button(window, text='5', padx=button_size_x, pady=button_size_y, command=lambda: number_click_action(5))
    button_6 = Button(window, text='6', padx=button_size_x, pady=button_size_y, command=lambda: number_click_action(6))
    button_7 = Button(window, text='7', padx=button_size_x, pady=button_size_y, command=lambda: number_click_action(7))
    button_8 = Button(window, text='8', padx=button_size_x, pady=button_size_y, command=lambda: number_click_action(8))
    button_9 = Button(window, text='9', padx=button_size_x, pady=button_size_y, command=lambda: number_click_action(9))
    button_0 = Button(window, text='0', padx=button_size_x, pady=button_size_y, command=lambda: number_click_action(0))

    button_add = Button(window, text='+', padx=button_size_x, pady=button_size_y, command=lambda: symbol_func('+'))
    button_subtract = Button(window, text='-', padx=button_size_x, pady=button_size_y, command=lambda: symbol_func('-'))
    button_multiply = Button(window, text='x', padx=button_size_x, pady=button_size_y, command=lambda: symbol_func('*'))
    button_divide = Button(window, text='/', padx=button_size_x, pady=button_size_y, command=lambda: symbol_func('/'))

    button_equal = Button(window, text='=', padx=button_size_x, pady=button_size_y, command=evaluate)
    button_clear = Button(window, text='C', padx=button_size_x, pady=button_size_y, command=clear)


    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_clear.grid(row=4, column=0)
    button_0.grid(row=4, column=1)
    button_equal.grid(row=4, column=2)

    button_add.grid(row=4, column=3)
    button_subtract.grid(row=3, column=3)
    button_multiply.grid(row=2, column=3)
    button_divide.grid(row=1, column=3)


if __name__ == "__main__":
    set_up()
    window.mainloop()

#complete
