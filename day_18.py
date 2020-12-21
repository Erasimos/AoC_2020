import ut

expressions = [line.replace(' ', '') for line in ut.read_input().splitlines()]


class ExpressionEvaluator:

    def __init__(self, expression):
        self.expr_index = 0
        self.expression = expression

    @staticmethod
    def evaluate_add_priority(expression):
        multiplication_terms = [eval(el) for el in expression.split('*')]
        evaluation = 1
        for mul_term in multiplication_terms:
            evaluation *= mul_term
        return str(evaluation)

    def evaluate_v2(self):
        evaluated_expression = ''
        while 0 <= self.expr_index < len(self.expression):
            char = self.expression[self.expr_index]
            if char == '(':
                self.expr_index += 1
                evaluated_expression += self.evaluate_v2()
            elif char == ')':
                return self.evaluate_add_priority(evaluated_expression)
            else:
                evaluated_expression += char
            self.expr_index += 1
        return self.evaluate_add_priority(evaluated_expression)

    def evaluate(self):
        evaluated_expression = ''

        while 0 <= self.expr_index < len(self.expression):
            char = self.expression[self.expr_index]
            if str.isnumeric(char):
                evaluated_expression += char

            elif char == '(':
                self.expr_index += 1
                evaluated_expression += self.evaluate()

            elif char == ')':
                return str(eval(evaluated_expression))

            elif char in ['+', '*']:
                if '+' in evaluated_expression or '*' in evaluated_expression:
                    evaluated_expression = str(eval(evaluated_expression))
                evaluated_expression += char

            self.expr_index += 1

        return str(eval(evaluated_expression))


def part_one():
    ut.print_answer(sum([int(ExpressionEvaluator(expression).evaluate()) for expression in expressions]))


def part_two():
    ut.print_answer(sum([int(ExpressionEvaluator(expression).evaluate_v2()) for expression in expressions]))

