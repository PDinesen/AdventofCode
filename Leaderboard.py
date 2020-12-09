from datetime import datetime
import sys


A = ""
with open("leaderboard.json", "r", encoding='utf-8') as f:
    for l in f:
        A += l
a = eval(A)

days = [datetime(2020, 12, i, 6) for i in range(1, 26)]

sys.stdout.write(a["event"] + "\n")
mem = a["members"]
best = {}
times = {i: {} for i in range(1, 26)}

for id in sorted(mem, key=lambda id: mem[id]["local_score"], reverse=True):
    m = mem[id]
    com = m["completion_day_level"]
    m["times"] = {}
    m["best"] = [None, None, 0, 0]
    if not com:continue
    sys.stdout.write("%s\t%s\n" % (m["local_score"], m["name"]))
    for c in sorted(com, key=int):
        D = int(c)
        S = "\t%2d" % int(c)
        d = []
        m["times"][D] = []
        for s in sorted(com[c], key=int):
            t = datetime.fromtimestamp(int(com[c][s]["get_star_ts"]))
            d += [t]
            S += "\t%s" % str(d[-1])[5:]
            dt = t - days[D - 1]
            m["times"][D] += [dt]
            if s == "1":
                if m["best"][0] is None or dt < m["best"][0]:
                    m["best"][0] = dt
                    m["best"][2] = D
        if len(d) == 2:
            dt2 = d[1] - d[0]
            S += "\t%s" % (dt2)
            m["times"][D] += [dt2]
            if m["best"][1] is None or dt2 < m["best"][1]:
                m["best"][1] = dt2
                m["best"][3] = D
        sys.stdout.write(S + "\n")
        times[D][m["name"]] = m["times"][D]
    best[m["name"]] = m["best"]

sys.stdout.write("\n")

sys.stdout.write("\nFastest part 1\n")
for d in range(1, 26):
    s = sorted([(v[0], n) for (n, v) in times[d].items() if v[:1]])
    v, n = s[0] if s else ("", "")
    if s:
        sys.stdout.write("{:2} {:>20}     {:24}\n".format(d, str(v), n))

sys.stdout.write("\nFastest part 2\n")
for d in range(1, 26):
    s = sorted([(v[1], n) for (n, v) in times[d].items() if v[1:2]])
    v, n = s[0] if s else ("", "")
    if s:
        sys.stdout.write("{:2} {:>20}     {:24}\n".format(d, str(v), n))

sys.stdout.write("\nFastest part 2 (relative to part 1)\n")
for d in range(1, 26):
    s = sorted([(v[2], n) for (n, v) in times[d].items() if v[2:3]])
    v, n = s[0] if s else ("", "")
    if s:
        sys.stdout.write("{:2} {:>20}     {:24}\n".format(d, str(v), n))

sys.stdout.write("\nPersonal bests\n")
b1 = [
    [(best[n][i], best[n][i + 2], n) for n in best if best[n][i] is not None]
    for i in (0, 1)
]

for i in 0, 1:
    sys.stdout.write("Part %d:\n" % (i + 1))
    for v, d, n in sorted(b1[i]):
        sys.stdout.write("{:>20}     {:24} Day {:}\n".format(str(v), n, d))
    sys.stdout.write("\n")