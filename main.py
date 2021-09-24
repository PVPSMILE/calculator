from tkinter import *


tk = Tk()
tk.title("Калькулятор")
tk.geometry("438x699")
tk.configure(bg='light blue')
tk.resizable(False, False)

pixelVirtual = PhotoImage(width=1, height=1)

frame = Frame(tk, width=328, height=168)
frame.place(x=0, y=0)

textArea = Text(frame,
                font=("Verdana", 35, "bold"))
textArea.place(x=0, y=0)
textArea.configure(state='disabled')

def out_green(text):
    print("\033[32m {}" .format(text))

def out_red(text):
    print("\033[31m {}" .format(text))

def out_white(text):
    print("\033[0m {}" .format(text))

a = []
b = []
first_num = []
second_num = []
math_function = []
red_light = True



math_list = ["+", "-", "*", "/", "."]

def add_num(num):
    global red_light

    if num in ["+", "-", "*", "/", "="]:

        math_function.clear()
        math_function.append(num)
        red_light = False
        out_red("")
        print(red_light)
        out_white("")

        print("Математические функции", math_function)



    elif num == 1:
        pass

    else:

        print("Числа")
        if num != ["+", "-", "*", "/", "="]:
            if red_light == True:
                print("Заполняеться первое число")
                a.append(num)
                first_num = ''.join(a)

                print("first_num", first_num)
                print(a)
            elif red_light == False:

                b.append(num)
                second_num = ''.join(b)
                print(type(second_num))
                print("Заполняеться второе число")
                print("second_num", second_num)
                print(b)

        else:
            print("ERRRRRRRRRRRRRRRRR")

    print("_"*5,num,"_"*5)

    textArea.configure(state='normal')
    text = textArea.get("1.0", 'end-1c')

    if num in ["+", "-", "*", "/", "."]:
        if text == "":
            num = ""
        try:
            if text[-1] in ["+", "-", "*", "/", "."]:
                clear()
        except Exception:
            pass

        if "+" in text or "-" in text or "*" in text or "/" in text:
            if num != ".":
                result(False)

            textArea.configure(state='normal')

    if len(text+num) % 10 == 0 and len(text) != 0:
        textArea.insert('end', "\n")
    print("-="*25)


    textArea.insert('end', num)
    textArea.configure(state='disabled')
def argument_clear():
    try:
        a.clear()
        b.clear()
        first_num.clear()
        second_num.clear()
        math_function.clear()
    except:
        pass

def clear_all():
    argument_clear()
    textArea.configure(state='normal')
    textArea.delete("1.0", END)
    textArea.configure(state='disabled')

def clear():
    textArea.configure(state='normal')
    textArea.delete("end-2c", END)
    textArea.configure(state='disabled')

def find_numbers(text, symbol):
    first_number_str = text[0:symbol]
    first_number = float(first_number_str)

    second_number_str = text[symbol + 1:]
    second_number = float(second_number_str)

    return first_number, second_number

def plus(text, symbol):
    plus = text.find(symbol)
    first_number, second_number = find_numbers(text, plus)
    result_num = first_number + second_number
    return round(result_num,5)

def minus(text, symbol):
    minus = text.find(symbol)
    first_number, second_number = find_numbers(text, minus)
    result_num = first_number - second_number
    return round(result_num,5)

def multiply(text, symbol):
    multiply = text.find(symbol)
    first_number, second_number = find_numbers(text, multiply)
    result_num = first_number * second_number
    return round(result_num,5)

def divide(text, symbol):
    divide = text.find(symbol)
    first_number, second_number = find_numbers(text, divide)
    try:
        result_num = first_number / second_number
    except ZeroDivisionError:
        result_num = "Ошибка!"
    return round(result_num,5)

