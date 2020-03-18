# EVERON (Python Library)

This module makes easier to write user command-line interfaces.

`everon.BaseCommand` makes use of the [argparse](https://docs.python.org/3/library/argparse.html), which is part of Python library.

`everon.MixinFontColor` is a mixin class, which allows to render color fonts in terminal.

## Basic Example



Below, a basic example of what the custom command should look like:

```python
# whats_time.py
from datetime import datetime
import everon


class WhatsTime(everon.BaseCommand):
    help = 'Display current time'

    def handle(self, *args, **kwargs):
        current_time = datetime.now().strftime('%X')
        print("It's now {}".format(current_time))
        
        
if __name__ == '__main__':
    whatstime = WhatsTime()
    whatstime.run()
```

See how we named our module `whatstime.py`.

This command can be executed as:

```
python -m whats_time
```

Output:

```
It's now 11:54:19
```

## Handling Arguments

 To handle arguments in command, we should define a method named `add_args`.

```python
# rand_str.py
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
```



#### Usage:

```
python -m rand_str 10 -l
```

Or

```
python -m rand_str 10 --lower
```

Output

```
Random String is wjaehxsnxc
```

## Font Color

We could setting an appropriate color to the out message with the example

```python
# say_hello.py
from everon import BaseCommand, MixinFontColor


class SayHello(BaseCommand, MixinFontColor):
    def __init__(self):
        MixinFontColor.__init__(self)

    def handle(self, *args, **kwargs):
        self.print_ok('Printing text ok')
        self.print_err('Printing text error')
        print(self.text_as_link('Printing text as link'))
        print(self.color.LIGHTMAGENTA_EX + 'Printing text with custom color')


if __name__ == '__main__':
    foo = SayHello()
    foo.run()
```

Checking with the following command

```
python -m say_hello
```
