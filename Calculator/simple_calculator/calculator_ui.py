
from tkinter import *
from Calculator.simple_calculator.calculator_logic import Calculator


class CalculatorUI:

    def __init__(self):
        self.gui = Tk()
        self.background = 'grey'
        self.title = 'Calculator'
        self.window_dimensions = '378x310'
        self.button_font_color = 'black'
        self.button_bg_color = 'white'
        self.equation = StringVar()
        self._build_calculator()
        self.calculator = Calculator()

    def _set_display(self, value):
        self.equation.set(value)

    def click_buttons(self, value):
        result = self.calculator.append_to_input(value)
        self._set_display(result)

    def click_equal(self):
        result = self.calculator.calculate_result()
        # print(result)
        self._set_display(result)

    def click_clear(self):
        result = self.calculator.clear_input_expression()
        self._set_display(result)

    def _build_calculator(self):
        self.gui.resizable(0, 0)
        self.gui.configure(background=self.background)
        self.gui.title(self.title)
        self.gui.geometry(self.window_dimensions)
        expression_field = Entry(self.gui, textvariable=self.equation,
                                 state="disabled", justify='right',
                                 disabledforeground='black')
        expression_field.grid(columnspan=4, ipadx=96, ipady=10)

        button1 = Button(self.gui, text=' 1 ', fg=self.button_font_color,
                         bg=self.button_bg_color,
                         command=lambda: self.click_buttons(1),
                         height=3, width=10)
        button1.grid(row=4, column=0)

        button2 = Button(self.gui, text=' 2 ', fg=self.button_font_color,
                         bg=self.button_bg_color,
                         command=lambda: self.click_buttons(2),
                         height=3, width=10)
        button2.grid(row=4, column=1)

        button3 = Button(self.gui, text=' 3 ', fg=self.button_font_color,
                         bg=self.button_bg_color,
                         command=lambda: self.click_buttons(3),
                         height=3, width=10)
        button3.grid(row=4, column=2)

        button4 = Button(self.gui, text=' 4 ', fg=self.button_font_color,
                         bg=self.button_bg_color,
                         command=lambda: self.click_buttons(4),
                         height=3, width=10)
        button4.grid(row=3, column=0)

        button5 = Button(self.gui, text=' 5 ', fg=self.button_font_color,
                         bg=self.button_bg_color,
                         command=lambda: self.click_buttons(5),
                         height=3, width=10)
        button5.grid(row=3, column=1)

        button6 = Button(self.gui, text=' 6 ', fg=self.button_font_color,
                         bg=self.button_bg_color,
                         command=lambda: self.click_buttons(6),
                         height=3, width=10)
        button6.grid(row=3, column=2)

        button7 = Button(self.gui, text=' 7 ', fg=self.button_font_color,
                         bg=self.button_bg_color,
                         command=lambda: self.click_buttons(7),
                         height=3, width=10)
        button7.grid(row=2, column=0)

        button8 = Button(self.gui, text=' 8 ', fg=self.button_font_color,
                         bg=self.button_bg_color,
                         command=lambda: self.click_buttons(8),
                         height=3, width=10)
        button8.grid(row=2, column=1)

        button9 = Button(self.gui, text=' 9 ', fg=self.button_font_color,
                         bg=self.button_bg_color,
                         command=lambda: self.click_buttons(9),
                         height=3, width=10)
        button9.grid(row=2, column=2)

        button0 = Button(self.gui, text=' 0 ', fg=self.button_font_color,
                         bg=self.button_bg_color,
                         command=lambda: self.click_buttons(0),
                         height=3, width=21)
        button0.grid(row=5, column=0, columnspan=2)

        button_sum = Button(self.gui, text=' + ', fg=self.button_font_color,
                            bg=self.button_bg_color,
                            command=lambda: self.click_buttons('+'),
                            height=3, width=10)
        button_sum.grid(row=5, column=3)

        button_diff = Button(self.gui, text=' - ', fg=self.button_font_color,
                             bg=self.button_bg_color,
                             command=lambda: self.click_buttons('-'),
                             height=3, width=10)
        button_diff.grid(row=4, column=3)

        button_mul = Button(self.gui, text=' x ', fg=self.button_font_color,
                            bg=self.button_bg_color,
                            command=lambda: self.click_buttons('*'),
                            height=3, width=10)
        button_mul.grid(row=3, column=3)

        button_div = Button(self.gui, text=' / ', fg=self.button_font_color,
                            bg=self.button_bg_color,
                            command=lambda: self.click_buttons('/'),
                            height=3, width=10)
        button_div.grid(row=2, column=3)

        button_equal = Button(self.gui, text=' = ', fg=self.button_font_color,
                              bg=self.button_bg_color,
                              command=lambda: self.click_equal(),
                              height=3, width=21)
        button_equal.grid(row=6, column=2, columnspan=2)

        button_clear = Button(self.gui, text=' C ', fg=self.button_font_color,
                              bg=self.button_bg_color,
                              command=lambda: self.click_clear(),
                              height=3, width=21)
        button_clear.grid(row=6, column=0, columnspan=2)

        button_decimal = Button(self.gui, text=' . ',
                                fg=self.button_font_color,
                                bg=self.button_bg_color,
                                command=lambda: self.click_buttons('.'),
                                height=3, width=10)
        button_decimal.grid(row=5, column=2)

    def run(self):
        if self.gui:
            self.gui.mainloop()
