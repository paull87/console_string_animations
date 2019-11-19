import sys
import time
import string
import random


class RandomChar:
    def __init__(self, expected_char):
        self.expected_char = expected_char
        self.random_chars = self.generate_random_chars()
        self.current_char = None

    @staticmethod
    def generate_random_chars():
        random_chars = list(string.ascii_letters + string.punctuation + string.digits + ' ')
        random.shuffle(random_chars)
        return random_chars

    @property
    def next_char(self):
        if self.current_char != self.expected_char:
            self.current_char = self.random_chars.pop()
        return self.current_char

    def __str__(self):
        return self.next_char


class StringGenerator:
    def __init__(self, target):
        self.target = target
        self.generators = self.generate_generators()

    def generate_generators(self):
        return [RandomChar(c) for c in self.target]

    @property
    def generator_string(self):
        return ''.join([str(x) for x in self.generators])

    def output_generator(self):
        generated_string = None
        while generated_string != self.target:
            generated_string = self.generator_string
            sys.stdout.write(f'\r {generated_string}')
            sys.stdout.flush()
            time.sleep(.1)
        sys.stdout.write(f'\r {generated_string}\n')


if __name__ == '__main__':
    text = 'When one desires reincarnation and satori, one is able to illuminate freedom.'
    generator = StringGenerator(text)
    generator.output_generator()
