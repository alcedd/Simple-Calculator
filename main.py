from tkinter import *
from PIL import Image, ImageTk
from math import factorial as math_factorial, sqrt as math_sqrt


calculation = ''
last_operation_index = 0

def insert_symbol(symbol):
    calculate_entry.insert(len(calculate_entry.get()), str(symbol))  

def is_float(number):
    number = str(number)
    if '.' in list(number):
        return True
    else:
        return False

def is_operation():
    global calculation
    try: 
        if len(calculation) == 0:
            return True
        elif calculation[len(calculation)-1] == '+' or calculation[len(calculation)-1] == '-' or calculation[len(calculation)-1] == '/':
            return True
        else:
            return False
    except:
        ERROR()
        

def is_pi(symbol):
    if symbol == 'π':
        return True
    else:
        return False

def is_num_const(symbol):
    if symbol == 'e':
        return True
    else:
        return False

def is_percentage(symbol):
    if symbol == '%':
        return True
    else:
        return False


def is_minus_mul(symbol):
    if symbol == '^(-1)':
        return True
    else:
        return False
    
def is_sqrt(symbol):
    if symbol == '√(':
        return True
    else:
        return False
    
def is_power(symbol):
    if symbol == '^(':
        return True
    else:
        return False
    
def operations_exist():
    global calculation
    operations = ['+', '-', '*', '/']
    for operation in operations:
      if operation in list(calculation):
          break
      else:
          return False
    return True

def last_operation():
    global last_operation_index
    global calculation
    last_operation_index = 0
    operations = ['+', '-', '*', '/']
    try:
        for operation in operations:
            index = calculation.rfind(operation)
            if index > last_operation_index:
                last_operation_index = index
    except:
        ERROR()

def is_factorial(symbol):
    if symbol == '!':
        return True
    else:
        return False

def factorial_calc():
    global calculation

    calculation_list = list(calculation)
    
    if operations_exist():
        last_operation()
        calculation_list.insert(last_operation_index + 1, 'math_factorial(')
        calculation_list.append(')')
    else:
        calculation_list.insert(0, 'math_factorial(')
        calculation_list.append(')')

    calculation = ''.join(calculation_list)

def percentage_calc():
    global calculation

    calculation_list = list(calculation)


    if operations_exist():
        last_operation()
        calculation_list.insert(last_operation_index + 1, '(')
        calculation_list.append('/100)')

        calculate_percentage = ''.join(calculation_list[last_operation_index + 1 : len(calculation_list)])
        print(calculation_list)
        del calculation_list[last_operation_index + 1 : len(calculation_list)]

        percentage = eval(calculate_percentage)
    else:
        calculation_list.insert(0, '(')
        calculation_list.append('/100)')

        calculate_percentage = ''.join(calculation_list[0 : len(calculation_list)])
        calculation_list = []

        percentage = eval(calculate_percentage)

    calculation_list += str(percentage)
    
    print(calculation_list)
    
    calculation = ''.join(calculation_list)


def sqrt_calc():
    global calculation

    calculation_list = list(calculation)

    last_operation()
    calculation_list.insert(last_operation_index + 1, 'math_sqrt(')

    calculation = ''.join(calculation_list)

def del_last_operation():
    global calculation 
    
    try:
        calculation_list = list(calculation)
        calculation_list.pop()
        calculation = ''.join(calculation_list)

        backspace()

    except:
        ERROR()

def ERROR():
    global calculation 
    calculation = ''
    calculate_entry.delete(0, 'end')
    calculate_entry.insert(0, 'ERROR')


def enter_text(symbol):
    global calculation
    if is_num_const(symbol):
        if is_operation():
            calculation += str('2.718')
        else:
            calculation += str('*2.718')

    elif is_pi(symbol):
        if is_operation():
            calculation += str('3.14159')
        else:
            calculation += str('*3.14159')

    elif is_minus_mul(symbol):
        if is_operation():
            ERROR()
        else:
            calculation += str('**(-1)')

    elif is_factorial(symbol):
        if is_operation():
            del_last_operation()
            factorial_calc()
        else:
            factorial_calc()

    elif is_power(symbol):
        calculation += str('**(')
    
    elif is_sqrt(symbol):
        sqrt_calc()
    else:
        if is_percentage(symbol):
            try:
                percentage_calc()
                calculate_entry.delete(0, 'end')
                print(calculation)
                insert_symbol(calculation)
            except:
                ERROR()
        else:   
            calculation += str(symbol)
            insert_symbol(symbol) 
    

def evaluate_calc():
    global calculation
    try:
        calculation = eval(str(calculation))
        calculate_entry.delete(0, 'end')
        calculate_entry.insert(0, str(calculation))
                
        calculation = str(calculation)
        if is_float(calculation) and len(calculation) > 13:
            calculate_entry.delete(13, 'end') 
    except:
        ERROR()
        

