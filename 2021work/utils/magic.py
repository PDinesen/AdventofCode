import inspect
import re
import sys
import traceback
from time import time

from submit import prompt_submit
from utils.constants import current_year
from utils.download import get_input, get_test_inputs


def get_caller_day(frame_count=0):
    current_frame = inspect.currentframe()
    calling_frame = inspect.getouterframes(current_frame, 2)
    calling_filename = calling_frame[frame_count + 2].filename
    regex_match = re.match('^solve(?P<day>\d+).py$', calling_filename)
    if regex_match is None:
        raise Exception(f'Should be called from solve<number>.py not {calling_filename}')
    return int(regex_match.group('day'))


def magic_submit(answer, level: str, submit_prompt: bool, year=current_year):
    print(f'{level} {answer}')
    if submit_prompt and answer:
        answer = str(answer)
        day = get_caller_day(1)
        current_frame = inspect.currentframe()
        was_test_mode = current_frame.f_back.f_back.f_locals['test_mode']
        if not was_test_mode:
            prompt_submit(day, level, year, answer)


def submit_hard(answer=None, submit_prompt=True):
    magic_submit(answer, 'hard', submit_prompt=submit_prompt)


def submit_easy(answer=None, submit_prompt=True):
    magic_submit(answer, 'easy', submit_prompt=submit_prompt)


def run_magic(fn_0, fn_1=None):
    def fn(*args, **kwargs):
        try:
            fn_0(*args, **kwargs)
        except Exception:
            traceback.print_exc()
        if fn_1:
            try:
                fn_1(*args, **kwargs)
            except Exception:
                traceback.print_exc()

    day = get_caller_day()
    print(f'Running program for day {day}')

    main_input = get_input(day)
    test_inputs = get_test_inputs(day)
    for file_name, contents in test_inputs.items():
        if not contents.strip():
            print(f'Skipping {file_name} since it is empty.')
            print()
            continue
        print(f'=== {file_name} ===')
        fn(contents, test_mode=True)
        print()

    print(f'=== Main Input ===')
    t0 = time()
    fn(main_input, test_mode=False)
    t1 = time()
    print('Time used for main input: {:5.2f} seconds'.format(t1 - t0), file=sys.stderr)