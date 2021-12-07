import json
from datetime import datetime
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import requests

from utils.constants import current_year
from utils.download import get_cookies


def get_data(leaderboard_id):
    year = current_year
    cached_files_dir = Path('cached_files')
    if not cached_files_dir.exists():
        cached_files_dir.mkdir(exist_ok=True)
    cached_file = cached_files_dir / f'leaderboard_{year}_{leaderboard_id}.json'
    if cached_file.exists():
        with cached_file.open('r', encoding='utf-8') as f:
            cached_contents = json.load(f)
        last_read = datetime.fromtimestamp(cached_contents['last_read_timestamp'])
        seconds_since_read = (datetime.now() - last_read).total_seconds()
        print(f'Seconds since read: {seconds_since_read}')
        # From the page: avoid sending requests more often than once every 15 minutes (900 seconds)
        if seconds_since_read <= 900:
            print('Using cache!')
            return cached_contents['contents']

    print('Downloading again :)')
    url = f'https://adventofcode.com/{year}/leaderboard/private/view/{leaderboard_id}.json'
    r = requests.get(url, cookies=get_cookies())
    contents = json.loads(r.content)

    with cached_file.open('w', encoding='utf-8') as f:
        json.dump({'last_read_timestamp': datetime.now().timestamp(), 'contents': contents}, f)
    return contents


def main():
    data = get_data(960884)
    # data = get_data(824705)

    members = data['members']
    n = len(members)

    all_days = sorted({
        int(day) for member in members.values()
        for day in member['completion_day_level']
    })
    events = []
    ignore_days = {1}
    for day in all_days:
        for star in (1, 2):
            solution_times = []
            for member in members.values():
                completion_time_str = member['completion_day_level'].get(str(day), {}) \
                    .get(str(star), {}).get('get_star_ts', None)
                if completion_time_str is not None:
                    solution_times.append((member['id'], int(completion_time_str)))
            solution_times = sorted(solution_times, key=lambda x: x[1])
            print(f'day = {day}, start = {star}:')
            start_time = datetime(current_year, 12, day, 6, 0, 0)
            for i, (member_id, solution_time) in enumerate(solution_times):
                points = n - i if day not in ignore_days else 0
                events.append((solution_time, member_id, day, star, points))
                member_name = members[member_id]['name']
                used_time = datetime.fromtimestamp(solution_time) - start_time
                print(f'   {member_name}: {used_time}')

    xs = []
    ys = []
    events = sorted(events)
    total_points = 0
    xs.append(datetime(current_year, 12, 1, 6, 0, 0))
    ys.append(0)
    for solution_time, member_id, *_ in events:
        total_points += 1
        xs.append(datetime.fromtimestamp(solution_time))
        ys.append(total_points)
    xs.append(datetime.now())
    ys.append(total_points)

    fig, ax = plt.subplots()
    ax.step(xs, ys, where='post', color='red')

    ax.xaxis.set_major_locator(mdates.HourLocator([6]))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('Day %d'))
    ax.xaxis.set_minor_locator(mdates.HourLocator())

    event_start = datetime(current_year, 12, 1, 0, 0, 0)
    next_day = datetime(current_year, 12, max(all_days) + 1, 0, 0, 0)
    ax.set_xlim(event_start, next_day)

    ax.grid(True)
    fig.autofmt_xdate()

    plt.show()


if __name__ == '__main__':
    main()


# import tkinter as tk

# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")

#         self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
#         self.quit.pack(side="bottom")

#     def say_hi(self):
#         print("hi there, everyone!")

# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()