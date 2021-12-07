import re
import webbrowser
from argparse import ArgumentParser
from functools import partial
from time import sleep

import requests
from tqdm import tqdm

from utils.constants import correct_answers_dir, current_year
from utils.download import get_cookies, read_file


class Verdict:
    def __init__(self, contents: str):
        self.contents: str = contents

    def title(self):
        raise NotImplementedError()

    def __repr__(self):
        return f'{self.title()}\n\n{self.contents}'

    def __str__(self):
        return self.__repr__()


class WrongAnswer(Verdict):
    def title(self):
        return 'Wrong Answer'


class WaitFor(Verdict):
    def title(self):
        return f'Wait to Submit ({self.amount_seconds} sec)'

    def __init__(self, contents: str, amount_seconds: int):
        super().__init__(contents)
        self.amount_seconds: int = amount_seconds


class Correct(Verdict):
    def title(self):
        return 'Correct!'


class ParseError(Verdict):
    def title(self):
        return 'Parse Error!'


class Unknown(Verdict):
    def title(self):
        return 'Unknown'


def submit_answer(day: int, level: int, year: int, answer: str) -> Verdict:
    url = f'https://adventofcode.com/{year}/day/{day}/answer'
    data = {
        'level': str(level),
        'answer': str(answer),
    }
    r = requests.post(url, cookies=get_cookies(), data=data)
    contents = str(r.content, encoding='utf-8')

    if '<body>' not in contents:
        return ParseError(contents)
    contents = contents.split('<body>', 1)[1]
    if '</body>' not in contents:
        return ParseError(contents)
    contents = contents.split('</body>', 1)[0]

    if '<article>' not in contents:
        return ParseError(contents)
    contents = contents.split('<article>', 1)[1]
    if '</article>' not in contents:
        return ParseError(contents)
    contents = contents.split('</article>', 1)[0]
    time_pattern = r'.*You have (?P<time>\d+)s left to wait\..*'
    time_match = re.match(time_pattern, contents)
    if time_match:
        return WaitFor(contents, int(time_match.group('time')))
    if 'That\'s the right answer!' in contents:
        return Correct(contents)
    return WrongAnswer(contents)


def submit_and_handle_wait_for(submit_fn) -> Verdict:
    result = submit_fn()
    print(result)
    if isinstance(result, WaitFor):
        print('Waiting to submit again..')
        for _ in tqdm(list(range(result.amount_seconds + 2))):
            sleep(1)
        result = submit_fn()
        print(result)
    return result


def prompt_submit(day: int, level_str: str, year: int, answer: str):
    if not correct_answers_dir.exists():
        correct_answers_dir.mkdir(exist_ok=True)
    file_marker = correct_answers_dir / f'correct-{level_str}-{day}.out'
    if file_marker.exists():
        correct_answer = read_file(file_marker).strip()
        if correct_answer != answer:
            print(f'WARNING! Answer for day {day} on {level_str} is {correct_answer}')
            print(f'You submitted: {answer}')
            print()
        else:
            print(f'Matches correct answer for day {day} on {level_str}: {correct_answer}')
        return
    assert level_str in ('easy', 'hard')
    level_int = 1 if level_str == 'easy' else 2
    submit_fn = partial(submit_answer, day, level_int, year, answer)
    query = input(f'Are you sure you want to submit for day {day} on '
                  f'{level_str} with the answer "{answer}"? [y/n] ')
    if query.lower() != 'y':
        return
    verdict = submit_and_handle_wait_for(submit_fn)
    if isinstance(verdict, Correct):
        with file_marker.open('w') as f:
            f.write(f'{answer}\n')
        print('Correct answer saved. Opening web page.')
        if level_str == 'easy':
            url = f'https://adventofcode.com/{year}/day/{day}'
        else:
            url = f'https://adventofcode.com/{year}/leaderboard/day/{day}'
        webbrowser.open(url)


def main():
    parser = ArgumentParser()
    parser.add_argument('day', type=int)
    parser.add_argument('level', choices=['easy', 'hard'])
    parser.add_argument('answer')
    parser.add_argument('--year', type=int, default=current_year)
    args = parser.parse_args()
    prompt_submit(args.day, args.level, args.year, args.answer)


if __name__ == '__main__':
    main()