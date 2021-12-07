import webbrowser
from datetime import datetime, timedelta
import re
from time import sleep

import requests
from tqdm import tqdm

from utils.constants import current_year


def wait_until(target_time: datetime) -> None:
    num_seconds = (target_time - datetime.now()).total_seconds()
    if num_seconds < 0:
        print(f'Target time, {target_time} already reached. No waiting necessary')
        return
    for i in tqdm(range(int(num_seconds), -1, -1)):
        current_target = target_time - timedelta(seconds=i)
        current_sleep_time = (current_target - datetime.now()).total_seconds()
        if current_sleep_time > 0:
            sleep(current_sleep_time)


def get_start_time(day: int) -> datetime:
    return datetime(current_year, 12, day, 6, 0, 0) - timedelta(seconds=0.5)


def has_day_started(day: int) -> bool:
    return datetime.now() > get_start_time(day)


def start_on_time(day: int) -> None:
    wait_until(get_start_time(day))
    webbrowser.open(f'https://adventofcode.com/{current_year}/day/{day}')

if __name__ == '__main__':
    start_on_time(15)