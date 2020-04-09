from tkinter import *
from tkmacosx import Button
import operator

root = Tk()
root.geometry('260x342')
root.title("Pawitra Calculator")


list_number = []
exist_num = Label(root, text = "0")
flg_ops = Label(root, text = 'n')
prev_obs = Label(root, text = 'n')
flg_first = Label(root, text = 'y')
tmp_repeat_num = Label(root, text = '0')
flg_prev_b = Label(root, text = 'n')

color_bg_darkblue = "#003368"
color_bg_yellow = "#F1C40F"
color_bg_lightblue = "#C1DFFF"
color_btn_yellow = "#FFC11D"
color_btn_blue = "#00B4D5"

frame = Frame(root, bg = color_bg_darkblue)
frame.grid(row=0, column=0, columnspan = 5, sticky='nswe')
frame0 = Frame(root, bg = color_bg_darkblue)
frame0.grid(row=1, column=0, columnspan = 5, sticky='nswe')
frame1 = Frame(root, bg = color_bg_yellow)
frame1.grid(row=2, column=0, columnspan = 4, sticky='nswe')
frame2 = Frame(root, bg = color_bg_yellow)
frame2.grid(row=2, column=3, rowspan = 5, sticky='nswe')
frame3 = Frame(root, bg = color_bg_lightblue)
frame3.grid(row=3, column=0, rowspan = 4, columnspan = 3, sticky='nswe')

def key(event):
    press = str(event.char)
    print('press = ', press)
    if press in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        OnClick(int(press))
    if press in ['+', '-', '*', '/']:
        OnClick(press)
    if press == '.':
        OnClick('dot')
    if press == '%':
        cal_percent()
    

def enter(event):
    OnClick('=')

def clear(event):
    clear_screen()

def delete(event):
    label_result.configure(text = str(label_result.cget('text')[0:-1]))

def clear_screen():
    tmp = '0'
    label_result.configure(text = tmp)
    tmp_repeat_num.configure(text = '0')
    exist_num.configure(text = "0")
    flg_first.configure(text = 'y')
    prev_obs.configure(text = 'n')
    flg_prev_b.configure(text = 'n')
    label_o.configure(text = "")
    label_result.configure(font = ('Tahoma', 35))

def change_sign():
    if label_result.cget("text") != '0':
        if str(label_result.cget('text'))[0] == '-':
            label_result.configure(text = str(label_result.cget('text'))[1:])
        else:
            label_result.configure(text = '-' + str(label_result.cget('text')))

def cal_percent():
    label_o.configure(text = "")
    if prev_obs.cget('text') == 'n' or flg_ops.cget('text') == '=':
        num = float(label_result.cget('text'))
        label_result.configure(text = str(num / 100.0))
    else:
        ops = { "+" : operator.add, "-" : operator.sub, "*" : operator.mul, '/' : operator.truediv }
        tmp = ops['*'](float(exist_num.cget('text')), float(label_result.cget('text')))
        label_result.configure(text = str(tmp / 100.0))

def OnClick(b):
    ops = { "+" : operator.add, "-" : operator.sub, "*" : operator.mul, '/' : operator.truediv }
    print(exist_num.cget('text'))
    if b == '=':
        label_o.configure(text = "")
        if flg_prev_b.cget('text') != b:
            tmp_repeat_num.configure(text = label_result.cget('text'))
        o = prev_obs.cget('text')
        tmp_exist_num = float(exist_num.cget("text"))
        tmp_num = float(tmp_repeat_num.cget("text"))
        result = ops[o](tmp_exist_num, tmp_num)
        exist_num.configure(text = str(result))
        label_result.configure(text = result)
        flg_ops.configure(text = '=')

    if b in ['+', '-', '*', '/']:
        print(b)
        label_o.configure(text = b)
        o = prev_obs.cget('text')
        if flg_first.cget('text') == 'n' and flg_ops.cget('text') == 'n':
            tmp_exist_num = float(exist_num.cget("text"))
            tmp_new_num = float(label_result.cget("text"))
            result = ops[o](tmp_exist_num, tmp_new_num)
            exist_num.configure(text = str(result))
            label_result.configure(text = result)
        flg_ops.configure(text = b)
        prev_obs.configure(text = b)
        flg_first.configure(text = 'n')


    if b in range(0, 10):
        if flg_ops.cget('text') in ['+', '-', '*', '/']:
            exist_num.configure(text = label_result.cget('text'))
            label_result.configure(text = list_number[b].cget("text"))
            flg_ops.configure(text = 'n')
        else:
            if label_result.cget("text") == '0':
                tmp = list_number[b].cget("text")
                
            else:
                tmp = label_result.cget("text") + list_number[b].cget("text")
            label_result.configure(text = tmp)
                 
    if b == 'dot':
        if '.' not in label_result.cget("text"):
            if label_result.cget("text") == '0':
                tmp = '0.'
            else:
                tmp = label_result.cget('text') + '.'
            label_result.configure(text = tmp) 
    
    flg_prev_b.configure(text = b)


    print(len(str(label_result.cget('text'))))
    
    int_len = int(len(str(label_result.cget('text'))))
    size = int(35 - int_len + 0.5)
    print(size)
    if len(str(label_result.cget('text'))) % 9 == 0:
        label_result.configure(font = ('Tahoma', size))
    

