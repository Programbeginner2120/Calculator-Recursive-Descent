import tkinter as tk
import Lexer as Lx
import Parser as Pr
import Calculate as Cal

class CalculatorGui():
    
    def __init__(self):
        self.build_gui_structure()
        self.configure_buttons()
        self.gui.mainloop()

    
    def build_gui_structure(self):
        self.gui = tk.Tk()
        self.gui.configure(background="light blue")
        self.gui.title("Recursive Descent Calculator")
        self.gui.geometry("400x200")

        self.equation = tk.StringVar()
        self.expression_field = tk.Entry(self.gui, textvariable=self.equation)
        self.expression_field.grid(columnspan=4, ipadx=70)


    def configure_buttons(self):
        button1 = tk.Button(self.gui, text=' 1 ', fg='black', bg='red',
                    command=lambda: self.press_button(1), height=1, width=7)
        button1.grid(row=2, column=0)
    
        button2 = tk.Button(self.gui, text=' 2 ', fg='black', bg='red',
                        command=lambda: self.press_button(2), height=1, width=7)
        button2.grid(row=2, column=1)
    
        button3 = tk.Button(self.gui, text=' 3 ', fg='black', bg='red',
                        command=lambda: self.press_button(3), height=1, width=7)
        button3.grid(row=2, column=2)
    
        button4 = tk.Button(self.gui, text=' 4 ', fg='black', bg='red',
                        command=lambda: self.press_button(4), height=1, width=7)
        button4.grid(row=3, column=0)
    
        button5 = tk.Button(self.gui, text=' 5 ', fg='black', bg='red',
                        command=lambda: self.press_button(5), height=1, width=7)
        button5.grid(row=3, column=1)
    
        button6 = tk.Button(self.gui, text=' 6 ', fg='black', bg='red',
                        command=lambda: self.press_button(6), height=1, width=7)
        button6.grid(row=3, column=2)
    
        button7 = tk.Button(self.gui, text=' 7 ', fg='black', bg='red',
                        command=lambda: self.press_button(7), height=1, width=7)
        button7.grid(row=4, column=0)
    
        button8 = tk.Button(self.gui, text=' 8 ', fg='black', bg='red',
                        command=lambda: self.press_button(8), height=1, width=7)
        button8.grid(row=4, column=1)
    
        button9 = tk.Button(self.gui, text=' 9 ', fg='black', bg='red',
                        command=lambda: self.press_button(9), height=1, width=7)
        button9.grid(row=4, column=2)
    
        button0 = tk.Button(self.gui, text=' 0 ', fg='black', bg='red',
                        command=lambda: self.press_button(0), height=1, width=7)
        button0.grid(row=5, column=0)
    
        plus = tk.Button(self.gui, text=' + ', fg='black', bg='red',
                    command=lambda: self.press_button("+"), height=1, width=7)
        plus.grid(row=2, column=3)
    
        minus = tk.Button(self.gui, text=' - ', fg='black', bg='red',
                    command=lambda: self.press_button("-"), height=1, width=7)
        minus.grid(row=3, column=3)
    
        multiply = tk.Button(self.gui, text=' * ', fg='black', bg='red',
                        command=lambda: self.press_button("*"), height=1, width=7)
        multiply.grid(row=4, column=3)
    
        divide = tk.Button(self.gui, text=' / ', fg='black', bg='red',
                        command=lambda: self.press_button("/"), height=1, width=7)
        divide.grid(row=5, column=3)
    
        equal = tk.Button(self.gui, text=' = ', fg='black', bg='red',
                    command=self.press_equals, height=1, width=7)
        equal.grid(row=5, column=2)
    
        clear = tk.Button(self.gui, text='clear', fg='black', bg='red',
                    command=self.clear_console, height=1, width=7)
        clear.grid(row=5, column=1)
    
        Decimal= tk.Button(self.gui, text='.', fg='black', bg='red',
                        command=lambda: self.press_button('.'), height=1, width=7)
        Decimal.grid(row=6, column=0)

        Exponent= tk.Button(self.gui, text='^', fg='black', bg='red',
                        command=lambda: self.press_button('^'), height=1, width=7)
        Exponent.grid(row=6, column=1)

        left_paren = tk.Button(self.gui, text='(', fg='black', bg='red',
                        command=lambda: self.press_button('('), height=1, width=7)
        left_paren.grid(row=6, column=2)

        right_paren = tk.Button(self.gui, text=')', fg='black', bg='red',
                        command=lambda: self.press_button(')'), height=1, width=7)
        right_paren.grid(row=6, column=3)


    def instantiate_lexer(self):
        self.lexer = Lx.Lexer()


    def instantiate_parser(self, token_list):
        self.parser = Pr.Parser(token_list)


    def press_button(self, choice):
        if self.equation.get() == "ERROR":
            self.clear_console()
        self.equation.set(self.equation.get() + str(choice))


    def press_equals(self):
        try:
            lexer = Lx.Lexer()
            lexer.lex(self.equation.get())
            parser = Pr.Parser(lexer.token_list)
            abstract_syntax_tree = parser.parse()
            self.equation.set(Cal.process_ast(abstract_syntax_tree)) 
        except:
            self.equation.set("ERROR")


    def clear_console(self):
        self.equation.set("")


