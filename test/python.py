"""test code"""

import random

from collections import Counter
from itertools import combinations
from operator import mul

def const(n):
    return lambda itp: itp.push(n)

def unary(f):
    return lambda itp: itp.push(f(itp.pop()))

def binary(f):
    return lambda itp: itp.push(f(itp.pop(), itp.pop()))

def direction(x, y):
    return lambda itp: itp.set_vpc(x, y)

def dup(itp):
    x = itp.pop()
    itp.push(x)
    itp.push(x)

def swap(itp):
    x = itp.pop()
    y = itp.pop()
    itp.push(x)
    itp.push(y)

opcodes = {
    '+': binary(lambda a, b: b + a),
    '-': binary(lambda a, b: b - a),
    '*': binary(lambda a, b: b * a),
    '/': binary(lambda a, b: b / a),
    '%': binary(lambda a, b: b % a),
    '!': unary(lambda a: not a),
    '`': binary(lambda a, b: b > a),

    '>': direction(1, 0),
    '<': direction(-1, 0),
    'v': direction(0, 1),
    '^': direction(0, -1),

    '?': lambda itp: itp.set_vpc(*random.choice(((1, 0), (-1, 0), (0, 1), (0, -1)))),

    '_': lambda itp: itp.set_vpc((-1)**(itp.pop() != 0), 0),
    '|': lambda itp: itp.set_vpc(0, (-1)**(itp.pop() != 0)),

    ':': dup,
    '\\': swap,

    '$': lambda itp: itp.pop(),
    '.': lambda itp: itp.output(str(itp.pop())),
    ',': lambda itp: itp.output(chr(itp.pop())),

    'p': lambda itp: itp.put(itp.pop(), itp.pop(), itp.pop()),
    'g': lambda itp: itp.push(itp.get(itp.pop(), itp.pop())),

    '#': lambda itp: itp.advance(),
    '@': lambda itp: itp.end(),
    ' ': lambda itp: None,
}

for i in range(10):
    opcodes[str(i)] = const(i)

class Interpreter:
    def __init__(self, code):
        self.mem = [list(l) for l in code.split('\n')]
        self.stack = []
        self.pc = 0, 0
        self.vpc = 1, 0
        self.obuf = []
        self.ended = False
        self.stringmode = False

    def run(self):
        while not self.ended:
            x, y = self.pc
            op = self.mem[y][x]

        if op == '"':
            self.stringmode = not self.stringmode
        elif self.stringmode:
            self.push(ord(op))
        else:
            opcodes[op](self)

        self.advance()

    def advance(self):
        x, y = self.pc
        vx, vy = self.vpc
        y = (y + vy) % len(self.mem)
        x = (x + vx) % len(self.mem[y])
        self.pc = x, y

    def set_vpc(self, x, y):
        self.vpc = x, y

    def push(self, x):
        self.stack.append(int(x))

    def pop(self):
        try:
            return self.stack.pop(-1)
        except IndexError:
            return 0

    def output(self, s):
        self.obuf.append(s)

    def end(self):
        self.ended = True

    def get(self, y, x):
        return ord(self.mem[y][x])

    def put(self, y, x, n):
        self.mem[y][x] = chr(n)

def interpret(code):
    itp = Interpreter(code)

    itp.run()

    return ''.join(itp.obuf)



def numeric_palindrome(*args):
    max_palindrome, args = 0, [n for n in args if n > 1] + [1] * (1 in args)
    for r in range(2, len(args) + 1):
        for c in combinations(args, r=r):
            digits = sorted(Counter(str(reduce(mul, c, 1))).items(), reverse = True)
            left = ''.join(v / 2 * k for k, v in digits)
            center = max(v % 2 * k for k, v in digits)
            max_palindrome = max(max_palindrome, int((left + center + left[::-1]).strip('0')))
    return max_palindrome