for i in range(0, 10):
    b = Button(root, text = '%s' % i, fg = "white", bg = color_btn_blue, width = 60, height = 45, highlightthickness = 0, font = ("Tahoma", 35), command = lambda idx = i: OnClick(idx))
    list_number.append(b)
    

# ROW0
label_o = Label(root, text = "", font = ("Tahoma", 16), fg = 'white', bg = color_bg_darkblue)
label_o.grid(row = 0, column = 0, sticky=W, padx = 2)


# ROW1
# root.grid_rowconfigure(4, weight=1)
label_result = Label(root, text = "0", font = ("Tahoma", 35), fg = 'white', bg = color_bg_darkblue)
label_result.grid(row = 1, columnspan = 4, pady = 10, sticky=E)
root.grid_rowconfigure(1, minsize = 70) 

# ROW2
# btn_ac = Button(root, text = 'AC', padx = 9, pady = 5, font = ("Tahoma", 28), command = clear_screen)
btn_ac = Button(root, text = 'AC',  fg = "white", bg = color_btn_yellow, width = 60, height = 45, highlightthickness = 0, font = ("Tahoma", 28), command = clear_screen)
btn_sign = Button(root, text = '+/-', fg = "white", bg = color_btn_yellow, width = 60, height = 45, highlightthickness = 0, font = ("Tahoma", 20), command = change_sign)
btn_percent = Button(root, text = '%', fg = "white", bg = color_btn_yellow, width = 60, height = 45, highlightthickness = 0, font = ("Tahoma", 28), command = cal_percent)
btn_devide = Button(root, text = '÷', fg = "white", bg = color_btn_yellow, width = 60, height = 45, highlightthickness = 0, font = ("Tahoma", 28), command = lambda: OnClick('/'))

btn_ac.grid(row = 2, column = 0, padx = 2, pady = 2)
btn_sign.grid(row = 2, column = 1, padx = 2, pady = 2)
btn_percent.grid(row = 2, column = 2, padx = 2, pady = 2)
btn_devide.grid(row = 2, column = 3, padx = 2, pady = 2)


# ROW3
list_number[7].grid(row = 3, column = 0, padx = 2, pady = 2)
list_number[8].grid(row = 3, column = 1, padx = 2, pady = 2)
list_number[9].grid(row = 3, column = 2, padx = 2, pady = 2)

btn_mul = Button(root, text = '×', fg = "white", bg = color_btn_yellow, width = 60, height = 45, highlightthickness = 0, font = ("Tahoma", 28), command = lambda: OnClick('*'))
btn_mul.grid(row = 3, column = 3, padx = 2, pady = 2)

# ROW4
list_number[4].grid(row = 4, column = 0, padx = 2, pady = 2)
list_number[5].grid(row = 4, column = 1, padx = 2, pady = 2)
list_number[6].grid(row = 4, column = 2, padx = 2, pady = 2)

btn_minus = Button(root, text = '-', fg = "white", bg = color_btn_yellow, width = 60, height = 45, highlightthickness = 0, font = ("Tahoma", 28), command = lambda: OnClick('-'))
btn_minus.grid(row = 4, column = 3, padx = 2, pady = 2)


# ROW5
list_number[1].grid(row = 5, column = 0, padx = 2, pady = 2)
list_number[2].grid(row = 5, column = 1, padx = 2, pady = 2)
list_number[3].grid(row = 5, column = 2, padx = 2, pady = 2)

btn_plus = Button(root, text = '+', fg = "white", bg = color_btn_yellow, width = 60, height = 45, highlightthickness = 0, font = ("Tahoma", 28), command = lambda: OnClick('+'))
btn_plus.grid(row = 5, column = 3, padx = 2, pady = 2)

# ROW6
list_number[0].config(width = 128, height = 45, highlightthickness = 0)
list_number[0].grid(row = 6, columnspan = 2, padx = 2, pady = 2)

btn_dot = Button(root, text = '.', fg = "white", bg = color_btn_blue, width = 60, height = 45, highlightthickness = 0, font = ("Tahoma", 36), command = lambda: OnClick('dot'))
btn_dot.grid(row = 6, column = 2, padx = 2, pady = 2)

btn_equal = Button(root, text = '=', fg = "white", bg = color_btn_yellow, width = 60, height = 45, highlightthickness = 0, font = ("Tahoma", 28), command = lambda: OnClick('='))
btn_equal.grid(row = 6, column = 3, padx = 2, pady = 2)


root.bind("<Key>", key)
root.bind('<Return>', enter)
root.bind('<Escape>', clear)
root.bind('<BackSpace>', delete)

root.mainloop()
