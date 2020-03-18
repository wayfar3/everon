import argparse
import random
import string

from everon import BaseCommand


class RandString(BaseCommand):

    def add_args(self, parser: argparse.ArgumentParser):
        parser.add_argument('length', type=int, help='Indicates length of string')
        parser.add_argument('-l', '--lowercase', action='store_true', help='Only get lowercase letters')

    def handle(self, *args, **kwargs):
        string_length = kwargs.get('length')
        allow_lowercase = kwargs.get('lowercase')
        letters = string.ascii_lowercase if allow_lowercase else string.ascii_letters
        print("Random String is {}".format(
            ''.join(random.choice(letters) for _ in range(string_length)))
        )


if __name__ == '__main__':
    rand_str = RandString()
    rand_str.run()
