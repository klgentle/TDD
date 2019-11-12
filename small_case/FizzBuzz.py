class FizzBuzz(object):
    def __init__(self, operator='/'):
        self.operator = operator

    def relate(self, input: int, judge_num: int):
        if self.operator == '/':
            return input % judge_num == 0
        elif self.operator == 'contain':
            return str(input).find(str(judge_num)) > -1
        elif self.operator == '/ or contain':
            return input % judge_num == 0 or str(input).find(str(judge_num)) > -1

    def fizzbuzz(self, num: int):
        if self.relate(num, 3) and self.relate(num, 5):
            return 'FizzBuzz'
        elif self.relate(num, 3):
            return 'Fizz'
        elif self.relate(num, 5):
            return 'Buzz'
        return str(num)
