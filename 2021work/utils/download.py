import os
from pathlib import Path
from typing import Dict

import requests
from dotenv import load_dotenv

from utils.constants import cached_file_dir, current_year

load_dotenv()


def get_cookies():
    session = os.environ['SESSION']
    return {'session': session}


def download_input(day, year=current_year):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    r = requests.get(url, cookies=get_cookies())
    return str(r.content, encoding='utf-8')


def read_file(path: Path) -> str:
    with path.open('r') as f:
        return f.read()


def get_input(day: int):
    if not cached_file_dir.exists():
        cached_file_dir.mkdir(exist_ok=True)
    easy_path: Path = cached_file_dir / f'input{day}.in'
    if easy_path.exists():
        return read_file(easy_path)
    downloaded = download_input(day)
    with easy_path.open('w') as f:
        f.write(downloaded)
    return downloaded


def get_test_inputs(day: int) -> Dict[str, str]:
    if not cached_file_dir.exists():
        return {}
    test_inputs = {}
    glob_pattenrs = [f'test{day}.*', f'test{day}-*', f'test{day}_*']
    for glob_pattern in glob_pattenrs:
        for path in cached_file_dir.glob(glob_pattern):
            test_inputs[path.name] = read_file(path)
    return test_inputs