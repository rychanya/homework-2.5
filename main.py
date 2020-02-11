from datetime import datetime
from time import sleep
from random import choice

class TimeMachine:
    def __enter__(self):
        self.start = datetime.now()
        print(f'начали в {self.start}')

    def __exit__(self, *args):
        self.end = datetime.now()
        print(f'закончили в {self.end}')
        print(f'всего времени затрачено {self.end - self.start}')

if __name__ == '__main__':
    with TimeMachine():
        time_to_sleep = choice(range(5))
        print(f'ждем {time_to_sleep} сек.')
        sleep(time_to_sleep)