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