def result(replacement):
    global red_light
    result_str = " "
    text = textArea.get("1.0", 'end-1c')
    text = text.replace('\n', '')
    for symbol in text:
        if symbol == "+":
             result_str = str(plus(text, symbol))
        elif symbol == "-":
             result_str = str(minus(text, symbol))
        elif symbol == "*":
             result_str = str(multiply(text, symbol))
        elif symbol == "/":
             result_str = str(divide(text, symbol))
    argument_clear()
    first_num.append(text)
    if replacement == False:
        red_light = True
    else:
        red_light = False
    out_green("")
    print(red_light)
    out_white("")


    clear_all()
    point = result_str.find(".")
    if result_str[point+1:] == "0":
        result_str = result_str.replace('.0', '')
    if result_str == " ":
        result_str = text


    add_num(result_str)


btnClear = Button(tk, text="Del",
             image=pixelVirtual,
             width=100,
             height=160,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= clear)
btnClear.place(x=330, y=0)

btn1 = Button(tk, text="1",
             image=pixelVirtual,
             width=100,
             height=100,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: add_num("1"))
btn1.place(x = 0, y=170)

btn2 = Button(tk, text="2",
             image=pixelVirtual,
             width=100,
             height=100,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: add_num("2"))
btn2.place(x=110, y=170)

btn3 = Button(tk, text="3",
             image=pixelVirtual,
             width=100,
             height=100,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: add_num("3"))
btn3.place(x=220, y=170)

btnPlus = Button(tk, text="+",
             image=pixelVirtual,
             width=100,
             height=100,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: add_num("+"))
btnPlus.place(x=330, y=170)

btn4 = Button(tk, text="4",
             image=pixelVirtual,
             width=100,
             height=100,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: add_num("4"))
btn4.place(x=0, y=280)

btn5 = Button(tk, text="5",
             image=pixelVirtual,
             width=100,
             height=100,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: add_num("5"))
btn5.place(x=110, y=280)

btn6 = Button(tk, text="6",
             image=pixelVirtual,
             width=100,
             height=100,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: add_num("6"))
btn6.place(x=220, y=280)

btnMinus = Button(tk, text="-",
             image=pixelVirtual,
             width=100,
             height=100,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: add_num("-"))
btnMinus.place(x=330, y=280)

btn7 = Button(tk, text="7",
             image=pixelVirtual,
             width=100,
             height=100,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: add_num("7"))
btn7.place(x=0, y=390)

btn8 = Button(tk, text="8",
             image=pixelVirtual,
             width=100,
             height=100,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: add_num("8"))
btn8.place(x=110, y=390)

btn9 = Button(tk, text="9",
             image=pixelVirtual,
             width=100,
             height=100,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: add_num("9"))
btn9.place(x=220, y=390)

btnMultiply = Button(tk, text="*",
             image=pixelVirtual,
             width=100,
             height=100,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: add_num("*"))
btnMultiply.place(x=330, y=390)

btn0 = Button(tk, text="0",
             image=pixelVirtual,
             width=100,
             height=100,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: add_num("0"))
btn0.place(x=0, y=500)

btn00 = Button(tk, text="00",
             image=pixelVirtual,
             width=100,
             height=100,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: add_num("00"))
btn00.place(x=110, y=500)

btnPoint = Button(tk, text=".",
             image=pixelVirtual,
             width=100,
             height=100,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: add_num("."))
btnPoint.place(x=220, y=500)

btnDivide = Button(tk, text="/",
             image=pixelVirtual,
             width=100,
             height=100,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: add_num("/"))
btnDivide.place(x=330, y=500)

btnC = Button(tk, text="C",
             image=pixelVirtual,
             width=210,
             height=80,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= clear_all)
btnC.place(x=0, y=610)

btnEquals = Button(tk, text="=",
             image=pixelVirtual,
             width=210,
             height=80,
             compound="c",
             font=("Verdana", 35, "bold"),
             command= lambda: result(True))
btnEquals.place(x=220, y=610)

tk.mainloop()
