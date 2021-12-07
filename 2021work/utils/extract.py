import re


def extract_numbers_from_line(line):
    pattern = r'((?<!\d)[+-]?)(\d+)'
    return [int(match.group()) for match in re.finditer(pattern, line)]


def extract_numbers(lines):
    return [extract_numbers_from_line(line) for line in lines]