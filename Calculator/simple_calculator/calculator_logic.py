
class Calculator:

    def __init__(self):
        self.input_expression = ''
        self.result = None
        self.prev_result = None
        self.history = []
        self.current_op = None
        self.current_num = None

    def read_input(self):
        """
        Can be used for providing input directly without UI
        :return:
        """
        i = input()
        if self.is_valid_expression(i):
            self.input_expression = i
        else:
            raise Exception("Invalid input!!")

    @staticmethod
    def is_valid_expression(expression):
        # To be completed later if the user is provisioned to give input
        # as long string instead of single button press
        return expression

    def append_to_input(self, val):
        self.input_expression += str(val)
        return self.input_expression

    def clear_input_expression(self):
        self.input_expression = ''
        return self.input_expression

    def calculate_result(self):
        try:
            if self.input_expression == '':
                return self.input_expression
            self.result = eval(self.input_expression)
            self.input_expression = str(self.result)
        except Exception as err:
            print(err)
            return "Invalid input"
        self.history.append('{} = {}'.format(self.input_expression,
                                             self.result))
        return self.result

    def continuous_calculate(self, input_char):
        if input_char == '=':
            if len(self.input_expression) <= 1:
                return self.input_expression
            else:
                return self.result
        elif input_char == '':
            self.input_expression = ''
        elif input_char in ('+', '-', '*', '/'):
            self.current_op = input_char
        else:
            self.input_expression += str(input_char)
            self.perform_op(self.current_op, input_char)
        return self.input_expression

    def perform_op(self, op, val):
        if type(self.result) != int:
            self.result = ''
            return
        if not self.current_num:
            self.current_num = val
            self.result = self.current_num
            return
        if op == '+':
            self.result += val
        elif op == '-':
            self.result -= val
        elif op == '*':
            self.result *= val
        elif op == '/':
            self.result *= val
