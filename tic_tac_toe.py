from tkinter import*
import  tkinter.messagebox as tkmsg
window = Tk()
window.title('Tic Tac Toe')

click = True

def checker(buttons):
    global click
    if buttons['text']== ' ' and click == True:
        buttons['text'] = 'x'
        click = False
    elif buttons['text']== ' ' and click == False:
        buttons['text'] = '0'
        click = True
        
    if (button1["text"] == "x" and button2["text"] == "x" and  button3["text"] == "x" or
        button4["text"] == "x" and button5["text"] == "x" and  button6["text"] == "x" or
        button7["text"] == "x" and button8["text"] == "x" and  button9["text"] == "x" or
        button1["text"] == "x" and button4["text"] == "x" and  button7["text"] == "x" or
        button2["text"] == "x" and button5["text"] == "x" and  button8["text"] == "x" or
        button3["text"] == "x" and button6["text"] == "x" and  button9["text"] == "x" or
        button1["text"] == "x" and button5["text"] == "x" and  button9["text"] == "x" or
        button3["text"] == "x" and button5["text"] == "x" and  button7["text"] == "x"):
        answer = tkmsg.askquestion("x player wins!!!!!, do you want to play again")
        tk.destroy()
        if answer == 'yes': start()
            
    elif(button1["text"] == "0" and button2["text"] == "0" and  button3["text"] == "0" or
         button4["text"] == "0" and button5["text"] == "0" and  button6["text"] == "0" or
         button7["text"] == "0" and button8["text"] == "0" and  button9["text"] == "0" or
         button1["text"] == "0" and button4["text"] == "0" and  button7["text"] == "0" or
         button2["text"] == "0" and button5["text"] == "0" and  button8["text"] == "0" or
         button3["text"] == "0" and button6["text"] == "0" and  button9["text"] == "0" or
         button1["text"] == "0" and button5["text"] == "0" and  button9["text"] == "0" or
         button3["text"] == "0" and button5["text"] == "0" and  button7["text"] == "0"):
        answer = tkmsg.askquestion("0 player wins!!!!!, do you want to play again")
        tk.destroy()
        if answer == 'yes': start()
        
buttons = StringVar()

global button1, button2, button3, button4, button5, button6, button7, button8, button9

button1 = Button(window,{'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda:checker(button1)})
button1.grid({'row': '0', 'column': '0'})

button2 = Button(window,{'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda:checker(button2)})
button2.grid({'row': '0', 'column': '1'})

button3 = Button(window,{'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda:checker(button3)})
button3.grid({'row': '0', 'column': '2'})

button4 = Button(window,{'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda:checker(button4)})
button4.grid({'row': '1', 'column': '0'})

button5 = Button(window,{'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda:checker(button5)})
button5.grid({'row': '1', 'column': '1'})

button6 = Button(window,{'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda:checker(button6)})
button6.grid({'row': '1', 'column': '2'})

button7 = Button(window,{'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda:checker(button7)})
button7.grid({'row': '2', 'column': '0'})

button8 = Button(window,{'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda:checker(button8)})
button8.grid({'row': '2', 'column': '1'})

button9 = Button(window,{'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda:checker(button9)})
button9.grid({'row': '2', 'column': '2'})

window.mainloop()