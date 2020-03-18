import datetime
import everon


class WhatsTime(everon.BaseCommand):
    help = 'Display current time'

    def handle(self, *args, **kwargs):
        current_time = datetime.datetime.now().strftime('%X')
        print("It's now {}".format(current_time))


if __name__ == '__main__':
    whatstime = WhatsTime()
    whatstime.run()