def delete_text():
    global calculation
    calculation = ''
    calculate_entry.delete(0, 'end')

def backspace():
    global calculation
    calculation_list = list(calculation)
    if len(calculation) != 0:
        calculation_list.pop()
        calculate_entry.delete(len(calculate_entry.get()) - 1, 'end')
        calculation = ''.join(calculation_list)
    else:
        pass

def change_theme():
    for button in buttons.values():
        if button.cget('fg') == 'white':
            button.config(fg='black', bg='white')
            root.config(bg='white')
            calculate_entry.config(fg='black', bg='white')
            buttons['but_theme'].config(image = dark_theme)

        else:
            button.config(fg='white', bg='black')
            root.config(bg='black')
            calculate_entry.config(fg='white', bg='black')            
            buttons['but_theme'].config(image = bright_theme)


root = Tk()
root.geometry(('500x700'))
root.resizable(False, False)
root.title('Calculator')

calculate_entry = Entry(root, relief=RAISED, borderwidth=5, font = ('Arial', 50, 'bold'), justify='right')
calculate_entry.place(x=0, y=0, width=500, height=100)

import_bright_theme = Image.open('images/bright_theme.png').resize((50, 50))
bright_theme = ImageTk.PhotoImage(import_bright_theme)

import_dark_theme = Image.open('images/dark_theme.png').resize((50, 50))
dark_theme = ImageTk.PhotoImage(import_dark_theme)

buttons = {}

button_data = {
    'but0': (200, 600, '0'), 'but1': (100, 500, '1'), 'but2': (200, 500, '2'),
    'but3': (300, 500, '3'), 'but4': (100, 400, '4'), 'but5': (200, 400, '5'),
    'but6': (300, 400, '6'), 'but7': (100, 300, '7'), 'but8': (200, 300, '8'),
    'but9': (300, 300, '9'), 'but_float': (300, 600, '.'), 'but_delete': (100, 200, 'C'),
    'but_backspace': (200, 200, '⌫'), 'but_plus': (400, 500, '+'), 'but_minus': (400, 400, '-'),
    'but_multiply': (400, 300, '*'), 'but_division': (400, 200, '/'), 'but_num_const': (100, 600, 'e'),
    'but_pi': (0, 500, 'π'), 'but_equal': (400, 600, '='), 'but_theme': (0, 600, dark_theme),
    'but_minus_mul': (0, 400, '1/x'), 'but_factorial': (0, 300, 'x!'), 'but_sqrt': (0, 200, '√x'),
    'but_opening_brackets': (300, 100, '('), 'but_closing_brackets': (400, 100, ')'), 'but_power': (0, 100, 'x^y'), 'but_percentage': (300, 200, '%'),
    'but_nothing': (100, 100, 'nothing :)')
}

for name, (x, y, text) in button_data.items():
    if text == '=':
        btn = Button(root, text=text, font=('Arial', 25, 'bold'),
                 command=evaluate_calc, relief='raised', borderwidth=5)
    elif name == 'but_theme':
        btn = Button(root, image=text, font=('Arial', 25, 'bold'),
                 command=change_theme, relief='raised', borderwidth=5)
    elif name == 'but_nothing':
        btn = Button(root, text=text, font=('Arial', 25, 'bold'),
                  relief='raised', borderwidth=5)
    elif text == 'C':
        btn = Button(root, text=text, font=('Arial', 25, 'bold'),
                 command=delete_text, relief='raised', borderwidth=5)
    elif text == '⌫':
        btn = Button(root, text=text, font=('Arial', 25, 'bold'),
                 command=backspace, relief='raised', borderwidth=5)     
    elif name == 'but_minus_mul':
        btn = Button(root, text=text, font=('Arial', 25, 'bold'),
                 command=lambda: enter_text('^(-1)'), relief='raised', borderwidth=5)
    elif name == 'but_factorial':
        btn = Button(root, text=text, font=('Arial', 25, 'bold'),
                 command=lambda: enter_text('!'), relief='raised', borderwidth=5)
    elif name == 'but_sqrt':
             btn = Button(root, text=text, font=('Arial', 25, 'bold'),
                 command=lambda: enter_text('√('), relief='raised', borderwidth=5)   
    
    elif name == 'but_power':
             btn = Button(root, text=text, font=('Arial', 25, 'bold'),
                 command=lambda: enter_text('^('), relief='raised', borderwidth=5)   
    else:    
        btn = Button(root, text=text, font=('Arial', 25, 'bold'),
                    command=lambda t=text: enter_text(t), relief='raised', borderwidth=5)
    if name == 'but_nothing':
        btn.place(x=x, y=y, width=200, height=100)
    else:
        btn.place(x=x, y=y, width=100, height=100)
    buttons[name] = btn 

root.mainloop()