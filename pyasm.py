import sys
import operator

class Parser:
    def __init__(self, content):
        self.registers = {}
        self.accumulator = 0
        self.tokens = content.read().split()

    def parse(self):
        while self.tokens:
            tok = self.next_token()

            if tok == 'get':
                self._op_get()
            elif tok == 'store':
                register = self.next_token()
                self._op_store(register)
            elif tok == 'put':
                self._op_put()
            elif tok == 'add':
                register = self.next_token()
                self._op_math(operator.add, register)
            elif tok == 'sub':
                register = self.next_token()
                self._op_math(operator.sub, register)
            elif tok == 'mul':
                register = self.next_token()
                self._op_math(operator.mul, register)
            elif tok == 'div':
                register = self.next_token()
                self._op_math(operator.truediv, register)

    def next_token(self):
        if self.tokens:
            nexttok = self.tokens[0]
            self.tokens = self.tokens[1:]
            return nexttok

    def peek(self):
        try:
            return self.tokens[0]
        except IndexError:
            return None

    def _op_get(self):
        self.accumulator = int(input("input > "))

    def _op_store(self, register):
        self.registers[register] = self.accumulator

    def _op_put(self):
        print(self.accumulator)

    def _op_math(self, op, register):
        self.accumulator = op(self.registers[register], self.accumulator)


def main(pyAsmFile):
    with open(pyAsmFile) as readFile:
        parser = Parser(readFile)
        parser.parse()

main(sys.argv[1])