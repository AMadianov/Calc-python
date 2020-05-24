# coding=utf-8

class Parser:
    def __init__(self, exp):
        self.__exp = '(' + exp + ')'
        self.__prev_token = None

        self.__operands = []

        self.__functions = []

        self.__pos = 0

    __OPERATORS = {
        '+': 2,
        '-': 2,
        '*': 1,
        '/': 1,
        '^': 1,
    }

    @staticmethod
    def __is_function(c):
        return c in Parser.__OPERATORS.keys()

    @staticmethod
    def __priority_function(c):
        if not Parser.__is_function(c):
            raise Exception('Не найден оператор "{}"'.format(c))

        return Parser.__OPERATORS[c]

    def __execute_function(self):
        if len(self.__operands) < 2:
            return

        a, b = self.__operands.pop(), self.__operands.pop()
        f = self.__functions.pop()

        if f == '+':
            self.__operands.append(b + a)
        elif f == '-':
            self.__operands.append(b - a)
        elif f == '*':
            self.__operands.append(b * a)
        elif f == '/':
            self.__operands.append(b / a)
        elif f == '^':
            self.__operands.append(b ** a)

    def __can_pop(self, c):
        if not self.__functions:
            return False

        head = self.__functions[-1]
        if not Parser.__is_function(head):
            return False

        p1 = Parser.__priority_function(c)
        p2 = Parser.__priority_function(head)

        return p1 >= p2

    @staticmethod
    def __isfloat(number):
        try:
            float(number)
            return True
        except ValueError:
            return False

    def __read_number(self):
        res = ''
        point = 0

        c = self.__exp[self.__pos]

        while c.isdigit() or c == '.':
            if c == '.':
                point += 1
                if point > 1:
                    raise Exception('Выражение не верное -- слишком '
                                    'много точек (pos: %s)' % self.__pos)

            res += c
            self.__pos += 1

            c = self.__exp[self.__pos]

        return res

    def __get_token(self):
        for i in range(self.__pos, len(self.__exp)):
            c = self.__exp[i]

            if c.isdigit():
                return self.__read_number()
            else:
                self.__pos += 1
                return c

        return None

    def calc(self):
        self.__pos = 0

        token = self.__get_token()

        while token:
            if token.isspace():
                pass

            elif token.isdigit():
                self.__operands.append(int(token))

            elif self.__isfloat(token):
                self.__operands.append(float(token))

            elif Parser.__is_function(token):
                if self.__prev_token and self.__prev_token == '(' and (token == '+' or token == '-'):
                    self.__operands.append(0)

                while self.__can_pop(token):
                    self.__execute_function()

                self.__functions.append(token)

            elif token == '(':
                self.__functions.append(token)

            elif token == ')':
                while self.__functions and self.__functions[-1] != '(':
                    self.__execute_function()

                self.__functions.pop()

            self.__prev_token = token

            token = self.__get_token()

        if self.__functions or len(self.__operands) > 1:
            raise Exception('Неверное выражение: operands={}, functions={}'.format(self.__operands, self.__functions))

        return self.__operands[0]